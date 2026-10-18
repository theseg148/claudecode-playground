"""Offline lever under the v3 campaign model (world 1, pow Seals, gate 6.24e15): flat vs stepped efficiency, cap 8 vs 24 h, by schedule (exact completion time)."""
import json, campaign3 as C
from campaign3 import World
def run(gaps,eff_fn,G=6.24e15):
    T=C.calibrate_T(C.carry_total(0,2.25),1.0,mode="pow"); W=World(0,C.carry_total(0,2.25),1.0,T,G,0.08,"pow",0.5)
    for d in range(400):
        for k,g in enumerate(gaps):
            W.cur=d*len(gaps)+k; W.advance(W.t+600)
            if W.done(): return W.t/86400
            e=eff_fn(g); P=W.prod()
            if P>0 and W.life+P*e>=W.goal: return (W.t+g*((W.goal-W.life)/(P*e)))/86400
            W.gold+=P*e; W.life+=P*e; W.run_life+=P*e; W.t+=g
    return None
flat=lambda g:min(g,8*3600)*0.5
stepped=lambda g:C.off_eff(g,8)
stepped24=lambda g:C.off_eff(g,24)
none=lambda g:0.0
S={"1/day (23.8 h gap)":[24*3600-600],"2/day 12/12 h":[12*3600-600]*2,"3/day 5/8/11 h":C.GAPS_3,"3/day 8/8/8 h":[8*3600-600]*3,"6/day 4 h":[4*3600-600]*6}
res={}
for sn,g in S.items():
    r={n:run(g,f) for n,f in [("no offline",none),("flat 50% cap8",flat),("stepped cap8",stepped),("stepped cap24",stepped24)]}
    res[sn]=r; print(f"{sn:20s}",{k:(round(v,2) if v else None) for k,v in r.items()})
json.dump(res,open("offline_lever.json","w"),indent=1)
