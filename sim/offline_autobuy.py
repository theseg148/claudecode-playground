"""Does auto-spending while away shorten worlds? (REVIEW_2 §3.1) Variants: (a) gold accrues offline and is spent at return (current model);
(b) auto-buy runs offline at the average efficiency (greedy purchases during the away window, rides still manual)."""
import campaign3 as C, json
from campaign3 import World
def run(gaps,autobuy,G=6.24e15,cap=8):
    T=C.calibrate_T(C.carry_total(0,2.25),1.0,mode="pow"); W=World(0,C.carry_total(0,2.25),1.0,T,G,0.08,"pow",0.5)
    for d in range(400):
        for k,g in enumerate(gaps):
            W.cur=d*len(gaps)+k; W.advance(W.t+600)
            if W.done(): return W.t/86400
            capped=min(g,cap*3600); eff=C.off_eff(g,cap)
            if autobuy:
                W.scale=eff/capped; W.no_ride=True
                t0=W.t; W.advance(W.t+capped)   # purchases happen along the way at scaled production
                W.scale=1.0; W.no_ride=False; W.t=t0+g
                if W.done(): return (t0+capped*(1.0))/86400
            else:
                P=W.prod()
                if P>0 and W.life+P*eff>=W.goal: return (W.t+g*((W.goal-W.life)/(P*eff)))/86400
                W.gold+=P*eff; W.life+=P*eff; W.run_life+=P*eff; W.t+=g
    return None
S={"1/day":[24*3600-600],"2/day 12/12":[12*3600-600]*2,"3/day 5/8/11":C.GAPS_3,"6/day 4 h":[4*3600-600]*6}
res={}
for n,g in S.items():
    a=run(g,False); b=run(g,True); res[n]=(a,b); print(f"{n:14s} spend-at-return {a:.2f} d | offline auto-buy {b:.2f} d | x{a/b:.2f}")
json.dump(res,open("offline_autobuy.json","w"))
