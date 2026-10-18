import json, numpy as np, itertools
from sim import *
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
rows=[]
for thr,exp,bonus,when in itertools.product([1e6,1e8,1e10],[0.4,0.5,0.7],[0.05,0.1,0.25],[1.5,2,3,5]):
    cfg=Config(n_tiers=6,growth=1.12,tier_cost_ratio=8,tier_rate_ratio=6,milestones=(10,25,50,100),
               prestige_enabled=True,prestige_threshold=thr,prestige_exp=exp,prestige_bonus=bonus,prestige_when_mult=when,horizon_s=6*3600)
    r=simulate(cfg,record=False)
    p=r["prestiges"]; ts=[x[0] for x in p]
    rows.append(dict(thr=thr,exp=exp,bonus=bonus,when=when,n_prestiges=len(p),
        first_min=ts[0]/60 if ts else None, med_interval_min=float(np.median(np.diff([0]+ts)))/60 if ts else None,
        final_mult=p[-1][2] if p else 1.0))
json.dump(rows,open("prestige_sweep.json","w"))
ok=[r for r in rows if r["first_min"] and 20<=r["first_min"]<=90 and r["n_prestiges"]>=3]
print(len(rows),len(ok))
for r in sorted(ok,key=lambda r:-r["n_prestiges"])[:12]: print({k:(round(v,2) if isinstance(v,float) else v) for k,v in r.items()})
fig,ax=plt.subplots(figsize=(6,4))
for thr in [1e6,1e8,1e10]:
    xs=[r["first_min"] for r in rows if r["thr"]==thr and r["first_min"]]; ax.hist(xs,alpha=.5,label=f"thr {thr:.0e}",bins=15)
ax.set_xlabel("first prestige (min)"); ax.legend(); plt.savefig("prestige_first.png",dpi=100)
