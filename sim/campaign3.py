"""Campaign sim v3 (answers REVIEW_2 P0-1..P0-3).
Changes vs campaign.py:
 * ALL designed carry sources: base c^w, Ride Cards (+10 %/card), archived Seals (bounded: +1 %/cleared world), achievements 1.05^rows*1.01^count (80 % fill).
 * Ride rule: ride when it would raise production by >= RIDE_GAIN (default 1.5x) -> well defined from ride 1; seals mult modes 'lin' (1+b*s) and 'pow' ((1+s)^p).
 * T_w auto-calibrated so the first ride (>= 2 seals) lands at ~8 min of play in every world (fixes first-ride drift, REVIEW_2 2.4).
 * Gate G_w auto-calibrated by bisection so a reference player (3 sessions/day, gaps 5h/8h/11h) clears the world in TARGET days -> output is the gate-size schedule needed.
 * Goals counted once per world (unique (tier,count) + one per ride); sessions with a new unique goal; all 9 worlds printed.
 * Exact time stamps; clear time = wall-clock day when the player *returns* and sees the gate completed (session granularity stated)."""
import math, json, sys
import numpy as np
from sim import Config, tier_mult

CFG=Config(n_tiers=8,base_cost=15.0,growth=1.12,tier_cost_ratio=8,tier_rate_ratio=6,milestones=(10,25,50,100,200))
GAPS_3=[5*3600-600, 8*3600-600, 11*3600-600]       # sessions ~08:00, 13:00, 21:00 -> gaps 5h,8h,11h (incl. 10 min play)
def off_eff(dur,cap_h=8,e1=.5,e2=.25,k=2*3600):
    d=min(dur,cap_h*3600); return min(d,k)*e1+max(0,d-k)*e2

