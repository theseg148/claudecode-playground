"""Combined campaign sim v2: sessions + stepped offline + Final Form Ride (sqrt prestige) + world hops with carryover.
Player: 3 sessions/day x 10 min (configurable). Offline: 50% for first 2h, 25% beyond, cap 8h (R23).
World clear: lifetime shots in the world >= goal * cost_scale^w (a gate on cumulative output, so rides help).
Player rides (Final Form) when pending seals >= 2x current seals and >=4 tiers seen (R13,R15)."""
import math, json, numpy as np
from sim import Config, tier_mult

def off_eff_seconds(dur, cap_h=8, e1=0.5, e2=0.25, k=2*3600):
    d=min(dur,cap_h*3600); return min(d,k)*e1+max(0,d-k)*e2

class World:
    def __init__(s, w, cost_scale, carry, cfg, seals_bonus, T0, goal_mult, seals0=0.0):
        s.cfg=cfg; s.n=cfg.n_tiers; s.w=w; s.cs=cost_scale**w; s.carry=carry**w
        s.c0=[cfg.base_cost*cfg.tier_cost_ratio**i*s.cs for i in range(s.n)]
        s.r0=[cfg.base_rate*cfg.tier_rate_ratio**i for i in range(s.n)]
        s.owned=[0]*s.n; s.gold=s.c0[0]; s.life=0.0; s.run_life=0.0; s.t=0.0
        s.seals=0.0; s.sb=seals_bonus; s.T=T0*s.cs; s.goal=goal_mult*s.cs
        s.events=[]; s.rides=[]; s.maxtier=0; s.sess_events=set(); s.cur_sess=0
    def mult(s): return s.carry*(1+s.sb*s.seals)
    def prod(s): return s.mult()*sum(s.owned[i]*s.r0[i]*tier_mult(s.owned[i],s.cfg) for i in range(s.n))
    def avail(s,i): return i==0 or s.owned[i-1]>=5
    def pend(s): return math.floor(math.sqrt(s.run_life/s.T))
    def step_buy(s, end):
        """buy greedily until time `end` (absolute world time); returns when out of time"""
        while True:
            P=s.prod(); best=None
            for i in range(s.n):
                if not s.avail(i): continue
                c=s.c0[i]*s.cfg.growth**s.owned[i]
                g=((s.owned[i]+1)*s.r0[i]*tier_mult(s.owned[i]+1,s.cfg)-s.owned[i]*s.r0[i]*tier_mult(s.owned[i],s.cfg))*s.mult()
                w=max(0,(c-s.gold)/P) if P>0 else (0 if c<=s.gold else math.inf)
                sc=c/g+w
                if best is None or sc<best[0]: best=(sc,i,c,w)
            _,i,c,w=best
            if not math.isfinite(w) or s.t+w>end:
                if P>0: d=end-s.t; s.gold+=P*d; s.life+=P*d; s.run_life+=P*d
                s.t=end; return
            s.t+=w; s.gold+=P*w; s.life+=P*w; s.run_life+=P*w
            s.gold-=c; s.owned[i]+=1; s.maxtier=max(s.maxtier,i)
            if s.owned[i]==1 or s.owned[i] in s.cfg.milestones: s.events.append(s.t); s.sess_events.add(s.cur_sess)
            # ride decision
            p=s.pend()
            if s.maxtier>=3 and p>=max(1,2*s.seals) and s.life<s.goal:
                s.seals+=p; s.rides.append((s.t,s.seals)); s.owned=[0]*s.n; s.gold=s.c0[0]; s.run_life=0.0; s.maxtier=0
                s.events.append(s.t); s.sess_events.add(s.cur_sess)
            if s.life>=s.goal: return
    def done(s): return s.life>=s.goal

def play_world(w, cost_scale, carry, cfg, sb, T0, goal_mult, spd=3, smin=10, e1=.5, e2=.25, cap=8, max_days=200):
    W=World(w,cost_scale,carry,cfg,sb,T0,goal_mult); day=86400; gap=day/spd-smin*60
    for d in range(max_days):
        for k in range(spd):
            W.cur_sess=d*spd+k
            W.step_buy(W.t+smin*60)
            if W.done(): return W
            eff=off_eff_seconds(gap,cap,e1,e2)
            P=W.prod(); W.gold+=P*eff; W.life+=P*eff; W.run_life+=P*eff; W.t+=gap
            if W.done(): return W
    return W

def campaign(cost_scale, carry, n=9, base_cost=15.0, T0=1e6, goal_mult=1e9, sb=0.08, **kw):
    cfg=Config(n_tiers=8,base_cost=base_cost,growth=1.12,tier_cost_ratio=8,tier_rate_ratio=6,milestones=(10,25,50,100,200))
    out=[]
    for w in range(n):
        W=play_world(w,cost_scale,carry,cfg,sb,T0,goal_mult,**kw)
        g=np.diff([0]+W.events) if W.events else np.array([0.])
        ns=int(W.cur_sess)+1; hit=sorted(W.sess_events); gaps=np.diff([-1]+hit+[ns]) -1 if ns else np.array([0])
        out.append(dict(world=w+1,days=W.t/86400,rides=len(W.rides),goals=len(W.events),sessions=ns,frac_sessions_with_goal=len(hit)/ns,max_dry_sessions=int(gaps.max()),
                        med_gap_min=float(np.median(g))/60,max_gap_h=float(g.max())/3600,done=W.done()))
    return out

if __name__=="__main__":
    res={}
    import sys
    gm=float(sys.argv[1]) if len(sys.argv)>1 else 1e9
    for cs,cr in [(3,3),(3,2.8),(3,2.5),(4,3.2)]:
        o=campaign(cs,cr,goal_mult=gm); res[f"s{cs}_c{cr}"]=o
        print(f"cost x{cs} carry x{cr} (ratio {cs/cr:.2f}):", [round(x['days'],1) for x in o], "total d", round(sum(x['days'] for x in o),1),
              "| rides", [x['rides'] for x in o], "| sess w/ goal", [round(x['frac_sessions_with_goal'],2) for x in o][:4], "| max dry sess", [x['max_dry_sessions'] for x in o][:4])
    json.dump(res,open("campaign.json","w"),indent=1)
