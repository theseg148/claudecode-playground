# Synergism
**Sources:** (URLs, required)
Evidence tags used in this file: [SRC] = read directly from the open-source code this session; [MEM] = recalled from memory, not re-verified (web fetch was blocked in the sandbox except raw.githubusercontent.com); [EST] = my estimate.
- https://raw.githubusercontent.com/Pseudo-Corp/SynergismOfficial/master/src/Synergism.ts (resetCurrency, prestige gain formulas) [SRC]
- https://raw.githubusercontent.com/Pseudo-Corp/SynergismOfficial/master/src/Buy.ts (building cost scaling) [SRC]
- https://raw.githubusercontent.com/Pseudo-Corp/SynergismOfficial/master/src/Calculate.ts (offline cap, many multipliers) [SRC]
- https://raw.githubusercontent.com/Pseudo-Corp/SynergismOfficial/master/src/Reset.ts (reset behaviour) [SRC, skimmed]
- https://store.steampowered.com/app/3552310/Synergism/ (Steam page; confirms "many reset layers" description via search snippet, page itself not fetched)
- https://synergism.cc (live game) and https://synergism.fandom.com/wiki/Synergism_Wiki (community wiki; not reachable from sandbox, so wiki-only numbers below are [MEM])

## Core loop
- Buy five tiers of Coin producers (Workers, Crusher, Offering/Alchemies... the five "coin buildings") plus Accelerators and Multipliers that raise production speed and multiplier. Coins buy more buildings, buildings make more coins (and later Diamonds, Mythos, Particles).
- Spend coins on one-time Upgrades, then Prestige -> Transcend -> Reincarnate -> Ascend -> Singularity. Each layer converts the previous layer's currency into a new currency that unlocks a new building set and a new minigame (Runes, Talismans, Challenges, Ants, Cubes, Octeracts, Ambrosia).
- The title idea is "synergy": every system multiplies the others, so progress is a web of multipliers not one number.
- [MEM] The first hour is a classic coin-clicker; by hour ~3-5 the player is juggling 4+ resource screens.

## Resource types
- Coins (layer 0), Diamonds (Prestige currency), Mythos (Transcend currency), Particles (Reincarnation currency), Offerings, Obtainium, Quarks (premium-ish meta currency earned from play and Ascension), Cubes (Wow cubes etc.), Octeracts, Ambrosia and Red Ambrosia (late "Singularity" era).
- Per-layer "shards": Prestige Shards, Transcend Shards (the input to Reincarnation gain), Reincarnation Shards. [SRC: transcendShards is used in reincarnationPointGain]
- Gameplay meta resources: Antiquities, Talisman shards, Runes (levelled with Offerings), Ants (Ant Elo / Sacrifice) etc. [MEM]

## Cost & production growth formulas (public or estimated; mark which)
- Building cost base multiplier is 1.25 per owned building; later tiers use a second base 1.03 and a factorial-style (n!) segment after thresholds. [SRC: decimalBases { building: 1.25, lateBuilding: 1.03 } in Buy.ts]
- Cost scaling thresholds scale with a "reduction" factor: threshold1000 = ceil(reduction*1000), threshold5000 = ceil(reduction*5000), threshold20000 = ceil(reduction*20000), threshold25000, threshold250000. Past each threshold the cost curve gets steeper (inverse factorial 1000/5000/20000 terms are cached). [SRC]
- `reduction = 1 + thrift rune costDelay + sum(researches 56-60)/200 + challenge-4 completions/200 + ant BuildingCostScale`. So the game gives players tools that move the cost "walls" rather than cheapening single buys. [SRC: getReductionValue]
- Softcap constants in Buy.ts: softcap = 1e15 and exponentDR = 1/8 for diminishing-return power on some costs. [SRC]
- Prestige point formula: `prestigePointGain = floor((coinsThisPrestige / 1e12) ^ prestigePow)`, with `prestigePow = 0.5 + CalcECC('transcend', challenge5 completions)/100` (so base is square root, creeping upward with Challenge 5 completions). In Challenge 5 the power drops to 0.01. [SRC]
- With upgrade 16 owned, prestige gain is multiplied by min(10^(1e33), acceleratorEffect^(1/3)). [SRC]
- Transcend: `floor((coinsThisTranscension / 1e100) ^ 0.03)`; upgrade 44 multiplies by min(1e6, 1.01^transcendCount). [SRC]
- Reincarnate: `floor((transcendShards / 1e300) ^ 0.01)`, x5 with upgrade 65, further x achievement "particleGain" reward; inside a challenge the result is raised to 0.01 again. [SRC]
- Offering/auto-generation: while idle the game adds `gain/4000 * dt/0.025` per tick of each currency (i.e. passive 1/160 of a reset per second at base). [SRC: Synergism.ts ~line 3145]
- Diminishing returns are used constantly (Math.pow(x, 0.5), pow 0.4...0.15 chain on overflux orbs, log10 squared on powder). [SRC: Calculate.ts ~1481-1550]

