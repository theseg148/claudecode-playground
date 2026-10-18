"""Sequential Rider worlds. Each world = fresh generator ladder (cost scaled), carryover mult applied."""
import json, numpy as np
from sim import *
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

def world_time(cfg, carry, goal_owned_top=40):
    """time until the top tier owned >= goal (world complete) under greedy play."""
    r = simulate(cfg, horizon=cfg.horizon_s, start_mult=carry, record=False)
    for (t,i,k,c) in r["events"]:
        if i==cfg.n_tiers-1 and k>=goal_owned_top: return t, r
    return None, r

def run(n_worlds=6, carry_per_world=2.0, cost_scale=1.0, n_tiers=6, goal=25, growth=1.12):
    out=[]; carry=1.0
    for w in range(n_worlds):
        cfg = Config(n_tiers=n_tiers, base_cost=10*cost_scale**w, tier_cost_ratio=8, tier_rate_ratio=6,
                     growth=growth, base_rate=1.0, milestones=(10,25,50,100), horizon_s=40*3600)
        t,r = world_time(cfg, carry, goal)
        s = goal_gap_stats(r["events"],cfg)
        out.append(dict(world=w+1, minutes=None if t is None else t/60, carry=carry, max_gap=s["max"], n_goals=s["n_goals"]))
        carry *= carry_per_world
    return out

if __name__=="__main__":
    results={}
    fig,ax=plt.subplots(1,2,figsize=(12,4))
    for cps in [1.0,1.5,2.0,3.0,5.0]:
        for cs in [1.0, 3.0, 10.0]:
            o=run(carry_per_world=cps,cost_scale=cs)
            results[f"carry{cps}_costscale{cs}"]=o
        o=results[f"carry{cps}_costscale3.0"]
        ax[0].plot([x["world"] for x in o],[x["minutes"] if x["minutes"] else np.nan for x in o],"o-",label=f"carry x{cps}")
    ax[0].set_yscale("log"); ax[0].set_xlabel("world #"); ax[0].set_ylabel("minutes to clear world"); ax[0].legend(); ax[0].set_title("cost_scale=3 per world")
    for cs in [1.0,3.0,10.0]:
        o=results[f"carry2.0_costscale{cs}"]
        ax[1].plot([x["world"] for x in o],[x["minutes"] if x["minutes"] else np.nan for x in o],"o-",label=f"cost x{cs}/world")
    ax[1].set_yscale("log"); ax[1].legend(); ax[1].set_title("carry x2 per world"); ax[1].set_xlabel("world #")
    plt.tight_layout(); plt.savefig("worlds.png",dpi=100)
    json.dump(results,open("worlds.json","w"),indent=1)
    for k,v in results.items(): print(k,[None if x["minutes"] is None else round(x["minutes"],1) for x in v])
