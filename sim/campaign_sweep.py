import itertools, json, numpy as np
from campaign import *
cfg=Config(n_tiers=8,base_cost=15.0,growth=1.12,tier_cost_ratio=8,tier_rate_ratio=6,milestones=(10,25,50,100,200))
rows=[]
for spd,cap,sb,T0 in itertools.product([1,2,3,6],[4,8,24],[0.02,0.05,0.08,0.10],[1e5,1e6,1e7]):
    W=play_world(0,3,3,cfg,sb,T0,1e18,spd=spd,cap=cap,max_days=120)
    ns=int(W.cur_sess)+1; hit=len(W.sess_events)
    rows.append(dict(spd=spd,cap=cap,bonus=sb,T0=T0,days=W.t/86400 if W.done() else None,rides=len(W.rides),
                     frac_sess_goal=hit/ns, first_ride_min=(W.rides[0][0]/60 if W.rides else None)))
json.dump(rows,open("campaign_sweep.json","w"))
def m(f,key):
    out={}
    for v in sorted(set(r[key] for r in rows)):
        d=[r["days"] for r in rows if r[key]==v and r["days"]]; out[v]=(round(float(np.median(d)),1),len(d))
    return out
for k in ["spd","cap","bonus","T0"]: print(k,m(None,k))
ok=[r for r in rows if r["days"] and 2<=r["days"]<=5 and r["frac_sess_goal"]>=0.9 and r["first_ride_min"] and r["first_ride_min"]<=15]
print(len(rows),len(ok),"configs: world 2-5 d, >=90% sessions with goal, first ride <=15 min")
for r in ok[:15]: print({k:(round(v,2) if isinstance(v,float) else v) for k,v in r.items()})
