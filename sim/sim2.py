"""Session-based model: player plays short sessions; between sessions offline gains accrue
at efficiency `eff` (capped at `cap_h`). Reports days to clear a world and progress/session."""
import math, numpy as np
from sim import Config, tier_mult

class Player:
    def __init__(s, cfg, mult=1.0):
        s.c=cfg; s.n=cfg.n_tiers; s.owned=[0]*s.n; s.gold=cfg.base_cost; s.t=0.0; s.mult=mult
        s.c0=[cfg.base_cost*cfg.tier_cost_ratio**i for i in range(s.n)]
        s.r0=[cfg.base_rate*cfg.tier_rate_ratio**i for i in range(s.n)]
        s.events=[]
    def prod(s): return s.mult*sum(s.owned[i]*s.r0[i]*tier_mult(s.owned[i],s.c) for i in range(s.n))
    def avail(s,i): return i==0 or s.owned[i-1]>=5
    def play(s, dur):
        end=s.t+dur
        while True:
            P=s.prod(); best=None
            for i in range(s.n):
                if not s.avail(i): continue
                c=s.c0[i]*s.c.growth**s.owned[i]
                g=((s.owned[i]+1)*s.r0[i]*tier_mult(s.owned[i]+1,s.c)-s.owned[i]*s.r0[i]*tier_mult(s.owned[i],s.c))*s.mult
                w=max(0,(c-s.gold)/P) if P>0 else (0 if c<=s.gold else math.inf)
                sc=c/g+w
                if best is None or sc<best[0]: best=(sc,i,c,w)
            _,i,c,w=best
            if not math.isfinite(w) or s.t+w>end:
                if P>0: s.gold+=P*(end-s.t)
                s.t=end; return
            s.t+=w; s.gold+=P*w-c; s.owned[i]+=1; s.events.append((s.t,i,s.owned[i]))
    def away(s, dur, eff, cap_h):
        d=min(dur,cap_h*3600); s.gold+=s.prod()*d*eff; s.t+=dur

def days_to_clear(cfg, sessions_per_day, session_min, eff, cap_h=8, goal_top=25, mult=1.0, max_days=60):
    p=Player(cfg,mult); day=86400; gap=day/sessions_per_day - session_min*60
    for d in range(max_days):
        for k in range(sessions_per_day):
            p.play(session_min*60)
            if p.owned[-1]>=goal_top: return p.t/day, p
            p.away(gap, eff, cap_h)
    return None, p
