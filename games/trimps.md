# Trimps
**Sources:** ([S] = seen in search snippet, [M] = memory, unverified, [E] = estimate. WebFetch was DNS-blocked.)
- https://trimps.fandom.com/wiki/Coordinated?oldid=6591 [S]
- https://trimps.fandom.com/wiki/Equipment?oldid=7908 and ?oldid=4674 [S]
- https://trimps.fandom.com/wiki/Anticipation?oldid=6805 [S]
- https://trimps.fandom.com/wiki/Power_II [S]
- https://reddit.com/r/Trimps (Perky calculator thread, 2017, via mirror reddit.birdcat.cafe/r/Trimps/comments/6n0mr7/) [S]
- https://trimps.github.io and https://github.com/Trimps/Trimps.github.io (source: main.js, config.js, perks) [M, not fetched]
- Note: wiki revisions are old and balance has changed (Universe 2 / Radon added later).

## Core loop
- Breed Trimps (idle population growth with Geneticists), assign them to Food/Wood/Metal/Science, buy buildings and equipment, send an army into the current zone, fight cells automatically. The player's agency is on economy and gear, not manual combat. (Note: this game does have auto-fighting; for our game we only borrow the economy.)
- Zones 1..~60-100 per run; at the end "Portal" out for Helium, spend Helium on Perks, repeat.

## Resource types
- Food, Wood, Metal, Science, Fragments, Gems, Trimps, Helium (prestige currency), Nurseries, Radon (Universe 2), Bones (from enemies), Dark Essence/Scruffy Perk currencies in later content.

## Cost & production growth formulas
- Perk cost [S]: Coordinated base 150,000 He, cost multiplier 1.3 per level, cap 15; each level cuts the army-size requirement per Coordination by 2% compounding (base 25%) -> ~25M He to max.
- Anticipation [S]: base 1,000 He, x1.3 per level, cap 10, +2% damage per second of breeding time (cap 30 s).
- Power II [S]: base 20,000 He, +500 per level (linear), no cap; +1% additive attack per level.
- General: exponential perks `base * mult^level`; linear perks `base + inc*level` [S pattern].
- Equipment [S/M]: level-1 price per prestige tier (I..X) goes ~40 -> ~1.67 quadrillion; per-level cost = `levelOneCost * costMult^level` (multiplier ~1.2) [M, exact value not retrieved]; each equipment prestige multiplies stats by ~1.19-1.5 [E].
- Zone enemy health ~ exponential in zone (about 1.1-1.2x per zone) and attack similarly [E].
- Helium gain per zone (from kills) rises with zone; big bonus after Z~60 and with Scientist/"Turkimp" [M].

## Prestige structure
- Portal -> Helium (computed from highest zone reached, total cells, and "Looting"-type perks) -> perks give: Resourceful, Power, Toughness, Agility, Looting, Carpentry, Coordinated, Anticipation, Pheromones, Meditation, Relentlessness, Siphonology, Cunning, Curious, Overkill, Capable (late)...
- Layered: Heirlooms (drop-based stat items) at Z~90; Nature (tokens) at Z~236; Universe 2 / Radon at Z~230-ish [M]; Mutations/Corruption at Z~181 [M]; Magma at Z~230 (Dimensional Generator) [M]. Treat zones as approximate [E].

## Unlock pacing
- First 15-30 min: Z1-10. Day 1: first portal around Z~30-50. Week 1: Z60+. Months: Z100-200+ with corruption [E]. Each layer is a "new game within the game".
- Time per run: 10 min early -> several hours late.

## Offline progress
- Yes: when the tab closes, the game simulates "catch-up" while you were gone, capped (a day or so) and the Trimps still gather (Trimps keep fighting?). Time warp is capped (offline limit ~48h?) [M/E].

## Monetization effects
- None: free browser game (also on Steam), by Greensatellite; donations via Patreon.

## What players love
- Satisfying exponential perk-spending; fascinating depth with calculators (Perky/AutoTrimps); tons of long-term layers; low-stress idle.

## What players hate
- Overwhelming late-game complexity; UI built around spreadsheets; needs a bot (AutoTrimps) to stay sane; unclear which perk to buy.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Mix additive perks (+500 per level) with multiplicative (x1.3 per level) so players have cheap/fast and expensive/exponential buys - good for a Rider "form" tree.
2. Give caps to key perks (Anticipation 10, Coordinated 15) so players get "complete" moments.
3. Prestige currency (Helium) driven by zone depth reached = world depth reached - natural analogue.
4. New permanent layers at zone thresholds unlock mid-run (Heirlooms) - drop surprise unlocks at milestones.
5. Do not copy the opaque late-game spreadsheet culture; give an in-game recommender.
6. Auto-fight is replaceable with auto-progress through worlds (no fighting rule) while keeping upgrade focus.
