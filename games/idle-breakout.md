# Idle Breakout
**Sources:** (URLs, required)
- https://idle-breakout.fandom.com/wiki/Idle_Breakout_Wiki (6 ball types, bricks harder as you progress, Prestige page; snippet only)
- https://kodiqi.itch.io/idle-breakout (game page, by Kodiqi)
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii
- https://raw.githubusercontent.com/SoBloxsy/idle-breakout/main/html5game/Coding_BreakOut1.js [CODE] (third-party GitHub mirror SoBloxsy/idle-breakout of the GameMaker HTML5 export; minified, so only string literals are readable, no formulas; extracted strings saved under /tmp/claude-0/-home-user-claudecode-playground/2e77cd6e-e441-551f-a27e-40f493265545/scratchpad/src5/idle-breakout/)
- https://kodiqi.itch.io/idle-breakout/comments (player comments)
- Legend: [PUB] seen in sources; [EST] my recollection or estimate. No exact formulas retrievable.
## Core loop
- Balls bounce and break bricks; each brick has HP (number); breaking gives money.
- Buy balls (types), upgrade ball power/speed/count, and break whole levels; when the board is cleared the next level has bricks with more HP [PUB].
- 6 different ball types buyable in the store [S wiki]. Code strings name Basic, Sniper, Scatter, Cannon(ball), Plasma and Poison balls, plus a separate Laser line with four lasers including a "VAUS Laser" [CODE https://raw.githubusercontent.com/SoBloxsy/idle-breakout/main/html5game/Coding_BreakOut1.js]. "Sand" balls were NOT found in the code; earlier guess removed.
- Ball behaviours from code strings: Basic = "Standard ball that bounces off walls"; Cannon = "Powerful ball that smashes through bricks"; Scatter = single-hit balls that self-destruct on impact; Sniper = "Bounces off walls toward the nearest brick"; Poison = poisoned bricks take damage over time and infect neighbours [CODE].
- Level count is the world axis: each level is one board; progress is a sequence of levels.
## Resource types
- Money (per run), Ball level, Ball count, Black Bricks (persistent: upgrade text "Retain earned Black Bricks after pretige", achievement "Break 1,000 Black Bricks") [CODE]. A boss fight is started from the skill tab for about 5,000 Black Bricks, cost may rise [S itch.io player comment, unofficial]. Whether a separate prestige-token currency exists is UNCONFIRMED [EST].
- Special bricks seen in code: Black Bricks (tougher, destroyed last), Boss Bricks (laser-immune), Gold Bricks ("Next Gold at Level"), Power Block, one-use power-ups [CODE].
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
- Code has upgrades such as "Basic Balls power multiplies for every Basic Ball you have", "Maximum Number of Balls", "Ball Speed Increase", "Increase speed limit to 60", "Power Ups duration doubled" and per-ball "always damage Black Bricks" / "small chance of damaging all bricks at once" perks [CODE]. Which currency buys which is UNCONFIRMED.
- Single-layer prestige in original; later versions/sequels (Idle Breakout 2?) add [EST].
- Prestige gets you further levels faster, each time.
## Unlock pacing
- Early: buy balls every few seconds; levels clear in ~1 min.
- New ball types unlock by level or prestige [EST].
- Bricks get harder as you progress [PUB]; first prestige in ~30 minutes [EST].
- Visual changes (brick colours) per tiers.
## Offline progress
- Offline earnings exist and can be boosted: code has the upgrade "Offline cash earnings 10X" [CODE]. Base rate and cap UNCONFIRMED [EST]; tab must stay open for best play [EST].
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

## Verification log (refreshed 2026-10-18)
- [CODE] Read (https://raw.githubusercontent.com/SoBloxsy/idle-breakout/main/html5game/Coding_BreakOut1.js) only as string literals; 2.3 MB obfuscated GameMaker output, so growth formulas, prestige payout and costs remain unread [EST]. It is a third-party mirror, not the author's repo; the kodiqi/idlebreakout.com source is not on GitHub (WebSearch + GitHub repo search found only mirrors/cheat tools).
- [S] Wiki main page (snippet) confirms 6 ball types and a Prestige page; its Prestige page content was not retrievable. Black Brick boss cost comes from one itch.io comment (unofficial).
- Removed guess: "sand" ball. Still [EST]: brick HP curve, ball cost ratio, token formula, first-prestige timing, throttling complaint.
