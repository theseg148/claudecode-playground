# How games with sequential worlds, zones, eras or layers keep each one fresh

Scope: all 37 `games/*.md`, `research/psychology.md`, `research/player_complaints.md`, `research/math_of_idle_games.md`, `research/decade_worlds.md`, `sim/results.md`.

## Method and honesty notes
- A game counts as "sequential" if its files describe an ordered series of worlds/zones/eras/layers/phases/chapters/realms. About 30 of 37 qualify in some form. Pure tier ladders inside one economy (AdCap businesses, CC buildings) are noted only where they use the same freshness tricks.
- Evidence tags are inherited: `[SRC]`/`[CODE]` for Evolve, Synergism, Bitburner, PK; `[S]` for AD, CH1, Melvor, Trimps; `[M]/[E]/[MEM]` for most others. Treat examples marked weak as inspiration.
- Counts are manual tallies of the technique being named in the file (not keyword counts).
- The sim (`sim/worlds.py`, `sim/results.md`) is a toy model with a greedy buyer, no active spikes and no prestige inside worlds.

## Technique index

| # | Technique | Games (count) |
|---|---|---|
| S1 | New rule or verb per stage | 14 |
| S2 | New currency per stage, with scoped counters | 12 |
| S3 | Carryover rules that make revisiting cheap but not trivial | 11 |
| S4 | Clear gate into the next stage (cap, challenge, objective, narrative) | 15 |
| S5 | Mid-run goals and ladders inside a stage | 14 |
| S6 | Replay variants, challenges and handicaps | 9 |
| S7 | Per-stage modifier tables | 5 |
| S8 | Narrative, theme and art swap | 10 |
| S9 | Progress that raises income without a reset | 4 |
| S10 | Reveal the next stage early | 4 |
| S11 | Throttle new systems (one per stage, few visible currencies) | 5 |

## S1. A new rule or verb per stage (14 games)
- UP: clips -> drone swarm -> space probes; each phase swaps the core verb and re-contextualises earlier upgrades (`games/universal-paperclips.md`).
- ADR: village economy -> world-map survival -> ship-flying shooter, each triggered by a story beat (`games/a-dark-room.md`).
- AD: each layer "re-teaches the same loop with new rules" (Infinity challenges, Eternity time studies, Reality glyphs, Celestials with their own rules) (`games/antimatter-dimensions.md`).
- Evolve: each reset type is a different mechanic with its own constants (`games/evolve.md`).
- Synergism: each layer unlocks a new building set and minigame (runes, ants, cubes, octeracts) (`games/synergism.md`).
- Idle Wizard: each realm adds "a twist (rule modification)"; classes change mechanics (`games/idle-wizard.md`).
- Idle Champions: "Introduce one new gimmick per world" (lesson); each campaign adds champions and a gimmick (`games/idle-champions.md`).
- Clicker Heroes 2: new monsters, boss mechanics and skill-tree nodes per world (`games/clicker-heroes-2.md`).
- Trimps: Heirlooms, Nature, Magma, Universe 2 "each layer is a new game within the game" (`games/trimps.md`, zone numbers `[M]`).
- Bitburner: BitNodes unlock new APIs/systems (Gang, Corporation, Bladeburner) (`games/bitburner.md`).
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
- Kittens Game, AD (IP -> EP -> RM), Idle Champions (Favor per patron).
- Risk: AdCap-style parallel economies "fragment the player base" (`games/adventure-capitalist.md`); CH2 4+ layers confuse.

## S3. Carryover rules (11 games)
- **Max-level memory.** PK: each task remembers best level; next life XP x `1 + maxLevel/10`; Rebirth Two zeroes it for a global Evil multiplier `[CODE]`.
- **Shared cap lift.** AFK Arena Resonating Crystal lets top heroes raise the level cap of the rest `[PUB]`.
- **Advanced start.** Tap Titans 2 starts new runs at a fraction of best stage `[PUB]`, f ~0.1-0.4 `[EST]`.
- **Keep knowledge, lose machines.** Factory Idle keeps recipes `[EST]`; Increlution keeps unlocked actions; Bitburner keeps augmentations/Source Files `[SRC]`.
- **Per-world prestige.** CH2; Idle Miner Tycoon: up to 5 prestiges per mine with ~4x income each `[S]`.
- **Patron favor.** Idle Champions favor persists; Trimps Helium -> perks (`[S]` perk costs).
- **Auto-prestige credited offline.** Synergism `timeAway / fastestPrestige` `[SRC]`.
- **Rebuild faster.** Cell to Singularity Metabits plus early auto-buy.
- **Sim rule:** world clear time scales as `(cost_scale / carryover)^world`. Carry x2 / cost x3: 8.4, 12.6, 18.8, 28.3, 42.4, 63.6 min (gentle 1.5x lengthening). Carry x3 / cost x3: flat 8.4. Carry x2 / cost x1: 8.4 -> 0.3 (trivialised). Carry x2 / cost x10: 8.4 -> 1047 (walls). Keep cost/carry in [1.0, 1.5] (`sim/results.md`).

