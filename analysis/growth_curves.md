# Growth curves across 37 idle/incremental games

Scope: cost-growth ratios, production scaling, milestone multipliers, unlock pacing. Inputs: all `games/*.md` (37), `research/*.md`, `sim/results.md`.

## 0. Evidence legend (read first)

- CONFIRMED = tags `[CODE]`, `[SRC]`, `[S]` (search snippet of a wiki or official page) in the game file, or `[SOURCE CODE]` in `research/math_of_idle_games.md`.
- ESTIMATED = tags `[M]` memory, `[E]`/`[EST]` estimate, `[unverified]`, `[MEM-LOW]`, `[PUB-ish]`, or the genre default pasted in because the game has no public data. These are NOT game data.
- DERIVED = my arithmetic on cited numbers.
- Only a minority of the 37 games have confirmed cost formulas (about 11). The rest copy the genre default of 1.07-1.15 (for example games/farm-away.md, games/idle-wizard.md, games/spaceplan.md, games/magic-research.md, games/guava-juice-tub-tapper.md, games/factory-idle.md, games/mr-mine.md), which cannot be used as independent evidence. Do not count them when averaging.
- Caveat on confirmed items: several `[S]` numbers come from search snippets only and some earlier numbers were corrected in the verification passes (NOTES.md run 1). The verification logs inside the game files are the final word.

## 1. Cost-growth ratios (price of the n-th unit = base * r^n)

### 1.1 Confirmed values

| Game (file) | r (per owned unit) | Evidence | Notes |
|---|---|---|---|
| Adventure Capitalist (games/adventure-capitalist.md) | 1.15 Newspaper, 1.14 Car Wash, 1.13 Pizza; community table falls 1.15 -> 1.07 across 10 tiers (Lemonade 1.07, Oil 1.07) | S for rows 2-4; the other rows unverified; the math file copies the whole table from a secondary GitHub synthesis | r falls 0.01 per tier; base cost x12 per tier (60, 720, 8,640 ...) per research/math_of_idle_games.md section 5.1 [DERIVED from secondary] |
| Cookie Clicker (games/cookie-clicker.md) | 1.15 | public wiki, confirmed also in research/math_of_idle_games.md 5.2 (S) | price doubles every ~5 buys; base price x10-15 per tier (15, 100, 1,100, 12,000 ...) is "recall" (M) |
| Clicker Heroes (games/clicker-heroes.md) | 1.07 hero cost (6.975%/level, doubling about every 10 levels); monster HP x1.145 per zone from zone 140 to 500 | S | HP doubles about every 5.1 zones [DERIVED]. Ace Scouts use 1.22 |
| Universal Paperclips (games/universal-paperclips.md) | 1.07 for MegaClipper (1000 * 1.07^n; table checked) | S | AutoClipper `1.07^level + 5` is M |
| Kittens Game (games/kittens-game.md, research/design_talks_postmortems.md 3.7) | 49 entries at 1.15; field 1.12, mine 1.15, barn 1.75, hut 2.5, space 1.12-1.18; others 1.10, 1.18, 1.25, 1.35, 1.5, 2 | CODE (research file); the game file's own ratios are tagged M and agree | production 1.12-1.15, storage/housing 1.75-2.5 |
| Synergism (games/synergism.md) | 1.25 buildings; 1.03 "late building" plus factorial segment after thresholds 1,000 / 5,000 / 20,000 / 25,000 / 250,000 owned (scaled by a "reduction" factor) | SRC | the player can push the walls out, not cheapen single buys |
| Antimatter Dimensions (games/antimatter-dimensions.md, research/math_of_idle_games.md 4) | per batch of 10: cost x1e3 (dim 1) up to x1e15 (dim 8); base costs 10, 100, 1e4, 1e6, 1e9, 1e13, 1e18, 1e24; tickspeed cost x10 per buy | SRC (math file) / S (game file; middle values unverified there) | equivalent to r = 1e3^(1/10) = 1.995 per single unit for dim 1 and 1e15^(1/10) = 31.6 for dim 8 [DERIVED]; compensated by x2 per batch |
| Bitburner (games/bitburner.md) | Hacknet node purchase x1.85; level upgrade 1.04; RAM upgrade 1.28; core upgrade 1.48; every augmentation bought in a run multiplies all remaining aug prices by 1.9; NeuroFlux Governor 1.14 per level | SRC | the clearest example of a deliberately steep "soft-reset batch" cost |
| Leaf Blower Revolution (games/leaf-blower-revolution.md) | shop items 3.5 / 3 / 3 / 1.5 (Golden Marketing, Max Combo, Combo Multiplier, Nuclear Fuel); tools 1.1-1.2 is E | S (shop); E (tools) | permanent shop items are far steeper than in-run items |
| Trimps (games/trimps.md) | perks (He currency) x1.3 per level with caps (Coordinated cap 15, Anticipation cap 10); linear perks base + 500/level; equipment about 1.2 (M) | S (perks) | caps instead of walls |
| Evolve (games/evolve.md) | 1.1-1.35 per structure (M); code reads `base * multiplier^count` | SRC for formula shape, M for values | |
| NGU Idle (games/ngu-idle.md) | Augmentations: cost = base * n (linear), upgrade cost n^2 | S | not exponential; "1.1^level" is unverified |
| Progress Knight (games/progress-knight.md) | XP need `base * (level+1) * 1.01^level` | CODE | effective per-level growth is only about 1.01-1.02 |
| A Dark Room (games/a-dark-room.md) | linear: trap `(n+1)*5` wood cap 30; hut `20 + 60n` wood cap 20 (mobile) | S | pacing by timers and caps |
| Melvor Idle (games/melvor-idle.md) | skill XP gap doubles about every 7 levels (L99 = 13,034,431 XP; L120 = 104,273,167) | S | RuneScape curve; equipment 5-10x per tier is unverified |
| Realm Grinder (games/realm-grinder.md) | base costs Farm 10, Inn 125, Blacksmith 600 (S); multiplier "1.08-1.15" unverified | S / unverified | |

