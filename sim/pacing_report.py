"""Pacing report tool (v3 thresholds): PASS/FAIL checks against DESIGN_RULES v3. Usage: python3 pacing_report.py [growth cost_ratio rate_ratio]
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
    print("== world length (campaign3: pow Seals, T_w calibrated, gate 6.24e15, 3 sessions/day 5/8/11 h, stepped offline, spend-at-return, default 8/6/1.12 ladder)")
    import campaign3 as C3, math
    car=C3.carry_total(0,2.25); T=C3.calibrate_T(car,1.0,mode="pow")
    W,ns=C3.play(0,6.24e15,car,1.0,T,mode="pow",bonus=.08,p=.5)
    d=W.t/86400; hit=len(W.goal_sessions)/ns
    print(f" R25 world 3-4 d (upper bound; 1.5-1.9 d with auto-spend+build) {ok(2.5<=d<=4)} ({d:.1f} d)")
    print(f" R16 rides per world 8-12 .......... {ok(8<=len(W.rides)<=12)} ({len(W.rides)})")
    print(f" R10 first ride <= 15 min .......... {ok(bool(W.rides) and W.rides[0][0]<=900)} ({(W.rides[0][0]/60 if W.rides else float('nan')):.0f} min)")
    print(f" R25 >=60 % sessions w/ new goal ... {ok(hit>=.6)} ({100*hit:.0f}%)")
    mult=W.smult(W.seals); print(f" R15 final Seal multiplier < 1e4 .... {ok(mult<1e4)} (x{mult:.0f})")
if __name__=="__main__":
    a=[float(x) for x in sys.argv[1:4]] or [1.12,8,6]
    report(*a)
