# Cookie Clicker
**Sources:** (WebFetch was blocked by DNS in this session; only the search snippet from the Cookie Clicker wiki was seen directly. Numbers below not marked [snippet] come from recall of the wiki and game source, and should be re-checked.)
- https://cookieclicker.fandom.com/wiki/Building (price formula, rounded up, free buildings F) [snippet-confirmed]
- https://cookieclicker.wiki.gg/wiki/Building
- https://cookieclicker.wiki.gg/wiki/Heavenly_Chips
- https://cookieclicker.fandom.com/wiki/Ascension
- https://orteil.dashnet.org/cookieclicker/ (the game; main.js is the ground truth for all formulas)
- https://dinogame.gg/blog/how-cookie-clicker-progression-works/ (low-quality secondary; treat as opinion)

## Core loop
- Click the big cookie, spend cookies on buildings and upgrades, and cookies per second (CPS) rises.
- Early game is click-heavy, and about 10 to 20 minutes in, buildings take over.
- Golden cookies appear every few minutes (roughly 5 to 15 min). They give Frenzy (x7 CPS for 77s), Lucky, Click Frenzy and similar. Reading the timers is the active skill layer.
- Once an ascension is done, the loop becomes "ascend, buy heavenly upgrades, rebuild faster".
- Late game adds mini-games (Garden, Stock Market, Grimoire, Pantheon), so there is a second layer of decisions inside the idle loop.

## Resource types
- Cookies: the main currency.
- CPS: derived from buildings, upgrades, kittens, milk and so on.
- Heavenly chips and prestige level: the meta currency.
- Sugar lumps: one ripens about every 24h and is spent on building levels and mini-games.
- Milk (from achievements) and kitten upgrades, which scale CPS.
- Golden cookie effects, wrinklers (cookies "fed" to them are refunded 1.1x on popping), and season tokens.

## Cost & production growth formulas
- Building price (public, wiki): `price = ceil(base * 1.15^(owned - free))`. The wiki notes this is roughly a doubling every 5 buildings, since 1.15^5 is about 2.01. [public]
- Base prices (public, from recall): Cursor 15, Grandma 100, Farm 1,100, Mine 12,000, Factory 130,000, Bank 1.4M, Temple 20M, Wizard Tower 330M, Shipment 5.1B, Alchemy Lab 75B, Portal 1T, Time Machine 14T, Antimatter Condenser 170T, Prism 2.1Q, Chancemaker 26Q.
- Base CPS per building (public, recall): 0.1, 1, 8, 47, 260, 1,400, 7,800, 44,000, 260,000, 1.6M, 10M, 65M, 430M, 2.9B, 21B.
- The tier pattern: base price grows about 10 to 15x per tier and CPS about 5 to 7x per tier. This keeps the "next tier is better" decision always live.
- Selling refunds 25% of the price at the current count (a tuning choice that discourages reshuffling).
- Upgrade multipliers: tier upgrades double a building's output. They unlock at 1, 5, 25, 50, 100... owned (approx.) and cost roughly 10x the building's base price per step.
- Click value scales with CPS via later upgrades (a percentage of CPS per click), so clicking never fully dies.
- Prestige (public): lifetime cookies baked `C` give prestige level `L = floor(cbrt(C / 1e12))`. Inversely, level `L` needs `1e12 * L^3` cookies. [public, confirmed in the guides by snippet]
- Each prestige level gives +1% CPS (a secondary guide claims 5%; that contradicts the wiki and I believe it is wrong). Heavenly chips equal the levels and are spent on upgrades. [public]
- Because it is a cube root, doubling the chips needs 8x the cookies. That is a deliberate diminishing-returns curve.