def carry_total(w, c=3.0, cards=True, archive=True, ach=True):
    m=c**w
    if cards: m*=1+0.10*w
    if archive: m*=1+0.01*w
    if ach:
        cnt=int(16*w*0.8); m*=1.05**(cnt//8)*1.01**cnt
    return m

class World:
    def __init__(s,w,carry,cost_scale,T,goal,bonus=0.08,mode="lin",p=0.5,ride_gain=1.5,cfg=CFG):
        s.cfg=cfg;n=cfg.n_tiers;s.n=n;s.carry=carry;s.T=T;s.goal=goal;s.bonus=bonus;s.mode=mode;s.p=p;s.ride_gain=ride_gain
        s.c0=[cfg.base_cost*cfg.tier_cost_ratio**i*cost_scale for i in range(n)]; s.r0=[cfg.base_rate*cfg.tier_rate_ratio**i for i in range(n)]
        s.owned=[0]*n; s.gold=s.c0[0]; s.life=0.0; s.run_life=0.0; s.t=0.0; s.seals=0.0; s.maxtier=0
        s.uniq=set(); s.rides=[]; s.goal_sessions=set(); s.cur=0; s.ride_sessions=set(); s.first_ride_t=None; s.scale=1.0; s.no_ride=False; s.cooldown=0.0; s.last_ride=-1e18
    def smult(s,seals): return 1+s.bonus*seals if s.mode=="lin" else (1+seals)**s.p
    def unit_out(s,i,n): return n*s.r0[i]*tier_mult(n,s.cfg)
    def prod(s): return s.scale*s.carry*s.smult(s.seals)*sum(s.unit_out(i,s.owned[i]) for i in range(s.n))
    def pend(s): return math.floor(math.sqrt(s.run_life/s.T))
    def mark(s,key):
        if key not in s.uniq: s.uniq.add(key); s.goal_sessions.add(s.cur)
    def done(s): return s.life>=s.goal
    def advance(s,end):
        while True:
            P=s.prod(); best=None
            for i in range(s.n):
                if not (i==0 or s.owned[i-1]>=5): continue
                c=s.c0[i]*s.cfg.growth**s.owned[i]
                g=(s.unit_out(i,s.owned[i]+1)-s.unit_out(i,s.owned[i]))*s.scale*s.carry*s.smult(s.seals)
                w=max(0,(c-s.gold)/P) if P>0 else (0 if c<=s.gold else math.inf)
                sc=c/g+w
                if best is None or sc<best[0]: best=(sc,i,c,w)
            _,i,c,w=best
            # time to goal completion within this window?
            if P>0 and s.goal-s.life<=P*min(w,end-s.t) and s.goal>s.life:
                dt=(s.goal-s.life)/P; s.t+=dt; s.gold+=P*dt; s.life=s.goal; s.run_life+=P*dt; return
            if not math.isfinite(w) or s.t+w>end:
                if P>0: d=end-s.t; s.gold+=P*d; s.life+=P*d; s.run_life+=P*d
                s.t=end; return
            s.t+=w; s.gold+=P*w-c; s.life+=P*w; s.run_life+=P*w; s.owned[i]+=1; s.maxtier=max(s.maxtier,i)
            if s.owned[i]==1 or s.owned[i] in s.cfg.milestones: s.mark(("t",i,s.owned[i]))
            p=s.pend()
            if s.maxtier>=3 and p>=1 and not s.no_ride and s.t-s.last_ride>=s.cooldown:
                new=s.seals+p
                if s.smult(new)/s.smult(s.seals)>=s.ride_gain:
                    s.seals=new; s.last_ride=s.t; s.rides.append((s.t,s.seals)); s.mark(("ride",len(s.rides))); s.ride_sessions.add(s.cur)
                    if s.first_ride_t is None: s.first_ride_t=s.t
                    s.owned=[0]*s.n; s.gold=s.c0[0]; s.run_life=0.0; s.maxtier=0

def calibrate_T(carry,cost_scale,target_s=480,mode="lin",bonus=.08,p=.5,seals_needed=None):
    """T so that sqrt(run_life(8 min)/T) = seals needed for ride_gain (1.5x)."""
    if seals_needed is None: seals_needed=math.ceil((0.5/bonus)) if mode=="lin" else 2  # lin: 1+b*s>=1.5 -> s>=0.5/b ; pow: (1+s)^.5>=1.5 -> s>=1.25
    W=World(0,carry,cost_scale,1e300,1e300,bonus,mode,p)  # no rides possible (T huge)
    W.advance(target_s); return W.run_life/(seals_needed**2)

def play(w,gates,carry,cost_scale,T,mode="lin",bonus=.08,p=.5,gaps=GAPS_3,spd=3,max_days=300):
    W=World(w,carry,cost_scale,T,gates,bonus,mode,p); day=0
    for d in range(max_days):
        for k in range(len(gaps)):
            W.cur=d*len(gaps)+k
            W.advance(W.t+600)
            if W.done(): W.t_exact=W.t; return W,W.cur+1
            e=off_eff(gaps[k]); P=W.prod()
            if P>0 and W.life+P*e>=W.goal: W.t_exact=W.t+gaps[k]*((W.goal-W.life)/(P*e))
            else: W.t_exact=None
            W.gold+=P*e; W.life+=P*e; W.run_life+=P*e; W.t+=gaps[k]
            if W.done(): return W,W.cur+1
    return W,W.cur+1

def calibrate_goal(w,carry,cost_scale,T,target_days,lo=1e6,hi=1e40,iters=26,**kw):
    for _ in range(iters):
        mid=math.sqrt(lo*hi); W,ns=play(w,mid,carry,cost_scale,T,**kw)
        days=W.t/86400
        if W.done() and days<=target_days: lo=mid
        else: hi=mid
    return lo

def campaign(target=lambda w:3.5, c=3.0, s=3.0, n=9, flags=(True,True,True), mode="lin", bonus=.08, p=.5, verbose=True):
    rows=[]; prevG=None
    for w in range(n):
        car=carry_total(w,c,*flags); cs=s**w
        T=calibrate_T(car,cs,mode=mode,bonus=bonus,p=p)
        G=calibrate_goal(w,car,cs,T,target(w),**({'lo':prevG/30,'hi':prevG*3e3,'iters':22} if prevG else {'lo':1e8,'hi':1e30,'iters':26}),mode=mode,bonus=bonus,p=p)
        W,ns=play(w,G,car,cs,T,mode=mode,bonus=bonus,p=p)
        hit=sorted(W.goal_sessions); dry=np.diff([-1]+hit+[ns])-1
        row=dict(world=w+1,days=W.t/86400,rides=len(W.rides),final_seals=W.seals,final_mult=W.smult(W.seals),carry=car,G=G,T=T,
                 first_ride_min=(W.first_ride_t/60 if W.first_ride_t else None),uniq_goals=len(W.uniq),sessions=ns,
                 frac_sessions_new_goal=len(hit)/ns,max_dry=int(dry.max()),frac_sessions_ride=len(W.ride_sessions)/ns,
                 G_growth=(G/prevG if prevG else None))
        prevG=G; rows.append(row)
        if verbose: print(f"W{w+1}: {row['days']:.2f}d rides {row['rides']:3d} seals {row['final_seals']:.3g} mult {row['final_mult']:.3g} carry {car:.3g} G {G:.3g} (x{row['G_growth'] or 1:.2f}) T {T:.3g} first ride {row['first_ride_min'] and round(row['first_ride_min'],1)} min | goals {row['uniq_goals']} sess w/ new goal {row['frac_sessions_new_goal']:.2f} max dry {row['max_dry']} sess w/ ride {row['frac_sessions_ride']:.2f}")
    return rows

if __name__=="__main__":
    out={}; c=float(sys.argv[1]) if len(sys.argv)>1 else 2.25
    for name,kw in {"lin8":dict(mode="lin",bonus=.08),"pow0.5":dict(mode="pow",p=.5)}.items():
        print("==",name,"c=",c,"s=3, all carry sources",flush=True); out[name]=campaign(target=lambda w:3.5,c=c,s=3.0,**kw)
    json.dump(out,open(f"campaign3_c{c}.json","w"),indent=1,default=float)
