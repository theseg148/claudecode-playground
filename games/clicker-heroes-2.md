# Clicker Heroes 2
**Sources:** (URLs, required)
- https://blog.clickerheroes.com/ancient-souls-per-transcension-how-to-maximize-your-gain/ (original Clicker Heroes 1 transcension/Ancient Souls math; CH2 differs)
- https://blog.clickerheroes.com/best-time-to-transcend-when-to-hit-zone-300-and-beyond/ (CH1 timing)
- https://clickerheroes.fandom.com/wiki/Clicker_Heroes (CH1 wiki; CH2 has its own wiki not reachable in this session)
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii (general prestige math)
- Research note: WebSearch returned only CH1 data; fandom CH2 pages failed DNS in this environment. Most CH2 specifics below are [EST]/recalled and flagged. Legend: [PUB] published, [EST] estimate/recollection.
## Core loop
- Click/auto-attack monsters in a zone, earn gold, buy hero levels and skills, push further zones.
- CH2 replaced CH1's single endless zone ladder with Worlds: each world is a self-contained biome with own zone count, monsters and bosses [EST].
- You push to a world's limit, then "Transcend" (prestige) to reset the world with permanent gains, and eventually unlock the next world [EST].
- Skill tree (Hero Soul-based nodes in the new design) lets you choose upgrades each run; Ancient-like temporary buffs [EST].
- Auto-progress and idle mode make the active play optional, but player decisions are around node and ancient choices.
## Resource types
- Gold (per run), Hero Souls (CH1 prestige currency; CH2 uses per-world "Primal"/Hero Souls) [EST].
- Ancient Souls (CH1 transcension currency) [PUB].
- Rubies / Gems (premium) [PUB for CH1].
- Skill-tree points / Nodes (CH2) [EST].
- Relics and Outsider bonuses persist after transcension in CH1 [PUB].
- World-specific currencies in CH2 so prestige in World N doesn't dilute World N-1 [EST].
## Cost & production growth formulas (public or estimated; mark which)
- CH1 Ancient Souls on transcension ~ conversion of Hero Souls; blog gives ~1 AS at 1e12 HS, ~4 at 1e15 [PUB, CH1 blog] (another blog's `5*log10(HS)` conflicts; do not trust).
- CH1 hero cost: exponential, around x1.07 per level for base hero cost [EST from memory; the standard CH1 hero cost growth is 1.07^level].
- CH1 monster HP: grows exponentially per zone, ~x1.55^zone up to zone 140, then slower [EST/recalled].
- CH1 transcension unlock after zone ~300; "three to four strong ascensions then transcend" [PUB, blog].
- CH2: costs per upgrade use geometric progression; node costs rise per purchase ("x1.2-1.5 per level") [EST].
- Prestige reward typically proportional to (highest zone)^k or log of total gold; use sqrt/log forms [EST design pattern, see gamedeveloper article].
- Multipliers stack multiplicatively across hero count milestones (every 25 levels x4 in CH1) [EST recalled].
## Prestige structure
- Ascension (CH1): resets heroes + gold, gives Hero Souls from boss kills above a threshold zone.
- Transcension (CH1): deeper reset: wipes heroes, ancients, hero souls; keeps rubies, achievements, relics, Outsider bonuses [PUB].
- CH2 layers: run reset (Transcend) -> world reset -> Great Ancients/Outsiders layer [EST].
- Prestige points are per-world so each world has its own power curve and its own "first clear" feeling.
- Player is told when prestige is worth it (breakpoint display) [EST].
## Unlock pacing
- First minutes: heroes cost small amounts; each hero reveals a new skill.
- First transcend roughly after 30-90 minutes [EST].
- Next world unlock requires clearing a threshold zone in current world and some points spent [EST].
- New worlds bring new monsters, new boss mechanics and new skill-tree nodes so the same upgrade loop uses different building blocks.
- Mid-game: dozens of tree nodes; end-game: a deep tree with "synergy" nodes only meaningful in specific worlds [EST].
## Offline progress
- CH1: Offline gold at a fraction of active rate; Ancients / "Dark ritual" enhance [PUB-ish].
- CH2: auto-progress continues; offline reward capped, with "Idle" upgrades [EST].
- Effective design: idle path is the baseline, active clicks add multiplier.
## Monetization effects
- CH1: Rubies buy skills, auto-clickers, time-warp style items [PUB].
- CH2 (Steam/mobile) is mostly premium-style with cosmetics [EST].
- Heavy tuning for ruby purchases in CH1 pushed players to spend; CH2 reduced it [EST].
## What players love
- Satisfying "number go up" feedback; boss kills with big rewards.
- Visible per-world identity in CH2 (different monsters and layout).
- Meaningful tree choices.
## What players hate
- CH1: huge mathematical complexity, spreadsheets needed for optimal ancient allocation [PUB, Steam threads].
- CH2: development delays, rework of the prestige system, bugs [EST].
- Deep prestige layers confusing (Hero Souls vs Ancient Souls vs Outsiders).
## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Make each Rider world have its own local prestige currency, so earlier worlds stay relevant but not dominant.
- Gate the next world on a clear threshold in the current one (e.g., "reach Form Rank 10 in Kuuga's world").
- Show a plain "prestige now gives X" breakpoint to avoid CH1's spreadsheet problem.
- Keep layers to 2-3 maximum; CH1/CH2's 4+ layers confuse.
- Swap the "monster HP wall" for a "task difficulty wall" (assembly times, research hours) for no-fight design.
- Give each world a unique node set so the upgrade tree is different, not just bigger.
- Use sublinear (log/sqrt) prestige payouts to prevent runaway.