### 1.2 Estimated or genre-default values (not evidence)
- Idle Miner Tycoon (games/idle-miner-tycoon.md): 1.1-1.3 per level, shaft x2-3 per new shaft [E].
- Idle Wizard 1.15, Idle Breakout 1.1-1.15, Idle Champions 1.07, Tap Titans 2 1.07-1.1, Cell to Singularity 1.07-1.15, Spaceplan 1.15, Magic Research 1.10-1.20, Idle Mining Empire 1.07-1.15 and x3-10 per shaft, Mr. Mine 1.1-1.2, Farm Away 1.07-1.15, Factory Idle 1.15, Guava Juice 1.15, Slayer 1.1-1.2, Reactor tier x5-20 and upgrades x2-10, Swamp Attack 1.3-1.6 per tier (all `[EST]`).
- AFK Arena (games/afk-arena.md): hero level cost about 1.02-1.05 per level and enemy power +3-5% per stage [EST]; income is a stage lookup table, not a ratio.
- Candy Box 2 (games/candy-box-2.md), Increlution (games/increlution.md), Swamp Attack: no exponential buildings at all; income is additive via equipment, polynomial progress, or mission index.
- Research-level rules of thumb: 1.07-1.15 (Pecorella via research/math_of_idle_games.md 1.2), Idle Idol 1.1 (costs overtook rewards at about level 35), Idle Ronin 14% -> 12.5% -> 11.5% by level band.

### 1.3 What the ratios mean (DERIVED, research/math_of_idle_games.md 1.3)
| r | buys to double price | buys to x10 | price after 25 | after 100 |
|---|---|---|---|---|
| 1.07 | 10.2 | 34 | x5.4 | x868 |
| 1.10 | 7.3 | 24 | x10.8 | x13.8k |
| 1.15 | 5.0 | 16.5 | x32.9 | x1.17M |
| 1.25 | 3.1 | 10.3 | x265 | x4.9e9 |

### 1.4 Derived range (confirmed games only)
- Production units (the thing you buy hundreds of): **1.07-1.15**, centre 1.12-1.15. Confirmed in AdCap, Cookie Clicker, Clicker Heroes, Paperclips, Kittens (production), Evolve (M).
- Walls, caps and capacity: **1.25-2.5** (Kittens storage/housing, Synergism 1.25, Bitburner 1.28-1.85, Leaf Blower shop 3-3.5, Trimps perk 1.3 with cap). Rule: the steeper the ratio, the lower the intended owned count (cap 10-30) or the more the item is a one-time permanent unlock.
- Within one game the ratio usually moves with tier: AdCap lowers r 0.01 per tier (1.15 -> 1.07); Idle Ronin lowers by band; Synergism switches from 1.25 to 1.03 + factorial late. So "cheaper to climb at the top" is a recurring pattern.
- Base cost between tiers: x12 (AdCap, S/secondary), x10-15 (Cookie Clicker, M), x10 to x1e15 per batch (AD, SRC).
- Simulation result (sim/results.md): growth between 1.07 and 1.15 mattered less than the ratio between tiers; the sweet spot was growth 1.10-1.15 with cost_ratio / rate_ratio about 1.2-1.5 (examples 8/6, 12/9, 20/14).

