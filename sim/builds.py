"""Do >=2 viable builds exist? Model 3 mastery builds on the campaign world 1 and compare clear time (R13 target: each within +-15% of the median, none dominated by >25%).
Builds modify the campaign model: SPEED = x1.5 production (+x1.5 more after 2 points), CASTOFF = x3 / x5 multiplier on tier-4+ units at 40 owned, RECIPES = offline eff e1 .5->.65 and more frequent ride (T0 x0.7).
Points: 1 mastery point per ride; budget = rides so far (cap 3 per branch)."""
import json, numpy as np
from campaign import *
import campaign as C

def run_build(build, spd=3, T0=1e6, goal=1e18, speed_f=1.5, co=(3,5), rec_T=0.7, rec_e1=0.65):
    cfg=Config(n_tiers=8,base_cost=15.0,growth=1.12,tier_cost_ratio=8,tier_rate_ratio=6,milestones=(10,25,50,100,200))
    W=World(0,3,3,cfg,0.08,T0,goal)
    base_mult=W.mult
    def mult_with_build():
        pts=min(len(W.rides),3)
        m=base_mult()
        if build=="speed": m*=speed_f**min(pts,2)           # speed branch: 2 nodes
        if build=="recipes": m*=1.0
        return m
    W.mult=mult_with_build
    e1=rec_e1 if build=="recipes" else 0.5
    if build=="recipes": W.T*=rec_T
    if build=="castoff":
        # Cast Off: units owned>=40 of tiers>=3 get extra x3 after 1 point, x5 after 2
        orig=W.prod
        def prod():
            pts=min(len(W.rides),3); f=1 if pts==0 else (co[0] if pts==1 else co[1])
            tot=0
            for i in range(W.n):
                x=W.owned[i]*W.r0[i]*tier_mult(W.owned[i],W.cfg)
                if i>=3 and W.owned[i]>=40: x*=f
                tot+=x
            return W.mult()*tot
        W.prod=prod
    day=86400; gap=day/spd-600
    for d in range(120):
        for k in range(spd):
            W.cur_sess=d*spd+k; W.step_buy(W.t+600)
            if W.done(): return W.t/day
            eff=off_eff_seconds(gap,8,e1,.25); P=W.prod(); W.gold+=P*eff; W.life+=P*eff; W.run_life+=P*eff; W.t+=gap
            if W.done(): return W.t/day
    return None
def balance():
    out=[]
    import itertools
    for sf,co,rt in itertools.product([1.2,1.3,1.5],[(1.5,2),(2,3),(3,5)],[0.3,0.5,0.7]):
        r={}
        for spd,T0 in [(2,1e5),(3,1e6),(3,1e5)]:
            for b in ["speed","castoff","recipes"]:
                r[(b,spd,T0)]=run_build(b,spd,T0,speed_f=sf,co=co,rec_T=rt)
        if any(v is None for v in r.values()): continue
        # spread per scenario
        spreads=[]
        for spd,T0 in [(2,1e5),(3,1e6),(3,1e5)]:
            v=[r[(b,spd,T0)] for b in ["speed","castoff","recipes"]]; spreads.append(max(v)/min(v))
        out.append((max(spreads),sf,co,rt,[round(x,2) for x in spreads]))
    out.sort(key=lambda x:x[0]); return out
if __name__=="__main__":
    import sys
    if len(sys.argv)>1: 
        for o in balance()[:8]: print(o)
        sys.exit()
    res={}
    for spd in [2,3]:
        for T0 in [1e5,1e6]:
            r={b:run_build(b,spd,T0) for b in ["none","speed","castoff","recipes"]}
            res[f"spd{spd}_T{T0:g}"]=r; print(spd,T0,{k:(round(v,2) if v else None) for k,v in r.items()})
    json.dump(res,open("builds.json","w"),indent=1)