## Prestige structure
- Layer 1 Prestige (reset coins/buildings 1) -> Diamonds. Exponent ~0.5 on coins/1e12. [SRC]
- Layer 2 Transcend -> Mythos. Exponent 0.03 on coins/1e100 (much stronger compression, since coin numbers get gigantic). [SRC]
- Layer 3 Reincarnate -> Particles. Exponent 0.01 on transcend shards/1e300. [SRC]
- Layer 4 Ascension (requires finishing challenge 10 enough times; ascension is triggered via `resetCheck('ascensionChallenge')` after challenge-10 completions reach `challengeRequirement`) -> Cubes, Quarks, constants. [SRC partial, MEM]
- Layer 5 Singularity -> Golden Quarks, Octeracts, Singularity upgrades; resets almost everything including Ascension progress. [MEM]
- Scaling rule that matters: each layer's exponent is smaller (0.5 -> 0.03 -> 0.01) because the inputs grow ever larger, so the gain *number* is always human-readable.
- There are also Corruptions (voluntary difficulty modifiers that boost Ascension rewards) and Challenges 1-15, plus Ascension and Singularity challenges. [MEM]

## Unlock pacing
- [MEM/EST] Prestige unlocks within the first ~15-30 minutes of the first run (coins 1e16-ish); Transcend about 1-2 hours; Reincarnate several hours; Challenge 10 / Ascension 1-2 weeks of casual play; Singularity unlocks months in (the game is intentionally multi-year).
- Mixing in the Steam release (2025) the developers state that the game has "hundreds of achievements" and "multiple prestige layers" per store snippet. [search snippet only]
- Offline queue and automation (auto-prestige, auto-challenge) unlock progressively as research/shop upgrades, so late game is mostly configuring automation. [MEM]

## Offline progress
- Cap: `(86400*3 + 7200*2*research31 + 7200*2*research32) * OFFLINE_TIMER_CAP_BUFF` seconds, i.e. 3 days base, +4 hours per level of research 31 and 32, with a purchasable buff multiplier (PCoinUpgrade). [SRC: calculateOffline]
- Offline time is simulated in 200 ticks (`timeTick = timeAdd/200`, `resourceTicks = 200`), not a closed-form jump, which preserves multiplier interactions. [SRC]
- Offline also credits auto-prestiges: `timeAdd / max(0.25, fastestPrestige)` prestige count, same for transcend/reincarnate; offerings = floor(seconds). [SRC]
- A "time warp" / "tips" path can exceed the cap (1e100) for special items. [SRC]
- On return an offline dialog displays what happened and blocks input during simulation. [SRC]

## Monetization effects
- Originally free browser game; Steam release (paid). In-game "PCoin" (Patreon/shop coins) upgrades exist: e.g. offline timer cap buff multiplier, instant-tick options, extra quark gain. [SRC: PCoinUpgradeEffects.OFFLINE_TIMER_CAP_BUFF used in calculation]
- Premium effects are speed/QoL boosts, not required to progress. [MEM]
- Quarks, the main meta currency, are earnable free through play (and Ascension), with paid upgrades that raise rate. [MEM]

## What players love
- Huge depth of interlocking systems (ants, runes, talismans, cubes, corruptions) with no hand-holding; many "aha" synergies. [MEM, community]
- Constant sense of "next reset is a bigger delta" because of consistent exponent compression.
- Transparent math: the code is open-source on GitHub and wiki-documented, so theorycrafters flourish.
- Frequent updates and large achievement list. [store snippet]

## What players hate
- Extreme complexity and menu sprawl; new players bounce by hour 3. [MEM]
- Lots of required babysitting around early layers before automation unlocks.
- Late-game numbers and timers (Singularity, Ambrosia) feel like a second game with its own grind. [MEM]
- Paid convenience upgrades sometimes read as pay-to-skip. [MEM, EST]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Compress reset gains with a falling exponent per layer (0.5 -> 0.03 -> 0.01 in Synergism): world reset = small readable number even when raw currency is e30+.
2. Use "cost walls" as designed milestones: steeper cost curves past N owned (Synergism: 1000/5000/20000/25000/250000), plus upgrades that push the wall out. Rider Form upgrades could shift each world's wall.
3. Reset passively accrues: auto-resets credited offline as `timeAway / fastestResetTime` is an elegant, honest offline model for a Decade world-cycle.
4. Simulate offline in ~200 ticks rather than one jump so multipliers interact; or fake it cheaply with closed forms plus a cap of ~3 days.
5. Make each new layer introduce *one* new subsystem (Synergism does; its weakness is too many). For Decade, each Rider world = one subsystem (e.g. Kuuga forms, Den-O Imagin contracts).
6. Gate big resets behind a challenge (Ascension needs Challenge 10): in a no-fighting game use "Rider trial" upgrade puzzles.
7. Keep a meta currency (Quarks) that is free-earnable; monetization should only buff offline caps/speeds.
8. Do not copy menu sprawl; show 2-3 screens max per world. [EST based on complaints]


