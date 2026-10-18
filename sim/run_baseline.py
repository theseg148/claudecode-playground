import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from sim import *
cfg = Config()
r = simulate(cfg)
print(len(r["events"]), goal_gap_stats(r["events"], cfg))
fig, ax = plt.subplots(1,2, figsize=(11,4))
t,g = zip(*r["trace"]); ax[0].semilogy(np.array(t)/60, np.maximum(g,1)); ax[0].set_xlabel("min"); ax[0].set_title("gold")
ms = milestone_events(r["events"], cfg); ax[1].semilogy(np.array(ms)/60, np.diff([0]+ms)+1e-3,"o-"); ax[1].set_title("gap between goals (s)"); ax[1].set_xlabel("min")
plt.tight_layout(); plt.savefig("baseline.png", dpi=100)
