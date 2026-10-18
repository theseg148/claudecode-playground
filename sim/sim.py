"""Idle game pacing simulator.

Greedy-payback player buys generators/upgrades; the gap between purchases is the
"time to next meaningful goal". Supports milestone multipliers, prestige, and
sequential worlds with carryover.
"""
import math, json
from dataclasses import dataclass, field, asdict
import numpy as np

@dataclass
class Config:
    n_tiers: int = 8
    base_cost: float = 10.0
    tier_cost_ratio: float = 12.0      # base cost of tier i+1 / tier i
    growth: float = 1.12               # per-unit cost multiplier
    base_rate: float = 1.0             # production of tier 0 unit / s
    tier_rate_ratio: float = 9.0       # rate ratio between tiers (< cost ratio => later tiers worse ROI, forces breadth)
    milestones: tuple = (10, 25, 50, 100, 200)   # owned counts giving x2
    milestone_mult: float = 2.0
    unlock_frac: float = 0.5           # tier i+1 unlocks when >= this*cost of it is... see unlock rule
    prestige_enabled: bool = False
    prestige_threshold: float = 1e9    # lifetime earnings before prestige allowed
    prestige_exp: float = 0.5          # points = (lifetime/threshold)^exp
    prestige_bonus: float = 0.10       # +10% per point
    prestige_when_mult: float = 3.0    # prestige when projected mult gain >= this x current
    session_s: float = 3600.0
    horizon_s: float = 6 * 3600.0
    carryover_mult: float = 1.0        # world->world permanent mult per prior world

def tier_mult(owned, cfg):
    return cfg.milestone_mult ** sum(owned >= m for m in cfg.milestones)

def simulate(cfg: Config, horizon=None, start_mult=1.0, record=True):
    """Return dict with event list [(t, tier, owned_after, cost)], resource trace, prestiges."""
    horizon = horizon or cfg.horizon_s
    n = cfg.n_tiers
    owned = [0]*n
    costs0 = [cfg.base_cost * cfg.tier_cost_ratio**i for i in range(n)]
    rates0 = [cfg.base_rate * cfg.tier_rate_ratio**i for i in range(n)]
    t = 0.0; gold = cfg.base_cost; lifetime = 0.0
    pp = 0.0; prestige_mult = 1.0
    events = []; trace = [(0, 0)]; prestiges = []
    run_lifetime = 0.0
    def prod():
        return start_mult * prestige_mult * sum(owned[i]*rates0[i]*tier_mult(owned[i], cfg) for i in range(n))
    # tier unlock: tier i available once tier i-1 has >=1 owned and gold seen... simple: owned[i-1]>=5
    def available(i):
        return i == 0 or owned[i-1] >= 5
    steps = 0
    while t < horizon and steps < 200000:
        steps += 1
        P = prod()
        # candidates
        best = None
        for i in range(n):
            if not available(i): continue
            c = costs0[i] * cfg.growth**owned[i]
            gain = (owned[i]+1)*rates0[i]*tier_mult(owned[i]+1, cfg) - owned[i]*rates0[i]*tier_mult(owned[i], cfg)
            gain *= start_mult*prestige_mult
            wait = max(0.0, (c - gold)/P) if P > 0 else (0 if c <= gold else math.inf)
            score = c/gain + wait   # payback incl. wait (classic greedy)
            if best is None or score < best[0]:
                best = (score, i, c, wait)
        if best is None: break
        _, i, c, wait = best
        if not math.isfinite(wait) or t + wait > horizon:
            break
        t += wait; gold += P*wait; lifetime += P*wait; run_lifetime += P*wait
        gold -= c; owned[i] += 1
        events.append((t, i, owned[i], c))
        if record and (len(events) % 5 == 0): trace.append((t, gold))
        if cfg.prestige_enabled and run_lifetime >= cfg.prestige_threshold:
            pts = (run_lifetime/cfg.prestige_threshold)**cfg.prestige_exp
            new_mult = 1 + cfg.prestige_bonus*(pp+pts)
            if new_mult/prestige_mult >= cfg.prestige_when_mult or (new_mult > prestige_mult*1.5 and t > horizon*0.9):
                pp += pts; prestige_mult = new_mult
                prestiges.append((t, pp, prestige_mult))
                owned = [0]*n; gold = cfg.base_cost; run_lifetime = 0.0
    return dict(events=events, trace=trace, prestiges=prestiges, final_time=t, lifetime=lifetime)

def gaps(events):
    ts = [e[0] for e in events]
    return np.diff([0]+ts) if ts else np.array([])

def milestone_events(events, cfg):
    """Meaningful goals = new tier first purchase or milestone-count purchase."""
    out = []
    for (t, i, k, c) in events:
        if k == 1 or k in cfg.milestones:
            out.append(t)
    return out

def goal_gap_stats(events, cfg):
    ms = milestone_events(events, cfg)
    g = np.diff([0]+ms) if ms else np.array([0.0])
    if len(g) == 0: g = np.array([0.0])
    return dict(n_goals=len(ms), median=float(np.median(g)), p90=float(np.percentile(g,90)),
                max=float(g.max()), frac_in_band=float(np.mean((g>=15)&(g<=600))),
                frac_over_30m=float(np.mean(g>1800)))