## Source-verified formulas
All excerpts [CODE]. Current repo is `Pseudo-Corp/SynergismOfficial` (branch `master`); base: `https://raw.githubusercontent.com/Pseudo-Corp/SynergismOfficial/master/` (files `src/Buy.ts`, `src/Synergism.ts`, `src/Cubes.ts`). The older `Pseudonian/SynergismOfficial` repo only has a v2.1.2 `Synergism.js` snapshot (`https://raw.githubusercontent.com/Pseudonian/SynergismOfficial/master/Synergism.js`), used below as a cross-check. `Calculate.ts` offline-cap logic (`runOfflineProgress`) was not read.

**Building base costs and growth** [CODE] `src/Buy.ts` L14-40 (`producerData`)
```ts
coin:    costs: [100, 1000, 2e4, 4e5, 8e6],   growth: [1, 2, 3, 4, 5]
diamond: costs: [100, 1e5, 1e15, 1e40, 1e100], growth: [1, 3, 6, 10, 15]
mythos:  costs: [1, 1e2, 1e4, 1e8, 1e16],      growth: [1, 3, 6, 10, 15]
```
**Cost formula** [CODE] `src/Buy.ts` L131-195 (`createBuildingCostCalculator`)
```ts
const add1s = 1 / (Math.pow(1.25, growth) - 1)
let steps = growth * owned           // cost *= 1.25^steps
cost = baseCost.times(decimalBases.building.pow(steps)); cost = cost.subtract(add1s)
```
So the per-purchase ratio of tier k is `1.25^growth_k`: coin tiers 1.25, 1.5625, 1.953, 2.441, 3.052; diamond/mythos tiers 1.25, 1.953, 3.815, 9.31, 28.4. Extra softcaps stack at owned >= 1000 (factorial + (1+growth/2)/1000 term), 5000 (100+100*growth), 20000 (1e7+1e7*growth), 250000 (x1.03 per extra) [CODE] same function L165-190.

**Tesseract buildings (ascension tier)** [CODE] `src/Buy.ts` L666, L737, L809
```ts
price = tesseractBuildingCosts[i] * Math.pow(owned + 1, 3)   // base [1,10,100,1000,10000]
```
Polynomial (cubic) cost instead of exponential for late-layer buildings.

**Prestige gain formulas (falling exponent per layer)** [CODE] `src/Synergism.ts` L3434-3456; same in old v2.1.2 `Synergism.js` L2321-2345
```ts
let prestigePow = 0.5 + CalcECC('transcend', player.challengecompletions[5]) / 100
let transcendPow = 0.03
prestigePointGain  = floor((coinsThisPrestige / 1e12) ^ prestigePow)
transcendPointGain = floor((coinsThisTranscension / 1e100) ^ transcendPow)
reincarnationPointGain = floor((transcendShards / 1e300) ^ 0.01)
```
Reset availability [CODE] `Synergism.js` (v2.1.2) L2363-2380: prestige when `coinsThisPrestige >= 1e16 || prestigePointGain >= 100`; transcend when `coinsThisTranscension >= 1e100 || transcendPointGain >= 0.5`.

**Multiplier base** [CODE] `Synergism.js` (v2.1.2) L1613: accelerator power `acceleratorPower = Math.pow(1.1 + ..., ...)` i.e. each Accelerator is ~+10% speed baseline.

**Design takeaways**: prestige currency = sqrt-ish of raw currency (^0.5) at layer 1, ^0.03 at layer 2, ^0.01 at layer 3; building ratio ladders are 1.25^(1,2,3,4,5) per tier so each next tier is harsher.

### Round 2: offline cap [CODE]
`src/Calculate.ts` (https://raw.githubusercontent.com/Pseudo-Corp/SynergismOfficial/master/src/Calculate.ts) L826-840 `runOfflineProgress`:
```ts
const maximumTimer = !fromTips ? (86400 * 3 + 7200*2*player.researches[31] + 7200*2*player.researches[32]) * PCoinUpgradeEffects.OFFLINE_TIMER_CAP_BUFF : 1e100
const timeAdd = Math.min(maximumTimer, Math.max(forceTime, (now - player.offlinetick)/1000))
const timeTick = timeAdd / 200;  // 200 simulated resource ticks
```
Base offline cap = 72 h (3 days); research 31 and 32 each add +4 h; multiplied by a paid-upgrade buff. Simulated in 200 slices; prestige/transcend/reincarnation counts credited as `timeAdd / max(0.25, fastestX)`.
