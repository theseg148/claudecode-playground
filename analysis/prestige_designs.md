# Prestige designs across 47 idle/incremental games

Inputs: all 47 `games/*.md` (the original 37 plus derivative-clicker, fallout-shelter, gnorp-apologue, idle-heroes, idle-loops, orb-of-creation, ordinal-markup, prestige-tree, shark-game, soda-dungeon), `research/formula_tables.md` (source mining rounds 1-2), `research/*.md`, `sim/results.md` (campaign sim v3 and the sections Build balance v3, Offline lever, Player archetypes), `DESIGN_RULES.md` (content v3; header still reads v2). Evidence legend: CONFIRMED = `[CODE]` / `[SRC]` (read from source) and `[S]` (search snippet); SECONDHAND = `[PUB]`; ESTIMATED = `[M]`, `[MEM]`, `[E]`, `[EST]`, `[unverified]`, `[MEM-LOW]`; DERIVED = my arithmetic. Verification logs in each game file override earlier text. Games with no prestige or no data are listed in section 6 so the survey is complete.

Refresh note (2026-10-18). Recounted tags across games/*.md: **326 code-read ([CODE] 255 + [SRC] 71), 486 [S], 77 [PUB], 681 estimated ([EST] 259, [M] 151, [MEM] 110, [E] 84, other 77)**; 24 of 47 games carry code-read tags (previously about 11 of 37 had confirmed formulas). The formula table below now marks which prestige formulas are code-confirmed. Game-file corrections applied: AD IP/EP formulas (found in `src/game.js`), Cookie Clicker is NOT closed-source (public mirror, `main.js`), Idle Wizard has two prestige tiers (Exile and Realm), Cell to Singularity premium currency is Darwinium, Clicker Heroes 2 was a paid Early Access title (16 July 2018) delisted 14 March 2024, Idle Champions has offline progress.

## 1. Formula comparison

"x to double" = factor by which the measured input must grow to double the prestige currency (DERIVED: 2^(1/exponent)).

| Game (file) | Input measured | Formula | x to double | Per-point value | Evidence |
|---|---|---|---|---|---|
| Cookie Clicker (games/cookie-clicker.md) | lifetime cookies | chips = floor(cbrt(C / 1e12)); M chips need 1e12 * M^3 (`HCfactor = 3`) | 8x | +1% CpS per level (100 chips = 1e18 cookies = only +100%); heavenly multiplier items +5 / 20 / 25 % | **CODE** `main.js` L4185-4192 (public mirror ozh/cookieclicker); guide claim of 5% rejected |
| Adventure Capitalist (games/adventure-capitalist.md) | lifetime earnings | angels = floor(150 * sqrt(L / 1e15)) minus owned; thresholds 44.4B, 177.8B, 400B for first 3 angels match | 4x | +2% per angel (additive, base rate) | formula consistent with S thresholds, text not seen; +2% S |
| Realm Grinder (games/realm-grinder.md, research/math_of_idle_games.md 3.1) | max currency | p = (sqrt(1 + 8c/1e12) - 1)/2 | 4x | +3% gold per gem (single PC Gamer guide) | formula S (Part III excerpt); per gem unconfirmed |
| Egg Inc (games/egg-inc.md) | earnings since reset | (c/1e6)^0.14 in Part III excerpt (article's own doubling number 128x implies 1/7); community ~ farm value^0.21 | 141x (exponent 0.14) / 128x | +10% earnings per soul egg, linear; +1 pt/level Soul Food (to 150%); x1.05-1.10 per prophecy egg | S; exponent unverified, official FAQ says each egg costs more |
| Clicker Heroes (games/clicker-heroes.md, research math 5.3) | highest zone | Hero Souls = floor(((zone - 100)/5 + 4)/5)^1.3 * bonus (wiki excerpt) or 1 per 2,000 hero levels (blog) - two sources disagree | zone x1.7 for exponent 1.3 | +10% damage per soul | S, conflicting |
| Clicker Heroes transcend | total hero souls | Ancient Souls = floor(5 * log10(HS)) per blog, contradicted by its own examples | log | | unverified |
| Antimatter Dimensions (games/antimatter-dimensions.md, research/formula_tables.md R2.1) | max antimatter this run | **IP = floor(10^(log10(maxAM)/308 - 0.75) x mults)**; the divisor 308 can be lowered by Achievement 103 / Time Study 111; unbroken Infinity always pays 1 IP | +92.7 orders of magnitude of AM (maxAM 1e308 gives only 10^0.25 = 1.78 IP) | x1 multiplier via upgrades | **CODE** `src/game.js` L89-118 (also S) |
| AD Eternity | max IP | **EP = 5^(log10(IP)/308 - 0.7) x mults**, minimum IP 1.79e308 | +133 OOM of IP (x5 EP per +308 OoM of IP) | | **CODE** `src/game.js` L138-163 (3 table points reproduced S) |
| AD Reality | max EP | RM = 1000^(log10(EP)/4000 - 1) x mults (linear `27/4000*logEP - 26` for gains under 10), hard cap 1e1000; before the first Reality log cap 8000 (only 25 % counts above 6000) | x1000 RM per +4000 OoM of EP | | **CODE** `src/core/machines.js` L1-32 |
| Synergism (games/synergism.md) | coins this prestige | floor((coins/1e12)^p), p = 0.5 + challenge-5 completions/100 | 4x (p = 0.5) | | **CODE** `Synergism.ts` L3434-3456 |
| Synergism Transcend | coins this transcension | floor((c/1e100)^0.03) | 1.1e10x | | CODE |
| Synergism Reincarnate | transcend shards | floor((s/1e300)^0.01) | 1.3e30x | | CODE |
| Evolve (games/evolve.md) | final population + knowledge | plasmid = round(pop / pop_divisor) + one per knowledge step (k_inc grows by k_mult); constants per reset: divisor 3 / 3 / 2.5 / 2.2, k_mult 1.1 / 1.015 / 1.014 / 1.012, cap 150 / 400 / 600 / 800 (MAD / bioseed / AI / big bang); overflow `o/(o+cap)*cap`; phage = floor(log2(plasmids) * e * phage_mult); effect `ln(1+p/50)/2.888` | linear in population | log curves on effect | **CODE** `functions.js` L1494-1660, `resources.js` L3238-3246 |
| Kittens Game (games/kittens-game.md) | kittens alive at reset (religion: faith) | paragon = kittens - 70 (above 70); karma kittens piecewise +1 / +3 / +4 / +5 / +10 / +15 per kitten past 35 / 60 / 100 / 150 / 300 / 750; paragon also +1 per 1000 years; faith: `faithRatio += faith/1e6 x (tier+1)^2 x bonus` | linear in kittens | +1 % production per paragon x ratio (limited DR, cap 2x); +10 % storage per 100 paragon; apocrypha `getUnlimitedDR(faithRatio, 0.1) x 0.1` | **CODE** `game.js` getResetPrestige, `prestige.js` L549-576, `calendar.js` L968-972, `religion.js` L1549-1651 |
| The Prestige Tree (games/prestige-tree.md, formula_tables R2.1) | points, then each layer's base resource | "normal" layer: `floor(((base/req)^exponent x gainMult)^gainExp)` with softcap `g^p c^(1-p)`; Prestige P: req 10, exponent 0.5 (0.75 mastered); "static" layer (Boosters, Generators): cost of n-th = `req x base^(n^exponent/gainExp)`, req 200, exponent 1.25, base 5; Time / Space exponent 1.85, base 1e15; Enhance 0.02; Hindrance 0.125; Quirk 0.0075 | sqrt for P (4x); exponents shrink with depth | | **CODE** `layers.js` L1-30, L281-293, L552-564, Modding Tree `game.js` L10-60 |
| Shark Game (games/shark-game.md) | completing a world (gate) | essence on win = 4 + floor(planetLevel / 4), flat; artifacts bought with essence at a per-artifact cost function; gate slot cost = floor(worldGateCost x planetLevel x 0.9^gateCostReducer) | n/a (flat) | permanent artifacts | **CODE** `gateway.js`, `world.js` (per-world gate table and artifact cost functions not read) |
| Derivative Clicker (games/derivative-clicker.md) | reset currency tiers | every 5 of tier N converts to 1 of tier N+1; global multiplier 1 + 0.01 x resetCurr per tier; thresholds `10 x (10 x (10+n))^6` (proofs); automatic "infini-reset" at infinite money | n/a | +1 % per unit; buyables unlock tiers 5-7 and cut build costs / auto-build clicks | **CODE** `script.js` ~L73, L262 |
| Reactor Incremental (games/reactor-incremental.md) | Exotic Particles from Particle Accelerator parts, not lifetime earnings | per tick chance = ln(heat contained, capped) / 10^(5 - level) x heat ratio; objectives also pay EP; Reboot clears the grid, a "refund" reboot lets EP be re-allocated | n/a | EP upgrades gate experimental parts | CODE (cwmonkey clone v1.3.2, parity with the original unverified) |
| Bitburner (games/bitburner.md) | batch of augmentations purchased | no currency formula; price x1.9 per aug bought; BitNode on hacking w0r1d_d43m0n | n/a | permanent multipliers | SRC for 1.9; BitNode text MEM |
| Progress Knight (games/progress-knight.md) | per task max level, evil | Rebirth One keeps max level, XP mult `1 + maxLevel/10`; Rebirth Two evil += evilControl.effect * bloodMeditation.effect, resets max levels to 0 | n/a | | CODE |
| Leaf Blower Revolution (games/leaf-blower-revolution.md) | run progress | prestige coins; "Prestige++" raises gain; formula not given | n/a | | S (shop), formula missing |
| Idle Miner Tycoon (games/idle-miner-tycoon.md) | production rate at prestige and prestige number | Super Cash; cost to prestige rises; max 5 per mine; ~x4 income | n/a | | S; closed form unknown |
| Cell to Singularity (games/cell-to-singularity.md) | entropy | Metabits "each requires more than the last" | likely k<1 power | | PUB comment, EST |
| Trimps (games/trimps.md) | highest zone, cells, looting perks | Helium; perks cost base * 1.3^level with caps | n/a | | S (perks), M (helium) |
| Idle Wizard (games/idle-wizard.md) | highest mana reached in the Realm | Exile pays Mysteries based on highest mana; the class growth-rate guide models Mysteries as the square root of mana; wizard level XP x1.09 per level | 4x if sqrt | | S (wiki Exile and Class Growth Rate Guide snippets); constants not retrieved |
| Idle Slayer (games/idle-slayer.md) | Slayer Points | `12 + lifetimeSP x 4` (wiki snippet, exact context unclear) | n/a | | S, weak |
| Idle Champions, Tap Titans 2, Factory Idle, Magic Research, Idle Mining Empire, Mr. Mine, Idle Breakout, Increlution, Farm Away, Gnorp Apologue, Soda Dungeon, Ordinal Markup, Orb of Creation | | sqrt / sqrt-of-progress guesses `floor(sqrt(lifetime / T))` or level^k | 4x if sqrt | +2-10% per point guesses | EST only; not evidence (Farm Away's and Idle Mining Empire's verification logs say their AdCap-style formulas belong to other games; Magic Research's reset is "Retirement") |

Observations (confirmed):
- Real exponents: 1/2 (AdCap, Realm Grinder, Synergism layer 1, Prestige Tree P, Idle Wizard Mysteries guide), 1/3 (Cookie Clicker, code-confirmed), 0.14 (Egg Inc), then 0.03 and 0.01 at deeper Synergism layers and 0.125 / 0.0075 deep in the Prestige Tree, log-of-log in AD (code-confirmed: one power of 10 per 308 OoM), a polynomial (zone^1.3) in Clicker Heroes, linear-in-population (Evolve, Kittens). Cube-root and 0.14 are deliberately slow; Synergism and AD pick tiny exponents/logs because their input numbers are astronomically large (rule: the gain number stays human-readable, games/synergism.md).
- Pecorella's survey: "most games use a fractional exponent such as sqrt or cbrt, not logs" (research/math_of_idle_games.md 3.1). AD, Evolve and Synergism deep layers are the exception, driven by Decimal-sized numbers.
- Lifetime-based versus since-reset versus max-currency: lifetime (AdCap, CC) pays the delta only; max-currency (Realm Grinder) pays nothing for resetting at the same peak; since-reset (Egg Inc) pays each run fresh.

## 2. Layers

| Game | Layers (resets, outermost last) | Evidence |
|---|---|---|
| Antimatter Dimensions | Dimension Boost / Galaxy -> Infinity -> Eternity -> Reality -> Celestials -> Doomed (Pelle, whole-game restart) ; challenges 12 normal + 8 infinity + 12 eternity | S, games/antimatter-dimensions.md |
| Synergism | Prestige -> Transcend -> Reincarnate -> Ascension (needs challenge-10 completions) -> Singularity; plus corruptions and challenges 1-15 | SRC for first three, MEM for the rest |
| Realm Grinder | Abdication -> Reincarnation (1e27 gems, each next 1000x) -> Ascension at R39/R99/R159/R219 (S, but first threshold conflicts with 1e144) | S, games/realm-grinder.md |
| Clicker Heroes | Ascension (zone ~100+) -> Transcension (Ancient Souls, Outsiders) -> Primal bosses | S, games/clicker-heroes.md |
| Clicker Heroes 2 | run (transcend) -> world reset -> Great Ancients/Outsiders; prestige points per world | EST, games/clicker-heroes-2.md. Only the commercial facts are confirmed: paid Steam Early Access from 16 July 2018 (not free like CH1), delisted 14 March 2024 [S]; the world and layer mechanics stay unsourced |
| Evolve | MAD, Bioseed/Cataclysm, Black Hole/Vacuum/Big Bang, AI Apocalypse, Matrix/Retired/Eden, Terraform/Ascension, Descend, Apotheosis; constants table per reset (pop_divisor 3 -> 1; k_mult 1.1 -> 1.004; plasmid_cap 150 -> 2,000) | SRC, games/evolve.md |
| Kittens Game | Reset (karma, paragon) -> Time crystals / Chronoforge -> Challenges (Winter Has Come, Ironwill) | M/S opinions, games/kittens-game.md |
| Bitburner | Install augmentations (soft) -> BitNode destruction (Source Files, up to 3 levels each; BN12 infinite) | SRC / MEM |
| Progress Knight | life -> maxLevel memory -> evil | CODE |
| Idle Wizard | two wiki-confirmed prestige tiers: **Exile** (from the start) and **Realm** (from e400 mysteries); Ascension forms (Demiurge etc.) and Paragon appear only in the wiki navigation | S for Exile and Realm; PUB nav for Ascension and Paragon, games/idle-wizard.md |
| Adventure Capitalist | Angels per planet; each planet has its own prestige unlocked by the previous planet's angels | S/estimate |
| Egg Inc | prestige (soul eggs) -> epic research / prophecy eggs -> Enlightenment farm | S |
| NGU Idle | Rebirth -> Nuke/Titan kills -> challenges, wishes | unverified details |
| Cookie Clicker | Ascension only; but layered via heavenly upgrade tree, sugar lumps, milk | S |
| Leaf Blower | Prestige -> Gold Leaf shop -> gems/cards/pets -> "Super Prestige" | S/M |
| Idle Miner Tycoon | per-mine prestige (<=5) plus continents | S |
| Tap Titans 2 | Master Reset (stage 60+) -> clan/skill tree -> equipment/pet evolution | PUB/EST |
| Idle Champions | per-adventure reset -> Patron Favor (Divine Favor) -> Modron automation; offline progress exists (champions keep fighting while the game is closed); premium currency is Platinum | S (offline, Platinum, Favor), PUB-ish (rest) |
| Trimps | Portal (Helium) -> Heirlooms Z~90 -> Nature Z~236 -> Radon universe 2, Corruption Z~181, Magma Z~230 | M, treat zones as approximate |
| Cell to Singularity | Reboot -> Metabits (spent in the Reality Engine) -> Singularity -> second timeline; premium currency is **Darwinium** (not Trilobites); sources conflict on the first-prestige trigger (Wikipedia: reaching the Singularity; EarlyGuides: since the Nov 2025 Reality Reboot update, reaching Ideas) | S (currency, timing conflict), EST (layers) |
| Prestige Tree | 31 layers in rows 0-6 (counted by grep, +-1): P -> B, G -> T, E, S -> H, Q, SB/SG ...; the first of T/E/S is cheap and each later one costs 1e180^(order^1.415) more; "Mastery" re-runs earlier layers with buffed exponents | CODE (layerShown, unlockOrder) |
| Idle Loops | each loop is a soft reset of resources; stats, skills, town exploration persist; nine zones opened by travel actions; no hard prestige in 1.0 (talents/challenges files exist, unverified) | CODE / M |
| Shark Game | world (run) -> Gateway: essence, artifact shop, random planet shortlist; 8 world types, gate with several cost slots | CODE |
| Soda Dungeon | run -> dimension resets (tavern upgrades permanent; Soda Dungeon 2: relic of choice per portal, final D11 Warrior's Dimension); one 2017 thread says the original has no true outer loop | S |
| Gnorp Apologue / Ordinal Markup | Gnorp: prestige bar (white = new, grey = banked), talent points, stalls after about two prestiges; Ordinal Markup: "factor shift" wipes all else, later Factor Boosts, Aleph Power, Singularities | S |

Layer count: 1 (Cookie Clicker, AdCap per planet, Factory, Reactor...), 2-3 (Realm Grinder, CH, Egg Inc, Progress Knight), 5+ (AD, Synergism, Evolve). A second layer appears when the first layer's cost to repeat reaches about 4^6 = 4,096x earnings or numbers near 1e30-1e50 (research/design_talks_postmortems.md section 6, DERIVED guideline).

## 3. Timing

- First-prestige times are mostly [EST]: 15-30 min (Synergism), ~30 min (Idle Breakout), 30-60 min (Idle Miner), ~1 h (Tap Titans 2), 1-2 h (AdCap, Leaf Blower, CH), 1-3 h (Evolve), 2-4 h (Slayer), 3-6 h (Bitburner augs, Factory), 1-3 days (Mr. Mine, Idle Mining Empire), 20-50 h (Kittens). See games/synergism.md, games/idle-slayer.md, games/bitburner.md, games/kittens-game.md.
- Mandatory versus optional: AD forces the first reset at 1.79e308 (a natural finish line); AdCap, Cookie Clicker, Egg Inc leave it to the player (research/design_talks_postmortems.md section 5).
- Cadence after first: Evolve 20-60 min once plasmids stack (EST); Idle Slayer 20-60 min (E); Trimps 10 min early to hours late (E); sim best config 22-45 min repeating 8-14 times in 6 h (sim/results.md).
- Reset rule of thumb: prestige when gain >= +50% to +200% of current prestige currency (Pecorella slide, secondhand) or pending >= current for AdCap; Cookie Clicker guides wait for 200+ chips (low-quality sources); Egg Inc guides ~50+ soul eggs. Sqrt means each doubling needs 4x lifetime earnings, so each cycle must buy at least a x4-per-cycle speedup or cycles lengthen (DERIVED, research math 3.2). **Decade rule (R17): ride when it raises production >= 1.5x** (equivalent to "pending >= current" early on); the earlier test "pending >= 2x current" was vacuous at 0 Seals (REVIEW_2).
- Sim guard rails (continuous-time prestige sweep, sim/results.md v1, **superseded for the Decade design by campaign sim v3**): first prestige around 25 min, threshold of 1e8 lifetime best, do not allow before the player has seen >= 60 % of the world's tiers; only 23 of 108 sweep configs satisfied "first prestige 20-90 min and >= 3 prestiges in 6 h". Session-based v2/v3 results replace this: first ride about 8 min via auto-calibrated T_w, no ride before >= 4 tiers bought (R19, about 50 % of an 8-tier world), then 9-11 rides per 3.2-day world, clustered at session starts because offline accrual makes pending jump.
- Complaint data (research/player_complaints.md C6): first prestige ~25-35 min in a postmortem, players who bounce before see no real game; resets "fine when sparse"; HN complaint about too many resets.
- Cliffs: players time resets just before reward jumps (Idle Ronin stage 200, Clicker Heroes primal bosses every 10 zones from 100, research/design_talks 4.4).

## 4. Carryover (what survives which reset)

| Game | Kept | Lost | Evidence |
|---|---|---|---|
| Cookie Clicker | achievements, heavenly upgrades, sugar lumps, milk | cookies, buildings, normal upgrades | S |
| AdCap | angels, gold, upgrades | cash, businesses, managers; spent angels | S |
| Egg Inc | permits, epic research, golden eggs, boosts, artifacts, soul eggs, prophecy eggs | chickens, common research, habs, silos, vehicles | S |
| Clicker Heroes | ascend: hero souls, ancients, gilds ; transcend wipes heroes/ancients/HS but keeps rubies, achievements, relics, Outsiders | S |
| AD | Infinity: IP, challenges, achievements; Eternity: EP, Time Studies, EC; Reality: glyphs, perks, RM | S |
| Realm Grinder | factions unlocked, gems, trophies, rubies, premium upgrades | buildings, upgrades, coins | S |
| Progress Knight | rebirth one: maxLevel per task ; rebirth two: evil, but maxLevel set to 0 | CODE |
| Idle Loops | stats exp, skills, town exploration, story flags (resources, gold, mana reset every loop); offline time banked as spendable x5 speed | CODE |
| Shark Game | essence and bought artifacts persist; `completedWorlds` tracked; world climate level drifts upward as worlds chain | CODE |
| Bitburner | augmentations (permanent); favor accumulates; reputation resets | SRC |
| Trimps | perks bought with Helium, heirlooms | zone, army | S/M |
| Idle Miner | other mines, achievements, Super Cash balance untouched | that mine's cash and levels | S |
| Idle Slayer | permanent upgrades (Permanent Slayer, Permanent Quests) | coins/upgrades | S |
| Evolve | genes/traits, plasmids, phage, dark energy, harmony per reset type | most else | SRC/MEM |
| Kittens | karma, paragon, challenge rewards | buildings, resources | M |
| AFK Arena | no reset; hero levels via Resonating Crystal shared cap | | PUB |
| Synergism | each layer keeps the next layer's currency; Singularity resets almost everything | MEM |

Common pattern: the currency of the layer just completed is permanent; unlocks (factions, recipes, autobuyers) are permanent; production and counts are not. Meta-QoL (autobuy, offline) is bought with the prestige currency so repeat runs do not repeat the grind (Cell to Singularity, Cookie Clicker Twin Gates, Synergism automation).

## 5. Classification

### 5.1 By exponent
1. **sqrt (1/2)**: AdCap, Realm Grinder, Synergism layer 1; guessed in Magic Research, Idle Mining Empire, Mr. Mine, Factory Idle, Increlution. Doubling needs 4x.
2. **cube root (1/3)**: Cookie Clicker. Doubling 8x; 100 chips = 1e18 cookies. Slowest of the pre-layer designs.
3. **small fractional exponent (0.01-0.14)**: Egg Inc 0.14 (about 141x), Synergism transcend/reincarnate. Used when the input range spans 100+ orders of magnitude.
4. **log / log-of-log**: AD (linear in log10; one layer = 308 OOM), Evolve phage (log2) and effect curves, Clicker Heroes ancient souls (5*log10, disputed), Progress Knight in-run effects (log10, log13, log33).
5. **linear in a count / state-based**: Evolve (population / divisor), Clicker Heroes (levels or zone^1.3), Idle Miner (production rate and prestige number), Bitburner (counts of augmentations), Trimps (zones).
6. **threshold with fixed award**: Realm Grinder Reincarnation (1e27 gems, then 1000x), Evolve Apotheosis constant plasmids.

### 5.2 By structure
- **Layered nested** (AD, Synergism, Realm Grinder, Evolve, Clicker Heroes): each layer changes the meaning of the previous one and adds a rule set (challenges) ; pros: freshness and number control (layer ~308 OOM wide); cons: opaque (AD needs wiki), mid-game stretches, long unlock stretches (weeks, community).
- **Single repeating prestige** (Cookie Clicker, AdCap Earth, Egg Inc early, Leaf Blower, Idle Slayer): clear and simple; cons: stagnates, "same loop" complaint (research/player_complaints.md C6).
- **Per-zone / per-area / per-world** (Idle Miner mine <= 5 times, Clicker Heroes 2 world points, Idle Champions adventure reset with favor, AdCap per planet, Trimps zone-based Helium, Tap Titans stage 60+ Master Reset): content progress and prestige are fused; pros: each area has its own power curve and "first clear" feeling (games/clicker-heroes-2.md); cons: planet-style parallel economies "fragment" players (games/adventure-capitalist.md hates).
- **Soft reset**: Bitburner install augmentations (hours), Realm Grinder abdication (10-30 min, unverified), Progress Knight rebirth one (any time), Kittens challenges; keeps most knowledge/meta.
- **Hard reset / whole-game restart**: Progress Knight evil (zeroes maxLevel), Synergism Singularity, AD Doomed, Evolve Apotheosis, Clicker Heroes transcension.
- **No prestige** (finite arc): A Dark Room, Candy Box 2, Spaceplan, Paperclips (small bonus on replay), Melvor (mastery instead), Swamp Attack, AFK Arena (monotone campaign). They hold interest with story beats, caps and finite content (3-10 h).

### 5.3 Pros and cons summary
| Design | Pros | Cons | Seen in |
|---|---|---|---|
| sqrt | readable, doubling 4x, tunable | late cycles lengthen unless bonus per point is large | AdCap, RG, Synergism L1 |
| cbrt | slow, stops runaway multipliers | slow and heavy; 100 chips = +100% only | Cookie Clicker |
| tiny exponent/log | human-readable numbers at 1e300+ | players cannot predict; needs preview UI | AD, Synergism deep |
| linear/state-based | very legible ("pop / 3") | unbounded unless soft capped (Evolve soft cap, overflow max doubles cap) | Evolve, CH |
| per-world | strong narrative fit; fresh start feeling | fragmentation; one-world prestige capped (<=5 in Idle Miner) | Idle Miner, CH2, AdCap |
| soft reset with permanent buy | choice and low loss aversion | cost walls like x1.9 per aug force batching | Bitburner |
| hard reset | resets meaning and rules | "feel like restart", polarizing (AD Doomed) | AD, PK evil |
| strong bonus per point (25%/pt, exp 0.7) | big visible leap | numbers outrun content: final mult 9e4 in sim; itch.io case reaching endgame after 3 points | sim, research 4.4 |
| sub-linear multiplier on sqrt points: (1 + Seals)^0.5 (Decade, R15) | rides stay >= 1.5x each yet the total stays in the hundreds; 9-11 rides per world | needs T_w calibration per world so the first ride lands at about 8 min | campaign sim v3 |

Sim numbers: in the continuous-time prestige sweep (sim v1), 5-10 % per point kept the final multiplier at 2e2-6e3x and exponent 0.5-0.7 with rebuy at >= 2x gave 22-45 min cycles. **Campaign sim v3 (all carry sources, 9 worlds) overturned the linear-bonus advice:** mult = 1 + 0.08 x Seals gives 28-30 rides per world and a final multiplier of 6e6-7e6 (Seals about 7e7-9e7), whereas mult = (1 + Seals)^0.5 gives 9-11 rides per world, final multiplier 240-320 (Seals 6e4-1e5), 64-73 % of sessions with a new unique goal, max dry streak 2 (4 in W4). Adopted: R15/R16/R17.

## 6. Games with no prestige or with no usable data
No prestige: A Dark Room (games/a-dark-room.md; mobile "ship cargo" is unverified), Candy Box 2 (games/candy-box-2.md), Spaceplan (games/spaceplan.md), Universal Paperclips (games/universal-paperclips.md, small carryover M), Melvor Idle (games/melvor-idle.md), Swamp Attack (games/swamp-attack.md), AFK Arena (games/afk-arena.md; hero ascension merge as soft analogue).
No public data: Guava Juice Tub Tapper (games/guava-juice-tub-tapper.md), Idle Mining Empire, Mr. Mine, Farm Away, Magic Research, Factory Idle, Idle Wizard numbers, Idle Breakout, Increlution, Reactor: any exponent here is a genre guess.

## Implications for Kamen Rider Decade world-progression idle game (no fighting, upgrade-focused)
(Rewritten to match DESIGN_RULES.md R15-R25 and DECADE_IDLE_DESIGN.md; the earlier version recommended 5-10 %/pt, a ~25 min first ride and carry/cost in [1.0, 1.5], all superseded by campaign sim v3.)

1. **Two Decade-specific layers plus one post-game layer (R20, R24):** Layer 1 is the in-world **Final Form Ride**; Layer 2 is the **Dimension Ride** between worlds, which is *not* a formula but a fixed world-clear carry c plus one Ride Card (only 8 hops, objective-gated; formula prestige would only add opacity); Layer 3 is **All Riders** after world 9, the only layer with a (log-scaled) formula. At most 3 layers, each deeper layer with a smaller exponent where a formula exists (Synergism 0.5 -> 0.03 -> 0.01 is the model). Cookie Clicker's cbrt is for a slow meta layer only.
2. **Layer 1 formula (R15):** Seals pending = floor(sqrt(run_lifetime / T_w)); production multiplier = **(1 + Seals)^0.5**, not +8 %/seal (linear explodes: about 30 rides per world, multiplier 6e6). Code-confirmed analogues: AdCap/Realm Grinder/Synergism L1 sqrt, Prestige Tree P sqrt. T_w is auto-calibrated per world so the first ride lands about 8 min into play (R10, R16).
3. **When to ride (R16, R17, R18, R19):** ride when it raises production at least 1.5x (the sim rule; highlight it and show before/after production and pending gain); 9-11 rides per 3.2-day world, about one per 7 h of wall-clock, each at least 1.5x by construction; no ride before at least 4 tiers have been bought. Second run's first 30 s must be visibly faster. Rides cluster at session starts (offline accrual makes pending jump), so the unit is "1 ride per 1-2 sessions", not a 20-45 min timer.
4. **Carryover (R21, R29, R42, R36):** keep permanent unlocks (forms, Ride Cards, auto-collectors, QoL, achievements) and the layer currency; reset Shots, generators, tier unlocks and milestone progress. The first-ride shop contains automation plus one QoL perk (Cookie Clicker Twin Gates, Cell to Singularity auto-buy). Never destroy the card collection. Offer banked offline time as an optional x5 spend (Idle Loops).
5. **World drift and carry budget (R23, R25):** world drift d = cost_scale s / total permanent carry should stay in [1.0, 1.07]; *every* carry source (base c, Ride Cards +10 %/card, archived Seals bounded +1 %/world, achievements about x10 at 144 entries) is counted inside c; s = 3, c approx 2.25 in sim v3 (total carry 6.3e3 vs cost scale 6.6e3 at W9). Leaving sources out collapses a 27 d campaign to 12 d, and an unbounded sqrt(archive) bonus to 0.3 d per world. Gates are outputs of calibration: x2.5-3.5 per world (6.2e15 -> 4.0e19), 3.2-day worlds, about 29 d total for the 3-sessions/day reference player (1/day 80-150 d, 6/day 16-33 d).
6. **Avoid (R20, R42):** AdCap-style parallel currencies, hard resets that wipe meaning (PK evil, AD Doomed), 4+ layers (CH2, Synergism). Gnorp Apologue's prestige bar (three conflicting explanations) and Ordinal Markup's full wipe are the new cautionary cases: show "banked / new / needed" numbers and keep at least one item per reset.
7. **Timing and offline guard rails (R9-R12, R33):** first purchase under 60 s, light automation at about 3 min, first ride about 8 min; no wait longer than one session without something to spend or decide. Offline is existential (about 10x faster than none) but its cap is a minor lever: stepped 50 % first 2 h / 25 % beyond, cap 8 h, an 8 -> 24 h cap as a light-player perk.
8. **Builds and events around the ride loop (R13b, R34, R34c):** builds should be balanced (slowest at most 25 % slower; sim 1.19x), and frequent play is rewarded roughly in proportion to sessions per day once rides exist (1 -> 6 sessions/day is about 4x faster); if heavy play should not run away, add a ride cooldown or per-world ride cap.
9. **Evidence discipline:** tag every exponent CONFIRMED-CODE (AdCap `150*sqrt(L/1e15)` [S], Cookie Clicker cbrt, AD IP/EP, Synergism 0.5/0.03/0.01, Evolve table, Kittens paragon, Prestige Tree layers) or TUNING GUESS (the sqrt placeholders in games with no data, and every Decade parameter marked [H]).

**Open items (not resolved):** (a) Whether the 1.5x ride threshold or a ride cooldown/per-world cap is needed to blunt the sessions-per-day advantage (R34, play-test). (b) T_w and the per-world carry c need play-test calibration; the sim is a greedy omniscient player. (c) Exact reward size of the All Riders layer is unspecified. (d) Idle Wizard Exile constants, CH2 layer mechanics and Cell to Singularity Metabit formula remain [EST].