## Prestige structure
- Ascension resets cookies, buildings and normal upgrades. It keeps achievements, heavenly upgrades, sugar lumps and milk.
- The first ascension is possible at 1 trillion cookies for 1 chip, and community guides suggest waiting for hundreds of chips (community guides quote ~200 as a minimum for the first ascension and ~440 to afford a starter set [S: ponderworthy.com guides via search; low-quality sources, still advice not rule]). Prestige = cube root of lifetime cookies in trillions, +1% CpS per level, chips 1:1 with levels [S: https://cookieclicker.wiki.gg/wiki/Prestige].
- The Heavenly upgrade tree is a spatial web: you must buy neighbours to unlock further nodes. This is itself a pacing gate.
- Key permanent perks: start with some cookies, golden cookies appear more, "Persistent memory", the Legacy permanent upgrade slots, offline CPS, and the "Season switcher".
- Players ascend repeatedly; the endgame is optimizing runs, not one giant run.

## Unlock pacing
- Cursor and Grandma appear in the first minute.
- Farm unlocks around 10 to 15 cookies/s; later buildings appear when you have earned roughly 1/3 to 1/2 of their price (they are "revealed" when visible, which sets up aspiration).
- Mid-game (hours 2 to 10): Wizard Tower unlocks the Grimoire mini-game, Farms unlock Garden, Banks unlock the Stock Market.
- Sugar lumps arrive after about 1 day of play; this is the first "real time gate".
- Late buildings (Prism, Chancemaker, Fractal engine, Javascript console, Idleverse, Cortex baker, You) are revealed over weeks of play. [estimate: weeks, depends on ascend cadence]

## Offline progress
- Base game: no offline cookie production. The "Twin Gates of Transcendence" heavenly upgrade grants offline CPS at 5% for up to 1h, costs 1 chip; beyond 1h the rate drops a further 90% (0.5% of CpS) [S: https://cookieclicker.wiki.gg/wiki/Prestige]. Angels adds +10% (15% total), Dominions (after Virtues) brings total to 45% per the wiki snippet; with all upgrades the wiki states 91% for 7 days 8 hours [S, snippet wording; verify the exact tier names].
- Grandmas never stop, but the player must return to click golden cookies. This keeps the game active.

## Monetization effects
- Free in browser and Steam release is paid (one-time), with no IAP, no ad boosts and no premium currency.
- Monetization is nil, so every design choice (golden cookies, wrinklers) exists purely for engagement.

## What players love
- Unbounded numbers with absurd naming, a huge list of achievements and secrets.
- Golden cookie reaction moments and the "combo" optimization (stacking Frenzy plus Click Frenzy plus Building Special).
- Layered systems that open as you play: garden, stock market, grimoire.
- Jokes and flavour text on every upgrade.

## What players hate
- Heavenly chips grow so slowly that a bad ascension feels wasted. Wiki pages and guides disagree on "best time", which shows the system is opaque.
- Click-fatigue early on and the need to be present for golden cookies.
- Wrinklers and Grandmapocalypse are punishing the first time a player meets them.
- No offline by default.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Use the `base * 1.15^n` cost curve as a baseline; tune the exponent per "world" so each Rider world feels different (1.07 to 1.15).
- Make each Rider world a "building tier" with roughly 10x cost and 5 to 7x output per tier.
- Use cube-root-style prestige ("Decade's Dimension Break") with an explicit preview of next-level chips so the player knows when to reset.
- Offer an in-game unlock (e.g. Kamen Ride cards) that grants a modest offline rate instead of forcing it.
- Give a short, active "golden cookie" analogue: a timed Rider Card event that creates a combo moment without fighting.
- Reveal future tiers at about 1/3 of price so that the next Rider world is always a visible goal.


## Verification log
Search date 2026-10-18; WebSearch snippets only (pages not opened).
- Confirmed [S]: building price = base * 1.15^(owned - free), rounded up (wiki.gg Buildings; twinfinite); Classic used 1.1; Classic Cursor base 15 (modern Cursor 15 not directly confirmed).
- Confirmed [S]: prestige = cube root of lifetime cookies in trillions, +1%/level, chips 1:1; Twin Gates 5% for 1h, 0.5% after, 1 chip; Angels/Dominions totals 15%/45% (https://cookieclicker.wiki.gg/wiki/Prestige).
- Ascend-timing numbers (200/440) are community advice, not rules. Late-building reveal timing remains [estimate].

## Source-verified formulas
All [CODE] from the public mirror `ozh/cookieclicker` (branch gh-pages = master), file `main.js` (976 KB): https://raw.githubusercontent.com/ozh/cookieclicker/gh-pages/main.js. Treat as data. Line numbers refer to that file.

**Building price** [CODE] L7972, L8092: `Game.priceIncrease=1.15`; `price = basePrice * 1.15^max(0, amount - free)`.
**Base price / CpS are generated, not hand-tabled** [CODE] L8018-8031 (Game.Object ctor, n = building id >= 1)
```js
baseCps   = ceil(n^(n*0.5+2) * 10)/10   // rounded to 2 sig. digits
basePrice = (n + 9 + (n<5 ? 0 : (n-5)^1.75 * 5)) * 10^n * max(1, n-14)   // rounded to 2 sig. digits
if (id>=16) *=10; if (id>=17) *=10; if (id>=18) *=10; if (id>=19) *=20
```
Cursor: base price 15 (L8979), 0.1 CpS base. Computed from the formula (matches in-game values):
| id | building | base price | base CpS |
|---|---|---|---|
| 1 | Grandma | 100 | 1 |
| 2 | Farm | 1.1e3 | 8 |
| 3 | Mine | 1.2e4 | 47 |
| 4 | Factory | 1.3e5 | 260 |
| 5 | Bank | 1.4e6 | 1.4e3 |
| 6 | Temple | 2e7 | 7.8e3 |
| 7 | Wizard tower | 3.3e8 | 4.4e4 |
| 8 | Shipment | 5.1e9 | 2.6e5 |
| 9 | Alchemy lab | 7.5e10 | 1.6e6 |
| 10 | Portal | 1e12 | 1e7 |
| 11 | Time machine | 1.4e13 | 6.5e7 |
| 12 | Antimatter condenser | 1.7e14 | 4.3e8 |
| 13 | Prism | 2.1e15 | 2.9e9 |
| 14 | Chancemaker | 2.6e16 | 2.1e10 |
| 15 | Fractal engine | 3.1e17 | 1.5e11 |
| 16 | Javascript console | 7.1e19 | 1.1e12 |
| 17 | Idleverse | 1.2e22 | 8.3e12 |
| 18 | Cortex baker | 1.9e24 | 6.4e13 |
| 19 | You | 5.4e26 | 5.1e14 |
(The explicit price args in the source, e.g. Farm 500, Mine 10000, are overridden by the generator for n != 0; the table is my calculation of the generator, so [CODE]-derived, not a literal table.) Each building also gets `(1 + level*0.01)` from sugar-lump levels (L5280).

**Prestige** [CODE] L4185-4192: `HCfactor = 3`; `prestige = (cookiesReset / 1e12)^(1/3)`; inverse `cookies = chips^3 * 1e12`. Heavenly multiplier items: +5% (Heavenly chip secret), +20%, +25%, +25%, +25% (L4211-4218), x1.01 for each of Lucky digit/number/payout, Dragon God aura +5%.
**Golden cookie timing** [CODE] L5934-5990: spawn gap = `ceil(30fps*60*m)` s with base **min 5 min, max 15 min** (m=5 / 15), then multipliers: Lucky day /2, Serendipity /2, Golden goose egg x0.95, Heavenly luck x0.95, Green yeast x0.99, Arcane Aura x0.95, Sugar blessing x0.9; chain cookies m=0.05, Gold hoard m=0.01. Lifetime L5617-5622: base **13 s**, x2 Lucky day, x2 Serendipity, x1.05 Decisive fate, x1.01 each Lucky digit/number/payout; x0.95 per other golden on screen.
**Dragon auras** [CODE] L15158-15180 (22): Breath of Milk kittens +5%; Dragon Cursor click +5%; Elder Battalion grandmas +1% per non-grandma building; Earth Shatterer sell 50% (vs 25%); Master of the Armory upgrades -2%; Fierce Hoarder buildings -2%; Dragon God prestige effect +5%; Arcane Aura golden freq +5%; Ancestral Metamorphosis golden +10%; Unholy Dominion wrath +10%; Epoch Manipulator effect duration +5%; Mind Over Matter drops +25%; **Radiant Appetite all production x2**; Dragon's Fortune +123% CpS per golden on screen; Dragon's Curve lumps +5%; Reality Bending 1/10 of all other auras; Dragon Guts +2 wrinklers, +20% digest and burst.
**Wrinklers** [CODE] L14589: hard limit 14 regardless of boosts.
**Offline (needs Twin Gates or Perfect idling)** [CODE] L3537-3580
```js
maxTime = 3600 s; x2 for each of Belphegor, Mammon, Abaddon, Satan, Asmodeus, Beelzebub, Lucifer (up to 128 h); Chimera +2 days, +5%
percent = 5; +10 each for Angels, Archangels, Virtues, Dominions, Cherubim, Seraphim, God (total 75%); Chimera +5; Fern tea +3; Ichor syrup +7; Fortune #102 +1
amount = (min(t,maxTime) + max(0,t-maxTime)*0.1) * cookiesPs * percent/100
```
Perfect idling: unlimited time at 100%. Without either upgrade there is no offline gain.
