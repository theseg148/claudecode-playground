# NGU Idle
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
- Training costs: the Basic Training / Adventure upgrades use a multiplier of roughly `base * 1.1^level` or `level^2` depending on type. [estimate]
- NGU: each NGU has an exponent-driven formula `bonus = (1 + level * speed)^..` with Energy NGU, Magic NGU and Evil variants. [estimate; verify in the wiki]
- Augmentations: `Aug Bonus = (Aug Level * Energy Power * Cap * Bar)^exponent`. [public structure from wiki, approximate]
- Boosts: each Boost is multiplied by diminishing-return exponents (e.g. 0.3 to 0.5) so doubling input does not double output. [estimate]
- Time Machine: speed multiplies production; gold-based speed is capped by Power. [public structure]
- Numeric scale: by the late game, values reach 1e50 to 1e200 and use scientific notation. [estimate]

## Prestige structure
- Rebirth: Reset all resources and upgrades except permanent numbers; gains from Number and Wish scoring.
- "Nuke" / "Titan" fights give permanent boosts; each Titan has a version requirement.
- Challenges (Basic, 24h, No Augments, Troll, etc.) grant permanent boosts.
- Daily Spin is a small bonus; Hacks and Wishes extend into late game.
- Numbers and "Evil" difficulty modes extend the arc by changing rules.

## Unlock pacing
- Day 0: Energy, Magic, Augmentations in the first minutes.
- Day 1: Adventure, Time Machine, Blood Magic, first Rebirth around hours 1 to 3. [estimate]
- Day 3+: NGU, Wandoos, Beards, Digger (a fixed number of features each day), R3.
- Week 2 to 8: Hacks, Wishes, Cards, Cooking, and Titans 8+. [estimate]
- The game has a heavy unlock ladder; many systems appear one after another.

## Offline progress
- Offline progress is supported (idle resource accumulation while closed), with a cap and an offline-time item; the player can also use "Offline time" calculators. 
- The Steam release has stronger offline support than the Kongregate original. [estimate]

## Monetization effects
- Steam: one-time purchase, Kongregate: free with optional packs and "Perks". 
- Premium shop includes cosmetics and "Beta" boosts. [estimate]
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
