import json, itertools
from sim import Config
from sim2 import *
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
cfg=lambda: Config(n_tiers=6,base_cost=2e3,growth=1.12,tier_cost_ratio=8,tier_rate_ratio=6,milestones=(10,25,50,100))
rows=[]
for spd,smin,eff in itertools.product([1,3,6,12],[3,10,30],[0.0,0.25,0.5,1.0]):
    d,_=days_to_clear(cfg(),spd,smin,eff)
    rows.append(dict(sessions_per_day=spd,session_min=smin,eff=eff,days=d, active_min_per_day=spd*smin))
json.dump(rows,open("sessions_sweep.json","w"))
for r in rows: print(r["sessions_per_day"],r["session_min"],r["eff"],None if r["days"] is None else round(r["days"]*24*60,0),"min wall-clock")
fig,ax=plt.subplots(1,3,figsize=(13,3.8))
for a,eff in zip(ax,[0.0,0.5,1.0]):
    for smin in [3,10,30]:
        xs=[r["sessions_per_day"] for r in rows if r["eff"]==eff and r["session_min"]==smin]
        ys=[r["days"]*24 if r["days"] else float('nan') for r in rows if r["eff"]==eff and r["session_min"]==smin]
        a.plot(xs,ys,"o-",label=f"{smin}-min sessions")
    a.set_title(f"offline eff {eff}"); a.set_xlabel("sessions/day"); a.set_ylabel("hours wall-clock to clear world"); a.set_yscale("log"); a.legend()
plt.tight_layout(); plt.savefig("sessions.png",dpi=100)
