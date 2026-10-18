# The Math of Idle Games (Pecorella) and Companion Formulas

Research notes for incremental/idle game design. Every claim carries a source URL inline.

## 0. Provenance and confidence (read first)

- The primary texts could NOT be opened directly in this research session: the egress proxy refused connections to
  gamedeveloper.com, kongregate.com, gdcvault.com, slideshare.net, sirpinski.com, medium.com, wikipedia.org and fandom wikis
  (only GitHub was reachable). Everything below about the articles comes from search-engine excerpts of those pages, plus
  a GitHub research file that cites them. Where an item is only from an excerpt or a secondary source, it is labelled.
- Items labelled **[DERIVED]** are my own arithmetic on the cited numbers (computed with Python in this session), not quotes.
- Items labelled **[SOURCE CODE]** were read directly from public GitHub source code
  (https://github.com/IvarK/AntimatterDimensionsSourceCode and https://github.com/nuclear-unicorn/kittensgame), which is the most reliable
  evidence in this file.
- The article series (all by Anthony Pecorella, then at Kongregate, originally published on the Kongregate developer blog, Oct 2016):
  - Part I: https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i (mirror https://www.kongregate.com/en/pages/the-math-of-idle-games-part-i, https://www.sirpinski.com/the-math-of-idle-games-part-i/)
  - Part II: https://www.gamedeveloper.com/game-platforms/the-math-of-idle-games-part-ii (mirror https://www.kongregate.com/en/pages/the-math-of-idle-games-part-ii)
  - Part III: https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii (mirror https://www.kongregate.com/en/pages/the-math-of-idle-games-part-iii, https://www.sirpinski.com/the-math-of-idle-games-part-iii/)
  - The author says the charts are generated from spreadsheets; worksheets are on the Internet Archive under CC BY 4.0:
    https://archive.org/details/idlegameworksheets (per search listing; not opened).
  - Companion talk: "Quest for Progress: The Math and Design of Idle Games", GDC Europe 2016:
    https://www.gdcvault.com/play/1023876/Quest-for-Progress-The-Math and slides
    https://media.gdcvault.com/gdceurope2016/presentations/Pecorella_Anthony_Quest%20for%20Progress.pdf
- Recommended follow-up for whoever has unrestricted web access: read the three articles and the slide PDF in full and
  verify every number in sections 1-4 against them.

---

## 1. Part I: the core model (costs vs. production)

### 1.1 The two base formulas
- Core tension: costs are made to grow **exponentially** while production grows **linearly or polynomially**. The costs eventually overtake
  production and the player hits "the wall" (time to afford the next generator becomes prohibitively long).
  Source (excerpt of Part I): https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i and https://www.kongregate.com/en/pages/the-math-of-idle-games-part-i
- Next cost of a generator:
  `cost_next = cost_base * rate_growth ^ owned`
- Total production of a generator type:
  `production_total = (production_base * owned) * multipliers`
  Both confirmed via excerpts of Part I and by the secondary file
  https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md (section 1.1, which also states the 1.07-1.15 range).
- Worked example in the article uses AdVenture Capitalist's Lemonade Stand: `rate_growth = 1.07`, `cost_base = 4` (excerpt notes the
  more precise value is 3.738 because the first stand is effectively free), `production_base = 1.67/sec`.
  At 10 owned: `cost_next = 4 * 1.07^10 = 7.87`, production `= 16.7/sec`.
  Source: https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i (excerpt via search).
- The article itself flags a simplification: modelling income per second (not per cycle timer) over-favours slow, high-end generators.
  Source: https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i

### 1.2 Typical growth coefficient
- Industry rule of thumb: exponential cost curves with a growth factor between **1.07 and 1.15** per owned unit/level.
  Sources: https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md and a vendor blog https://game-ace.com/blog/idle-game-development/
  (the vendor claim is a single-blog assertion, but it matches the shipped-game data in section 5).
- Idle Idol dev team started at 1.1 for both cost and reward growth, quoting an 11%-19% rise per level, and found costs overtook rewards at
  about level 35 in their chart; they stress that small changes to the exponent compound fast.
  Source: https://www.gamedeveloper.com/design/balancing-tips-how-we-managed-math-on-idle-idol (excerpt).
- Idle Ronin (via Onirealms) lowers the coefficient as levels rise: +14% per level up to level 300, +12.5% up to 1000, +11.5% beyond, so the late curve flattens.
  Source: https://onirealms.com/guides/how-to-design-an-idle-game/ (excerpt).

### 1.3 What a coefficient means in practice [DERIVED]
| growth r | purchases to double price | purchases to x10 price | price after 25 | price after 100 | cost of next 25 (multiple of current price) |
|---|---|---|---|---|---|
| 1.07 | 10.2 | 34.0 | x5.4 | x868 | 63x |
| 1.10 | 7.3 | 24.2 | x10.8 | x13,781 | 98x |
| 1.12 | 6.1 | 20.3 | x17.0 | x83,522 | 133x |
| 1.15 | 5.0 | 16.5 | x32.9 | x1,174,314 | 213x |
| 1.25 | 3.1 | 10.3 | x265 | x4.9e9 | 1,055x |
- Cookie Clicker's wiki independently notes "price roughly doubles every 5 buildings" at 1.15 (matches 4.96 above).
  Source: https://cookieclicker.wiki.gg/wiki/Buildings (via search excerpt).
- Design reading: 1.07 = very long, forgiving ladders (hundreds of purchases per generator); 1.15 = wall within ~50-100 purchases;
  >1.25 is used for storage/housing-type buildings (see Kittens Game, section 5.4).

### 1.4 Bulk purchase and max-affordable formulas
- Cost of buying `k` units when `n` owned (geometric series):
  `cost_k = cost_base * r^n * (r^k - 1) / (r - 1)`
  Cookie Clicker form for cumulative cost of n buildings from zero: `base * (1.15^n - 1) / 0.15`
  (https://cookieclickercalc.com/buildings via search excerpt). Kittens Game source uses the same series in code:
  `resPrice * (Math.pow(priceRatio, num) - 1)/(priceRatio - 1)` [SOURCE CODE] https://github.com/nuclear-unicorn/kittensgame (game.js).
- Max affordable `k` with budget `c`: `k = floor( log( c*(r-1)/(cost_base*r^n) + 1 ) / log(r) )` (inverse of the above; standard algebra [DERIVED]).
- The article warns both closed forms only hold for simple exponential costs with no shifting costs or exponents.
  Source: https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i (excerpt).
- Practical rule: if you add soft-caps or "cost scaling after N", switch to a loop or binary search (Antimatter Dimensions does exactly this for its bulk-buy of dimension boosts:
  "do binary search for appropriate boost amount" in dimboost.js) [SOURCE CODE] https://github.com/IvarK/AntimatterDimensionsSourceCode.

### 1.5 Payback time and "time to next unlock"
- Time to afford the next unit: `t_next = (cost_next - currency) / income_per_sec`. Time to a milestone: `(target - current) / rate`
  (formula stated in https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md section 3).
- Payback time of one unit (seconds to earn back its price) for the Lemonade Stand example [DERIVED]: `cost_next / production_base`
  = 2.4 s for the first, 4.7 s at 10 owned, 13 s at 25, 70.6 s at 50, 2,078 s (about 35 min) at 100 owned. This is the "wall" made concrete:
  payback grows by r per purchase while production per unit stays flat.
- Design target implied by exponential cost / flat unit yield: payback of a single generator should be well below the session length early,
  and only exceed it when you deliberately want a wall that motivates prestige.

---

## 2. Part II: alternative growth models (generators that produce generators)

- Part II explores a model outside the Cookie Clicker pattern: each generator tier produces the tier below, so tier k is a derivative/integral of tier k+1.
  Source: https://www.gamedeveloper.com/game-platforms/the-math-of-idle-games-part-ii and GDC slides
  https://media.gdcvault.com/gdceurope2016/presentations/Pecorella_Anthony_Quest%20for%20Progress.pdf (slide: "What if generators produced generators?").
- The resulting production curves are the series of integrals: `1, x, x^2/2, x^3/6, x^4/24, ... x^n/n!`. With n tiers the currency grows as x^n/n! (polynomial
  of degree n); as the number of tiers grows the sum approaches `e^x`, i.e. exponential.
  Source: https://www.kongregate.com/en/pages/the-math-of-idle-games-part-ii (excerpt).
- The article's example, Derivative Clicker, still keeps costs exponential (e.g. High Schoolers cost `5 * 1.1^n`), so growth is sub-exponential while cost is exponential,
  which the author considers a good balance.
  Source: https://www.kongregate.com/en/pages/the-math-of-idle-games-part-ii (excerpt).
- GDC slide point: `x^k` (polynomial) is never exponential and is always eventually outpaced by `k^x`. Source: Quest for Progress PDF above.
- Derivative Clicker detail from the secondary summary: each tier-1 building adds 0.05% to tier-1 production.
  Source: https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md section 1.1.
- Antimatter Dimensions follows this model: 8 dimensions, each produces the one below, the first produces antimatter.
  Its author says he liked the polynomial growth of Derivative Clicker and borrowed it.
  Source: https://www.incrementaldb.com/community/interview/31 (via search excerpt).
- Use as design rule: with N chained tiers, the number of purchases per tier needed to keep pace falls quickly; choose N between 4 and 8
  to get strongly polynomial but non-exploding growth (AD uses 8; Part II example uses 4) [DERIVED from sources above].

---

## 3. Part III: prestige math

### 3.1 The four prestige-currency formulas compared
All from Part III (https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii, mirrors https://www.kongregate.com/en/pages/the-math-of-idle-games-part-iii and
https://www.sirpinski.com/the-math-of-idle-games-part-iii/), as excerpted by search:

| Game | Variable measured | Formula | Earnings multiple needed to double prestige currency |
|---|---|---|---|
| Realm Grinder | max currency `c_M` | `p = (sqrt(1 + 8*c_M/10^12) - 1) / 2` | 4x the previous run |
| AdVenture Capitalist | lifetime earnings `c_L` | `p = 150 * sqrt(c_L / 10^15)` | roughly 4x (article says "likely somewhere in the 3x-4x range") |
| Cookie Clicker | lifetime earnings `c_L` | `p = cbrt(c_L / 10^12)` | roughly 8x |
| Egg, Inc. | since-reset earnings `c_R` | `delta_p = (c_R / 10^6)^0.14` | 128x per the article (2^7) |

- [DERIVED] Doubling with exponent e requires `2^(1/e)`: sqrt 4x, cbrt 8x, and for exponent 0.14 it is 141x (the article's 128x corresponds to exponent 1/7 = 0.143, so
  the formula as excerpted is rounded; use 1/7 if you want to reproduce the article's number).
- Taxonomy used in the article: "lifetime stats" (AdCap, Cookie Clicker, max-currency in Realm Grinder) versus "since reset" (Egg, Inc.). Lifetime-based formulas
  give the same total if you reset at the same point repeatedly (you only gain the delta); Realm Grinder's max-currency version means resetting at the same peak earns nothing new.
  Source: Part III excerpts above.
- The article observes that most prestige formulas are fractional exponents (sqrt, cbrt), not logs, so prestige currency still grows large; later versions of
  Realm Grinder (Reincarnation) and AdCap (Mega Bucks) added further layers that "substantially rein in numbers".
  Source: Part III excerpts above.
- GDC slide rule: prestige currency "typically grows at a slower order of magnitude" than primary currency; prestiges can be nested.
  Source: https://media.gdcvault.com/gdceurope2016/presentations/Pecorella_Anthony_Quest%20for%20Progress.pdf (excerpt).

### 3.2 When to reset: timing heuristics
- Pecorella's slide rule of thumb (as excerpted): players typically reset when they would gain roughly **+50% to +200%** of their current prestige currency.
  Source: Quest for Progress PDF above (excerpt; flagged as secondhand).
- The GitHub synthesis says "prestige when you can at least double your prestige currency" and for AdCap "reset when pending Angels >= current Angels".
  Source: https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md sections 1.2 and 2.5.
- Community rule: prestige when progress slows to about 10-20% of peak speed / when the next milestone takes longer than restarting and re-reaching the same point.
  Source: https://gridinc.co.za/blog/idle-games-best-practices (via search excerpt; not authoritative).
- A well-tuned prestige should give about a 2x-4x speedup on the second run.
  Source: search excerpt of a design guide (the one quoted in the Machinations-style query result), see https://onirealms.com/guides/prestige-rebirth-ascension-explained/ for the related rebirth write-up.
- Design check: reset cadence is set by the exponent. With a sqrt formula, hitting "pending = current" requires 4x lifetime earnings per doubling, so the Nth reset needs ~4^N times the first run
  unless production multipliers from earlier resets compensate [DERIVED]. This is why each prestige currency unit must buy a multiplier (e.g. +2% per angel) large enough that
  4x earnings arrives in a *shorter* time than the previous cycle.
- Onirealms advice: look for reward cliffs (e.g. Idle Ronin's formula grows faster after stage 200); reaching the cliff just before a reset can double the payout.
  Source: https://onirealms.com/guides/how-to-design-an-idle-game/ (excerpt).

### 3.3 What a prestige point is worth
- AdVenture Capitalist: each Angel gives +2% to all profits, additive; 50 angels = +100% = x2. Angels formula `150 * sqrt(lifetime earnings in quadrillions)` minus angels already spent.
  Sources: https://adventure-capitalist.fandom.com/wiki/Angel_Investors (via search excerpt), https://steamcommunity.com/sharedfiles/filedetails/?id=420273770, and the help center
  https://screenzilla.helpshift.com/hc/en/5-adventure-capitalist/faq/3-how-do-i-get-angels/
- [DERIVED] Angels at lifetime earnings: 150 at 1e15; ~4,743 at 1e18; 150,000 at 1e21. Bonus = 1 + 0.02*angels, so ~x95 at 1e18 and ~x3,000 at 1e21.
- Spending guidance for angel upgrades (community): no more than 20% of angels for x2, 30% for x3, 40% for x4, 50% for x5-x9, 60% for x10+; game warns past 1% for non-"all profit" upgrades.
  Sources: https://adventure-capitalist.fandom.com/wiki/Angel_Upgrades (search excerpt) and the GitHub synthesis above.
- Cookie Clicker: chips = floor(cbrt(forfeited cookies / 1e12)); total cookies for M chips = 1e12 * M^3; cost of the next chip = 1e12*(3K^2 + 3K + 1); each prestige level is +1% CpS.
  Sources: https://cookieclicker.fandom.com/wiki/Heavenly_Chips and https://en.wikipedia.org/wiki/Cookie_Clicker (via search excerpts; some guides give conflicting formulas, the wiki one is the most precise).
  [DERIVED] Reaching 100 chips needs 1e18 cookies, giving only +100% CpS: prestige in Cookie Clicker is a slow, high-effort multiplier compared with AdCap's 2%/angel on a sqrt curve.
- Clicker Heroes: Hero Souls +10% DPS each (Cid click damage also affected); Ancient Souls = floor(5*log10(total hero souls)) on transcendence (single-source claim).
  Sources: https://clickerheroes.fandom.com/wiki/Hero_Souls and https://blog.clickerheroes.com/clicker-heroes-ancient-souls-master-the-ultimate-currency/
- Egg, Inc.: base +10% earnings bonus per Soul Egg, Soul Food research adds +1 percentage point per level; community approximation of gain: farm value^0.21 (unofficial).
  Sources: https://egg-inc.fandom.com/wiki/Earnings_Bonus/Soul_Eggs, https://jzr.uz/blog/egg-inc-mystical-eggs-math, https://en.wikipedia.org/wiki/Egg,_Inc. (search excerpts).
  Official FAQ: the prestige counter "becomes continuously more difficult as each soul egg becomes more and more expensive to earn": https://auxbrain.freshdesk.com/support/solutions/folders/47000774544

### 3.4 Antimatter Dimensions prestige formulas [SOURCE CODE]
From https://github.com/IvarK/AntimatterDimensionsSourceCode (src/game.js):
- Infinity Points: `IP = 10^( log10(maxAntimatterThisInfinity) / 308 - 0.75 )` (after Break Infinity; before it you get a flat 308/div = 1 IP). The trigger is antimatter reaching
  `Number.MAX_VALUE` (1.79e308).
  So the first break-infinity crunch at 1.79e308 gives 10^(1 - 0.75) = about 1.8 IP, and each additional 308 orders of magnitude multiplies IP by 10.
- Eternity Points: `EP = 5^( log10(maxIP + gainedIP) / 308 - 0.7 ) * EPmult`. Inverse: IP required for EP is `10^(308 * (log5(EP/mult) + 0.7))`, min 1.79e308.
  [DERIVED] Each 5x of EP needs 1e308 more IP: a log-of-log-style curve, deliberately far flatter than sqrt/cbrt, because values are tracked as Decimals up to enormous exponents.
- Take-away: when your numbers are stored as logs (big-number libraries), prestige gain is made linear in `log10(currency)` and pegged to a fixed "layer width" (308 orders of magnitude).
  This gives the clean rule "one layer = ~308 OOM of growth".

---

## 4. Antimatter Dimensions numbers (open-source) [SOURCE CODE]

Source: https://github.com/IvarK/AntimatterDimensionsSourceCode (src/core/dimensions/antimatter-dimension.js, tickspeed.js, dimboost.js, galaxy.js, cache.js).

- Dimension base costs tiers 1-8: `10, 100, 1e4, 1e6, 1e9, 1e13, 1e18, 1e24`.
- Per-tier cost multipliers (applied per bought batch): `1e3, 1e4, 1e5, 1e6, 1e8, 1e10, 1e12, 1e15`.
- Cost formula: `cost = baseCost * baseIncrease ^ floor(bought/10)` (an ExponentialCostScaling with cost-scale 10 per batch; exact function body not read). Items are bought in batches of 10,
  and each full batch multiplies that dimension's output by `buyTenMultiplier = 2` by default (`Decimal.pow(buyTenMultiplier, floor(bought/10))`).
  [DERIVED] Therefore, per batch of 10: price x`baseIncrease` (1e3 for tier 1), output x2. That cost/benefit ratio forces a brand-new purchase tier every few minutes, which is what powers the "unlock next dimension" rhythm.
- Tickspeed upgrade: base cost 1000, cost x10 per purchase; each tickspeed purchase multiplies tick speed by 1/0.8 once galaxies >= 3 (base multiplier 0.8) and by 1/1.1245 with no galaxies
  (1/1.11888888 with one galaxy, 1/1.11267177 with two). Galaxies reduce the per-purchase factor by 0.02 each (before 3 galaxies).
- Dimension Boost requirement: first boosts need 20 of the highest unlocked tier; for the 8th-dimension tier: `20 + (boosts - 5) * 15` of dimension 8.
- Galaxy requirement: `80 + 60 * galaxies` 8th dimensions (Galaxy.baseCost 80, costMult 60); a 1.002^n escalator applies from "remote" galaxies at count 800.
  [DERIVED] Galaxy n costs 80, 140, 200, 260, 320 dim-8s: a linear requirement used to meter a stronger multiplicative reward.
- Infinity wall: 1.79e308 antimatter (Number.MAX_VALUE); this is what makes each run end naturally, so the first "prestige" is mandatory, not optional.
- Community time-to-milestone estimates (not authoritative): first Infinity from a few hours to a couple of days; first Eternity a couple of days to a week;
  first Reality a week to a month; finishing one to three months. Source: https://antimatter-dimensions.fandom.com/wiki/Guide and https://antimatter-dimensions.fandom.com/wiki/BubbaCow%27s_Antimatter_Dimensions_Guide (search excerpt; see design_talks_postmortems.md).
- Author's own explanation of the layer design (borrowed ideas): layered prestige from Realm Grinder, automation from Transport Defender, challenges from Idle Wizard, polynomial growth from Derivative Clicker.
  Source: https://www.incrementaldb.com/community/interview/31 (search excerpt).

---

## 5. Shipped-game coefficient tables

### 5.1 AdVenture Capitalist (Earth), from the research file that cites the AdCap wiki
Source: https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md section 2.2 (secondary; I fetched and read it in full).

| # | Business | Base cost | Cost growth | Base profit | Cycle |
|---|---|---|---|---|---|
| 1 | Lemonade Stand | 4 | 1.07 | 1 | 0.6 s |
| 2 | Newspaper | 60 | 1.15 | 60 | 3 s |
| 3 | Car Wash | 720 | 1.14 | 540 | 6 s |
| 4 | Pizza | 8,640 | 1.13 | 4,320 | 12 s |
| 5 | Donut | 103,680 | 1.12 | 51,840 | 24 s |
| 6 | Shrimp Boat | 1,244,160 | 1.11 | 622,080 | 96 s |
| 7 | Hockey Team | 14,929,920 | 1.10 | 7,464,960 | 384 s |
| 8 | Movie Studio | 179,159,040 | 1.09 | 89,579,520 | 1,536 s |
| 9 | Bank | 2,149,908,480 | 1.08 | 1,074,954,240 | 6,144 s |
| 10 | Oil Company | 25,798,901,760 | 1.07 | 12,899,450,880 | 36,864 s |

- [DERIVED] Base cost ratio between consecutive tiers is exactly 12x from tier 2 on (60, 720, 8,640, ...). Base profit is 0.5 x base cost for tiers 3+ (540/720 = 0.75, 4320/8640 = 0.5; tiers
  vary), cycle times grow 2x-4x per tier (3, 6, 12, 24, then 4x: 96, 384, 1536, 6144, 36864). Cost growth *decreases* by 0.01 per tier from 1.15 down to 1.07: expensive generators
  are bought fewer times but climb less steeply.
- Milestone multipliers: thresholds 25, 50, 100, 200, 300, 400, 500 ... 1,100 owned give x2, x3, x5, x7, x9, x11 style jumps, and "100 of everything" gives a global x3.
  Source: same file section 2.4 and 1.5 (secondary; thresholds not verified against the AdCap wiki).
- Offline: AdCap pays offline income only with managers; Pecorella's article notes a 2-hour offline cap in one context. Treat as unverified (search excerpt: https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii).
- Discount managers cut costs 99.999% in that file (post-launch content).

### 5.2 Cookie Clicker
- Modern price: `ceil( baseCost * 1.15 ^ (owned - free) )`; Classic used 1.1 and rounding.
  Sources: https://cookieclicker.wiki.gg/wiki/Buildings and https://cookieclicker.wiki.gg/wiki/Building_(Cookie_Clicker_Classic) (search excerpts).
- Cursor base cost 15; classic table: Factory 500 base, 20 cookies per 5 s; Mine 2,000 base, 10 CpS (Classic page above).
- 20 building types in the modern game: https://cookieclickercalc.com/buildings (search excerpt).
- Frenzy x7, Click Frenzy x777, stacked in combination can reach x5,439 clicking power per the research file section 1.13 (secondary).

### 5.3 Clicker Heroes
- Hero level cost: `base * 1.07^level` (floored), i.e. 1.07 growth. Hero DPS gets x4 per 25 hero levels from level 200, x10 at levels 1000, 2000, ... up to 8000; heroes after Frostleaf get x5 per 25 levels from 525 to 725.
  Source: https://clickerheroes.fandom.com/wiki/Formulas (search excerpt; flagged community wiki).
- [DERIVED] Combining 1.07 growth with x4 per 25 levels: price rises x5.43 per 25 levels, damage x4: roughly balanced, which is why the player can keep levelling heroes without a hard wall until the 25-level multiplier tiers run out.
- Hero Souls on ascension: wiki formula `floor(pow(((level - 100)/5 + 4)/5, 1.3) * bonus)` where level is the highest zone reached, +10% damage each; 1 soul per 2,000 hero levels bought; first ascension is recommended around zone 100-130 (official blog says 130).
  Sources: https://clickerheroes.fandom.com/wiki/Hero_Souls and https://blog.clickerheroes.com/ascension-in-clicker-heroes-the-ultimate-guide/ (search excerpts).
- Ancients: cost `n^1.5` for some ancients (closed-form total in the wiki); summon cost grows with the number summoned.
  Source: https://clickerheroes.fandom.com/wiki/Formulas.

### 5.4 Kittens Game [SOURCE CODE]
Source: https://github.com/nuclear-unicorn/kittensgame (js/buildings.js, js/space.js, js/prestige.js, game.js).
- 49 `priceRatio` entries at 1.15 and the rest spread across 1.10 (x2), 1.12 (x2), 1.18, 1.25 (x5), 1.35, 1.5, 1.75 (x3), 2 and 2.5 (x9).
- Field: priceRatio 1.12; Mine: 1.15; Barn: 1.75; Hut (housing): 2.5; space buildings: 1.12-1.18.
- Rule from the data: production buildings sit at 1.12-1.15; capacity/housing buildings are punished with 1.75-2.5 so that population and storage do not outrun the economy.
- Paragon: +1% production per paragon (`value * 0.010 * paragonRatio`) with a diminishing-returns limiter (`getLimitedDR(..., 2*paragonRatio)`), and storage +10% per 100 paragon.

---

## 6. Design rules distilled (with the evidence for each)

1. Cost curve: `cost = base * r^owned`, r in 1.07-1.15 (AdCap tiers 1.07-1.15; Clicker Heroes 1.07; Cookie Clicker 1.15; Idle Idol 1.1; Kittens 1.12-1.15 for production). Evidence: sections 1 and 5.
2. Lower r for expensive generators (AdCap drops r by 0.01 per tier); higher r for capacity buildings (Kittens 1.75-2.5).
3. Tier spacing: consecutive generator base cost x12 in AdCap, x1e3-1e15 in AD (AD multiplies costs by far more because it relies on x2 per 10 bought).
4. Milestone multipliers: AdCap 25/50/100/200/300/400... for x2-x11; AD x2 per batch of 10; Clicker Heroes x4 per 25 levels. All three put a power-of-two-ish multiplier at roughly every 10-25 purchases,
   which is the number of purchases required for price to rise ~2x-10x at r=1.07-1.15 [DERIVED]; this keeps production-per-price roughly constant between milestones.
5. Prestige formula: choose exponent first (sqrt = doubling needs 4x earnings, cbrt = 8x); pick bonus per point so that a doubling costs LESS time than the previous cycle.
6. First-prestige trigger: an obvious wall (AD forces it at 1.79e308); otherwise show pending prestige gains and surface the "double it" rule (reset at +50-200%).
7. Prestige currency should be a smaller order of magnitude than the main currency (GDC slide) and should nest into further layers when numbers get unmanageable (Realm Grinder Reincarnation, AdCap Mega Bucks, AD Infinity/Eternity/Reality).
8. For bulk-buy UX use the geometric series; for anything with soft-caps use iterative or binary search.
9. Make progress "bumpy" (surprise events) instead of purely smooth curves: GDC 2016 "Idle Chatter" lesson. Source: https://kongregatedev.ghost.io/idle-chatter-gdc-2016/ (search excerpt).

## 7. Open items for verification
- Confirm AdCap milestone table directly from the AdCap wiki: https://adventure-capitalist.fandom.com/wiki/Angel_Investors and product pages (not fetched).
- Confirm the 50%-200% reset rule's exact wording in the Quest for Progress PDF (excerpt only).
- Confirm the Egg Inc exponent: article says doubling needs 128x (exponent ~1/7) while the formula excerpt shows 0.14.
- Read the Internet Archive worksheets https://archive.org/details/idlegameworksheets to reuse Pecorella's spreadsheet models.
