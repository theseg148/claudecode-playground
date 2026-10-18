# NGU Idle
> Verification pass 2026-10-18 (WebSearch snippets only; pages not opened). [S] = confirmed in a search snippet with the URL given; [unverified] = not confirmed, treat as a design placeholder. See "Verification log" at the bottom.
**Sources:** (WebFetch was blocked by DNS in this session; this is recalled from the wiki and community guides and is largely estimate-level for numbers.)
- https://ngu-idle.fandom.com/wiki/NGU_Idle_Wiki
- https://ngu-idle.fandom.com/wiki/Rebirth
- https://ngu-idle.fandom.com/wiki/Adventure
- https://ngu-idle.fandom.com/wiki/NGU
- https://store.steampowered.com/app/1147690/NGU_IDLE/ (verify app id)
- https://www.kongregate.com/games/somethingggg/ngu-idle (Kongregate original)

## Core loop
- Allocate Energy and Magic to Augmentations, Time Machine, NGUs, Wandoos, Blood Magic and others.
- Energy buys Augmentation power, Magic buys Time Machine and Blood Magic, R3 (Resource 3) arrives later.
- Fight in Adventure Mode to gather gear and bosses, with automatic combat; the player picks zones.
- Rebirth to reset, and keep the permanent multipliers (Number-based boosts).
- Use Challenges for permanent boosts and special rules.

## Resource types
- Energy, Magic, Resource 3 (R3), Gold, Exp, Titans' loot and gear, AP (Adventure points), Beards, Wandoos OS, Number, Boosts, Perks (Perks come from AP), Gear, Cooking (late), Hacks, Wish points, Beta.

## Cost & production growth formulas
- Energy/Magic/R3 production scales with Power, Cap and Bars, which are multiplied by many permanent boosts. [public structure; no single formula]
- Training: each Basic Training has an energy cap that shrinks with its levels (up to 10% of previous value per rebirth); Insta Training Cap costs 10,000 AP and Double Basic Training 100 PP [S https://ngu-idle.fandom.com/wiki/Basic_Training]. The '1.1^level or level^2' cost law is [unverified].
- NGU [S https://ngu-idle.fandom.com/wiki/NGU via search summary]: Time Machine NGU base cost 1E14, gold bonus L*0.2% up to a soft cap at 1000 levels, then about L^0.8 * 0.7962%; Evil and Sadistic variants have much larger base costs and slower speed. Respawn NGU approaches a 60% cap in normal mode (player report). A general NGU formula is [unverified].
- Augmentations [S https://ngu-idle.fandom.com/wiki/Augmentations]: level cost = Base cost * n (linear in target level n); upgrades multiply the augmentation bonus by (1 + UpgradeLevel^2), costing Base cost * n^2 gold and Base cost * n energy. Time-scaling per augmentation is 17x in one cached page and 12x in another. The bonus exponent formula is [unverified].
- Boosts: diminishing-return exponents (e.g. 0.3 to 0.5). [unverified]
- Time Machine: speed multiplies production; gold-based speed is capped by Power. [public structure]
- Numeric scale: late-game values reach 1e50 to 1e200. [unverified]

## Prestige structure
- Rebirth: Reset all resources and upgrades except permanent numbers; gains from Number and Wish scoring.
- "Nuke" / "Titan" fights give permanent boosts; each Titan has a version requirement.
- Challenges (Basic, 24h, No Augments, Troll, etc.) grant permanent boosts.
- Daily Spin is a small bonus; Hacks and Wishes extend into late game.
- Numbers and "Evil" difficulty modes extend the arc by changing rules.

## Unlock pacing
- Day 0: Energy, Magic, Augmentations in the first minutes.
- Day 1: Adventure, Time Machine, Blood Magic, first Rebirth around hours 1 to 3. [unverified]
- Day 3+: NGU, Wandoos, Beards, Digger (a fixed number of features each day), R3.
- Week 2 to 8: Hacks, Wishes, Cards, Cooking, Titans 8+. [unverified]
- The game has a heavy unlock ladder; many systems appear one after another.

## Offline progress
- Offline progress is supported (idle resource accumulation while closed), with a cap and an offline-time item; the player can also use "Offline time" calculators. 
- The Steam release has stronger offline support than Kongregate. [unverified; no offline cap or platform comparison found]

## Monetization effects
- Steam: one-time purchase, Kongregate: free with optional packs and "Perks". 
- Premium shop includes cosmetics and 'Beta' boosts. [unverified]
- The game is mostly free of pay-to-win.

## What players love
- Extreme depth: dozens of interlocking systems.
- Frequent updates and a lively Discord.
- The active-vs-idle blend with Adventure.

## What players hate
- Overwhelming UI and system count for new players.
- Slow mid-game and some very long timers.
- Required wiki use; no in-game explanations for some systems.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- NGU shows the cost of too many systems; introduce at most one new system per Rider world.
- Use a Cap / Bar / Power split sparingly; keep a single readable multiplier visible.
- Allocate points between a few upgrade tracks (an "energy allocation" mechanic) to give meaningful choices without combat.
- Add a daily or per-world feature drip so there is always something new.
- Include in-game tooltips with real numbers to avoid the wiki dependency.
- Use challenges as optional rule changes (no-X runs) that reward permanent boosts.

## Verification log

Confirmed [S]:
- Augmentation linear cost and (1+L^2) upgrade multiplier with n^2 gold / n energy costs; Time Machine NGU base 1E14 and 0.2% per level soft cap at 1000; Basic Training cap mechanic, Insta Training Cap 10,000 AP, Double Basic Training 100 PP; Evil entry recommendations of roughly power 1e13 / toughness 6e12 and EM power*cap >= 4e13 (not yet used in the file); base energy speed useful only to 50 (player report).
Unconfirmed [unverified]:
- Training cost law, general NGU formula, boost exponents, day-by-day pacing, offline behavior, numeric scale, premium shop contents.
Note: the Augmentation time-scaling factor differs between cached wiki versions (17x vs 12x).
