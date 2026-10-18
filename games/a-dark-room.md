# A Dark Room
**Sources:** ([S] = seen in a search snippet, [M] = memory of the open-source code, unverified, [E] = estimate.)
- https://adarkroom.fandom.com/wiki/Buildings_(Mobile) [S - costs]
- https://adarkroom.fandom.com/wiki/Events_(Browser) [S - events list]
- https://adarkroom.fandom.com/wiki/Outside_(Browser) [S - village stages]
- https://adarkroom.fandom.com/wiki/Room_(Mobile) [S]
- https://www.arrpeegeez.com/2026/02/a-dark-room-walkthrough.html [S - walkthrough]
- https://www.mobygames.com/game/65127 (credit: Michael Townsend / Doublespeak Games) [S]
- https://github.com/doublespeakgames/adarkroom (open source, script/room.js, outside.js, events/*.js - not fetched) [M]

## Core loop
- Text-only. Stoke fire (click) -> a stranger/builder arrives -> gather wood -> build Trap -> check traps for fur/meat -> build Cart -> Huts -> population -> Workers (gatherers, hunters, trappers, tanners, charcutiers, iron/coal miners, steelworkers, armourers) -> trade (Trading Post, Caravan) -> explore the world map -> ship (Spaceship) -> fly.
- Three distinct "genres" in one game: idle village economy, survival map exploration, and a final ship-flying Space Invaders-style shooter - each triggered by a story beat.

## Resource types
- wood, fur, meat, scales, teeth, cloth, leather, cured meat, iron, coal, steel, sulphur, bait, torch, bullets, energy cells, bolas, alien alloy, medicine, compass, charm. Population (villagers) is a resource too.

## Cost & production growth formulas
- Builder income: +5 wood per 10 s (constant), so fire can't go out while building [S].
- Trap: cost = `(n+1) * 5` wood, max 30 [S]. Hut: cost = `20 + n*60` wood per search (max 20 huts) [S]; actual code: 100 + ... verify [M]. Each hut +4 population [S].
- Cart: 30 wood, gathering wood becomes 18? per click [S] (original was 10 -> 50 in early versions [M]).
- Lodge 200 wood, 10 fur, 5 meat; Trading Post 300 wood + 100 fur; Workshop 800 wood, 100 leather, 10 scales [S].
- Worker output (per 10 s) [M]: gatherer +1 wood, hunter +0.5 fur & +0.5 meat, charcutier -5 meat -> +1 cured meat, miner +1/+3 ore with cured meat/food upkeep; negative-cost jobs create supply chains.
- Costs scale as linear in n (`a + b*n`) rather than exponential - the game's pacing is driven by event timers, not by exponential costs.

## Prestige structure
- None per se. The Spaceship ending allows "Restart" on ending; a Prestige mode in newer builds gives "ship cargo" carry-over (mobile) [M]. Essentially a one-time ~3-5 hr story.

## Unlock pacing
- 0-2 min: dark room, fire. 2-5 min: builder, wood. 10 min: traps, cart. 20-30 min: huts & village growth (stage names: Silent Forest -> Lonely Hut (1 hut, 4 pop) -> Tiny Village (2-4) -> Modest Village (5-8) -> Large Village (9-14) -> Raucous Village (15-20 huts, 60-80 pop)) [S].
- 30-60 min: Lodge, Trading Post. 1-2 hr: compass & wander world; 2-3 hr: ship & space. Random events (Shady Builder, Nomad, Wanderer) fire on timers; Shady Builder appears when less than 20 huts built [S].

## Offline progress
- Timers/jobs: A Dark Room's browser version stores to localStorage but does not simulate offline; income persists only while open (mobile may differ) [M]. Fire cools down while away?? (no, state frozen) [M/E].

## Monetization effects
- Free in browser; paid iOS/Android app ($0.99-ish) with no IAP. No ads. Pure game-as-art.

## What players love
- The minimalism and the "reveal" of mechanics one step at a time: each button appears only when relevant. Atmosphere, writing, and the late-game twist.
- Mystery: the player is never told what to do; the narrative is delivered via event text.

## What players hate
- Early game waiting (stoke fire constantly); trap/fur tedium; the map exploration can be punishing (starvation, losing items); some find the end-game space shooter jarring.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Reveal UI only as unlocked; each new tab is a story beat - map to "new world arrives".
2. Linear cost formulas (`a+b*n`) with hard caps (30 traps, 20 huts) make predictable pacing - good for a tight tutorial.
3. Stage names tied to counts (Lonely Hut...Raucous Village) give flavorful feedback - do the same for each Rider world's "development level".
4. Random timed events (Shady Builder, Nomad) add variety without combat.
5. Supply-chain jobs (hunter -> charcutier) create upgrade puzzles with no fighting.
6. Short 3-5 hr arc with a twist ending is a fine target for a world-hop story.
