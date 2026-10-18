# Idle Breakout
**Sources:** (URLs, required)
- https://idle-breakout.fandom.com/wiki/Idle_Breakout_Wiki (6 ball types, bricks harder as you progress, Prestige page; snippet only)
- https://kodiqi.itch.io/idle-breakout (game page, by Kodiqi)
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii
- Legend: [PUB] seen in sources; [EST] my recollection or estimate. No exact formulas retrievable.
## Core loop
- Balls bounce and break bricks; each brick has HP (number); breaking gives money.
- Buy balls (types), upgrade ball power/speed/count, and break whole levels; when the board is cleared the next level has bricks with more HP [PUB].
- 6 different ball types buyable in the store [PUB]: basic, sniper, scatter, laser, sand, etc. [EST].
- Level count is the world axis: each level is one board; progress is a sequence of levels.
## Resource types
- Money (per run), Prestige tokens (Prestige currency), Prestige upgrades, Ball level, Ball count.
- Level number as score.
- No premium currency (browser game) [EST].
## Cost & production growth formulas (public or estimated; mark which)
- Ball cost: geometric ~x1.1-1.15 per purchase [EST].
- Brick HP: grows with level, roughly exponential `hp = base * 1.1^level` in early levels, with periodic jumps [EST].
- Ball upgrades: power doubles every few levels at rising cost [EST].
- Prestige tokens ~ function of highest level reached (e.g. `tokens ~ level^k` or exponential in level) [EST].
- Reward per brick = proportion of HP [EST].
- Breakout shape means production is bounded by geometry (ball speed) as well as stats.
## Prestige structure
- Prestige after a certain level (wiki Prestige page) [PUB nav]: reset balls and money for tokens that give permanent multipliers.
- Tokens buy upgrades for ball types and start-level.
- Single-layer prestige in original; later versions/sequels (Idle Breakout 2?) add [EST].
- Prestige gets you further levels faster, each time.
## Unlock pacing
- Early: buy balls every few seconds; levels clear in ~1 min.
- New ball types unlock by level or prestige [EST].
- Bricks get harder as you progress [PUB]; first prestige in ~30 minutes [EST].
- Visual changes (brick colours) per tiers.
## Offline progress
- Original browser game: offline progress is limited (some earnings at a reduced rate) [EST]; tab must stay open for best play.
- Auto-play: balls play themselves.
## Monetization effects
- Free browser game; ads on host site; no IAP [EST].
## What players love
- Simple visual clarity; the breakout satisfaction; auto-play.
- Short learning time.
## What players hate
- Prestige slowdown, repetitive; limited depth [EST].
- Browser tab throttling [EST].
## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- A visible, watchable "engine" (balls bouncing) makes idle fun; for Decade use a visible assembly line or card shuffle animation.
- Each level = a board; the numbers on bricks are a built-in progress bar. Use a "target number" per stage.
- Ball types = tools; unlocking new types per world changes the rhythm.
- Keep prestige single-layer early; add depth later.
- Simplicity wins: 5-6 purchasable item types is enough.