## 2. Production scaling

| Game | Production model | Per-tier ratio | Evidence |
|---|---|---|---|
| Cookie Clicker | `count * base_cps * multipliers`; base CPS 0.1, 1, 8, 47, 260, 1,400, 7,800 ... | CPS about x5-7 per tier vs price x10-15 (games/cookie-clicker.md) | M (recall) |
| Adventure Capitalist | `owned * base_revenue * mult`, cycle 0.6 s to 36,864 s | revenue 0.5-0.75 of base cost, cycle x2 then x4 per tier | secondary / M |
| Antimatter Dimensions | dim N feeds dim N-1; polynomial `x^n/n!` growth; x2 per 10 bought; tickspeed x1.124 per buy (x0.89) then +2%/galaxy | cost x1e3..1e15 per batch vs output x2 | S/SRC |
| Clicker Heroes | hero DPS x4 per 25 levels from 200, x10 at 1000, 2000 ... 8000 | price x5.43 per 25 levels vs damage x4 [DERIVED, math file] | S |
| Paperclips | MegaClipper = 500 AutoClippers of output | x500 per tier at x1.07 cost | S |
| Egg Inc | egg value ladder 0.25, 1.25, 6.25, 30, 150, 700, 3,000, 50,000, ... (x5 early, uneven later) | farm-value gates, e.g. Superfood ~10M, Medical ~840M, Rocket Fuel ~38B | S |
| Kittens Game | `base * count * (1 + additive bonuses)` then multiplicative paragon/religion layers; 5 ticks/s | n/a | M / CODE |
| Progress Knight | job income `1 + log10(level+1)` ; max-level XP `1 + maxLevel/10`; lifespan `1 + log33(level+1)` | log-shaped | CODE |
| Synergism | diminishing-return powers 0.5, 0.4 ... 0.15 on many outputs; softcap at 1e15 with exponent 1/8 | n/a | SRC |
| Evolve | log curves on plasmid and dark-energy power (`log(50+x)`) | n/a | SRC |
| Melvor | action interval fixed (3 s woodcutting) reduced by upgrades; XP doubling every 7 levels | n/a | S |
| Bitburner | Hacknet income `level * 1.5 * 1.035^(ram-1) * (cores+5)/6`; hack money fraction `/240` per hack | n/a | SRC |

Patterns:
1. Cost exponential, production linear in owned count, boosted by multiplier gates. Gates convert linear counts to exponential output (all of AdCap, AD, Clicker Heroes per research/design_talks_postmortems.md section 5).
2. Chained-tier (AD style, "generators produce generators") gives polynomial growth degree N (4-8 tiers recommended, research/math_of_idle_games.md section 2).
3. Late-game production inside a layer almost always uses a log or fractional exponent (Progress Knight log10/log33/log13, Evolve log, Synergism powers 0.15-0.5). This keeps a single permanent upgrade from dominating.
4. Production ladders with confirmed numbers have **price ratio above output ratio** by about 1.2-2x per tier (Cookie Clicker 10-15x price vs 5-7x CPS; CH x5.43 price vs x4 damage per 25 levels; sim best band 1.2-1.5). Inverted ladders produce "skip the early game" (sim/results.md).

## 3. Milestone multipliers

| Game | Milestone rule | Evidence |
|---|---|---|
| Adventure Capitalist | cycle time halved at 25, 50, 100, 200, 300, 400 owned (per business), and again at same marks across all businesses; max 12 halvings = 1/4096; x3 profit at 100 by a forum post; x2 to x11 profit steps and global x3 at 100-of-everything come from the secondary synthesis | S (halving rule); unverified (x3/x4 steps) , games/adventure-capitalist.md |
| Antimatter Dimensions | x2 per 10 purchased of that dimension | S/SRC |
| Clicker Heroes | x4 per 25 levels from 200, x5 per 25 for later heroes 525-725, x10 at 1000, 2000 ... 8000 | S (math file, wiki excerpt) |
| Cookie Clicker | tier upgrades double a building at about 1, 5, 25, 50, 100 owned, cost about 10x base | M (games/cookie-clicker.md) |
| Idle Miner Tycoon | x2 at fixed levels every 25/50/100 (10/25/50 variants) | M/E |
| Idle Mining Empire, Idle Wizard, Spaceplan, Farm Away, Factory Idle | x2 at 10/25/50/100 or 25/50/100/200 | EST copied from genre |
| Trimps | each equipment prestige tier x1.19-1.5 stats | E |
| Tap Titans 2 / Hero games | per-hero milestone doublings | E |
| Cell to Singularity | x2 at preset node levels | E |

