"""Build balance v3 (REVIEW_2 P1-7): campaign3 world, greedy bot sees build bonuses (unit_out hook), exact completion time (not session-quantised),
mastery points capped (POINTS) and earned by rides, world 1 calibrated gate. Builds: SPEED x f per node (2 nodes), CASTOFF extra x a/b on tiers>=4 at 40 owned (after 1/2 points), RECIPES = rides need T x r and offline e1 .65 (not offline-only)."""
import itertools, math, json
import campaign3 as C
from campaign3 import World, off_eff, GAPS_3
class BWorld(World):
    def __init__(s,*a,build="none",pts_cap=4,speed_f=1.3,co=(2,3),rec_T=0.5,**k):
        super().__init__(*a,**k); s.build=build; s.pc=pts_cap; s.sf=speed_f; s.co=co
        if build=="recipes": s.T*=rec_T
    def pts(s): return min(len(s.rides)+1,s.pc)        # +1 starting point at world entry (REVIEW_2: fork before first ride)
    def smult(s,seals):
        m=super().smult(seals)
        if s.build=="speed": m*=s.sf**min(s.pts(),2)
        return m
    def unit_out(s,i,n):
        x=n*s.r0[i]*C.tier_mult(n,s.cfg)
        if s.build=="castoff" and i>=3 and n>=40:
            pts=s.pts(); x*=(s.co[0] if pts==1 else s.co[1]) if pts>=1 else 1
        return x
def run(build,gaps,goal,T,mode="pow",**kw):
    car=C.carry_total(0,2.25); W=BWorld(0,car,1.0,T,goal,0.08,mode,0.5,build=build,**kw)
    for d in range(200):
        for k,g in enumerate(gaps):
            W.cur=d*len(gaps)+k; W.advance(W.t+600)
            if W.done(): return W.t/86400
            e=off_eff(g); P=W.prod()
            if P>0 and W.life+P*e>=W.goal: return (W.t+g*((W.goal-W.life)/(P*e)))/86400
            W.gold+=P*e; W.life+=P*e; W.run_life+=P*e; W.t+=g
    return None
if __name__=="__main__":
    T=C.calibrate_T(C.carry_total(0,2.25),1.0,mode="pow"); G=6.24e15
    sched={"3/day 5-8-11h":GAPS_3,"2/day 12h":[12*3600-600]*2,"4/day 6h":[6*3600-600]*4}
    res={}
    for sn,g in sched.items():
        r={b:run(b,g,G,T) for b in ["none","speed","castoff","recipes"]}
        res[sn]=r; print(sn,{k:(round(v,2) if v else None) for k,v in r.items()})
    # balance search
    best=[]
    for sf,co,rt in itertools.product([1.2,1.3,1.5],[(1.5,2),(2,3),(3,5)],[0.3,0.5,0.7]):
        sp=[]
        for sn,g in sched.items():
            v=[run(b,g,G,T,speed_f=sf,co=co,rec_T=rt) for b in ["speed","castoff","recipes"]]
            if None in v: sp=None; break
            sp.append(max(v)/min(v))
        if sp: best.append((max(sp),sf,co,rt,[round(x,3) for x in sp]))
    best.sort(); print("best balanced (spread = slowest/fastest build, exact time):")
    for b in best[:6]: print(b)
    json.dump(dict(res=res,best=best[:10]),open("builds3.json","w"),indent=1)
