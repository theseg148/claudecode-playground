"""Event-layer budget sims (answers events_and_choices.md 5.9 items 1-3).
1. Photo Window: share of daily progress from windows for a 3x10 min/day player.
2. Form Deck: 6 forms x 3 slots (3:2:1): spread of the best loadouts when forms are built from a fixed power budget.
3. Achievement multiplier 1.05^rows * 1.01^count: size vs world carry."""
import random, itertools, json, numpy as np
random.seed(1); np.random.seed(1)   # seeded (REVIEW_2 P1-8)
# ---- 1. windows
OUT=[("windfall",.35),("frenzy",.30),("quick",.15),("spotlight",.15),("card",.05)]
def window_value(bank_s, develop=False):
    """value in seconds-of-production"""
    r=random.random(); acc=0
    for name,w in OUT:
        acc+=w
        if r<=acc: break
    v={"windfall":min(0.15*bank_s,600)+13,"frenzy":6*45,"quick":3*10*0.1*20,"spotlight":2*0.3*30,"card":0}[name]
    if develop: v*= 2 if random.random()<.5 else .5
    return v
def session_windows(hit=0.6, gap=(90,240), dur=600, develop=False, bank_s=450):
    # bank_s = production-seconds of spendable stock when the window opens; windfall = min(15 % of stock, 600 s)+13 s
    t=0; tot=0; n=0
    first=random.uniform(150,180)
    t=first
    while t<dur:
        n+=1
        if random.random()<hit: tot+=window_value(bank_s,develop)
        t+=random.uniform(*gap)
    return tot,n
def daily_share(spd=3, hit=0.6, develop=False, trials=2000, exposures_cap=6, offline_eff_avg=0.31):
    ws=[];
    for _ in range(trials):
        # first session of the day opens with a large stock (overnight accrual ~ 8h*0.31 = 8900 production-seconds); others ~450 s
        s=session_windows(hit,develop=develop,bank_s=8900)[0]+sum(session_windows(hit,develop=develop)[0] for _ in range(spd-1))
        s+=min(exposures_cap, 8*3600//1800)*window_value(450)*0.5*(spd>0)   # banked exposures, taken at half EV (delivered as a strip) — one night
        ws.append(s)
    window_s=float(np.mean(ws))
    base=spd*600 + (86400-spd*600)*0*0  # active seconds of production
    # offline: each gap earns off_eff for up to 8h: use eff_avg*min(gap,8h)
    gap=86400/spd-600; offline_s=spd*min(gap,8*3600)*offline_eff_avg
    return window_s, base, offline_s, window_s/(base+offline_s+window_s), window_s/(base+window_s)
for spd in (1,3,6):
    for hit in (0.3,0.6,0.9):
        w,b,o,share_day,share_active=daily_share(spd,hit)
        print(f"spd{spd} hit{hit}: windows {w:.0f}s-prod/day; active {b:.0f}; offline {o:.0f}; share of daily {100*share_day:.1f}%  share of active-session gain {100*share_active:.0f}%")
# ---- 2. form deck
def deck_spread(n_trials=400, budget=1.0):
    spreads=[]
    for _ in range(n_trials):
        forms=[]
        for f in range(6):
            w=np.random.dirichlet([1,1,1])                 # split budget across (production, offline, charge)
            forms.append(w*budget)
        # value of deck = sum over slots strength*(prod + 0.6*offline + 0.4*charge) -> weights express how much each axis is worth to progress
        val=lambda f:f[0]*1.0+f[1]*0.6+f[2]*0.4
        vs=[]
        for perm in itertools.permutations(range(6),3):
            vs.append(sum(s*val(forms[i]) for s,i in zip((3,2,1),perm)))
        vs=sorted(vs,reverse=True); spreads.append(vs[0]/vs[2]-1)
    return float(np.mean(spreads)), float(np.percentile(spreads,90))
print("deck spread (top1 vs top3) random budget split:",deck_spread())
def deck_stats(n=400):
    best_med=[];best_worst=[]
    for _ in range(n):
        forms=[np.random.dirichlet([1,1,1]) for _ in range(6)]
        val=lambda f:f[0]+0.6*f[1]+0.4*f[2]
        vs=sorted(sum(s*val(forms[i]) for s,i in zip((3,2,1),p)) for p in itertools.permutations(range(6),3))
        best_med.append(vs[-1]/vs[len(vs)//2]-1); best_worst.append(vs[-1]/vs[0]-1)
    return float(np.mean(best_med)),float(np.mean(best_worst))
print("deck best vs median / best vs worst: +%.1f%% / +%.1f%%"%tuple(100*x for x in deck_stats()))
# equalised axes (every form has same value 1.0 but different shape): spread 0
# ---- 3. achievement multiplier
for w in (1,3,6,9):
    rows=2*w; cnt=16*w; m=1.05**rows*1.01**cnt
    print(f"world {w}: {cnt} achievements {rows} rows -> x{m:.2f}")
