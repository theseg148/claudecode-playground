"""Decade campaign: 9 worlds in sequence (Kabuto first). Each world: 6-tier ladder; cost scale s^w; permanent
carryover multiplier after each world = carry^w. World cleared when top tier owned >= goal. 3 sessions/day x 10 min, offline eff 0.5, cap 8h."""
import json, numpy as np
from sim import Config
from sim2 import Player
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
WORLDS=["Kabuto","Den-O","Faiz","Ryuki","Blade","Kiva","Agito","Hibiki","Kuuga"]
def campaign(cost_scale, carry, base0=2e2, goal=25, spd=3, smin=10, eff=0.5, cap=8, max_days=400):
    mult=1.0; out=[]; t_total=0
    for w,name in enumerate(WORLDS):
        cfg=Config(n_tiers=6,base_cost=base0*cost_scale**w,growth=1.12,tier_cost_ratio=8,tier_rate_ratio=6,milestones=(10,25,50,100))
        p=Player(cfg,mult); day=86400; gap=day/spd-smin*60; done=None
        for d in range(max_days):
            for k in range(spd):
                p.play(smin*60)
                if p.owned[-1]>=goal: done=p.t; break
                p.away(gap,eff,cap)
            if done: break
        if done is None: out.append((name,None,None)); break
        # goal-gap stats
        ev=[e[0] for e in p.events if e[2]==1 or e[2] in cfg.milestones]
        g=np.diff([0]+ev)
        out.append((name,done/86400,float(np.max(g))/3600)); mult*=carry
    return out
if __name__=="__main__":
    res={}
    for cs,cr in [(3,3),(3,4),(4,4),(4,5),(5,5),(5,7),(8,8),(8,10)]:
        o=campaign(cs,cr); res[f"cost{cs}_carry{cr}"]=o
        print(f"cost x{cs}/world, carry x{cr}:", [(n, None if d is None else round(d,1)) for n,d,_ in o], "total days", round(sum(d for _,d,_ in o if d),1))
    json.dump(res,open("decade_model.json","w"))
    fig,ax=plt.subplots(figsize=(7,4))
    for k,o in res.items(): ax.plot(range(1,len(o)+1),[d if d else np.nan for _,d,_ in o],"o-",label=k)
    ax.set_yscale("log"); ax.set_xlabel("world # (Kabuto=1)"); ax.set_ylabel("days to clear"); ax.legend(fontsize=7); plt.tight_layout(); plt.savefig("decade_model.png",dpi=100)
