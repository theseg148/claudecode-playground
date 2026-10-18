"""R34: does a ride cooldown compress the heavy/light player gap? (world 1, exact completion time, spend-at-return model)"""
import campaign3 as C, json
from campaign3 import World
def run(gaps,cd,G=6.24e15):
    T=C.calibrate_T(C.carry_total(0,2.25),1.0,mode="pow"); W=World(0,C.carry_total(0,2.25),1.0,T,G,0.08,"pow",0.5); W.cooldown=cd*3600
    for d in range(600):
        for k,g in enumerate(gaps):
            W.cur=d*len(gaps)+k; W.advance(W.t+600)
            if W.done(): return W.t/86400
            eff=C.off_eff(g); P=W.prod()
            if P>0 and W.life+P*eff>=W.goal: return (W.t+g*((W.goal-W.life)/(P*eff)))/86400
            W.gold+=P*eff; W.life+=P*eff; W.run_life+=P*eff; W.t+=g
    return None
S={"1/day":[24*3600-600],"2/day":[12*3600-600]*2,"3/day":C.GAPS_3,"4/day":[6*3600-600]*4,"6/day":[4*3600-600]*6}
res={}
print("cooldown h:",[0,4,8,12,24])
for n,g in S.items():
    r=[run(g,cd) for cd in (0,4,8,12,24)]; res[n]=r; print(f"{n:6s}",[None if x is None else round(x,2) for x in r])
print("heavy(6/day) vs light(1/day) speed ratio by cooldown:",[round(res['1/day'][i]/res['6/day'][i],2) for i in range(5)])
json.dump(res,open("ride_cooldown.json","w"))
