# Antimatter Dimensions
> Verification pass 2026-10-18 (WebSearch snippets only; pages not opened). [S] = confirmed in a search snippet with the URL given; [unverified] = not confirmed, treat as a design placeholder. See "Verification log" at the bottom.
**Sources:** (WebFetch was blocked by DNS in this session; formulas are from recall of the wiki and open source repo, so verify.)
- https://antimatter-dimensions.fandom.com/wiki/Antimatter_Dimensions_Wiki
- https://antimatter-dimensions.fandom.com/wiki/Infinity
- https://antimatter-dimensions.fandom.com/wiki/Eternity
- https://antimatter-dimensions.fandom.com/wiki/Reality
- https://github.com/IvarK/AntimatterDimensionsSourceCode (the source is public; ground truth for formulas)
- https://ivark.github.io/ (the game)

## Core loop
- Buy Antimatter Dimensions: the 1st makes antimatter, the 2nd makes 1st dimensions, and so on up to the 8th.
- Buy tickspeed upgrades, Dimension Boosts and Antimatter Galaxies.
- Reach Infinity (about 1.79e308 antimatter), spend Infinity Points on upgrades, then repeat.
- Higher layers: Eternity, Reality, then Celestials. Each layer re-teaches the same loop with new rules.

## Resource types
- Antimatter, Infinity Points (IP), Infinities, Eternity Points (EP), Eternities, Time Theorems and Time Dimensions, Replicanti, Reality Machines, Perk Points, Glyphs, Relic Shards, Celestial-specific currencies (Teresa's Reality Machines pour, Effarig's relic shards, Enslaved's Hint, V's Achievements, Ra's memories, Laitela's Dark Matter, Pelle's Remnants).

## Cost & production growth formulas
- Base dimension costs: 1st 10, 2nd 100, 3rd 1e4, 8th 1e24 with per-purchase cost multipliers of x1e3 (1st) rising to x1e15 (8th) [S https://antimatterdimensions.wiki.gg/wiki/Antimatter_Dimensions]. The middle rows (4th 1e6, 5th 1e9, 6th 1e13, 7th 1e18) were not shown in the snippet [unverified].
- Per-dimension multipliers: endpoints x1e3 and x1e15 confirmed [S https://antimatterdimensions.wiki.gg/wiki/Antimatter_Dimensions]; the middle values (1e4, 1e5, 1e6, 1e8, 1e10, 1e12) are [unverified]. The wiki describes cost growth as linear-exponential/exponential-quadratic [S https://antimatterdimensions.wiki.gg/wiki/Dimensions].
- Each batch of 10 bought doubles that dimension's multiplier (x2 per 10) [S https://raw.githack.com/jacorb90/IvarK.github.io/master/howto.html, old community how-to]; dimension N produces dimension N-1 per second [recall].
- Production per second: `D_n_amount * multiplier * tickspeed` feeding the one below. [public]
- Tickspeed: each upgrade reduces the tick interval by 11% (x0.89, about 1.124x faster) [S https://antimatter-dimensions.fandom.com/wiki/Guide]; each Antimatter Galaxy strengthens the effect by 2%, multiplicatively [S old how-to above]. The 1000 ms start, 1e3 starting cost and x10 cost growth are [unverified]. Time Dimension tickspeed upgrades scale x1.33 each, a separate currency [S https://antimatterdimensions.wiki.gg/wiki/Time_Dimensions].
- Dimension Boosts: a dimension shift unlocks the next dimension; a boost needs 20 + 15 x (boosts) base 8th Dimensions (the earlier '20x 4th dimension' was wrong) [S old how-to above]. The 'x2 per boost' effect is [unverified].
- Galaxies: need 80 + 60 x (galaxies owned) base 8th Dimensions [S old how-to above].
- Infinity: reached at 1.80e308 (displayed as 1.79e308 / 'Infinite') [S https://antimatterdimensions.wiki.gg/wiki/Eternity, consistent with 2^1024].
- IP gain: 10^(log10(antimatter)/308 - 0.75) x bonuses, where the divisor is 308 by default, 307.8 with the achievement 'This achievement doesn't exist II', 290 with a Time Study [S old how-to]. Floor is implied [unverified].
- Eternity: requires 1.79e308 (displayed 1.80e308) IP [S https://antimatterdimensions.wiki.gg/wiki/Eternity]. EP table without bonuses: 1 EP at 1.8e308 IP, 2 EP at 1e349, 10 EP at 1e657 [S https://antimatter-dimensions.fandom.com/wiki/Eternity]. The formula EP = 5^(log10(IP)/308 - 0.7) reproduces these three points (my own arithmetic) but the formula text was not seen in a source [unverified].
- Reality: the real unlock requirement was not found [unverified]. Note 1e4000 EP appears only as the condition of specific Reality Upgrades and a Pelle milestone, not as the Reality unlock [S https://antimatterdimensions.wiki.gg/wiki/Reality_Upgrades, https://antimatterdimensions.wiki.gg/wiki/Pelle].
- Replicanti: unlock costs 1e140 IP [S https://antimatterdimensions.wiki.gg/wiki/Replicanti]; base chance 1%, +1% per chance upgrade up to 100%; base interval 1000 ms, each interval upgrade x0.9 with a 50 ms floor; cannot exceed Infinity without Time Study 192 [S Replicanti pages]. Upgrade base costs conflict between sources [unverified].

## Prestige structure
- Infinity: resets Dimensions and Antimatter; keeps IP, Challenges and Achievements.
- Eternity: resets Infinity-related upgrades; keeps EP, Time Studies, Eternity Challenges.
- Reality: resets almost everything; keeps Glyphs, Perks, and Reality Machines and unlocks Celestials.
- Each Celestial has a Reality-gated challenge with its own rules and unique rewards (e.g. Teresa's Perk Shop).
- Doomed (Pelle) is a final reset that restarts the entire game in a hostile mode (Endgame update).

## Unlock pacing
- First Infinity: about 30 minutes to 2 hours for a fresh player. [unverified]
- Break Infinity requires the Big Crunch autobuyer interval at 0.1 s [S https://antimatterdimensions.wiki.gg/wiki/Break_Infinity]. Infinity Challenges unlock after breaking Infinity at antimatter thresholds from e2,000 (IC1, goal e650) to e28,000 (IC8, goal e27,000) [S https://antimatterdimensions.wiki.gg/wiki/Infinity_Challenges]. Hour 3 to 8 timing is [unverified].
- Eternity: first at about 1 to 3 days; Reality: about 1 to 3 weeks; Celestials: weeks to months. [unverified]
- There is a 12-normal-challenge, 8-infinity-challenge and 12-eternity-challenge stack for the first three layers.
- Achievements: 150+ with row-by-row reward bonuses (e.g., Row 1: +x1.1 multipliers).

## Offline progress
- The game simulates offline time with a chunked tick, with the number of ticks configurable in settings (default 1000 ticks per session). Real speed is a "Game speed" multiplier.
- A 'max offline ticks' setting trades accuracy for load time; a skip option computes almost instantly with almost no gain (player report, Reddit mirror). Whether Time Dimensions run offline and the default are [unverified].

## Monetization effects
- None. Free, no ads, no premium currency; Steam version is free. Developer funded by donations/Patreon (Antimatter Dimensions: Steam).

## What players love
- Every layer reinvents the game; the first few hours feel like discovery.
- Big-number satisfaction and many puzzles (challenges).
- Open source, active modding and community spreadsheets.

## What players hate
- Mid-game (Break Infinity to Eternity) can feel long with little change.
- Late layers require wiki reading; it is opaque and math-heavy.
- Endgame content is paced in weeks, and Doomed restarts are polarizing.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- A natural prestige cap (like 1.79e308) is a good "world complete" gate: the player sees a clear finish line for each Rider world.
- Each new layer should change rules (new challenge type) rather than just add a bigger number.
- Use multiples-of-10 purchases that double output; it gives readable breakpoints.
- Provide a pre-prestige preview (IP pending) and show log-scale progress.
- Keep an achievement ladder with small multipliers so every session ends with something earned.
- Free and ad-free play builds trust, so consider placing premium in cosmetics only.

## Verification log

Confirmed [S]:
- Dimension 1/2/3/8 base costs and x1e3..x1e15 multiplier endpoints; x2 per 10 bought; tickspeed x0.89 and +2% per galaxy; boost = 20+15n and galaxy = 80+60n 8th Dimensions (corrected 4th -> 8th); Infinity at 1.80e308; IP formula with divisor 308 and -0.75; Eternity at 1.80e308 IP and three EP table points; Replicanti 1e140 / 1% / 1000 ms / x0.9 / 50 ms; Break Infinity condition; IC unlock range.
Unconfirmed [unverified]:
- Middle dimension costs/multipliers, tickspeed starting cost, exact EP formula text, Reality unlock requirement (1e4000 EP claim was a misattribution), play-time estimates, offline defaults.
Note: boost/galaxy/IP figures come from an old community how-to and may differ in the current Reality-era version.


## Source-verified formulas
All excerpts [CODE], read from `IvarK/AntimatterDimensionsSourceCode` (branch `master`) via raw.githubusercontent.com. Base: `https://raw.githubusercontent.com/IvarK/AntimatterDimensionsSourceCode/master/`. Round 2 (below) located `gainedInfinityPoints()` / `gainedEternityPoints()` in `src/game.js`.

**Antimatter Dimension costs (8 tiers)** [CODE] `src/core/dimensions/antimatter-dimension.js` L337-340, L363
```js
const BASE_COSTS = [null, 10, 100, 1e4, 1e6, 1e9, 1e13, 1e18, 1e24];
const BASE_COST_MULTIPLIERS = [null, 1e3, 1e4, 1e5, 1e6, 1e8, 1e10, 1e12, 1e15];
return this.costScale.calculateCost(Math.floor(this.bought / 10) + this.costBumps);
```
Cost steps once per block of 10 bought (price multiplier per block = tier ratio above: 1e3 ... 1e15), then an extra quadratic-in-log scaling after Number.MAX_VALUE.

**Milestone multiplier (every 10 bought)** [CODE] `src/core/dimensions/antimatter-dimension.js` L632-636
```js
get buyTenMultiplier() { ... let mult = DC.D2.plusEffectsOf(Achievement(141).effects.buyTenMult, EternityChallenge(3).reward);
```
Base x2 per 10 bought of a tier (so each block of 10 doubles that tier AND costs 1e3..1e15 more).

**Tickspeed** [CODE] `src/core/tickspeed.js` L154-160 and L38-43
```js
new ExponentialCostScaling({ baseCost: 1000, baseIncrease: 10, costScale: Player.tickSpeedMultDecrease, scalingCostThreshold: Number.MAX_VALUE });
let baseMultiplier = 1 / 1.1245;  // <3 galaxies; 1/1.11888888 at 1, 1/1.11267177 at 2
```
Tickspeed cost: 1000 x 10^n (ratio 10). Each purchase multiplies speed by 1.1245 at 0 galaxies; galaxies add `0.02 * effects` to the per-purchase step.

**Dimension Boost** [CODE] `src/core/dimboost.js` L16-29 (power), L92-110 (requirement)
```js
let boost = Effects.max(2, InfinityUpgrade.dimboostMult, InfinityChallenge(7).reward, ...)
let amount = 20;                                  // first boosts need 20 of tier (targetResets+3)
if (tier === 8) amount += Math.round((targetResets - 5) * (15 - discount));
```
Boost multiplier x2 base to affected dimensions; boosts 1-5 unlock tiers 5-8 (tier = resets+3, max 8), then cost 20 + 15 x (boosts - 5) of 8th dimension.

**Galaxy** [CODE] `src/core/galaxy.js` L69-75, L42-43, L98-105
```js
baseCost: 80 ; costMult: 60   // amount = 80 + galaxies * 60 (8th dims)
amount += Math.pow(galaxiesBeforeDistant, 2) + galaxiesBeforeDistant;  // distant galaxies, scaling starts at 100
static get costScalingStart() { return 100 + ... }
```

**Cost scaling helper** [CODE] `src/core/math.js` L377-384
```js
const logCost = excess > 0 ? currentPurchases*logMult + logBase + 0.5*excess*(excess+1)*this._logCostScale
                           : currentPurchases*logMult + logBase;
```
Geometric ratio `baseIncrease`, then each purchase past the threshold adds one more factor of `costScale` (cost grows like exp(n^2)).

**Infinity Dimensions** [CODE] `src/core/dimensions/infinity-dimension.js` L53-57, L151
```js
COST_MULTS = [null, 1e3, 1e6, 1e8, 1e10, 1e15, 1e20, 1e25, 1e30];
BASE_COSTS = [null, 1e8, 1e9, 1e10, 1e20, 1e140, 1e200, 1e250, 1e280];
POWER_MULTS = [null, 50, 30, 10, 5, 5, 5, 5, 5];   // multiplier per 10 bought: x50, x30, x10, x5...
mult = mult.times(Decimal.pow(this.powerMultiplier, Math.floor(this.baseAmount / 10)));
```

**Time Dimensions** [CODE] `src/core/dimensions/time-dimension.js` L143-150, L162-180
```js
BASE_COSTS = [null, 1, 5, 1e2, 1e3, 1e2350, 1e2650, 1e3000, 1e3350] (EP);  COST_MULTS = [null, 3, 9, 27, 81, 24300, 72900, 218700, 656100];
costMultIncreases = [1, 1.5, 2.2]; thresholds [Number.MAX_VALUE, 1e1300, 1e6000]  // ratio x1.5 past 1.8e308, x2.2 past 1e1300
```

**Misc constants**: Infinity limit = `Decimal.NUMBER_MAX_VALUE` (1.79e308), tickspeed/dimension purchases lock without Break Infinity: `player.break || this.cost.lt(Decimal.NUMBER_MAX_VALUE)` [CODE] `src/core/tickspeed.js` L131-135. Infinity upgrade IP costs start at 1,1,1,... then 2,3,5,7 [CODE] `src/core/secret-formula/infinity/infinity-upgrades.js`. Dimension infinity-count upgrade: `Currency.infinitiesTotal.value.times(0.2).plus(1)` (+20% per infinity) [CODE] same file L4.

**Design takeaways**: per-tier ratios 1e3..1e15 (10x between tiers) with x2 per 10 bought is the verified "readable breakpoint" engine; time dimensions use small ratios 3/9/27/81 early.

### Round 2: IP / EP / Reality gains [CODE]
Files: `src/game.js` (https://raw.githubusercontent.com/IvarK/AntimatterDimensionsSourceCode/master/src/game.js) L89-160, `src/core/machines.js` (https://raw.githubusercontent.com/IvarK/AntimatterDimensionsSourceCode/master/src/core/machines.js). (Earlier `src/core/*.js` guesses were 404; definition is in `src/game.js`.)

**Infinity Points** [CODE] `src/game.js` L89-118
```js
const div = Effects.min(308, Achievement(103), TimeStudy(111));   // 308 -> lower with those
let ip = player.break ? Decimal.pow10(player.records.thisInfinity.maxAM.log10() / div - 0.75) : new Decimal(308 / div);
ip = ip.times(GameCache.totalIPMult.value);  // Teresa run ^0.55, V run ^0.5
return ip.floor();
```
So un-broken infinity always gives 1 IP (308/308); broken: IP = 10^(log10(maxAM)/308 - 0.75) x mults, i.e. one more power of 10 per +308 orders of antimatter (maxAM 1e308 -> 10^0.25 = 1.78).

**Eternity Points** [CODE] `src/game.js` L138-157
```js
let ep = DC.D5.pow(player.records.thisEternity.maxIP.plus(gainedInfinityPoints()).log10() / (308 - PelleRifts.recursion.effectValue.toNumber()) - 0.7).times(totalEPMult());
```
EP = 5^(log10(IP)/308 - 0.7) x mults: x5 EP per +308 orders of IP. Inverse: `requiredIPForEP(ep) = 10^(308*(log5(ep/mult)+0.7))`, min 1.79e308 (L160).

**Reality Machines** [CODE] `src/core/machines.js` L1-32
```js
baseRMCap = 1e1000;  // hardcap
let log10FinalEP = player.records.thisReality.maxEP.plus(gainedEternityPoints()).log10();
// before first Reality: cap 8000, and above 6000 only 25% counts
let rmGain = 1000 ^ (log10FinalEP / 4000 - 1);   // = 10^(3*(logEP/4000 - 1))
if (rmGain >= 1 && rmGain < 10) rmGain = 27/4000 * log10FinalEP - 26;
rmGain = floor(rmGain * realityMachineMultiplier);
```
So Reality needs ~1e4000 EP for 1 RM (the 1e4000 claim from notes is therefore correct for the *RM gain* anchor; unlock gate itself not read). Each +4000 orders of EP = x1000 RM.

**Offline** [CODE] `src/game.js` L935: Infinity upgrade `ipOffline` adds `bestIPMsWithoutMaxAll * seconds*1000 / 2` IP offline (i.e. 50% of best IP/ms rate). Default option `offlineTicks: 1e5` (`src/core/player.js` L798).
