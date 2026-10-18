# Simulation results (draft v1)
Code: `sim.py` (greedy-payback player), `sweep.py` (512 configs), `worlds.py` (sequential worlds). Charts: `baseline.png`, `sweep_params.png`, `worlds.png`. Raw: `sweep.json`, `worlds.json`.
Model: 8 tiers; cost_i = base*cost_ratio^i * growth^owned; rate_i = rate_ratio^i; x`mm` multiplier at ownership milestones; tier i+1 unlocks at 5 owned of tier i. "Goal" = first purchase of a tier or hitting a milestone count. Satisfying band = 15-600 s between goals; wall = gap > 30 min.

## Sweep (3 h horizon, 512 configs: growth {1.07,1.09,1.12,1.15} x cost_ratio {5,8,12,20} x rate_ratio {4,6,9,14} x 4 milestone sets x mult {2,3})
- Best configs have **cost_ratio / rate_ratio ~ 1.2-1.5** (e.g. 8/6, 12/9, 20/14). Ratio ~1 -> tiers all equally good ROI, no reason to progress, goals arrive in <3 s bursts. Ratio >2 (5/14 inverted or 20/4) -> walls (max gap > 2 h).
- Worst configs: rate_ratio > cost_ratio (higher tiers pay so well the early game is skipped: median gap 0.1-2.5 s, frac in-band 4-8 %) and milestone starting at 5 with x3.
- Growth 1.07-1.15 matters less than ratios: 1.12/8/6/x2 gave 97 % of goals in-band, max gap 344 s, median 46 s, 32 goals in 3 h.
- Milestone multiplier x2 beat x3 on average (x3 compresses early goals and leaves later walls).
- Takeaway: the *shape* (cost ratio slightly above rate ratio between tiers + milestone doublers) beats the exact growth constant. Sweet spot growth 1.10-1.15.

## Sequential worlds
World clear time scales as (cost_scale / carryover)^world. Examples (minutes to clear world 1..6):
- carry x2, cost x3: 8.4, 12.6, 18.8, 28.3, 42.4, 63.6  -> gentle 1.5x lengthening, good "later worlds feel bigger".
- carry x3, cost x3: 8.4 flat -> every world same length.
- carry x2, cost x1: 8.4 -> 0.3 min (carry trivialises later worlds; anti-pattern).
- carry x2, cost x10: 8.4, 42, 209, 1047 min (walls).
Rule: choose cost_scale/carryover in [1.0, 1.5] per world; 1.0 = constant length, ~1.3 = lengthening worlds.
Caveat: toy model; no prestige inside worlds yet, no active-play spikes. See follow-up runs.

## Prestige sweep (108 configs, 6 h horizon, 6 tiers, growth 1.12; prestige_sweep.py / prestige_sweep.json / prestige_first.png)
Params: threshold (1e6/1e8/1e10 lifetime), point exponent (0.4/0.5/0.7), bonus per point (5/10/25 %), player prestiges when mult gain >= {1.5,2,3,5}x.
- Only 23/108 configs give a first prestige at 20-90 min AND >= 3 prestiges in 6 h (the "satisfying" band).
- Threshold 1e8 dominates the good set; 1e6 prestiges so early (<20 min) it's a tutorial reset, 1e10 pushes first prestige past 90 min or never.
- Exponent 0.5-0.7 with rebuy rule "prestige at >= 2x gain" gives a 22-45 min cycle repeating 8-14 times; exponent 0.4 shrinks returns (cycles stretch to ~48 min).
- Strong bonus (25 %/pt, exp 0.7) explodes final multiplier (9e4x) -> numbers outrun content; 5-10 %/pt keeps final mult 2e2-6e3x.
- Rule of thumb: first prestige ~25 min, then cycles 20-45 min, each cycle must be >= 2x faster to repeat the same content. Don't allow prestige before the player has seen >=60 % of the world's tiers.
