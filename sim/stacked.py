"""Stack the design's own speed-ups on the 3.2-day baseline: offline auto-spend (R21/R37) and a balanced build (R13b)."""
import campaign3 as C, builds3 as B, json
G=6.24e15; T=C.calibrate_T(C.carry_total(0,2.25),1.0,mode="pow")
def run(gaps,autobuy,build,cap=8):
    W=B.BWorld(0,C.carry_total(0,2.25),1.0,T,G,0.08,"pow",0.5,build=build,speed_f=1.2,co=(1.5,2),rec_T=0.3)
    for d in range(400):
        for k,g in enumerate(gaps):
            W.cur=d*len(gaps)+k; W.advance(W.t+600)
            if W.done(): return W.t/86400
            capped=min(g,cap*3600); eff=C.off_eff(g,cap)
            if autobuy:
                W.scale=eff/capped; W.no_ride=True; t0=W.t; W.advance(W.t+capped); W.scale=1.0; W.no_ride=False; W.t=t0+g
                if W.done(): return (t0+capped)/86400
            else:
                P=W.prod()
                if P>0 and W.life+P*eff>=W.goal: return (W.t+g*((W.goal-W.life)/(P*eff)))/86400
                W.gold+=P*eff; W.life+=P*eff; W.run_life+=P*eff; W.t+=g
S={"1/day":[24*3600-600],"2/day":[12*3600-600]*2,"3/day":C.GAPS_3,"6/day":[4*3600-600]*6}
res={}
for n,g in S.items():
    r={f"{'auto' if a else 'manual'}+{b}":run(g,a,b) for a in (False,True) for b in ("none","speed","castoff","recipes")}
    res[n]=r; print(n,{k:round(v,2) for k,v in r.items()})
json.dump(res,open("stacked.json","w"),indent=1)
