# Clicker Heroes 2
**Sources:** (URLs, required)
- https://blog.clickerheroes.com/ancient-souls-per-transcension-how-to-maximize-your-gain/ (original Clicker Heroes 1 transcension/Ancient Souls math; CH2 differs)
- https://blog.clickerheroes.com/best-time-to-transcend-when-to-hit-zone-300-and-beyond/ (CH1 timing)
- https://clickerheroes.fandom.com/wiki/Clicker_Heroes (CH1 wiki; CH2 has its own wiki not reachable in this session)
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii (general prestige math)
- https://delistedgames.com/clicker-heroes-2/ , https://steambase.io/games/clicker-heroes-2/info , https://www.gamestar.de/videos/clicker-heroes-2,11_138/ , https://www.gamespark.jp/article/2018/07/17/82310.html (CH2 release/delisting facts via snippets) [S]
- Research note: 3 more WebSearch queries found essentially no CH2 mechanics text (only release/delisting). Most CH2 specifics below stay [EST]/recalled and flagged. Legend: [PUB]/[S] snippet, [EST] estimate/recollection.
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
- CH1 Ancient Souls: a search snippet attributes `floor(5 * log10(total Hero Souls sacrificed))` to the CH1 blog, and an older GameSkinny guide says 5 AS per 10x Hero Souls [S]; the earlier line in this file (about 1 AS at 1e12 HS) could not be reconfirmed and conflicts. CH1 only; not a CH2 formula.
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
- CH2 launched in Steam Early Access on 16 July 2018 as a paid (~$25 range) game, unlike the free CH1 [S gamestar/steambase]; delisted from sale 14 March 2024, with the developers saying they could not obtain the SDK for newer builds and the original team is gone; owners can still play [S https://delistedgames.com/clicker-heroes-2/]. Cosmetics claim and mobile version unverified [EST].
- Heavy tuning for ruby purchases in CH1 pushed players to spend; CH2 reduced it [EST].
## What players love
- Satisfying "number go up" feedback; boss kills with big rewards.
- Visible per-world identity in CH2 (different monsters and layout).
- Meaningful tree choices.
## What players hate
- CH1: huge mathematical complexity, spreadsheets needed for optimal ancient allocation [PUB, Steam threads].
- CH2: long Early Access, then delisting with no updates for a long time [S delistedgames]; prestige rework and bugs unverified [EST].
- Deep prestige layers confusing (Hero Souls vs Ancient Souls vs Outsiders).
## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Make each Rider world have its own local prestige currency, so earlier worlds stay relevant but not dominant.
- Gate the next world on a clear threshold in the current one (e.g., "reach Form Rank 10 in Kuuga's world").
- Show a plain "prestige now gives X" breakpoint to avoid CH1's spreadsheet problem.
- Keep layers to 2-3 maximum; CH1/CH2's 4+ layers confuse.
- Swap the "monster HP wall" for a "task difficulty wall" (assembly times, research hours) for no-fight design.
- Give each world a unique node set so the upgrade tree is different, not just bigger.
- Use sublinear (log/sqrt) prestige payouts to prevent runaway.

## Verification log (refreshed 2026-10-18)
- Refreshed 2026-10-18: 3 more WebSearch queries. CH2 mechanics (worlds, skill tree, transcend layers, currencies) are still unsourced and must stay [EST]; confirmed only the release date, premium price class and the 2024 delisting.
- CH1 relic persistence also conflicts across sources (wiped vs kept at transcension). The CH1 Ancient Souls formula is disputed; do not design from it. No code (commercial).
