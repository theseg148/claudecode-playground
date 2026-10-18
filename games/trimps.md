# Trimps
**Sources:** ([S] = seen in search snippet, [M] = memory, unverified, [E] = estimate. WebFetch was DNS-blocked.)
- https://trimps.fandom.com/wiki/Coordinated?oldid=6591 [S]
- https://trimps.fandom.com/wiki/Equipment?oldid=7908 and ?oldid=4674 [S]
- https://trimps.fandom.com/wiki/Anticipation?oldid=6805 [S]
- https://trimps.fandom.com/wiki/Power_II [S]
- https://reddit.com/r/Trimps (Perky calculator thread, 2017, via mirror reddit.birdcat.cafe/r/Trimps/comments/6n0mr7/) [S]
- https://trimps.github.io and https://github.com/Trimps/Trimps.github.io (source: main.js, config.js, perks) [M, not fetched]
- Note: wiki revisions are old and balance has changed (Universe 2 / Radon added later).

## Core loop
- Breed Trimps (idle population growth with Geneticists), assign them to Food/Wood/Metal/Science, buy buildings and equipment, send an army into the current zone, fight cells automatically. The player's agency is on economy and gear, not manual combat. (Note: this game does have auto-fighting; for our game we only borrow the economy.)
- Zones 1..~60-100 per run; at the end "Portal" out for Helium, spend Helium on Perks, repeat.

## Resource types
- Food, Wood, Metal, Science, Fragments, Gems, Trimps, Helium (prestige currency), Nurseries, Radon (Universe 2), Bones (from enemies), Dark Essence/Scruffy Perk currencies in later content.

## Cost & production growth formulas
- Perk cost [S]: Coordinated base 150,000 He, cost multiplier 1.3 per level, cap 15; each level cuts the army-size requirement per Coordination by 2% compounding (base 25%) -> ~25M He to max.
- Anticipation [S]: base 1,000 He, x1.3 per level, cap 10, +2% damage per second of breeding time (cap 30 s).
- Power II [S]: base 20,000 He, +500 per level (linear), no cap; +1% additive attack per level.
- General: exponential perks `base * mult^level`; linear perks `base + inc*level` [S pattern].
- Equipment [S/M]: level-1 price per prestige tier (I..X) goes ~40 -> ~1.67 quadrillion; per-level cost = `levelOneCost * costMult^level` (multiplier ~1.2) [M, exact value not retrieved]; each equipment prestige multiplies stats by ~1.19-1.5 [E].
- Zone enemy health ~ exponential in zone (about 1.1-1.2x per zone) and attack similarly [E].
- Helium gain per zone (from kills) rises with zone; big bonus after Z~60 and with Scientist/"Turkimp" [M].

## Prestige structure
- Portal -> Helium (computed from highest zone reached, total cells, and "Looting"-type perks) -> perks give: Resourceful, Power, Toughness, Agility, Looting, Carpentry, Coordinated, Anticipation, Pheromones, Meditation, Relentlessness, Siphonology, Cunning, Curious, Overkill, Capable (late)...
- Layered: Heirlooms (drop-based stat items) at Z~90; Nature (tokens) at Z~236; Universe 2 / Radon at Z~230-ish [M]; Mutations/Corruption at Z~181 [M]; Magma at Z~230 (Dimensional Generator) [M]. Treat zones as approximate [E].

## Unlock pacing
- First 15-30 min: Z1-10. Day 1: first portal around Z~30-50. Week 1: Z60+. Months: Z100-200+ with corruption [E]. Each layer is a "new game within the game".
- Time per run: 10 min early -> several hours late.

## Offline progress
- Yes: when the tab closes, the game simulates "catch-up" while you were gone, capped (a day or so) and the Trimps still gather (Trimps keep fighting?). Time warp is capped (offline limit ~48h?) [M/E].

## Monetization effects
- None: free browser game (also on Steam), by Greensatellite; donations via Patreon.

## What players love
- Satisfying exponential perk-spending; fascinating depth with calculators (Perky/AutoTrimps); tons of long-term layers; low-stress idle.

## What players hate
- Overwhelming late-game complexity; UI built around spreadsheets; needs a bot (AutoTrimps) to stay sane; unclear which perk to buy.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Mix additive perks (+500 per level) with multiplicative (x1.3 per level) so players have cheap/fast and expensive/exponential buys - good for a Rider "form" tree.
2. Give caps to key perks (Anticipation 10, Coordinated 15) so players get "complete" moments.
3. Prestige currency (Helium) driven by zone depth reached = world depth reached - natural analogue.
4. New permanent layers at zone thresholds unlock mid-run (Heirlooms) - drop surprise unlocks at milestones.
5. Do not copy the opaque late-game spreadsheet culture; give an in-game recommender.
6. Auto-fight is replaceable with auto-progress through worlds (no fighting rule) while keeping upgrade focus.