Derived design rule (research/design_talks_postmortems.md 4.2): choose multiplier M and spacing S such that **M approx r^S**. At r = 1.07, S = 10 gives x1.97 so a x2 every 10 buys neutralises price growth; at r = 1.15, S = 5 gives x2.01; CH uses S = 25 with M = 4 vs 5.43 price.
- Typical spacing: 10 (AD), 25-100 (AdCap, CC, CH), power-of-two-ish multiplier each time.
- Sim result (sim/results.md): x2 milestones beat x3 on average; x3 compresses early goals and leaves later walls; starting milestones at 5 with x3 is among the worst configs.

## 4. Unlock pacing

### 4.1 First prestige / first reset (time to first)
| Game | Time | Evidence |
|---|---|---|
| Synergism | 15-30 min (coins 1e16-ish) | M/EST |
| Idle Breakout | ~30 min | EST |
| Idle Miner Tycoon | 30-60 min to first mine prestige | E |
| Magic Research | 30-90 min | EST |
| Tap Titans 2 | ~1 h (stage 60+) | EST |
| Clicker Heroes 2 | 30-90 min | EST |
| Adventure Capitalist | 1-2 h (angels) | unverified |
| Leaf Blower Revolution | 1-2 h | E |
| Clicker Heroes | first ascension about zone 100-130, 1-2 h | one guide S for zone 130; time unverified |
| Evolve | first MAD 1-3 h (2-4 h in another line of the same file) | EST |
| Idle Slayer | 2-4 h, later 20-60 min cycles | E |
| Bitburner | first augmentation install 3-6 h; first BitNode 12-30 h | MEM/EST |
| Reactor Incremental | 2-6 h | EST |
| Factory Idle | 3-6 h | EST |
| Antimatter Dimensions | first Infinity 30 min-2 h in the game file (unverified) vs "few hours to 2 days" (community, research file) | conflicting estimates |
| Idle Mining Empire | 1-2 days | EST |
| Mr. Mine | 1-3 days | EST |
| Farm Away | ~1 day | EST |
| Kittens Game | first reset 20-50 h | E |
| Trimps | first portal Z30-50 on day 1 | E |
| Cookie Clicker | ascension possible at 1e12 cookies for 1 chip; guides advise waiting for 200+ chips | S (formula) , guides low quality |
| Progress Knight | first rebirth immediate (life-length based); first evil in 10-30 lives | EST |
| None: A Dark Room, Candy Box 2, Spaceplan, Paperclips, Melvor, Swamp Attack, AFK Arena | finite arc or monotonic progress | |

Median of the estimates: first prestige 1-2 h in mobile/web idles, 15-30 min in the fastest, days only in the slow mobile ones. Research recommendation: first purchase under 60 s, first automation about 3 min, first prestige 10-15 min (single-author heuristics; design_talks 4.3); dev postmortem: first prestige took 25-35 min for most players and bounce before first reset is the churn (research/player_complaints.md C6). Sim sweet spot: first prestige about 25 min, then cycles of 20-45 min (sim/results.md).

### 4.2 Cadence of new content
- A Dark Room: stage names tied to hut counts (1, 2-4, 5-8, 9-14, 15-20 huts) S; Lodge/Trading Post at 30-60 min; whole game 3-5 h E (games/a-dark-room.md).
- Cookie Clicker: building revealed at 1/3-1/2 of price; first real time gate (sugar lumps) at about 1 day (games/cookie-clicker.md).
- Egg Inc: egg tiers gated by farm value (10M, 840M, 38B, 27T, 8Q, 3.6 quintillion) = **x45 to x710 per egg unlock, geometric mean about x200** [DERIVED from S gates; wall-clock unverified].
- Paperclips: new project every few minutes; phase 1 ends in 2-3 h; total 4-10 h (games/universal-paperclips.md; author says 4-6 h in research file).
- Spaceplan: new item/dialogue every 3-10 min E.
- Cell to Singularity: new tree node every 30-60 s, new era every 20-40 min E.
- NGU Idle: features unlocked day by day (day 0 energy/magic/augments, day 1 rebirth, day 3+ NGU etc.) E.
- AD layers (community estimates, unverified): Infinity hours-2 days, Eternity 1-3 days / 2 days-1 week, Reality 1-3 weeks / 1-4 weeks, Celestials weeks-months.
- Progression layer width: each AD layer is ~308 orders of magnitude (SRC), Synergism layers use ever-smaller exponents.

