# Kittens Game
**Sources:** (WebFetch DNS-blocked; WebSearch had weak hits. [S] = seen in a snippet, [M] = recalled from the game's public JS/wiki, unverified, [E] = estimate.)
- https://kittensgame.com/wiki/ and https://kittensgame.com/web/ (game + source JS; not fetched)
- https://github.com/nuclear-unicorn/kitten-game (source: buildings.js, religion.js, resets; not fetched)
- https://docs.google.com/spreadsheets/d/1GoT2xOk-s2WRc40K-uL9xCoUoMnD6XRbSVUX6PZkcjc/edit (community calculator with per-building price ratios from code: pastures 1.664? and tombs 1.15 per snippet [S - number unusual, verify])
- https://coderpatsy.bitbucket.io/kittens/catnip.html (catnip calculator with karma/paragon/burned-paragon inputs) [S]
- https://lars3.ingebrigtsen.no/?p=13044 (Kitten Game resetting guide) [S]
- https://www.tvtropes.org/pmwiki/pmwiki.php/VideoGame/KittensGame [S]

## Core loop
- Gather catnip -> refine to wood -> build Catnip Fields, Huts, Libraries -> science unlocks workshop crafts -> kittens become jobs (farmer, woodcutter, scholar, priest ...) -> new resources (minerals, iron, coal, titanium, uranium, unobtainium...) -> space/religion/time layers -> reset.
- Seasons/weather change production (winter weak catnip; "Winter Has Come" challenge nullifies paragon bonus on catnip [S]).
- The game is deep: ~8 interlocking subsystems (Bonfire, Science, Workshop, Trade, Religion, Space, Time, Challenges).

## Resource types
- Raw: catnip, wood, minerals, coal, iron, titanium, gold, oil, uranium, unobtainium, antimatter, science, culture, faith, kittens (population), manpower (hunt), furs, ivory, spice, etc.
- Meta: karma (from kittens at reset), paragon (from reset, boosts production), burned paragon, Chronospheres/Time crystals, relics, void, Epiphany (religion), blueprints.

## Cost & production growth formulas
- Standard [M, matches the game's code]: `price(n) = basePrice * priceRatio^n` where n = buildings owned. Typical ratios: Catnip Field 1.12 (base 10 catnip), Hut ~2.5 initial -> ~1.15 later, Library 1.15 (base 25 wood), Barn 1.75, Mine 1.15, Workshop 1.15, Lumber Mill 1.15 [M]. Wiki's sheet lists some other ratios [S].
- Price ratio reductions via Paragon/philosophies ("-0.02 ratio" from the Engineering/Cryochamber-like upgrades [M]).
- Production per tick (5 ticks/s) = `base * count * (1 + sum of bonuses)`; bonuses are mostly additive within one resource then multiplicative across "paragon", "religion", "time" [M].
- Catnip Field base 0.125/tick x seasonal modifier (spring 1.5, summer 1, autumn 1, winter 0.25) [M].
- Karma [M]: reset with N kittens > 35 gives karma via triangular-like sum; guides say resetting at 35+ kittens gives karma [S] (other pages suggest 130 kittens minimum). Exact formula uncertain.
- Paragon [M]: bonus ~ `paragon * 0.01` to production (up to 200ish), then diminishing by `x/(x+...)`-style hyperbola in later patches; one forum suggests aiming for 100+ paragon on a later run [S].

## Prestige structure
- Reset ("Reset Game") gives karma + paragon (from year/cap-based) and conversion of resources into unlocks like Chronosphere. Challenges (Winter Has Come, Ironwill, etc.) are optional reset-with-modifiers that give permanent bonuses.
- Multi-layer: Karma and Paragon (reset) -> Time crystals / Void / Chronospheres (time layer) -> Challenges. Veteran players reset many times, guides say to reset early and often because of storage bonus accumulation [S, opinions].

## Unlock pacing
- Minute 0: refine catnip -> wood. ~5 min: huts, kittens appear every X catnip. ~30 min: workshop and science tree. 1-3 hr: trade, religion (faith). 10-30 hr: space (first reset typically 20-50 hr of play) [E].
- Whole-game a "multi-week" endeavor: Cryptotheology, Chronoforge, Space layers 50-200+ hr [E].

## Offline progress
- Yes: on loading, game computes "catch-up" ticks for the time away (capped); Time Crystals can also be burned for "time acceleration" (temporal flux). Resources cap by storage so offline is bounded [M].

## Monetization effects
- Completely free; web and Steam (Kitten Game Mobile paid port); no IAP in the browser version. Donations only.

## What players love
- Depth and "aha" system revelations; text-based charm; clear strategic tuning of kitten jobs; hundreds of hours of content; community with calculators and wiki.

## What players hate
- Overwhelming complexity and hidden formula knowledge; confusing resets; very long mid-game walls; tooltips/UI clutter; lots of micromanagement of jobs.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Use a single clear formula family `base * ratio^n` with a few ratios (1.12-1.15 for cheap, 1.75 for storage) and display next-cost transparently.
2. Layer resets (Karma/Paragon) but introduce them slowly; do not dump 8 subsystems at once.
3. Seasons = per-world modifiers: each Rider world could apply multipliers to certain resources, like winter catnip penalty.
4. Fixed reset thresholds (35 kittens) are discoverable thresholds: telegraph in UI.
5. Challenge modes that nerf a mechanic for a permanent reward fit Decade's world-specific rule changes.
6. Offline catch-up capped by storage naturally bounds offline gains.


## Verification log
Search date 2026-10-18; WebSearch snippets only (pages not opened).
- Confirmed only weakly [S]: catnip field production varies strongly by season (forum: +50% summer, -75% winter - differs from my [M] values; treat as UNRESOLVED); game balance changes between versions (videogamegeek).
- NOT confirmed (several searches): price ratios (field 1.12, library 1.15, hut 2.5), 0.125/tick, karma/paragon formulas. Remain [M]/[E]. Wiki is on bloodrizer.ru; source code is the authority.


## Source-verified formulas
All excerpts [CODE] from `bloodrizer/kittensgame` (branch `master`). Base: `https://raw.githubusercontent.com/bloodrizer/kittensgame/master/`. (`js/game.js` / `js/kittens.js` returned 404, so the generic paragon-gain-on-reset code and some core production functions were not verified.)

**Building price formula** [CODE] `js/buildings.js` L2589-2607 (`getPricesWithAccessor`) and L2567-2578
```js
var cost = bldPrices[i].val * Math.pow(ratio, bldVal + fakeBought) * priceModifier * resPriceModifier;
// ratio = priceRatio + dynamic reductions (limited diminishing returns): getLimitedDR(ratioDiff, ratio-1)
```
**priceRatio per building** [CODE] `js/buildings.js` (field L358, hut L491, barn L799, library/mine/workshop etc.)
- Ratios seen across the ~50 building defs: field 1.12 (10 catnip), hut 2.5 (5 wood, L484-491), barn 1.75 (L799), mine/workshop and most others 1.15, a few later ones 1.25 / 1.35 / 1.5 / 1.75 (L1289, L2197, L1797, L2040). Modal value is 1.15.
```js
name: "field", prices: [{ name:"catnip", val:10 }], priceRatio: 1.12, effects: { "catnipPerTickBase": 0.125 }
```

**Time scale** [CODE] `js/calendar.js` L217-218: `ticksPerDay: 10, daysPerSeason: 100` (400 days per year, year = 4 seasons).

**Paragon (prestige) bonuses** [CODE] `js/prestige.js` L549-576
```js
getParagonProductionRatio: productionRatioParagon = paragon * 0.010 * paragonRatio;  // limited DR cap 2*paragonRatio
 + burnedParagon * 0.010 * paragonRatio  // cap 1*paragonRatio (4x after dark future)
getParagonStorageRatio: (paragon/1000)*paragonRatio  // "every 100 paragon = +10% storage"
getBurnedParagonRatio: getUnlimitedDR(burnedParagon, 500)
```
Paragon income: +1 paragon per millennium (1000 years) [CODE] `js/calendar.js` L968-972 (`milleniums * paragonRatio`). Paragon upgrade costs range 5 ... 60000 paragon [CODE] `js/prestige.js`.

**Faith / Apocrypha (religion prestige)** [CODE] `js/religion.js` L1549-1557, L1648-1651
```js
getApocryphaBonus: getUnlimitedDR(this.faithRatio, 0.1) * 0.1
_resetFaithInternal: this.faithRatio += this.faith / 1000000 * ttPlus1 * ttPlus1 * bonusRatio;  // ttPlus1 = transcendenceTier+1
getSolarRevolutionRatio: getLimitedDR(getUnlimitedDR(faith,1000)/100, 10 + solarRevolutionLimit)
```
Production bonus for "adore" ("Epiphany") is quadratic in transcendence tier.

**Diminishing-returns helpers** `getLimitedDR(value, limit)` (asymptote) and `getUnlimitedDR(value, stretch)` are used across the game to keep every % bonus capped or sub-linear [CODE call sites above].

**Design takeaways**: single universal price ratio of 1.15 (1.12 first-tier, 2.5/1.75 for gating buildings) plus dynamic ratio reduction effects; prestige scales with how long you waited (calendar years), not with currency.