## Verification log
Search date 2026-10-18; WebSearch snippets only (pages not opened).
- Confirmed [S] (trimps.fandom.com/wiki/Broken_Planet): Improbabilities begin at zone 59, last cell of Z59 gives 5x helium; portal first use gives 30 helium (wiki Portal page); Corruption starts zone 181 (tvtropes secondary).
- NOT confirmed: equipment cost multiplier ~1.2, enemy scaling 1.1-1.2/zone, Heirlooms Z90, Magma/Nature/Universe 2 zones, offline cap. Remain [M]/[E].


## Source-verified formulas
All excerpts [CODE] from `Trimps/Trimps.github.io` (branch `master`). Base: `https://raw.githubusercontent.com/Trimps/Trimps.github.io/master/` (files `main.js`, `config.js`).

**Generic building price** [CODE] `main.js` L4819-4833 (`getBuildingItemPrice`)
```js
price = Math.floor((thisCost[0] * Math.pow(thisCost[1], toBuy[compare])) * ((Math.pow(thisCost[1], purchaseAmt) - 1) / (thisCost[1] - 1)));
```
i.e. cost = base x ratio^owned, with geometric-series bulk pricing.

**Building cost table (`[base, ratio]`)** [CODE] `config.js` L11450-11740
| Building | Cost [base, ratio] |
|---|---|
| Hut | food [125, 1.24], wood [75, 1.24] |
| House | food [1500, 1.22], wood [750, 1.22], metal [150, 1.22] |
| Mansion | gems [100, 1.2], food [3000, 1.2], wood [2000, 1.2], metal [500, 1.2] |
| Hotel | gems [2000, 1.18], food [10000, 1.18], wood [12000, 1.18], metal [5000, 1.18] |
| Resort | gems [20000, 1.16], food [1e5, 1.16], wood [1.2e5, 1.16], metal [5e4, 1.16] |
| Gateway | fragments [3000, 1.14], gems [20000, 1.14], metal [75000, 1.14] |
| Collector | gems [5e11, 1.12] |
| Warpstation | gems [1e14, 1.4], metal [1e15, 1.4] |
| Gym | wood [400, 1.185] |
| Tribute | food [10000, 1.05] |
Pattern: ratio drops by 0.02 per housing tier (1.24 -> 1.12) while base cost rises ~10x per tier. Barn uses (verified; Shed/Forge not checked) `calculatePercentageBuildingCost(what,res,0.25)` = `floor(0.25 * resourceMax * increase.by^(purchased-owned))` (cost = 25% of current max storage) [CODE] `main.js` L5017-5023.

**Equipment prestige** [CODE] `main.js` L5953-5970
```js
prestigeMod = (nextPrestigeCount >= 4) ? ((nextPrestigeCount - 3) * 0.85) + 2 : nextPrestigeCount - 1;
cost  = Math.round(equipment.oc * Math.pow(1.069, prestigeMod * game.global.prestige.cost + 1));
stat  = Math.round(equipment[stat] * Math.pow(1.19, equipment.prestige * game.global.prestige[stat] + 1));
```
+19% stat per prestige level vs +6.9% cost.

**Perks (portal / meta prestige currency, Helium)** [CODE] `main.js` L3846-3880 (`getPortalUpgradePrice`) and `config.js` L2959-2995
```js
var growth = (toCheck.specialGrowth) ? toCheck.specialGrowth : 1.3;
amt += Math.ceil(((tempLevel + x) / 2) + toCheck.priceBase * Math.pow(growth, tempLevel + x));
```
Power: modifier 0.05, priceBase 1 (+5% attack/level); Looting: modifier 0.05, priceBase 1; Carpentry modifier 0.1 (+10% housing, compounds) priceBase 25; Resourceful priceBase 50000 (-5% costs, compounding); Coordinated priceBase 150000. So a typical perk costs 1.3^level helium, with a +level/2 additive term.

**Design takeaways**: building ratios 1.24 -> 1.12 across the housing line (soft tapering curves), perks cost 1.3^L but give flat +5%/level (the cost curve, not a hard cap, is what limits perk levels).
