# Factory Idle
**Sources:** (URLs, required)
VERIFICATION UPDATE 2026-10-18: Factory Idle is a game by Hein Stain (itch.io, same author as Reactor Idle), with conveyor belts, money + research, and a 'hard for an idle game' framing [S]. No Steam page, prestige, or numbers could be confirmed; 'Steam one-time purchase' is UNVERIFIED. See Verification log.
CONFIDENCE WARNING (LOW): sandbox could only fetch raw.githubusercontent.com. I could not fetch the Steam page or wiki for Factory Idle. Everything is [MEM-LOW] or [EST].
- https://hein-stain.itch.io/factory-idle (developer page, Hein Stain; via search snippets) [S]
- https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/FactoryIdle (summary; via snippet) [S]
- https://hein-stain.itch.io/factory-idle/devlog (devlog; snippets) [S]
- https://www.wurb.com/stack/archives/date/2016/05 (2016 blog post on the game; snippet) [S]
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii (genre math; not fetched)

## Core loop
- Build production chains in a factory-floor layout: raw resources -> processed goods -> sold or exported for money. Think Factorio/Shapez simplified with idle automation.
- You place or upgrade machines, connect them via conveyors, and increase throughput; bottlenecks are the puzzle.
- Money funds more machines and new product lines; research unlocks higher-tier goods.
- A prestige-like reset ("Rebuild"/"Relocate factory") grants meta currency for permanent boosts. [MEM-LOW]

## Resource types
- Money, raw materials (ore, wood, oil... ), intermediate goods (plates, gears, circuits), final goods, Research points, Prestige currency, Workers/energy. [MEM-LOW]
- Per-machine throughput (items/s) is the key stat. [EST]

## Cost & production growth formulas (public or estimated; mark which)
- Not verified. Typical for factory idles: [EST]
  - Machine cost = base * 1.15^owned (or x2 per new tier of machine).
  - Throughput per machine upgrade +25-100% at milestone levels.
  - Product value roughly equals the sum of input values * 1.5-3 (value-add multiplier), so deeper chains pay more. [EST]
  - Conveyor/capacity upgrades cost x2-x3 per level. [EST]
- Prestige points roughly sqrt of total lifetime money with +X% per point. [EST]
- Supply-and-demand price drift for sold goods may exist. [MEM-LOW]

## Prestige structure
- One main reset with permanent boosts; later additional layer (research reset) is possible. [EST]
- Reset keeps blueprints/unlocked recipes while losing machines. [EST]
- Meta-currency used for automation of previously manual tasks. [EST]

## Unlock pacing
- [EST] 0-10 min: first miner/smelter chain; 1 h: second product line and research; 3-6 h: first reset; days: full tech tree.
- Each tier of product appears only when the previous tier is stable, a "bottleneck tutorial" pace.

## Offline progress
- [MEM-LOW] Likely simulates income at current throughput with a cap (8-24 h typical for Steam idles); precise rules unknown. [EST]
- Factory layouts mean offline income = throughput of the bottleneck machine, simpler than a full simulation. [EST]

## Monetization effects
- Steam one-time purchase, no microtransactions (typical for factory idles). [MEM-LOW]
- Possible cosmetic DLC. [EST]

## What players love
- Optimising the chain; seeing items flow on belts.
- Idle-friendly automation while still engaging the Factorio instinct.
- No predatory monetization.

## What players hate
- Bottleneck hunting gets repetitive. [EST]
- Late-game UI clutter and long reset cycles. [EST]
- Balance patches that change recipes. [EST]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Production chains give strategic depth without combat: Rider Cards could be crafted from world materials (raw -> processed -> card). Keep chains to 3 steps maximum.
2. Offline = throughput of the bottleneck is a simple, honest rule to calculate; keep the game graph shallow for that reason.
3. Value-add multiplier of ~1.5-3x per processing step makes deeper chains worthwhile [EST].
4. Each world introduces one new raw material and one recipe, avoiding UI clutter.
5. Prestige keeps recipes (knowledge) but resets machines: matches the fantasy "Decade remembers every world he's passed through."
6. Highlight the current bottleneck in the UI (red arrow) to cut the tedious hunt.
7. One-time purchase and no pressure monetization suits this audience; consider the same for a premium release.
8. Low confidence; verify before relying on numbers.

## Verification log (2026-10-18)
Method: WebSearch snippets only.
Confirmed [S]:
- TV Tropes: an idle game about running a fully automated factory; you set up machines to buy resources, process them and sell them, linked by conveyor belts; the intro itself says it is hard for an idle game; one mistake can drag output down and jam the system; buying upgrades forces you to reshuffle because machines' requirements and outputs change. https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/FactoryIdle
- Developer Hein Stain on itch.io; description centred on conveyor belts, machines and automation to generate income; alpha announced in a 2023 devlog; update 0.4.17 live; later Assembler added with several new recipes. https://hein-stain.itch.io/factory-idle , https://hein-stain.itch.io/factory-idle/devlog
- A 2016 blog post says Factory Idle has conveyor belts and two goals, money and research, and is by the same artist as Reactor Idle (UI/structure shared, but Reactor Idle has no belts). https://www.wurb.com/stack/archives/date/2016/05 . Factory Idle Missions is a spin-off belt puzzle sorting coloured boxes.
- Items are variously sized components placed on a grid (wurb.com snippet).
Contradicted/unverified: the Fandom wiki, subreddit and Steam store listing could not be found; I did not find a 'Rebuild/Relocate' prestige, 'workers/energy' resource, or any cost formula, so they stay [MEM-LOW]/[EST]; the offline-cap and one-time-price claims are unverified. Do not confuse with 'Factory Works Idle' (EnricoBC, Steam Dec 2025), 'From Zero: Idle Factory' or 'Factory: Idle & Tycoon Game'. If the Steam title in question is one of those, this file does not describe it.
