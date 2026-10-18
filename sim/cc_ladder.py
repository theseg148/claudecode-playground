"""Sanity check of R2 against Cookie Clicker's real ladder (formula from games/cookie-clicker.md [CODE], ozh mirror main.js L8018-8031).
baseCps = ceil(n^(n*0.5+2)*10)/10 ; basePrice = (n+9+(n<5?0:(n-5)^1.75*5))*10^n*max(1,n-14) (n>=1), Cursor 15/0.1. growth 1.15.
Greedy payback player, no upgrades / no clicking: how do the gaps between 'goals' (first purchase of each building + every 25th/50th/100th) look?"""
import math, numpy as np
from sim import goal_gap_stats, Config
def ladder(n_max=10):
    rows=[(15.0,0.1)]
    for n in range(1,n_max):
        cps=math.ceil(n**(n*0.5+2)*10)/10
        price=(n+9+(0 if n<5 else (n-5)**1.75*5))*10**n*max(1,n-14)
        rows.append((price,cps))
    return rows
def simulate(rows,growth=1.15,horizon=6*3600,milestone=(25,50,100),mm=2.0,start=15.0,click_cps=1.0):
    n=len(rows); own=[0]*n; gold=start; t=0.0; ev=[]
    mult=lambda k:mm**sum(k>=m for m in milestone)
    prod=lambda:click_cps+sum(own[i]*rows[i][1]*mult(own[i]) for i in range(n))
    while t<horizon:
        P=prod(); best=None
        for i in range(n):
            if i>0 and own[i-1]==0 and not (i==1): 
                if i>1 and own[i-1]==0: continue
            c=rows[i][0]*growth**own[i]
            g=((own[i]+1)*rows[i][1]*mult(own[i]+1)-own[i]*rows[i][1]*mult(own[i]))
            w=max(0,(c-gold)/P)
            sc=c/g+w
            if best is None or sc<best[0]: best=(sc,i,c,w)
        _,i,c,w=best
        if t+w>horizon: break
        t+=w; gold+=P*w-c; own[i]+=1; ev.append((t,i,own[i],c))
    return ev,own
if __name__=="__main__":
    rows=ladder(10)
    print("tier cost-ratio vs rate-ratio (R2 band 1.2-1.5):")
    for i in range(1,len(rows)): print(f" tier {i}: cost x{rows[i][0]/rows[i-1][0]:.1f}  rate x{rows[i][1]/rows[i-1][1]:.1f}  ratio {rows[i][0]/rows[i-1][0]/(rows[i][1]/rows[i-1][1]):.2f}")
    for label,ms,mm in [("no upgrades",(),1.0),("x2 at 25/50/100 (approx. upgrade ladder)",(25,50,100),2.0)]:
        ev,own=simulate(rows,milestone=ms,mm=mm)
        cfg=Config(milestones=ms)
        g=np.diff([0]+[e[0] for e in ev if e[2]==1 or e[2] in (ms or (25,50,100))])
        print(label,"| purchases",len(ev),"| owned",own,"| goal gaps median %.0fs p90 %.0fs max %.0fs | in 15-600s: %.0f%% | >30min: %.0f%%"%(np.median(g),np.percentile(g,90),g.max(),100*np.mean((g>=15)&(g<=600)),100*np.mean(g>1800)))
