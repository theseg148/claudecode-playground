"""Sanity tests for the simulators (run: python3 test_sim.py)."""
import math
from sim import Config, tier_mult, simulate, goal_gap_stats
from sim2 import Player
from campaign import off_eff_seconds, play_world, Config as C

def test_milestones():
    cfg=Config(milestones=(10,25),milestone_mult=2.0)
    assert tier_mult(9,cfg)==1 and tier_mult(10,cfg)==2 and tier_mult(25,cfg)==4

def test_cost_growth_monotone_and_affordable():
    cfg=Config(n_tiers=4); r=simulate(cfg,horizon=600)
    t=[e[0] for e in r["events"]]; assert t==sorted(t) and len(t)>5
    # cost paid for k-th unit of tier i equals base*ratio^i*growth^(k-1)
    for (_,i,k,c) in r["events"][:50]:
        assert math.isclose(c, cfg.base_cost*cfg.tier_cost_ratio**i*cfg.growth**(k-1), rel_tol=1e-9)

def test_offline_stepped():
    assert math.isclose(off_eff_seconds(3600),1800)           # 1h at 50%
    assert math.isclose(off_eff_seconds(8*3600),7200*.5+6*3600*.25)  # 8h
    assert math.isclose(off_eff_seconds(30*3600),off_eff_seconds(8*3600))  # cap

def test_no_softlock_after_reset():
    cfg=C(n_tiers=8,base_cost=15.0,growth=1.12,tier_cost_ratio=8,tier_rate_ratio=6,milestones=(10,25,50,100,200))
    for w in range(3):
        W=play_world(w,3,3,cfg,0.08,1e6,1e12,max_days=30)
        assert W.done() or W.t>0 and len(W.events)>0     # world makes progress from the first second
        assert W.events[0] < 120                         # first goal within 2 minutes (R10)

def test_world_scaling_flat_when_ratio_one():
    cfg=C(n_tiers=8,base_cost=15.0,growth=1.12,tier_cost_ratio=8,tier_rate_ratio=6,milestones=(10,25,50,100,200))
    d=[play_world(w,3,3,cfg,0.08,1e6,1e16,max_days=60).t for w in (0,1,2)]
    assert max(d)/min(d) < 1.5, d

if __name__=="__main__":
    for n,f in list(globals().items()):
        if n.startswith("test_"): f(); print("ok",n)
