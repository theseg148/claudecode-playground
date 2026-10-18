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
- The first ascension is possible at 1 trillion cookies for 1 chip, and community guides suggest waiting for hundreds of chips (365 to 440 is quoted by low-quality sources; treat as estimate).
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
- Base game: no offline cookie production. The "Twin Gates of Transcendence" heavenly upgrade grants offline CPS at 5% for up to 1h, rising with further upgrades ("Angels" 10%, "Archangels" 15%, "Virtues"), at most about 25% over a 24h window or so. [estimate from recall of values]
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
