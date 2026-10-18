# How games with sequential worlds, zones, eras or layers keep each one fresh

Scope: all 47 `games/*.md` (original 37 plus derivative-clicker, fallout-shelter, gnorp-apologue, idle-heroes, idle-loops, orb-of-creation, ordinal-markup, prestige-tree, shark-game, soda-dungeon), `research/formula_tables.md`, `research/psychology.md`, `research/player_complaints.md`, `research/math_of_idle_games.md`, `research/decade_worlds.md`, `sim/results.md` (campaign sim v3), `DESIGN_RULES.md` (content v3; header reads v2).

## Method and honesty notes
- A game counts as "sequential" if its files describe an ordered series of worlds/zones/eras/layers/phases/chapters/realms. About 37 of 47 qualify in some form (was about 30 of 37; the added Shark Game, Prestige Tree, Idle Loops, Soda Dungeon, Idle Heroes, Orb of Creation and Ordinal Markup all have ordered stages). Pure tier ladders inside one economy (AdCap businesses, CC buildings) are noted only where they use the same freshness tricks.
- Evidence tags are inherited and were recounted (games/*.md: 326 code-read, 486 [S], 77 [PUB], 681 estimated). Code-read now: Evolve, Synergism, Bitburner, PK, AD, Kittens, Cookie Clicker (public `main.js` mirror), Trimps, Paperclips, A Dark Room, plus the added Shark Game, Prestige Tree and Idle Loops. `[S]` for CH1, Melvor, Egg Inc, Idle Wizard; `[M]/[E]/[MEM]` for most others. Treat examples marked weak as inspiration.
- Counts are manual tallies of the technique being named in the file (not keyword counts).
- The sim is a toy model with a greedy omniscient buyer. `sim/worlds.py` (v1) had no prestige inside worlds; **campaign sim v3 (`campaign3.py`) adds sessions, stepped offline, in-world Final Form Rides, all carry sources and auto-calibrated gates**, and its results below override the v1 numbers.

## Technique index

| # | Technique | Games (count) |
|---|---|---|
| S1 | New rule or verb per stage | 17 (was 14; +Shark Game, Prestige Tree, Orb of Creation) |
| S2 | New currency per stage, with scoped counters | 14 (was 12; +Prestige Tree, Shark Game essence) |
| S3 | Carryover rules that make revisiting cheap but not trivial | 14 (was 11; +Idle Loops, Shark Game, Soda Dungeon) |
| S4 | Clear gate into the next stage (cap, challenge, objective, narrative) | 18 (was 15; +Shark Game gate slots, Idle Loops travel actions, Idle Heroes campaign clears) |
| S5 | Mid-run goals and ladders inside a stage | 15 (+Idle Loops Survey bar) |
| S6 | Replay variants, challenges and handicaps | 10 (+Prestige Tree Mastery) |
| S7 | Per-stage modifier tables | 6 (+Shark Game world modifiers) |
| S8 | Narrative, theme and art swap | 10 |
| S9 | Progress that raises income without a reset | 4 |
| S10 | Reveal the next stage early | 5 (+Shark Game progressive planet modifiers) |
| S11 | Throttle new systems (one per stage, few visible currencies) | 5 |

## S1. A new rule or verb per stage (14 games)
- UP: clips -> drone swarm -> space probes; each phase swaps the core verb and re-contextualises earlier upgrades (`games/universal-paperclips.md`).
- ADR: village economy -> world-map survival -> ship-flying shooter, each triggered by a story beat (`games/a-dark-room.md`).
- AD: each layer "re-teaches the same loop with new rules" (Infinity challenges, Eternity time studies, Reality glyphs, Celestials with their own rules) (`games/antimatter-dimensions.md`).
- Evolve: each reset type is a different mechanic with its own constants (`games/evolve.md`).
- Synergism: each layer unlocks a new building set and minigame (runes, ants, cubes, octeracts) (`games/synergism.md`).
- Idle Wizard: classes change mechanics; the wiki confirms two prestige tiers, Exile and Realm (from e400 mysteries); that a Realm adds a themed twist is unconfirmed (`games/idle-wizard.md`).
- Idle Champions: "Introduce one new gimmick per world" (lesson); each campaign adds champions and a gimmick (`games/idle-champions.md`).
- Clicker Heroes 2: new monsters, boss mechanics and skill-tree nodes per world (`games/clicker-heroes-2.md`).
- Trimps: Heirlooms, Nature, Magma, Universe 2 "each layer is a new game within the game" (`games/trimps.md`, zone numbers `[M]`).
- Bitburner: BitNodes unlock new APIs/systems (Gang, Corporation, Bladeburner) (`games/bitburner.md`).
- Shark Game: each world removes or restricts part of the base tree (`includedResources`, `absentResources`, `planetaryGeneratorRestriction`) so the same buttons behave differently `[CODE]`. Prestige Tree: each layer is a new resource, upgrades and minigame `[CODE]`.
- Spaceplan, Swamp Attack (new enemy type every 3-5 missions `[EST]`), Increlution (each loop reveals a new action `[EST]`), Melvor expansions.

## S2. A new currency per stage, with scoped counters (12 games)
- Synergism: coins -> diamonds -> mythos -> particles -> cubes/quarks -> octeracts/ambrosia; each exponent falls (0.5 -> 0.03 -> 0.01) `[SRC]`.
- Cell to Singularity: Entropy -> Ideas (later eras gate on Ideas) -> Metabits (`games/cell-to-singularity.md`).
- Idle Wizard: counters scoped to the realm ("All Mana This Realm") (`games/idle-wizard.md`, `[PUB]`).
- Evolve: plasmids, phage, dark energy, harmony, artifacts, cores (`[SRC]`).
- CH2: per-world prestige currencies "so prestige in World N doesn't dilute World N-1" `[EST]`.
- AdCap planets with their own currencies; Idle Miner Tycoon continents with "own currency scale".
- Egg Inc: each egg type is 5-1000x+ the previous, gated by farm value `[S]` (Superfood ~10M farm value, Medical ~840M, Rocket Fuel ~38B).
- Spaceplan: each beat unlocks a currency/building category (Energy -> Matter -> planets) `[MEM]`.
- Kittens Game, AD (IP -> EP -> RM, formulas now `[CODE]`), Idle Champions (Favor per patron), Cell to Singularity (premium currency is Darwinium, separate from Metabits). Shark Game: essence, flat `4 + floor(planetLevel/4)` on completion `[CODE]`.
- Risk: AdCap-style parallel economies "fragment the player base" (`games/adventure-capitalist.md`); CH2 4+ layers confuse.

## S3. Carryover rules (11 games)
- **Max-level memory.** PK: each task remembers best level; next life XP x `1 + maxLevel/10`; Rebirth Two zeroes it for a global Evil multiplier `[CODE]`.
- **Shared cap lift.** AFK Arena Resonating Crystal lets top heroes raise the level cap of the rest `[PUB]`.
- **Advanced start.** Tap Titans 2 starts new runs at a fraction of best stage `[PUB]`, f ~0.1-0.4 `[EST]`.
- **Keep knowledge, lose machines.** Factory Idle keeps recipes `[EST]`; Increlution keeps unlocked actions; Bitburner keeps augmentations/Source Files `[SRC]`.
- **Persistent stats, reset consumables.** Idle Loops keeps stats, skills, town exploration and story flags while mana/gold reset every loop `[CODE]`; Shark Game keeps essence and artifacts and drifts planet level upward as worlds chain `[CODE]`; Soda Dungeon tavern upgrades survive a dimension reset `[S]`.
- **Per-world prestige.** CH2 (mechanics unsourced; only the paid 2018 Early Access and the March 2024 delisting are confirmed); Idle Miner Tycoon: up to 5 prestiges per mine with ~4x income each `[S]`.
- **Patron favor.** Idle Champions favor persists; Trimps Helium -> perks (`[S]` perk costs).
- **Auto-prestige credited offline.** Synergism `timeAway / fastestPrestige` `[SRC]`.
- **Rebuild faster.** Cell to Singularity Metabits plus early auto-buy.
- **Sim rule, v1 toy (superseded):** world clear time scales as `(cost_scale / carryover)^world`. Carry x2 / cost x3: 8.4, 12.6, 18.8, 28.3, 42.4, 63.6 min (gentle 1.5x lengthening). Carry x3 / cost x3: flat 8.4. Carry x2 / cost x1: 8.4 -> 0.3 (trivialised). Carry x2 / cost x10: 8.4 -> 1047 (walls). The advice "keep cost/carry in [1.0, 1.5], target 1.3" is replaced by **world drift d = cost_scale / total permanent carry in [1.0, 1.07] (R23), with every carry source (base c, Ride Cards +10 %/card, archived Seals bounded +1 %/world, achievements about x10 at W9) counted inside c**. Campaign sim v3: s = 3 and c about 2.25 give d about 1.0 (carry 6.3e3 vs 6.6e3 at W9); gates grow x2.5-3.5 per world (6.2e15 -> 4.0e19) for 3.2-day worlds, about 29 d for the 3-sessions/day reference player. World length grows only sublinearly in d (about d^(0.65 n)), but d > 1.2 gave dry-session streaks of 5-7 and campaign length is proportional to 1/sessions-per-day (1/day 81-147 d, 3/day 27-48 d, 6/day 16-33 d).

## S4. Gate into the next stage (15 games)
- **Natural cap:** AD's 1.79e308 (`Decimal.NUMBER_MAX_VALUE`, `[CODE]`) makes each layer end itself.
- **Challenge gate:** Synergism Ascension needs Challenge 10 `[SRC]`; AD challenge stacks (12 normal, 8 infinity, 12 eternity); Idle Wizard exile.
- **Quest chain plus one purchase:** Idle Slayer ascension needs two Rookie Quests and the first Slayer Point `[S]`.
- **Objective threshold:** Idle Champions patron objectives at set areas (e.g., Mirt at area 325) `[PUB]`.
- **Depth meter:** Mr. Mine new resource/character every 100-500 m `[EST]`; Trimps Improbabilities at zone 59, Corruption at 181 `[S]`.
- **Farm-value gates:** Egg Inc `[S]` (x45-x710 per egg; Decade world gates are x2.5-3.5, not this).
- **Multi-slot gate:** Shark Game gate = several resource slots, each `floor(worldGateCost[slot] x planetLevel x 0.9^reducer)` `[CODE]`; the Decade gate is likewise 3-4 named costs shown up front (R28).
- **Travel action:** Idle Loops opens each of nine zones with a one-off action, gated by stats not waiting `[CODE]`.
- **Price reveal:** CC shows later buildings at ~1/3 of price so the next tier is visible `[S]`.
- **Narrative gate:** Spaceplan and UP Trust milestones on Fibonacci-spaced counts `[S]`.
- **Spend-to-unlock:** Leaf Blower first-prestige "Areas 20 coins" pushes past Platinum to Bismuth `[S]`; Tap Titans 2 stage 60.
- **Currency gate:** AdCap planets unlock via prior planet's angel total.
- Anti-pattern: fixed gates the player cannot see (C6; PK late unlocks "need wiki"). KG lesson: "Fixed reset thresholds are discoverable thresholds: telegraph in UI."

## S5. Mid-run goals and ladders inside a stage (14 games)
- AdCap: cycle halvings at 25/50/100/200/300/400 owned, 12 max halvings `[S]`.
- AD: x2 per 10 bought; 150+ achievements; boosts at `20 + 15*n`; galaxies `80 + 60*n` `[S]`.
- CH1/IC: boss every 5 zones/areas; IC patron objectives at depth thresholds.
- ADR: village stage names by hut count (Lonely Hut ... Raucous Village) `[S]`.
- C2S: "Milestones keep fresh goals every few minutes" `[EST]`.
- UP: Trust, WireBuyer (7,000 ops), MegaClippers at 75 AutoClippers `[S]`.
- Farm Away orders `[EST]`; IMT 5 prestiges per mine `[S]`; Leaf Blower Combo cap "done moments"; Trimps perk caps (Anticipation 10, Coordinated 15) `[S]`.
- Psychology: nested goal gradients (Kivetz 2006) and endowed progress (Nunes and Dreze 2006; 34% vs 19% completion) (`research/psychology.md` 5-6).
- Sim: best sweep config gave 97% of goals in the 15-600 s band, 32 goals in 3 h. Campaign sim v3 (per world about 51 unique goals = 8 tiers x (1 + 5 milestones) + about 11 rides): only 64-73 % of sessions contain a new unique goal, max dry streak 2 (4 in W4), so at least one more beat per session (mastery node, album entry, Photo Window, fusion discovery) must be designed in (R25).

## S6. Replay variants, challenges, handicaps (9 games)
- Idle Champions: restricted variants re-skin the same levels with extra rewards `[PUB]`.
- KG challenges (Winter Has Come, Ironwill) `[S]`; NGU challenges and Evil modes; Evolve challenge genes multiply all reset rewards `[SRC]`; AD challenge stack; Synergism corruptions `[MEM]`; Bitburner BitNodes with multiplier tables; RG factions/abdication; Idle Wizard classes (each ascension form differs).
- Role: they extend value of old content without writing new worlds.

## S7. Per-stage modifier tables (5 games)
- Bitburner `currentNodeMults` (server growth, hacknet income, etc.) `[SRC]`; KG seasons (winter catnip penalty) `[M]`; Evolve universes (heavy, micro, antimatter, magic) `[SRC]`; Trimps Universe 2/Radon; Synergism corruptions.
- Cost to implement: a handful of tuned numbers per world gives strong variety (Bitburner lesson 6).

## S8. Narrative, theme and art swap (10 games)
- C2S: evolution timeline, per-era art and educational card text (cell -> fish -> mammals -> humans -> singularity).
- ADR: reveal as story beats. Spaceplan: sarcastic narrator reacts to unlocks. UP: horror escalation, "ending with a real 'oh no'".
- Swamp Attack: chapter palette swap plus boss; AFK Arena: story chapters; Tap Titans 2: biome visuals each set of stages; Mr. Mine and Farm Away: the visible mine/farm as progress meter; Idle Breakout: brick colours per tier.

## S9. Progress that raises income without a reset (4 games)
- AFK Arena: each cleared stage raises AFK income permanently, "progress compounds without a reset" `[PUB]`; Melvor (no prestige; breadth and mastery); Swamp Attack/ADR (single run). Also AD's achievements give small permanent multipliers.
- Value: instant reward and no loss-aversion cost (`research/psychology.md` section 8: frame as gain).

## S10. Reveal the next stage early (4 games)
- CC 1/3-price reveal; Candy Box 2 "page grows" as thresholds are crossed; C2S era unlock costs jump ~1e3-1e6 but are visible; Egg Inc shows egg tiers by farm value.

## S11. Throttle new systems (5 games)
- Good: Spaceplan 2-4 visible resources; Synergism intends one subsystem per layer; Bitburner unlocks subsystems only through the outer prestige.
- Bad: NGU, Synergism and Leaf Blower show too many at once; NGU lesson "at most one new system per Rider world".

## Pacing numbers collected
- Era every ~20-40 min with a new tree node every 30-60 s (C2S `[EST]`). The v1 continuous-time sweep (first prestige ~25 min, cycles 20-45 min, threshold 1e8) is superseded for Decade by campaign sim v3: first Final Form Ride at about 8 min in every world (T_w calibrated), 9-11 rides per 3.2-day world, about one per 7 h.
- A world sized to about 3.2 days for the reference 3x10 min/day player (sessions at about 08:00/13:00/21:00, stepped offline 50/25 %, cap 8 h): 2 sessions/day about 4.5 d, 1/day about 9 d, 6/day about 2 d (`sim/results.md` Offline lever, Player archetypes).
- AD community estimates: first Infinity hours to 2 days, first Eternity days to a week (`research/math_of_idle_games.md` 4, weak). Cookie Clicker golden cookies: spawn gap 5-15 min, lifetime 13 s `[CODE]` (R38 reference, rescaled by R38b).

## Failure modes (sequential specific)
1. Skin-only restart (AdCap planets; Swamp Attack chapters).
2. Carryover too strong (sim carry x2, cost x1) or too weak (cost x10).
3. Too many layers (CH2, Synergism, NGU).
4. Mid-game lull between layers (AD Break Infinity -> Eternity).
5. Diluting earlier worlds with a global currency (CH2 mitigates with per-world currencies `[EST]`); in Decade, archived Seals give only a bounded flat +1 % per cleared world.
6. Mandatory event/parallel worlds (IMT event mines).
7. Second-layer soft wall (Magic Research, Mr. Mine second prestige): make the second layer's first purchase affordable in ~10-15 minutes.

## Implications for Kamen Rider Decade world-progression idle game
Source hooks from `research/decade_worlds.md` are partly author knowledge (Agito unverified); verify before shipping. Show order is Kuuga, Kiva, Ryuki, Blade, Faiz, Agito, Den-O, Kabuto, Hibiki; the game starts with Kabuto and ends with Kuuga as the finale (DECADE_IDLE_DESIGN section 3). Aligned with DESIGN_RULES.md (R-numbers).

1. **One new rule/verb per world (S1; R26).** Kabuto Clock Up + Cast Off (at 40 owned), Den-O contracts, Faiz routing, Ryuki Advent cards, Blade fusion, Kiva day/night, Agito forms, Hibiki rhythm, Kuuga colour switch. **Additional systems at most one per world** (Photo Window + mastery tree in World 1 as the tutorial set; Album W2, Form Deck W3, Approach pick W4, Constraint Shoots W5, Studio Garden W6; W7-9 none, deepen existing).
2. **A world is a data record (S7; R27, R28).** {name, tier names, ratio table, rule id, local currency, gate of 3-4 named costs, per-world T_w, carry c}; adding a world is a data edit (Shark Game `world.js`, Evolve per-reset constants, Bitburner `currentNodeMults`). World-local currency from world 2-3, at most 3 visible currencies on the main screen (Shots, Seals, one per-world counter; Idle Wizard "This Realm" scoping).
3. **Carryover (S3; R23, R24, R29, R42).** Dimension Ride = fixed world-clear carry c plus one Ride Card, not a formula (8 hops). Card collection, automation, forms never reset; archived Seals add a bounded flat +1 % per cleared world; per-world best memory `1 + best/10` for revisits (Progress Knight, CODE); cleared worlds raise passive income immediately (AFK Arena). **Budget every carry source inside c so that world drift d = s / total carry stays in [1.0, 1.07]** (s = 3, c about 2.25); the old "cost/carry in [1.0, 1.5], target 1.3, worlds lengthening 1.3-1.5x" is superseded. If cards, archive or achievements are left outside c, worlds collapse (27 d campaign -> 12 d).
4. **Gate by a visible objective (S4; R28).** Three named costs: lifetime Shots >= G_w (pacing-controlled), a collection requirement ("3 Zecters"), a mechanic requirement ("use Hyper Clock Up once"); completing always pays a flat Ride Card (Shark Game essence analogue). **Gates grow x2.5-3.5 per world** (6.2e15, 1.8e16, 5.5e16, 1.9e17, 4.9e17, 1.3e18, 4.2e18, 1.4e19, 4.0e19) because they are outputs of calibration for 3.2-day worlds, not free parameters. Reveal the next world's card at about 1/3 of the gate (R30 endowed progress on arrival, with the reason shown).
5. **Mid-world goals (S5; R3, R4, R25, R32).** x2 milestones at 10/25/50/100/200 shown as bars; 9-11 Final Form Rides per world; plus at least one further beat per session because only 64-73 % of sessions get a ride/tier/milestone goal. Worlds 4-6 each need a mid-world surprise (AD Break Infinity -> Eternity lull is the counter-example). Keep goal gaps in the 15-600 s band and never longer than 30 min inside a session; avoid x3 milestones.
6. **Variants (S6; R31).** World 9 (Kuuga) ends in a finale plus a post-credits mode: replay worlds with restrictions ("Another World") and an optional "All Riders" layer (the only formula layer, log-scaled). Prestige Tree "Mastery" re-runs earlier layers with changed rules; Shark Game's random planet shortlist is an alternative to a fixed order (not adopted: fixed order, Kabuto first).
7. **Narrative skin (S8).** Tsukasa photographs and restores each world (no fighting); narrator quips on unlock; Ride Cards as the reward verb.
8. **Time budget (S3, R25, R34).** About 3.2 days per world for the 3 x 10 min/day reference player, about 29 days (4 weeks) for 9 worlds; 1 session/day 80-150 d, 6/day 16-33 d (campaign length is proportional to 1/sessions-per-day). Offline production is existential and stepped (50 % first 2 h, 25 % beyond, cap 8 h; 24 h as light-player upgrade, R33); optionally bank offline time as x5 spendable speed (Idle Loops, R36). First Final Form Ride about 8 min into every world (not 25 min), then about one per 7 h. Calibrate gates with offline auto-spend on (it shortens worlds 26-44 %, R37); a ride cooldown was simulated and rejected as a fairness lever (R34).
9. **Avoid (failure modes).** Skin-only worlds; parallel mandatory event worlds; carry sources outside the budget (d < 1) or d > 1.2 (dry streaks of 5-7); cost-scale walls; more than 3 prestige layers; more than one extra system per world; Gnorp-style opaque banked-progress semantics.
10. **Evidence caveat and open items.** Sim v3 is a toy with a greedy omniscient player; builds and events are not coupled to the campaign model; worlds 3-9 gates are placeholders until content design; exact world length, whether nine worlds is right, and the fixed carry per world need play-test. Treat all `[M]/[E]` numbers in the game files as hypotheses.
