# Prestige designs across 37 idle/incremental games

Inputs: all `games/*.md`, `research/*.md`, `sim/results.md`. Evidence legend: CONFIRMED = `[CODE]`, `[SRC]`, `[S]`, `[SOURCE CODE]`; ESTIMATED = `[M]`, `[E]`, `[EST]`, `[unverified]`, `[MEM-LOW]`; DERIVED = my arithmetic. Verification logs in each game file override earlier text. Games with no prestige or no data are listed in section 6 so the survey is complete.

## 1. Formula comparison

"x to double" = factor by which the measured input must grow to double the prestige currency (DERIVED: 2^(1/exponent)).

| Game (file) | Input measured | Formula | x to double | Per-point value | Evidence |
|---|---|---|---|---|---|
| Cookie Clicker (games/cookie-clicker.md) | lifetime cookies | chips = floor(cbrt(C / 1e12)); M chips need 1e12 * M^3 | 8x | +1% CpS per level (100 chips = 1e18 cookies = only +100%) | S; guide claim of 5% rejected |
| Adventure Capitalist (games/adventure-capitalist.md) | lifetime earnings | angels = floor(150 * sqrt(L / 1e15)) minus owned; thresholds 44.4B, 177.8B, 400B for first 3 angels match | 4x | +2% per angel (additive, base rate) | formula consistent with S thresholds, text not seen; +2% S |
| Realm Grinder (games/realm-grinder.md, research/math_of_idle_games.md 3.1) | max currency | p = (sqrt(1 + 8c/1e12) - 1)/2 | 4x | +3% gold per gem (single PC Gamer guide) | formula S (Part III excerpt); per gem unconfirmed |
| Egg Inc (games/egg-inc.md) | earnings since reset | (c/1e6)^0.14 in Part III excerpt (article's own doubling number 128x implies 1/7); community ~ farm value^0.21 | 141x (exponent 0.14) / 128x | +10% earnings per soul egg, linear; +1 pt/level Soul Food (to 150%); x1.05-1.10 per prophecy egg | S; exponent unverified, official FAQ says each egg costs more |
| Clicker Heroes (games/clicker-heroes.md, research math 5.3) | highest zone | Hero Souls = floor(((zone - 100)/5 + 4)/5)^1.3 * bonus (wiki excerpt) or 1 per 2,000 hero levels (blog) - two sources disagree | zone x1.7 for exponent 1.3 | +10% damage per soul | S, conflicting |
| Clicker Heroes transcend | total hero souls | Ancient Souls = floor(5 * log10(HS)) per blog, contradicted by its own examples | log | | unverified |
| Antimatter Dimensions (games/antimatter-dimensions.md, research math 3.4) | max antimatter this run | IP = 10^(log10(AM)/308 - 0.75) | +92.7 orders of magnitude of AM | x1 multiplier via upgrades | SRC |
| AD Eternity | max IP | EP = 5^(log10(IP)/308 - 0.7) | +133 OOM of IP | | SRC (3 table points reproduced S) |
| Synergism (games/synergism.md) | coins this prestige | floor((coins/1e12)^p), p = 0.5 + challenge-5 completions/100 | 4x (p = 0.5) | | SRC |
| Synergism Transcend | coins this transcension | floor((c/1e100)^0.03) | 1.1e10x | | SRC |
| Synergism Reincarnate | transcend shards | floor((s/1e300)^0.01) | 1.3e30x | | SRC |
| Evolve (games/evolve.md) | final population + knowledge | plasmid = round(pop / pop_divisor) + one per knowledge step (k_inc grows by k_mult); soft cap plasmid_cap, overflow adds at most another cap; phage = floor(log2(plasmids) * e * phage_mult) | linear in population | log curves on effect | SRC |
| Bitburner (games/bitburner.md) | batch of augmentations purchased | no currency formula; price x1.9 per aug bought; BitNode on hacking w0r1d_d43m0n | n/a | permanent multipliers | SRC for 1.9; BitNode text MEM |
| Progress Knight (games/progress-knight.md) | per task max level, evil | Rebirth One keeps max level, XP mult `1 + maxLevel/10`; Rebirth Two evil += evilControl.effect * bloodMeditation.effect, resets max levels to 0 | n/a | | CODE |
| Leaf Blower Revolution (games/leaf-blower-revolution.md) | run progress | prestige coins; "Prestige++" raises gain; formula not given | n/a | | S (shop), formula missing |
| Idle Miner Tycoon (games/idle-miner-tycoon.md) | production rate at prestige and prestige number | Super Cash; cost to prestige rises; max 5 per mine; ~x4 income | n/a | | S; closed form unknown |
| Cell to Singularity (games/cell-to-singularity.md) | entropy | Metabits "each requires more than the last" | likely k<1 power | | PUB comment, EST |
| Trimps (games/trimps.md) | highest zone, cells, looting perks | Helium; perks cost base * 1.3^level with caps | n/a | | S (perks), M (helium) |
| Idle Champions, Tap Titans 2, Idle Slayer, Idle Wizard, Reactor, Factory Idle, Magic Research, Idle Mining Empire, Mr. Mine, Idle Breakout, Increlution, Farm Away | | sqrt / sqrt-of-progress guesses `floor(sqrt(lifetime / T))` or level^k | 4x if sqrt | +2-10% per point guesses | EST only; not evidence |

Observations (confirmed):
- Real exponents: 1/2 (AdCap, Realm Grinder, Synergism layer 1), 1/3 (Cookie Clicker), 0.14 (Egg Inc), then 0.03 and 0.01 at deeper Synergism layers, log-of-log in AD, a polynomial (zone^1.3) in Clicker Heroes, linear-in-population (Evolve). Cube-root and 0.14 are deliberately slow; Synergism and AD pick tiny exponents/logs because their input numbers are astronomically large (rule: the gain number stays human-readable, games/synergism.md).
- Pecorella's survey: "most games use a fractional exponent such as sqrt or cbrt, not logs" (research/math_of_idle_games.md 3.1). AD, Evolve and Synergism deep layers are the exception, driven by Decimal-sized numbers.
- Lifetime-based versus since-reset versus max-currency: lifetime (AdCap, CC) pays the delta only; max-currency (Realm Grinder) pays nothing for resetting at the same peak; since-reset (Egg Inc) pays each run fresh.

## 2. Layers

| Game | Layers (resets, outermost last) | Evidence |
|---|---|---|
| Antimatter Dimensions | Dimension Boost / Galaxy -> Infinity -> Eternity -> Reality -> Celestials -> Doomed (Pelle, whole-game restart) ; challenges 12 normal + 8 infinity + 12 eternity | S, games/antimatter-dimensions.md |
| Synergism | Prestige -> Transcend -> Reincarnate -> Ascension (needs challenge-10 completions) -> Singularity; plus corruptions and challenges 1-15 | SRC for first three, MEM for the rest |
| Realm Grinder | Abdication -> Reincarnation (1e27 gems, each next 1000x) -> Ascension at R39/R99/R159/R219 (S, but first threshold conflicts with 1e144) | S, games/realm-grinder.md |
| Clicker Heroes | Ascension (zone ~100+) -> Transcension (Ancient Souls, Outsiders) -> Primal bosses | S, games/clicker-heroes.md |
| Clicker Heroes 2 | run (transcend) -> world reset -> Great Ancients/Outsiders; prestige points per world | EST, games/clicker-heroes-2.md |
| Evolve | MAD, Bioseed/Cataclysm, Black Hole/Vacuum/Big Bang, AI Apocalypse, Matrix/Retired/Eden, Terraform/Ascension, Descend, Apotheosis; constants table per reset (pop_divisor 3 -> 1; k_mult 1.1 -> 1.004; plasmid_cap 150 -> 2,000) | SRC, games/evolve.md |
| Kittens Game | Reset (karma, paragon) -> Time crystals / Chronoforge -> Challenges (Winter Has Come, Ironwill) | M/S opinions, games/kittens-game.md |
| Bitburner | Install augmentations (soft) -> BitNode destruction (Source Files, up to 3 levels each; BN12 infinite) | SRC / MEM |
| Progress Knight | life -> maxLevel memory -> evil | CODE |
| Idle Wizard | realm -> Exile -> Ascension (Demiurge etc.) -> Paragon | PUB nav, games/idle-wizard.md |
| Adventure Capitalist | Angels per planet; each planet has its own prestige unlocked by the previous planet's angels | S/estimate |
| Egg Inc | prestige (soul eggs) -> epic research / prophecy eggs -> Enlightenment farm | S |
| NGU Idle | Rebirth -> Nuke/Titan kills -> challenges, wishes | unverified details |
| Cookie Clicker | Ascension only; but layered via heavenly upgrade tree, sugar lumps, milk | S |
| Leaf Blower | Prestige -> Gold Leaf shop -> gems/cards/pets -> "Super Prestige" | S/M |
| Idle Miner Tycoon | per-mine prestige (<=5) plus continents | S |
| Tap Titans 2 | Master Reset (stage 60+) -> clan/skill tree -> equipment/pet evolution | PUB/EST |
| Idle Champions | per-adventure reset -> Patron Favor -> Modron automation | PUB-ish |
| Trimps | Portal (Helium) -> Heirlooms Z~90 -> Nature Z~236 -> Radon universe 2, Corruption Z~181, Magma Z~230 | M, treat zones as approximate |
| Cell to Singularity | Reboot -> Metabits -> Singularity -> second timeline | PUB / EST |

Layer count: 1 (Cookie Clicker, AdCap per planet, Factory, Reactor...), 2-3 (Realm Grinder, CH, Egg Inc, Progress Knight), 5+ (AD, Synergism, Evolve). A second layer appears when the first layer's cost to repeat reaches about 4^6 = 4,096x earnings or numbers near 1e30-1e50 (research/design_talks_postmortems.md section 6, DERIVED guideline).

## 3. Timing

- First-prestige times are mostly [EST]: 15-30 min (Synergism), ~30 min (Idle Breakout), 30-60 min (Idle Miner), ~1 h (Tap Titans 2), 1-2 h (AdCap, Leaf Blower, CH), 1-3 h (Evolve), 2-4 h (Slayer), 3-6 h (Bitburner augs, Factory), 1-3 days (Mr. Mine, Idle Mining Empire), 20-50 h (Kittens). See games/synergism.md, games/idle-slayer.md, games/bitburner.md, games/kittens-game.md.
- Mandatory versus optional: AD forces the first reset at 1.79e308 (a natural finish line); AdCap, Cookie Clicker, Egg Inc leave it to the player (research/design_talks_postmortems.md section 5).
- Cadence after first: Evolve 20-60 min once plasmids stack (EST); Idle Slayer 20-60 min (E); Trimps 10 min early to hours late (E); sim best config 22-45 min repeating 8-14 times in 6 h (sim/results.md).
- Reset rule of thumb: prestige when gain >= +50% to +200% of current prestige currency (Pecorella slide, secondhand) or pending >= current for AdCap; Cookie Clicker guides wait for 200+ chips (low-quality sources); Egg Inc guides ~50+ soul eggs. Sqrt means each doubling needs 4x lifetime earnings, so each cycle must buy at least a x4-per-cycle speedup or cycles lengthen (DERIVED, research math 3.2).
- Sim guard rails (sim/results.md): first prestige around 25 min, threshold of 1e8 lifetime best (1e6 = tutorial reset under 20 min; 1e10 pushes past 90 min), do not allow before player has seen >= 60% of the world's tiers. Only 23 of 108 sweep configs satisfied "first prestige 20-90 min and >= 3 prestiges in 6 h".
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

Sim numbers (sim/results.md): 5-10% per point keeps final multiplier 2e2-6e3x; exponent 0.5-0.7 with rebuy at >=2x gives 22-45 min cycles; 0.4 stretches to ~48 min.

## 6. Games with no prestige or with no usable data
No prestige: A Dark Room (games/a-dark-room.md; mobile "ship cargo" is unverified), Candy Box 2 (games/candy-box-2.md), Spaceplan (games/spaceplan.md), Universal Paperclips (games/universal-paperclips.md, small carryover M), Melvor Idle (games/melvor-idle.md), Swamp Attack (games/swamp-attack.md), AFK Arena (games/afk-arena.md; hero ascension merge as soft analogue).
No public data: Guava Juice Tub Tapper (games/guava-juice-tub-tapper.md), Idle Mining Empire, Mr. Mine, Farm Away, Magic Research, Factory Idle, Idle Wizard numbers, Idle Breakout, Increlution, Reactor: any exponent here is a genre guess.

## Implications for Kamen Rider Decade world-progression idle game (no fighting, upgrade-focused)

1. Treat the world hop itself as the prestige: "Ride into the next world" keeps Ride Cards and a compact Decade Driver meta multiplier (research/psychology.md: frame prestige as gain, not loss; AFK Arena's shared cap and Idle Miner's per-mine prestige show how to avoid wipes). Pair with a per-world mini-prestige ("Final Form Ride") that gives world-local points, like Idle Miner (cap 5 per world) or CH2 per-world points.
2. Use a sqrt formula with threshold T around the earnings reached by minute 20-25 (sim: threshold 1e8 lifetime, exponent 0.5-0.7, 5-10% per point) so the first Final Form Ride is at about 25 min and later cycles are 20-45 min, each at least 2x faster. Show pending gain and highlight at pending >= 50-100% of current (AdCap rule). Use cbrt only if you want a slow second-tier (Cookie Clicker style) meta layer.
3. Layer plan: L1 per-world "Final Form Ride" (sqrt); L2 "Dimension Travel" between worlds, which carries a Decade-wide currency with an exponent around 0.14-0.25 or log10-based to keep it small; L3 optional endgame "All Riders" challenge layer. Do not exceed 2-3 layers: A Dark Room, Paperclips and Spaceplan show a finite arc works, while AD/Synergism opacity shows the cost of 5+ layers.
4. Carryover rule: keep permanent unlocks (forms, allies, auto-collectors, QoL) and the layer currency; reset counts and cash. Put automation (like Cookie Clicker Twin Gates, Cell to Singularity autobuy) into the first prestige shop so repeat runs are not manual.
5. Carry ratio vs cost: world n+1 cost scale / carryover in [1.0, 1.5] (sim: 1.3 gives worlds lengthening 1.5x each; <1 trivialises; carry x2 with cost x1 clears world 6 in 0.3 min). Block prestige before the player has seen 60% of the world's tiers (sim) and show a before/after production comparison.
6. Avoid planet-style parallel currencies (AdCap complaint) and hard resets that wipe meaning (PK evil, AD Doomed) in a fan-service game; prefer soft resets where cards persist. If a hard layer is wanted, make it a once-only "Decade Final Form" ending with a New Game+ flag.
7. Timing guard rails: first world gate 10-25 min, no wait longer than one session without a new option, the active layer must carry its own appeal because offline efficiency 0.5 already feeds light players (sim/results.md sessions section).
8. Evidence discipline: every exponent in the game spec must be tagged CONFIRMED (AdCap 150*sqrt(L/1e15), CC cbrt, Synergism 0.5/0.03/0.01, AD 308-OOM layers, Evolve table) or TUNING GUESS (all sqrt placeholders in games with no data).