## S4. Gate into the next stage (15 games)
- **Natural cap:** AD's 1.79e308 makes each layer end itself.
- **Challenge gate:** Synergism Ascension needs Challenge 10 `[SRC]`; AD challenge stacks (12 normal, 8 infinity, 12 eternity); Idle Wizard exile.
- **Quest chain plus one purchase:** Idle Slayer ascension needs two Rookie Quests and the first Slayer Point `[S]`.
- **Objective threshold:** Idle Champions patron objectives at set areas (e.g., Mirt at area 325) `[PUB]`.
- **Depth meter:** Mr. Mine new resource/character every 100-500 m `[EST]`; Trimps Improbabilities at zone 59, Corruption at 181 `[S]`.
- **Farm-value gates:** Egg Inc `[S]`.
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
- Sim: best sweep config gave 97% of goals in the 15-600 s band, 32 goals in 3 h.

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
- Era every ~20-40 min with a new tree node every 30-60 s (C2S `[EST]`); first prestige ~25 min, later cycles 20-45 min, repeated 8-14 times in 6 h (prestige sweep, threshold 1e8, exponent 0.5-0.7); first gate within 10-15 min (`research/player_complaints.md` C1).
- A world sized to ~3-5 days for a 3x10 min/day player at 50% offline efficiency, ~2 days for heavy players (`sim/results.md` sessions).
- AD community estimates: first Infinity hours to 2 days, first Eternity days to a week (`research/math_of_idle_games.md` 4, weak).

## Failure modes (sequential specific)
1. Skin-only restart (AdCap planets; Swamp Attack chapters).
2. Carryover too strong (sim carry x2, cost x1) or too weak (cost x10).
3. Too many layers (CH2, Synergism, NGU).
4. Mid-game lull between layers (AD Break Infinity -> Eternity).
5. Diluting earlier worlds with a global currency (CH2 mitigates with per-world currencies).
6. Mandatory event/parallel worlds (IMT event mines).
7. Second-layer soft wall (Magic Research, Mr. Mine second prestige): make the second layer's first purchase affordable in ~10-15 minutes.

## Implications for Kamen Rider Decade world-progression idle game
Source hooks from `research/decade_worlds.md` are author knowledge, not fetched; verify before shipping. Show order is Kuuga, Kiva, Ryuki, Blade, Faiz, Agito, Den-O, Kabuto, Hibiki; the user's game starts with Kabuto.

1. **One rule per world (S1).** Kabuto: Clock Up (speed/cast-off). Den-O: contracts/time-skip. Ryuki: Advent-card collection. Faiz: resource routing. Blade: card fusion. Kiva: day/night cycle (a KG-season-style modifier). Agito: form tiers. Hibiki: rhythm/training. Kuuga: colour form switching. Implement as a per-world multiplier table plus one mechanic (Bitburner/Evolve pattern, S7).
2. **Scoped currency per world (S2).** Each world has its own counter (Idle Wizard "This Realm"). Max ~3 visible currencies. A late-world secondary currency (C2S "Ideas") makes later worlds mechanically new.
3. **Carryover rule (S3):** pick one rule, show it. Suggested stack: (a) per-world best-result memory multiplier `1 + best/10` (PK) for revisits; (b) a shared "Decade Driver" cap/multiplier lifted by cleared worlds (AFK Resonating Crystal); (c) card collection never resets. Keep cost_scale/carryover in [1.0, 1.5], target ~1.3 so later worlds lengthen about 1.3-1.5x (carry x2 / cost x3 yields 8.4 -> 63.6 min).
4. **Gate by a visible objective (S4).** "Final Form Ride" challenge puzzle per world (Synergism Challenge 10 analogue), or a natural cap; reveal the next world's card at ~1/3 of its cost (CC). Tie the first world gate to ~10-15 min.
5. **Mid-world goals (S5).** Boss-every-5 as "key moments" (timed assembly, no combat), x2 milestones at 25/50/100, patron-style objectives per Rider, achievement multipliers. Keep goal gaps 15-600 s; avoid x3 milestones.
6. **Variants (S6).** Replay a world with a restriction ("only Form X cards") for extra reward; Decade can revisit each world in "Another World" mode.
7. **Narrative skin (S8).** Photograph each world: Tsukasa narrator quips on unlock, background art per world, "Ride Cards" as the reward verb.
8. **Income bump on clear (S9).** Each cleared world should immediately raise passive income (AFK Arena), so progress feels like a gain, not a reset.
9. **Prestige economy.** World ride = soft prestige (frequent, sqrt/cbrt, 5-10% per point, no resets of collection); a single global "Dimension Break" as the second layer, max 2-3 layers total. Do not offer a ride before ~60% of the world's tiers are seen.
10. **Time budgeting.** Per world 3-5 days for a casual (3 x 10 min/day) with offline eff ~0.5 and 8 h cap; 9 worlds then give a multi-month campaign. This pairs with a ~25 min first micro-gate and 20-45 min cycles inside the world. Spaceplan/UP show a finite arc (2-10 h) is also valid; a finale plus a bonus mode after the credits is an option (Spaceplan lesson 4).
11. **Avoid:** skin-only worlds, parallel mandatory event worlds, strong carryover that trivialises (carry x2, cost x1), cost-scale walls (x10), more than 3 prestige layers.
12. **Evidence caveat:** the sim is a toy; run play-tests per world and treat all `[M]/[E]` numbers in the game files as hypotheses.
