# Reactor Incremental
**Sources:** (URLs, required)
CONFIDENCE WARNING (LOW-MED): sandbox could only fetch raw.githubusercontent.com. I could not confirm the repo or wiki for Reactor Incremental. Details are [MEM-LOW] or [EST].
- https://www.kongregate.com/games/ (original host, exact URL unverified)
- https://reactor-incremental.fandom.com (guess; unverified)
- https://www.reddit.com/r/incremental_games/ (community; not fetched)
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii (genre math; surfaced in search; not fetched)

## Core loop
- Place components on a grid inside a nuclear reactor: fuel cells generate power and heat; vents, heat exchangers and coolant cells manage heat; reflectors boost neighbouring cells.
- Sell power for money, buy better components, and rebuild the layout. Layout optimisation (grid design) is the puzzle, similar to Factorio-lite.
- If heat exceeds capacity, the reactor melts down (component loss), so risk management matters.
- Prestige ("Reboot"/"Exotic particles") converts accumulated progress into permanent upgrades. [MEM-LOW]

## Resource types
- Money, Power (energy output), Heat, Exotic Particles / Protium-type prestige resources (names uncertain), Research/Upgrades tokens. [MEM-LOW]
- Component types: Uranium cell (1x, 2x, 4x), Plutonium, Thorium, Seaborgium..., Vent, Heat exchanger, Coolant cell, Reflector, Capacitor, Plating. [MEM-LOW]

## Cost & production growth formulas (public or estimated; mark which)
- Not verified. Typical shape in this game: [EST]
  - Each component tier costs ~x5-x20 the previous; fuel cells' power ~x4-x8 per tier, heat grows in proportion.
  - Upgrades (e.g. "Improved chronometers") cost grows ~x2-x10 per level with +x% or double effects.
  - Cell neighbours: a fuel cell's output is multiplied by (1 + adjacent cells) in the Reactor-style design (the "Nuclear fission" logic). [EST, from the real-world analogue]
- Prestige formula: exotic particles ~ floor(log or sqrt(total power/threshold)). [EST]

## Prestige structure
- Reboot-like: the reactor and money reset; exotic particles are kept and spent on permanent upgrades. [MEM-LOW]
- Possibly a second deeper reset (Protium or Experimental) that resets everything including exotic upgrades. [MEM-LOW]
- A layout design unlocked at later tiers continues the "puzzle" element across resets.

## Unlock pacing
- [EST] 0-10 min: manual click for power, first cell; 30-60 min: first vents and heat management; 2-6 h: first reboot; days: later prestige and big grids.
- Grid expansions unlock gradually (more rows/columns) as upgrades are bought. [MEM-LOW]

## Offline progress
- [MEM-LOW] Browser version runs in a tab; offline progress is limited (probably a simulated cap). Unknown; mark [EST]: capped at a small multiple of tick rate.
- Design assumption: because the grid is a puzzle, progress is measured by layout quality, not offline.

## Monetization effects
- Free browser game, no purchases; later forks/mobile ports may have ads. [MEM-LOW]

## What players love
- Layout puzzle plus risk of meltdown gives interesting decisions.
- Clear feedback: heat/power bars and the satisfying "balanced" reactor.
- Strong theorycrafting (optimal grid designs shared in the community).

## What players hate
- Meltdown can wipe progress, frustrating new players. [MEM-LOW]
- Late game becomes spreadsheet-like. [EST]
- Little narrative or goal beyond bigger numbers.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. A small grid-layout puzzle can provide depth without combat: arrange Rider Cards in a grid whose adjacency boosts neighbours (Kamen Ride/Attack Ride synergy), just like reflectors. Optional, not mandatory.
2. Use a *soft* failure state (a heat meter that only throttles output, never destroys items) to avoid the meltdown complaint.
3. Adjacency bonuses give reasons to rearrange layouts after each prestige.
4. Keep component tiers ~x5-x20 apart and unlock by world.
5. Prestige currency that buys layout expansions (more rows/cols) is a tidy permanent-upgrade type.
6. Share/export a "layout code" so the community can theorycraft; cheap virality.
7. Provide an auto-arrange helper for casual players.
8. Low confidence; re-verify before use.
