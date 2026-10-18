"""Robustness: do the 'good' configs stay good for non-greedy players?
Strategies: greedy; noisy (epsilon picks random affordable-soon tier); lazy (only acts every `check` seconds, buying greedily at that time)."""
import math, random, json, numpy as np
from sim import Config, tier_mult, goal_gap_stats
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

def run(cfg, strategy="greedy", eps=0.0, check=60.0, horizon=3*3600, seed=0, tiers_override=None):
    rnd=random.Random(seed); n=cfg.n_tiers
    c0=[cfg.base_cost*cfg.tier_cost_ratio**i for i in range(n)]; r0=[cfg.base_rate*cfg.tier_rate_ratio**i for i in range(n)]
    owned=[0]*n; gold=cfg.base_cost; t=0.0; ev=[]
    prod=lambda: sum(owned[i]*r0[i]*tier_mult(owned[i],cfg) for i in range(n))
    avail=lambda i: i==0 or owned[i-1]>=5
    def cand():
        P=prod(); out=[]
        for i in range(n):
            if not avail(i): continue
            c=c0[i]*cfg.growth**owned[i]
            g=(owned[i]+1)*r0[i]*tier_mult(owned[i]+1,cfg)-owned[i]*r0[i]*tier_mult(owned[i],cfg)
            w=max(0,(c-gold)/P) if P>0 else (0 if c<=gold else math.inf)
            out.append((c/g+w,i,c,w))
        return out
    while t<horizon:
        cs=cand()
        if not cs: break
        cs.sort()
        pick=cs[0] if (strategy!="noisy" or rnd.random()>eps) else rnd.choice(cs[:3])
        _,i,c,w=pick
        if strategy=="lazy":
            # only acts at multiples of `check`: wait until next check after affordable
            t_aff=t+w; t_act=math.ceil(t_aff/check)*check
            w=t_act-t
        if not math.isfinite(w) or t+w>horizon: break
        P=prod(); gold+=P*w; t+=w
        if gold<c: gold=c  # numeric guard
        gold-=c; owned[i]+=1; ev.append((t,i,owned[i],c))
    return ev

if __name__=="__main__":
    good=Config(n_tiers=8,growth=1.12,tier_cost_ratio=8,tier_rate_ratio=6,milestones=(10,25,50,100),horizon_s=3*3600)
    bad=Config(n_tiers=8,growth=1.12,tier_cost_ratio=5,tier_rate_ratio=14,milestones=(5,10,25,50,100,200),milestone_mult=3.0,horizon_s=3*3600)
    out={}
    for name,cfg in [("good",good),("bad",bad)]:
        for strat,kw in [("greedy",{}),("noisy",{"eps":0.3}),("noisy",{"eps":0.6}),("lazy",{"check":60}),("lazy",{"check":600})]:
            stats=[]
            for s in range(10):
                ev=run(cfg,strat,seed=s,**kw); stats.append(goal_gap_stats(ev,cfg))
            key=f"{name}-{strat}-{kw}"
            out[key]={k:float(np.mean([x[k] for x in stats])) for k in stats[0]}
            print(key,{k:round(v,2) for k,v in out[key].items()})
    json.dump(out,open("robustness.json","w"),indent=1)
