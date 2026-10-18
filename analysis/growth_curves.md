# Growth curves across 47 idle/incremental games

Scope: cost-growth ratios, production scaling, milestone multipliers, unlock pacing. Inputs: all `games/*.md` (47 = the original 37 plus derivative-clicker, fallout-shelter, gnorp-apologue, idle-heroes, idle-loops, orb-of-creation, ordinal-markup, prestige-tree, shark-game, soda-dungeon), `research/formula_tables.md` (source mining rounds 1-2), `research/*.md`, `sim/results.md` (campaign sim v3), `DESIGN_RULES.md` (rules R1-R42, content v3; the file header still reads v2).

Refresh note (2026-10-18): this file was first written before the source-code mining rounds, the weak-game verification passes and campaign sim v3. Evidence tags were recounted from the games/*.md files; numbers that are now [CODE] replace the earlier [M]/[S] text; Decade implications at the bottom follow DESIGN_RULES.md.

## 0. Evidence legend (read first)

- CONFIRMED = tags `[CODE]` / `[SRC]` (read from source code; `[SRC]` is the older spelling of the same thing) and `[S]` (search snippet of a wiki or official page, page itself not opened), or `[SOURCE CODE]` in `research/math_of_idle_games.md`.
- PUBLISHED-SECONDHAND = `[PUB]`, `[public]`, `[COMMUNITY]` (a cited page/guide that was not independently checked). Reported separately, not counted as confirmed.
- ESTIMATED = tags `[M]` memory, `[MEM]`/`[MEM-LOW]`, `[E]`/`[EST]` estimate, `[unverified]`, or the genre default pasted in because the game has no public data. These are NOT game data.
- DERIVED = arithmetic on cited numbers.
- **Recount of evidence tags in games/*.md (47 files, lines containing the word "legend" excluded; counts are tag mentions, not distinct claims):** [CODE] 255 + [SRC] 71 = **326 code-read**; [S] **486** snippet-confirmed; so **812 confirmed** (54 % of confirmed+estimated); [PUB] 77 secondhand; estimated **681** = [EST] 259 + [M] 151 + [MEM]/[MEM-LOW] 110 + [E] 84 + [unverified]/other 77. Original 37 files: 504 confirmed vs 539 estimated (48 %); the 10 added files: 308 vs 142 (68 %).
- **Games with at least one code-read tag: 24 of 47** (was "about 11 of 37 with confirmed cost formulas"). Of these, games whose *cost or production numbers* were actually read from code: AD, A Dark Room, Bitburner, Cookie Clicker, Derivative Clicker, Evolve, Kittens Game, Progress Knight, Reactor Incremental (via the cwmonkey clone), Synergism, Trimps, Universal Paperclips (12 with a per-purchase cost law), plus Prestige Tree, Shark Game and Idle Loops (layer/gate/progress formulas). The other [CODE] tags (Candy Box 2 index.html/faq only, Idle Breakout string literals, Increlution fan tools, Fallout Shelter/Idle Heroes/Soda Dungeon/Gnorp/Orb stray tags) confirm facts other than formulas. 22 games have only [S] snippets (AdCap, Cell to Singularity, CH1, CH2, Egg Inc, Factory Idle, Farm Away, Guava Juice, Idle Champions, Idle Miner, Idle Mining Empire, Idle Slayer, Idle Wizard, Leaf Blower, Magic Research, Melvor, Mr. Mine, NGU, Realm Grinder, Spaceplan, Swamp Attack, Tap Titans 2) and AFK Arena has only [PUB]/[EST].
- The remaining games copy the genre default of 1.07-1.15 (for example games/farm-away.md, games/idle-wizard.md, games/spaceplan.md, games/magic-research.md, games/guava-juice-tub-tapper.md, games/factory-idle.md, games/mr-mine.md); the verification logs of Farm Away and Idle Mining Empire say outright that those formulas belong to other games. They cannot be used as independent evidence. Do not count them when averaging.
- Caveat on [S] items: they come from search snippets only, and several earlier numbers were corrected in the verification passes (NOTES.md runs 1-2; e.g. CH1 monster HP x1.145 not 1.55, AD boost uses the 8th dimension, Spaceplan Steam id 616110 and ~6 h, Mr. Mine by Playsaurus). The verification logs inside the game files are the final word.

## 1. Cost-growth ratios (price of the n-th unit = base * r^n)

### 1.1 Confirmed values

| Game (file) | r (per owned unit) | Evidence | Notes |
|---|---|---|---|
| Adventure Capitalist (games/adventure-capitalist.md) | 1.15 Newspaper, 1.14 Car Wash, 1.13 Pizza; community table falls 1.15 -> 1.07 across 10 tiers (Lemonade 1.07, Oil 1.07) | S for rows 2-4; the other rows unverified; the math file copies the whole table from a secondary GitHub synthesis | r falls 0.01 per tier; base cost x12 per tier (60, 720, 8,640 ...) per research/math_of_idle_games.md section 5.1 [DERIVED from secondary] |
| Cookie Clicker (games/cookie-clicker.md) | 1.15 (`Game.priceIncrease`, `price = base * 1.15^max(0, owned-free)`) | **CODE** `main.js` L7972, L8092 in the public mirror ozh/cookieclicker (the game is NOT closed-source; the earlier "no public code" claim is superseded) | price doubles every ~5 buys. Base prices are generated, not tabled: `(n+9+[n>=5](n-5)^1.75*5)*10^n*max(1,n-14)` gives Grandma 100, Farm 1.1e3, Mine 1.2e4, Factory 1.3e5, Bank 1.4e6, Temple 2e7 ... Portal 1e12 ... You 5.4e26 = x11-12 per tier early, x13-16 later (the old "x10-15 recall" is now confirmed) |
| Clicker Heroes (games/clicker-heroes.md) | 1.07 hero cost (6.975%/level, doubling about every 10 levels); monster HP x1.145 per zone from zone 140 to 500 | S | HP doubles about every 5.1 zones [DERIVED]. Ace Scouts use 1.22 |
| Universal Paperclips (games/universal-paperclips.md) | 1.07 MegaClipper (`1000*1.07^n`); **1.1 AutoClipper (`1.1^n + 5`, the earlier 1.07 was wrong)**; ads cost x2 per buy (start 100, effect 1.1^(lvl-1)); wire +0.05 per buy then decays 0.1 % per 250 ticks, +-6 sine noise | **CODE** `main.js` L1661, L1674, L2334, L3341, L12-50 (ianfixes mirror; may be an older version than the live site); MegaClipper also S | trust at Fibonacci x 1000 clips (3000, 5000, 8000, 13000 ...), ops cap = memory x 1000 [CODE] |
| Kittens Game (games/kittens-game.md, research/formula_tables.md) | modal 1.15; field 1.12, hut 2.5, barn 1.75, a few later 1.25 / 1.35 / 1.5 / 1.75; cost = `val * ratio^count * modifiers`, ratio reduced by `getLimitedDR` | **CODE** `buildings.js` L2589-2607, L358, L491, L799 (the game file's [M] values are now confirmed) | production 1.12-1.15, storage/housing 1.75-2.5. **Paragon (CODE):** reset gives paragon = kittens - 70 (>70); production x(1 + 0.01 x paragon x ratio) with limited DR capped at 2 x ratio; storage +10 % per 100 paragon; +1 paragon per 1000 years; burned paragon is a second, capped bonus (`prestige.js` L549-576, `game.js` getResetPrestige) |
| Synergism (games/synergism.md) | per tier `1.25^growth`: coin 1.25 / 1.5625 / 1.953 / 2.441 / 3.052; diamond and mythos 1.25 / 1.953 / 3.815 / 9.31 / 28.4; extra softcaps at 1k / 5k / 20k / 250k owned; tesseract buildings are cubic `base*(n+1)^3` | CODE `Buy.ts` L14-40, L131-195, L666 | the player can push the walls out, not cheapen single buys |
| Antimatter Dimensions (games/antimatter-dimensions.md, research/formula_tables.md) | per batch of 10: cost x1e3, 1e4, 1e5, 1e6, 1e8, 1e10, 1e12, 1e15 for dims 1-8; base costs 10, 100, 1e4, 1e6, 1e9, 1e13, 1e18, 1e24; tickspeed cost x10 per buy; Infinity Dims x1e3...1e30 (bases 1e8...1e280); Time Dims x3, 9, 27, 81, 24300 ... | **CODE** `antimatter-dimension.js` L337-363, `tickspeed.js` L154, `infinity-dimension.js` L53-57, `time-dimension.js` L145-175 (middle dimension values are no longer "unverified") | equivalent to r = 1e3^(1/10) = 1.995 per single unit for dim 1 and 1e15^(1/10) = 31.6 for dim 8 [DERIVED]; compensated by x2 per batch |
| Bitburner (games/bitburner.md) | Hacknet node purchase x1.85 (`1000*1.85^(n-1)`); level upgrade 1.04; RAM upgrade 1.28; core upgrade 1.48; Hacknet servers x3.2; every augmentation bought in a run multiplies all remaining aug prices by 1.9; NeuroFlux Governor 1.14 per level | CODE `Hacknet/data/Constants.ts`, `src/Constants.ts` L35-45 | the clearest example of a deliberately steep "soft-reset batch" cost; NeuroFlux 1.14 is the model for an endless gentle sink (R7), x1.9 is finite |
| Leaf Blower Revolution (games/leaf-blower-revolution.md) | shop items 3.5 / 3 / 3 / 1.5 (Golden Marketing, Max Combo, Combo Multiplier, Nuclear Fuel); tools 1.1-1.2 is E | S (first-pass wiki snippet; the later verification log found no further gameplay data, so treat as weakly confirmed); E (tools) | permanent shop items are far steeper than in-run items |
| Trimps (games/trimps.md) | buildings `base*ratio^owned`, ratio falls 1.24 (Hut) / 1.22 / 1.20 / 1.18 / 1.16 / 1.14 / 1.12 (Collector), Gym 1.185, Tribute 1.05, Warpstation 1.4; perks (Helium) `ceil(L/2 + priceBase*1.3^L)`; equipment prestige stat x1.19 vs cost x1.069; Barn costs 25 % of max storage | **CODE** `main.js` L4819-4833, L3846-3880, L5953-5970; `config.js` L11450-11740 (the old "equipment about 1.2 (M)" is replaced). Per-perk caps (Coordinated 15, Anticipation 10) and Power II linear +500/level are [S] | in the generic perk formula it is the 1.3^L cost curve, not a hard cap, that limits levels; caps are per-perk design choices |
| Evolve (games/evolve.md) | `round(ratio^count * base)`, ratio floor 1.005; basic housing 1.17 (money) / 1.23 (lumber), cottage 1.15 / 1.25, farm 1.32 / 1.36, smelter 1.32, warehouse 1.26, mine 1.6 / 1.38, lumber yard 1.85-1.95 | **CODE** `functions.js` L776-833, `actions.js` (values are no longer [M]) | 2-3 resources per building; evolution (RNA/DNA) costs are linear |
| NGU Idle (games/ngu-idle.md) | Augmentations: cost = base * n (linear), upgrade cost n^2 | S | not exponential; "1.1^level" is unverified |
| Progress Knight (games/progress-knight.md) | XP need `base * (level+1) * 1.01^level` | CODE `classes.js` L10-12 | effective per-level growth is only about 1.01-1.02 |
| A Dark Room (games/a-dark-room.md) | linear, browser source: trap `10 + 10n` wood cap 10, hut `100 + 50n` wood cap 20, cart 30, lodge 200; mobile wiki: trap `(n+1)*5` cap 30, hut `20+60n` cap 20 | CODE `room.js` L13-58 (browser, authoritative); S (mobile wiki) | pacing by timers (fire 5 min, villager every 0.5-3 min) and hard caps |
| Derivative Clicker (games/derivative-clicker.md) | per-building factors 1.05 (mathematician) / 1.1 / 1.2 / 1.3 / 1.8 up to 2.7 (deriv 7) and 4 (Isaac Newton); geometric bulk price; tier-unlock upgrades 1e6, 1e9 ... 1e24; reset currency +1 % each | CODE `script.js` ~L73-79, `tierUpgradeCosts` | ratio climbs with tier here (opposite of AdCap/Trimps) because each tier builds the one below |
| Reactor Incremental (games/reactor-incremental.md) | part and upgrade cost multipliers, grid size, heat/power formulas read from the clone | CODE (cwmonkey/reactor-knockoff v1.3.2; parity with the original not guaranteed) | heat scales with the square of neighbouring pulses |
| Prestige Tree (games/prestige-tree.md, research/formula_tables.md R2.1-2.2) | layer "static" type: cost of the n-th unit `req * base^(n^exponent / gainExp)`; Boosters and Generators req 200, exponent 1.25, base 5; Time and Space exponent 1.85, base 1e15 | CODE `layers.js`, Modding Tree `game.js` L10-60 | layer gains use exponents 0.5 / 0.125 / 0.0075 as depth grows |
| Shark Game (games/shark-game.md) | not a ratio: gate cost per slot `floor(worldGateCost[slot] * planetLevel * gateCostMultiplier)`, multiplier `0.9^level` of an artifact; essence reward `4 + floor(planetLevel/4)` | CODE `gateway.js`, `world.js` (per-unit costs and the per-world gate cost table were not read) | scale is linear in planet level, not exponential |
| Melvor Idle (games/melvor-idle.md) | skill XP gap doubles about every 7 levels (L99 = 13,034,431 XP; L120 = 104,273,167) | S | RuneScape curve; equipment 5-10x per tier is unverified |
| Realm Grinder (games/realm-grinder.md) | base costs Farm 10, Inn 125, Blacksmith 600 (S); multiplier "1.08-1.15" unverified | S / unverified | |
| Idle Wizard (games/idle-wizard.md) | wizard level XP 1500 for level 2, each later level costs x1.09 | S (wiki Level page snippet); spell cost ratio 1.15 stays [EST] | |
| Idle Loops (games/idle-loops.md) | town progress `expFromLevel(L) = 50*L*(L+1)`, cap 505,000 (level 100); Survey mana cost `10,000*(zone+1)`; talent to stat `totalTalent^0.2` | CODE `town.js`, `actionList.js`, `stats.js` | quadratic, not exponential |

### 1.2 Estimated or genre-default values (not evidence)
- Idle Miner Tycoon (games/idle-miner-tycoon.md): 1.1-1.3 per level, shaft x2-3 per new shaft [E].
- Idle Wizard spell cost 1.15, Idle Breakout 1.1-1.15, Idle Champions 1.07, Tap Titans 2 1.07-1.1, Cell to Singularity 1.07-1.15, Spaceplan 1.15, Magic Research 1.10-1.20, Idle Mining Empire 1.07-1.15 and x3-10 per shaft, Mr. Mine 1.1-1.2, Farm Away 1.07-1.15, Factory Idle 1.15, Guava Juice 1.15, Slayer 1.1-1.2, Reactor tier x5-20 and upgrades x2-10, Swamp Attack 1.3-1.6 per tier (all `[EST]`). The Farm Away, Idle Mining Empire and Factory Idle verification logs state that the AdCap-style formulas in those files do not belong to those games.
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
- Production units (the thing you buy hundreds of): **1.07-1.15**, centre 1.12-1.15. Code-confirmed in Cookie Clicker 1.15, Kittens 1.12-1.15, Trimps 1.12-1.24, Paperclips 1.07-1.1, Evolve 1.15-1.17 (basic), Derivative Clicker 1.05-1.3 early; snippet-confirmed in AdCap and Clicker Heroes. Matches DESIGN_RULES R1 (1.12-1.15 main generators, 1.07 only late/bulk; decade model uses 1.12).
- Walls, caps and capacity: **1.25-2.5** (Kittens storage/housing, Synergism 1.25-3, Evolve mine 1.6 / lumber yard 1.9, Bitburner 1.28-1.85, Leaf Blower shop 3-3.5, Trimps perk 1.3). Rule: the steeper the ratio, the lower the intended owned count (cap 10-30) or the more the item is a one-time permanent unlock. Endless sinks need a gentle ratio (NeuroFlux 1.14); finite ladders may be steep (x1.9 per augmentation) (R7).
- Within one game the ratio usually moves with tier: AdCap lowers r 0.01 per tier (1.15 -> 1.07); Trimps housing falls 1.24 -> 1.12 (confirmed in code); Idle Ronin lowers by band; Synergism switches from 1.25 to 1.03 + factorial late. So "cheaper to climb at the top" is a recurring pattern; Derivative Clicker (1.05 -> 4) is the counter-example.
- Base cost between tiers: x12 (AdCap, S/secondary), x11-16 (Cookie Clicker, now CODE), x10 per tier in Trimps housing [CODE], x10 to x1e15 per batch (AD, CODE). DESIGN_RULES R2: x8-12.
- Simulation result (sim/results.md): growth between 1.07 and 1.15 mattered less than the ratio between tiers; the sweet spot was growth 1.10-1.15 with cost_ratio / rate_ratio about 1.2-1.5 (examples 8/6, 12/9, 20/14). That is R2's "rate ratio = cost ratio / 1.3". Real games run higher: Cookie Clicker's price/CPS ratio per tier is 1.4 (Farm), 1.9-2.0 (Mine to Bank) and 2.1-2.9 (Temple onward) [DERIVED from the CODE table], offset by upgrade multipliers; this is outside the sim band and is an open calibration question (see Implications, open items).

## 2. Production scaling

| Game | Production model | Per-tier ratio | Evidence |
|---|---|---|---|
| Cookie Clicker | `count * base_cps * multipliers`; base CPS 0.1, 1, 8, 47, 260, 1,400, 7,800 ... generated by `ceil(n^(0.5n+2)*10)/10` | CPS about x5.4-6.3 per tier (x8 for Farm, x10 for Grandma) vs price x11-16; price/CPS ratio per tier 0.67, 1.38, 1.86, 1.98, 1.97, 2.57, 2.87, 2.65, 2.40 [sim/cc_ladder.py] | CODE `main.js` L8018-8031 |
| Adventure Capitalist | `owned * base_revenue * mult`, cycle 0.6 s to 36,864 s | revenue 0.5-0.75 of base cost, cycle x2 then x4 per tier | secondary / M |
| Antimatter Dimensions | dim N feeds dim N-1; polynomial `x^n/n!` growth; x2 per 10 bought; tickspeed x1.124 per buy (x0.89) then +2%/galaxy | cost x1e3..1e15 per batch vs output x2 | S/SRC |
| Clicker Heroes | hero DPS x4 per 25 levels from 200, x10 at 1000, 2000 ... 8000 | price x5.43 per 25 levels vs damage x4 [DERIVED, math file] | S |
| Paperclips | MegaClipper = 500 AutoClippers of output | x500 per tier at x1.07 cost | S |
| Egg Inc | egg value ladder 0.25, 1.25, 6.25, 30, 150, 700, 3,000, 50,000, ... (x5 early, uneven later) | farm-value gates, e.g. Superfood ~10M, Medical ~840M, Rocket Fuel ~38B | S |
| Kittens Game | `base * count * (1 + additive bonuses)` then `perTick *= 1 + paragonProductionRatio` (limited DR, cap 2 x ratio); 10 ticks per day, 100 days per season | n/a | CODE `game.js` L3727-3732, `calendar.js` L217-218 |
| Progress Knight | job income `1 + log10(level+1)` ; max-level XP `1 + maxLevel/10`; lifespan `1 + log33(level+1)` | log-shaped | CODE |
| Synergism | diminishing-return powers 0.5, 0.4 ... 0.15 on many outputs; softcap at 1e15 with exponent 1/8 | n/a | SRC |
| Evolve | log curves on plasmid and dark-energy power (`ln(1 + p/50)/2.888`), flatter past `p_cap = 250 + Phage` | n/a | CODE `resources.js` L3238-3246 |
| Melvor | action interval fixed (3 s woodcutting) reduced by upgrades; XP doubling every 7 levels | n/a | S |
| Bitburner | Hacknet income `level * 1.5 * 1.035^(ram-1) * (cores+5)/6`; hack money fraction `/240` per hack | n/a | SRC |

Patterns:
1. Cost exponential, production linear in owned count, boosted by multiplier gates. Gates convert linear counts to exponential output (all of AdCap, AD, Clicker Heroes per research/design_talks_postmortems.md section 5).
2. Chained-tier (AD style, "generators produce generators") gives polynomial growth degree N (4-8 tiers recommended, research/math_of_idle_games.md section 2).
3. Late-game production inside a layer almost always uses a log or fractional exponent (Progress Knight log10/log33/log13, Evolve log, Synergism powers 0.15-0.5). This keeps a single permanent upgrade from dominating.
4. Production ladders with confirmed numbers have **price ratio above output ratio** by about 1.4-2.9x per tier (Cookie Clicker x11-16 price vs x5.4-8 CPS [CODE, derived]; CH x5.43 price vs x4 damage per 25 levels = 1.36; sim best band 1.2-1.5). Inverted ladders (rate ratio > cost ratio) produce "skip the early game" (sim/results.md).
5. Universal Paperclips shows the two-sided version of the same idea: AutoClipper costs `1.1^n + 5` (cheap, many) while MegaClipper costs `1000 * 1.07^n` for x500 output and unlocks only at 75 AutoClippers [CODE/S], so the new tier arrives as a visible goal, not as a surprise.

## 3. Milestone multipliers

| Game | Milestone rule | Evidence |
|---|---|---|
| Adventure Capitalist | cycle time halved at 25, 50, 100, 200, 300, 400 owned (per business), and again at same marks across all businesses; max 12 halvings = 1/4096; x3 profit at 100 by a forum post; x2 to x11 profit steps and global x3 at 100-of-everything come from the secondary synthesis | S (halving rule); unverified (x3/x4 steps) , games/adventure-capitalist.md |
| Antimatter Dimensions | x2 per 10 purchased of that dimension (`buyTenMultiplier` base 2); Infinity Dimensions x50 / x30 / x10 / x5 per 10 | CODE `antimatter-dimension.js` L632-636, `infinity-dimension.js` L55, L151 |
| Guava Juice Tub Tapper | per-tub milestone levels 5, 10, 25, 50, 100, 200, 300, 400, 500, 700, 1000; collection automation unlocks at level 50 (ladder adopted in R3 for late tiers; automation-as-milestone in R10/R21) | S (one guide snippet; not confirmed in-game) |
| Clicker Heroes | x4 per 25 levels from 200, x5 per 25 for later heroes 525-725, x10 at 1000, 2000 ... 8000 | S (math file, wiki excerpt) |
| Cookie Clicker | tier upgrades double a building at about 1, 5, 25, 50, 100 owned, cost about 10x base | M (games/cookie-clicker.md); the upgrade tables in `main.js` were not read in the mining rounds |
| Idle Miner Tycoon | x2 at fixed levels every 25/50/100 (10/25/50 variants) | M/E |
| Idle Mining Empire, Idle Wizard, Spaceplan, Farm Away, Factory Idle | x2 at 10/25/50/100 or 25/50/100/200 | EST copied from genre |
| Trimps | each equipment prestige tier x1.19-1.5 stats | E |
| Tap Titans 2 / Hero games | per-hero milestone doublings | E |
| Cell to Singularity | x2 at preset node levels | E |

Derived design rule (research/design_talks_postmortems.md 4.2): choose multiplier M and spacing S such that **M approx r^S**. At r = 1.07, S = 10 gives x1.97 so a x2 every 10 buys neutralises price growth; at r = 1.15, S = 5 gives x2.01; CH uses S = 25 with M = 4 vs 5.43 price.
- Typical spacing: 10 (AD), 25-100 (AdCap, CC, CH), power-of-two-ish multiplier each time.
- Sim result (sim/results.md): x2 milestones beat x3 on average; x3 compresses early goals and leaves later walls; starting milestones at 5 with x3 is among the worst configs. DESIGN_RULES R3 adopts x2 at 10/25/50/100/200 (300/400/500/700/1000 for late tiers, per the Guava Juice ladder; 200+ was not swept) and R4 shows the next milestone as a bar and a count.

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
| Cookie Clicker | ascension possible at 1e12 cookies for 1 chip (`prestige = (C/1e12)^(1/3)` [CODE]); guides advise waiting for 200+ chips | CODE (formula), guides low quality |
| Progress Knight | first rebirth immediate (life-length based); first evil in 10-30 lives | EST |
| None: A Dark Room, Candy Box 2, Spaceplan, Paperclips, Melvor, Swamp Attack, AFK Arena | finite arc or monotonic progress | |

Median of the estimates: first prestige 1-2 h in mobile/web idles, 15-30 min in the fastest, days only in the slow mobile ones. Research recommendation: first purchase under 60 s, first automation about 3 min, first prestige 10-15 min (single-author heuristics; design_talks 4.3); dev postmortem: first prestige took 25-35 min for most players and bounce before first reset is the churn (research/player_complaints.md C6). **Decade target (DESIGN_RULES R10/R16, campaign sim v3): first Final Form Ride at about 8 min of play in every world (T_w auto-calibrated), light automation at about 3 min, then 9-11 rides per 3.2-day world (about one per 7 h of wall-clock, clustered at session starts).** The earlier sim v1 figure "first prestige about 25 min, then cycles of 20-45 min" came from the continuous-time prestige sweep and is superseded for a session-based mobile game.

### 4.2 Cadence of new content
- A Dark Room: stage names tied to hut counts (1, 2-4, 5-8, 9-14, 15-20 huts) S; Lodge/Trading Post at 30-60 min; whole game 3-5 h E (games/a-dark-room.md).
- Cookie Clicker: building revealed at 1/3-1/2 of price; first real time gate (sugar lumps) at about 1 day (games/cookie-clicker.md). **Golden cookie [CODE] `main.js` L5934-6000, L5617: spawn gap base 5-15 min (halved by Lucky day and by Serendipity, x0.95 per several upgrades), lifetime 13 s (x2 Lucky day, x2 Serendipity)**; wrinkler hard limit 14; Radiant Appetite aura x2 production. DESIGN_RULES R38 adopted this, then R38b scaled it for 10-minute sessions (Photo Window every 90-240 s, first at about 3:00).
- Prestige Tree (games/prestige-tree.md, CODE): 31 layers in rows 0-6; each layer reveal is the pacing beat; the first of Time/Enhance/Space is cheap and each later one costs `1e180^(order^1.415)` more (`unlockOrder`), a path choice that creates replay reasons.
- Shark Game (games/shark-game.md, CODE): a world is a data record (included/absent resources, modifiers, gate slots); World 1 teaches the base tree, later worlds remove or restrict parts of it; essence on completion is flat `4 + floor(level/4)` so finishing always pays.
- Idle Loops (games/idle-loops.md, CODE): nine zones opened by one-off travel actions; zone gating by stats and skills, not waiting.
- Egg Inc: egg tiers gated by farm value (10M, 840M, 38B, 27T, 8Q, 3.6 quintillion) = **x45 to x710 per egg unlock, geometric mean about x200** [DERIVED from S gates; wall-clock unverified].
- Paperclips: new project every few minutes; phase 1 ends in 2-3 h; total 4-10 h (games/universal-paperclips.md; author says 4-6 h in research file).
- Spaceplan: new item/dialogue every 3-10 min E.
- Cell to Singularity: new tree node every 30-60 s, new era every 20-40 min E.
- NGU Idle: features unlocked day by day (day 0 energy/magic/augments, day 1 rebirth, day 3+ NGU etc.) E.
- AD layers (community estimates, unverified): Infinity hours-2 days, Eternity 1-3 days / 2 days-1 week, Reality 1-3 weeks / 1-4 weeks, Celestials weeks-months.
- Progression layer width: each AD layer is ~308 orders of magnitude (SRC), Synergism layers use ever-smaller exponents.

### 4.3 Offline pacing (related lever)
- Confirmed caps and rates: Melvor 24 h (12 h in 0.13, 18 h in 1.0 beta) S; Synergism 72 h base + 4 h per level of researches 31 and 32, times a paid buff, simulated in 200 ticks (CODE `Calculate.ts` L826-840); Bitburner offline script income x0.75 (CODE); Cookie Clicker needs Twin Gates: 5 % of CpS for 1 h (cap doubles per demon upgrade, up to 128 h) then 10 % of that rate past the cap, up to 75 % from angel tiers and 91 % with all extras, or Perfect idling for unlimited 100 % (CODE `main.js` L3537-3580; no offline gain at all without them); AD `ipOffline` upgrade gives 50 % of best IP/ms (CODE); Prestige Tree template `offlineLimit` 1 h (CODE); Reactor Incremental replays elapsed time as ticks with a steady-state fast-forward, no hour cap found in the clone (CODE); Idle Champions **does** have offline progress (App Store text: champions keep fighting until defeated; cap and rate unknown) [S]; Idle Heroes 8 h cap (10 h per one review, version conflict) [S]; AFK Arena chest cap 12 h (PUB).
- Banked rather than automatic: Idle Loops banks offline time (`addOffline(ticks * offlineRatio)`) and lets the player spend it at 5x speed [CODE]; Evolve has a banked skip. DESIGN_RULES R36 adopts banked time as an optional spendable x5 next to automatic gains.
- Genre rules: cap 2-24 h, rate 50% (research 4.5). **Campaign sim v3 (offline_lever.py, sim/results.md "Offline lever"):** offline production is existential, since with no offline a 3-session/day world takes 26 d instead of 2.5-3.2 d; stepped 50 %/25 % with an 8 h cap is only 13-28 % slower than flat 50 %; raising the cap 8 -> 24 h helps only players with gaps over 8 h (x1.47 at 1 session/day, x1.08 at 12/12 h, at most x1.05 at 3/day, x1.0 at 6/day). The sim v1 numbers "0 -> 0.25 about 9x, 0.25 -> 1.0 about 2x, 3 -> 12 sessions only 1.5x" were measured without in-world rides and are superseded. R33: 50 % for the first 2 h, 25 % beyond, cap 8 h (average about 0.31 for an 8 h gap), never 0; the cap upgrade is a late light-player perk.

## 5. Typical ranges (what to copy)
| Parameter | Typical range | Confidence |
|---|---|---|
| Cost ratio, production tiers | 1.07-1.15 (median ~1.12-1.15) | code-confirmed in 6+ games, snippet-confirmed in 2 more |
| Cost ratio, caps and one-time perma shop | 1.25-3.5 | code-confirmed in 4 games (Kittens, Synergism, Bitburner, Evolve), S in Leaf Blower |
| Price doubling | every 5-10 buys | derived |
| Tier-to-tier base cost | x10-x16 (AdCap x12; Cookie Clicker x11-16, Trimps housing about x10) | AdCap secondary; CC and Trimps CODE |
| Tier-to-tier output | x5-x10 (cost/output ratio 1.2-1.5 in the sim; 1.4-2.9 measured in Cookie Clicker) | CC CODE-derived, CH derived, sim |
| Milestone multiplier | x2 (sometimes x3-x4 later) every 10-25 owned; M ~ r^S | confirmed in AD, CH, AdCap halving |
| Number of tiers | 8-10 (AD 8, AdCap 10, CC 15-20) | confirmed |
| First prestige | 15-60 min fast designs; 1-3 h typical; days in slow mobile (Decade target about 8 min, R10/R16) | estimated (games), sim v3 (Decade) |
| Cycle after first prestige | typical games 20-45 min, each cycle 2-4x faster than the first; Decade: about 1 ride per 7 h wall-clock, 9-11 per 3.2-day world, each >= 1.5x | guides (games), sim v3 (Decade) |
| Offline | 50 % rate, 8 h cap (2-24 h seen); Decade: stepped 50 % first 2 h / 25 % beyond, cap 8 h | sim v3 + survey |

## Implications for Kamen Rider Decade world-progression idle game (no fighting, upgrade-focused)
Matches DESIGN_RULES.md (R-numbers) and DECADE_IDLE_DESIGN.md; numbers marked [H] are hypotheses from the toy campaign sim (sim/results.md v3).

1. **Skeleton per world (R1, R2, R3, R5):** 8 tiers per world, per-unit growth 1.12 (1.12-1.15 for main generators, 1.07 only for late/bulk tiers), base cost x8-12 per tier, rate ratio = cost ratio / 1.3 (sim: x8 cost, x6 rate), tier N+1 revealed at about 5 owned. Do not copy unverified genre-default ratios as if proven; the confirmed anchors are Cookie Clicker 1.15, Kittens 1.12-1.15, Trimps 1.12-1.24, Synergism 1.25 and AD's 1e3-1e15 block steps.
2. **Milestones (R3, R4):** x2 at 10/25/50/100/200 owned (300/400/500/700/1000 on late tiers), shown as a bar and a count ("x2 in 7"). M approx r^S: r = 1.12 gives x2 per 6, r = 1.10 per 7. Prefer x2 over x3 (sim).
3. **Steep ratios only for finite or capped things (R6, R7):** world gates, Driver/Form slots, permanent perks with level caps of 5-15. If a late endless sink is wanted, give it a gentle ratio (NeuroFlux 1.14), not x1.9.
4. **Timing (R9, R10, R16, R25) replaces the earlier "first gate in 10-25 min, first ride at about 25 min":** first purchase under 60 s, light automation at about 3 min, first Final Form Ride at about 8 min (T_w calibrated per world), 9-11 rides per world, each at least 1.5x production; a world lasts about 3.2 days for a 3 x 10 min/day player; gates grow x2.5-3.5 per world (6.2e15 -> 4.0e19). The 3.2-day world gate is the "world gate"; the 8-minute ride is the first micro-goal.
5. **World drift (R23):** the old rule "cost_scale/carryover in [1.0, 1.5], target 1.3" is superseded: keep world drift d = cost_scale s / total permanent carry in [1.0, 1.07] (aim d approx 1.0), with every carry source (base c, Ride Cards +10 %/card, bounded archived-Seals +1 %/world, achievements) counted inside c; s = 3 and c approx 2.25 in sim v3. Gates are outputs of calibration, not free parameters.
6. **Prestige scale (R15):** Seals = floor(sqrt(run_lifetime / T_w)); production multiplier (1 + Seals)^0.5; a linear +8 %/seal explodes (about 30 rides per world, multiplier 6e6). Compare the code-confirmed exponents: AdCap/Realm Grinder/Synergism L1 use sqrt, Cookie Clicker cbrt, Prestige Tree layers 0.5 -> 0.125 -> 0.0075.
7. **Egg Inc-style gates (x45-x710) are NOT the model for world gates:** a world gate is x2.5-3.5 the previous one because the whole world is a rescale (d approx 1.0). Use stage-name feedback (A Dark Room) and a new reveal every 3-10 minutes early (Spaceplan, Paperclips), plus at least one non-ride "beat" per session (mastery node, album entry, Photo Window, fusion discovery), since only 64-73 % of sessions contain a ride/tier/milestone goal (R25).
8. **Offline (R33, R36):** production while away is existential (about 10x faster than none), the cap is minor: stepped 50 % first 2 h / 25 % beyond, cap 8 h, never 0; an 8 -> 24 h cap upgrade is a light-player perk; auto-spend while away shortens worlds 26-44 % (x1.26 at 6/day to x1.44 at 1/day) so gates are calibrated with it on (R37); optional banked time (Idle Loops style, x5) next to automatic gains.
9. **Builds (R13b):** keep every build within about 25 % of the best (sim: 1.19x at Speed x1.2/node, Cast Off x1.5 then x2, Recipes rides need 70 % less); do not make a build that only changes offline efficiency; calibrate gates with the build mix because builds clear 20-45 % faster than none.
10. **Numbers (R40a, R40):** no big-number library needed (peak about 6.6e21 at s = 3, doubles reach 1.8e308); use log/diminishing exponents on late permanent bonuses (Progress Knight, Evolve, Synergism) and cap the achievement multiplier (about x10 at 144 entries, R38c).
11. **Evidence discipline:** label numbers CONFIRMED-CODE (Cookie Clicker 1.15 and generated prices, golden cookie 5-15 min / 13 s, Kittens ratios and paragon, Trimps tables, AD cost blocks and IP/EP, Paperclips costs, Synergism 1.25 and exponents, Evolve ratios) or TUNING GUESS (all remaining 1.07-1.15 defaults).

**Open items (marked, not resolved):** (a) Cookie Clicker's price/CPS ratio (0.67, 1.38, 1.86, 1.98, 1.97, 2.57, 2.87, 2.65, 2.40 for tiers 1-9, cc_ladder.py) is above R2's 1.2-1.5 band, and a passive buyer there sees a ~16 min median goal gap; DESIGN_RULES now marks 1.2-1.5 and the 15-600 s band as a mobile-session target, not a law. (b) x2 milestones beyond 200 owned were not swept (R3). (c) Whether Photo Window spacing should follow Cookie Clicker's 5-15 min base once real session length is measured (R38/R38b). (d) Leaf Blower shop ratios are weakly sourced. (e) DESIGN_RULES.md header still says v2 although its rules are the v3 content.
