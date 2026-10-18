# Factory Idle
**Sources:** (URLs, required)
CONFIDENCE WARNING (LOW): sandbox could only fetch raw.githubusercontent.com. I could not fetch the Steam page or wiki for Factory Idle. Everything is [MEM-LOW] or [EST].
- https://store.steampowered.com/search/?term=Factory+Idle (search; not fetched)
- https://factoryidle.fandom.com (guess; unverified)
- https://www.reddit.com/r/FactoryIdle/ (guess; unverified)
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
