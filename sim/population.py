"""Campaign length for player archetypes (sessions/day) under the two recommended world-scaling variants."""
import json
from campaign import campaign
res={}
for spd,label in [(1,"1/day (very light)"),(2,"2/day (light)"),(3,"3/day (casual)"),(4,"4/day"),(6,"6/day (heavy)")]:
    for name,(cs,cr) in {"flat (3/3)":(3,3),"gentle (3/2.8)":(3,2.8),"lengthening (3/2.5)":(3,2.5)}.items():
        o=campaign(cs,cr,goal_mult=1e18,spd=spd)
        days=[x['days'] for x in o]; res[f"{label}|{name}"]={"world_days":days,"total_days":sum(days),"min_goal_sessions":min(x['frac_sessions_with_goal'] for x in o),"max_dry":max(x['max_dry_sessions'] for x in o)}
        print(f"{label:20s} {name:20s} total {sum(days):6.1f} d  worlds {[round(d,1) for d in days]}  min sessions-with-goal {min(x['frac_sessions_with_goal'] for x in o):.2f} max dry {max(x['max_dry_sessions'] for x in o)}")
json.dump(res,open("population.json","w"),indent=1)
