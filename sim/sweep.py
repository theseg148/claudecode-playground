import itertools, json, random
import numpy as np
from sim import *
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
rows=[]
grid = itertools.product([1.07,1.09,1.12,1.15],[5,8,12,20],[4,6,9,14],
                         [(10,25,50,100),(10,25,50,100,200,400),(25,50,100),(5,10,25,50,100,200)],[2.0,3.0])
for g,cr,rr,ms,mm in grid:
    cfg = Config(n_tiers=8,growth=g,tier_cost_ratio=cr,tier_rate_ratio=rr,milestones=ms,milestone_mult=mm,horizon_s=3*3600)
    r = simulate(cfg, record=False)
    s = goal_gap_stats(r["events"],cfg)
    # score: want many goals, high in-band, small worst gap
    score = s["frac_in_band"]*min(s["n_goals"],60)/60 - s["frac_over_30m"] - min(s["max"],7200)/7200*0.3
    rows.append(dict(growth=g,cost_ratio=cr,rate_ratio=rr,ms=len(ms),ms_first=ms[0],mm=mm,score=score,**s))
rows.sort(key=lambda x:-x["score"])
json.dump(rows,open("sweep.json","w"))
print(len(rows)); 
for r in rows[:10]: print({k:(round(v,2) if isinstance(v,float) else v) for k,v in r.items()})
print("worst");
for r in rows[-3:]: print({k:(round(v,2) if isinstance(v,float) else v) for k,v in r.items()})
# charts: mean score by param
fig,ax=plt.subplots(1,4,figsize=(14,3.5))
for a,k in zip(ax,["growth","cost_ratio","rate_ratio","mm"]):
    vals=sorted(set(r[k] for r in rows)); a.bar([str(v) for v in vals],[np.mean([r["score"] for r in rows if r[k]==v]) for v in vals]); a.set_title("mean score by "+k)
plt.tight_layout(); plt.savefig("sweep_params.png",dpi=100)