### 4.3 Offline pacing (related lever)
- Confirmed caps: Melvor 24 h (12 h in 0.13, 18 h in 1.0 beta) S; Synergism 3 days base + 4 h per level of two researches SRC; Bitburner offline hacking at 75% SRC; Cookie Clicker 5% of CpS for 1 h (then x0.1) with upgrades up to 91% for 7 d 8 h S; AFK Arena chest cap 12 h (PUB).
- Genre rules: cap 2-24 h, rate 50% (research 4.5). Sim (sim/results.md): offline efficiency 0 -> 0.25 speeds a 3x10-min/day player about 9x; 0.25 -> 1.0 only about 2x; 3 -> 12 sessions/day only 1.5x at eff 0.5. Recommended eff 0.5 with an 8 h cap.

## 5. Typical ranges (what to copy)
| Parameter | Typical range | Confidence |
|---|---|---|
| Cost ratio, production tiers | 1.07-1.15 (median ~1.12-1.15) | confirmed in 5+ games |
| Cost ratio, caps and one-time perma shop | 1.25-3.5 | confirmed in 4 games |
| Price doubling | every 5-10 buys | derived |
| Tier-to-tier base cost | x10-x15 (AdCap x12) | AdCap secondary, CC recall |
| Tier-to-tier output | x5-x10 (cost/output ratio 1.2-2) | CC recall, CH derived, sim |
| Milestone multiplier | x2 (sometimes x3-x4 later) every 10-25 owned; M ~ r^S | confirmed in AD, CH, AdCap halving |
| Number of tiers | 8-10 (AD 8, AdCap 10, CC 15-20) | confirmed |
| First prestige | 15-60 min fast designs; 1-3 h typical; days in slow mobile | estimated |
| Cycle after first prestige | 20-45 min, each cycle 2-4x faster than the first | sim + guides |
| Offline | 50% rate, 8 h cap (2-24 h seen) | sim + survey |

## Implications for Kamen Rider Decade world-progression idle game (no fighting, upgrade-focused)

1. Use the confirmed AdCap shape as the skeleton for each world: 8-10 upgrade tracks per Rider world ("Ride Cards", forms, allies), cost ratio per owned unit 1.15 at the cheap end falling to 1.07 at the expensive end, base cost x10-12 per tier, output x6-9 per tier (cost/output about 1.2-1.5 per sim). Do not copy unverified genre-default ratios as if proven.
2. Put x2 milestones every 10-25 purchases with M ~ r^S (r=1.12 -> x2 per 6; r=1.10 -> x2 per 7-10). Show the next milestone on each card (AdCap lesson). Prefer x2 over x3 (sim).
3. Use steep ratios (1.3-3.5) only for one-time or capped items: world-unlock gates, Driver/Form slots, permanent shop. Cap counts (Trimps perk caps 10-15, A Dark Room trap cap 30, hut cap 20) to give predictable pacing instead of walls.
4. Make a Rider world last 3-5 days of a 3-sessions-a-day player (sim sizing) for the main arc, but first world gate within 10-25 minutes, and first "Final Form Ride" (prestige-like boost) at about 25 min. Per-world clear time should scale as (cost_scale / carryover)^world with the ratio held in [1.0, 1.5] (sim: 1.3 gives 1.3x longer worlds; ratio below 1 trivialises; ratio 10 makes walls).
5. Pace with Egg Inc style gates: world n+1 content unlocks at a multiple of the previous gate in value (Egg Inc uses x45-x710, geometric mean x200; a smaller x10-x50 step suits a short per-world arc), not at fixed time; add "stage name" feedback à la A Dark Room per development level, and a new reveal every 3-10 minutes early (Spaceplan, Paperclips).
6. Offline: 50% rate, 8 h cap extendable with progress (AFK Arena / Egg Inc pattern), banking time for the player to spend (Evolve) as optional. With no fighting there is no combat wall, so walls must come from cost curves only; use the sim guard rail that max gap between goals stays under 30 min.
7. Keep numbers readable: use log/diminishing exponents on late permanent bonuses (Progress Knight, Evolve, Synergism pattern) and reset scale between worlds so players never face e47 (research/player_complaints.md C8).
8. Evidence caution for the design doc: label every number used as CONFIRMED (AdCap tiers 2-4, CC 1.15, CH 1.07/1.145, Kittens ratios, AD costs, Synergism 1.25) or TUNING GUESS (all 1.07-1.15 defaults borrowed for games with no data).
