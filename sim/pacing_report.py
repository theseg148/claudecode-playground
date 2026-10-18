"""Pacing report tool: given a Config (and campaign params) print the checks from DESIGN_RULES for a designer.
Usage: python3 pacing_report.py  [growth cost_ratio rate_ratio]"""
import sys, numpy as np
from sim import Config, simulate, goal_gap_stats
from campaign import play_world, Config as C

def report(growth=1.12,cost_ratio=8,rate_ratio=6):
    cfg=Config(n_tiers=8,growth=growth,tier_cost_ratio=cost_ratio,tier_rate_ratio=rate_ratio,milestones=(10,25,50,100),horizon_s=3*3600)
    s=goal_gap_stats(simulate(cfg,record=False)["events"],cfg)
    ok=lambda c:"PASS" if c else "FAIL"
    print(f"== in-session pacing (3 h greedy) growth={growth} cost/rate={cost_ratio}/{rate_ratio} (ratio {cost_ratio/rate_ratio:.2f})")
    print(f" R2  cost/rate ratio 1.2-1.5 ........ {ok(1.2<=cost_ratio/rate_ratio<=1.5)}")
    print(f" R9  median gap 30-60 s ............ {ok(30<=s['median']<=60)} ({s['median']:.0f}s)")
    print(f" R9  p90 <= 600 s .................. {ok(s['p90']<=600)} ({s['p90']:.0f}s)")
    print(f" R9  max gap <= 30 min ............. {ok(s['max']<=1800)} ({s['max']:.0f}s)")
    print(f" R9  in-band 15-600 s >= 90 % ...... {ok(s['frac_in_band']>=.9)} ({100*s['frac_in_band']:.0f}%)")
    print("== world length (3 sessions/day, stepped offline, T0=1e6, bonus 8 %) goal 1e18")
    c=C(n_tiers=8,base_cost=15.0,growth=growth,tier_cost_ratio=cost_ratio,tier_rate_ratio=rate_ratio,milestones=(10,25,50,100,200))
    W=play_world(0,3,3,c,0.08,1e6,1e18,max_days=60)
    d=W.t/86400; ns=int(W.cur_sess)+1
    print(f" R25 world 3-5 days ................ {ok(3<=d<=5)} ({d:.1f} d)")
    print(f" R16 rides per world 8-12 .......... {ok(8<=len(W.rides)<=12)} ({len(W.rides)})")
    print(f" R10 first ride <= 15 min .......... {ok(bool(W.rides) and W.rides[0][0]<=900)} ({(W.rides[0][0]/60 if W.rides else float('nan')):.0f} min)")
    print(f" R25 >= 90 % of sessions w/ goal ... {ok(len(W.sess_events)/ns>=.9)} ({100*len(W.sess_events)/ns:.0f}%)")
if __name__=="__main__":
    a=[float(x) for x in sys.argv[1:4]] or [1.12,8,6]
    report(*a)
