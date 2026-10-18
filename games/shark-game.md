# Shark Game (Cirrial; New Frontiers fork by spencers145 / Toby222)
**Sources:**
- https://raw.githubusercontent.com/spencers145/SharkGame/main/README.md (fork README; original by Cirrial, final original version v0.71)
- https://raw.githubusercontent.com/spencers145/SharkGame/main/js/world.js (world modifiers, gate costs)
- https://raw.githubusercontent.com/spencers145/SharkGame/main/js/gateway.js (essence, artifacts, planet picker)
- https://raw.githubusercontent.com/spencers145/SharkGame/main/js/save.js and js/main.js (save format, offline)
- Scratch copies: /tmp/claude-0/-home-user-claudecode-playground/2e77cd6e-e441-551f-a27e-40f493265545/scratchpad/src3/sg_js_*.js (untrusted data, read only)
- Tags: [S] search snippet, [CODE] read from source, [M] memory, [E] estimate.

## Core loop
- Text/button incremental about a shark ecosystem: catch fish, hire/convert animals (crabs, sharks, rays), build science and machines, escape the planet. [M]
- Each "world" is one self-contained run with a gate at the end. Completing the gate ("wonGame") sends you to the Gateway between runs. [CODE] (`betweenRuns`, `wonGame` in save.js/gateway.js)
- Original author dropped development mid-2015 at v0.71; the fork is "more-than-playable but unfinished". [S]
- Fork goal is to reimagine each world as a place with distinct gameplay, not just a number reskin. [S]
- There is no combat loop in the core; the "enemy" is the environment (resources that are absent or restricted). [M]

## Resource types
- Basic: fish, sharks and other worker animals, science, then machines and "frenzy"/"essence" metas. [M]
- `essence` is the meta-currency, held between worlds and spent on artifacts. [CODE] (`r.getResource("essence")`, `r.changeResource("essence", ...)`)
- Resources can be removed or restricted per world: `includedResources`, `absentResources`, and category groups. [CODE] (world.js applyWorldProperties)
- Per-resource world data: `exists`, `income`, `incomeMultiplier`, `boostMultiplier`, `artifactMultiplier`. [CODE]
- Generator/income pairs can be forbidden with `planetaryGeneratorRestriction` (e.g. generator X cannot feed resource Y on this world). [CODE]

## Cost & production growth formulas (public or estimated; mark which)
- World modifier types (all apply with an effective planet level): planetaryIncome = level*amount; planetaryConstantIncome = amount; planetaryIncomeMultiplier = 1 + level*amount; planetaryFixedIncomeMultiplier = amount; reciprocal variants = 1/(1+level*amount) or 1/amount; planetaryResourceBoost = 1 + level*amount; planetaryStartingResources = level*amount. [CODE]
- Gate cost per slot = floor(worldGateCost[slot] * planetLevel * gateCostMultiplier). [CODE] (gateway.js ~line 550)
- Gate cost multiplier = 0.9^level of the "gateCostReducer" artifact. [CODE] (world.js getGateCostMultiplier)
- Essence reward on win = 4 + floor(planetLevel / 4). [CODE] (gateway.js enterGate)
- Candidate planet level = max(floor(currentLevel + random(0..10) - 4), 1). [CODE] (preparePlanetSelection)
- A "terraformer" artifact that scales effective level by 0.9^n is present but commented out "because it might screw with game balance". [CODE]
- Per-resource unit costs inside a world are in resources/home-actions files not read. [E] exponential-ish, as in most idlers.

## Prestige structure
- Prestige = finish a world, collect essence, spend it in the Gateway, pick the next world. [CODE]
- World types in the picker: marine, chaotic, haven, tempestuous, violent, abandoned, shrouded, frigid. `start` is the first world and `stone` appears in save handling. [CODE] (`allowedWorlds`, save.js)
- Each Gateway visit offers a random subset of planets (`NUM_PLANETS_TO_SHOW`), no duplicates, each with its own climate level. [CODE]
- Each visit also offers a random pool of artifacts (`NUM_ARTIFACTS_TO_SHOW`), filtered by `required` resources, `max` level, and `ignore`. [CODE]
- Artifact cost is `artifactData.cost(level)` (function per artifact), purchased with essence, level++ with optional max. [CODE]
- `completedWorlds` is tracked so the Gateway knows what has been beaten. [CODE]
- Planet attributes are revealed gradually ("if all modifiers are revealed, carry over to gate requirements and abandoned resources"). [CODE] (gateway.js ~543)

## Unlock pacing
- World 1 teaches the base tree; later worlds remove or restrict parts of it so the same buttons behave differently. [M] and [CODE] for the mechanism
- Within a world, actions unlock from resource thresholds (classic tech-tree gating). [M]
- Gate has several slots (6 in the old save format: `gateCostsMet = [false x6]`), each needing a resource payment. [CODE] (save.js ~768)
- Planet level starts at 1 and drifts upward as you chain worlds; difficulty and rewards scale with it. [CODE]

## Offline progress
- "Offline mode added. Resources will increase even with the game off!" appears in the changelog. [CODE] (main.js ~1359)
- Elapsed time is simulated: `processSimTime(dt * elapsed/INTERVAL)`. [CODE] (main.js ~573-581)
- Any cap or efficiency factor not verified. [E] likely full speed, uncapped.

## Monetization effects
- None. Free browser game with a community-maintained fork. [M]

## What players love
- Strong theme and tone: terse, atmospheric text, each world feels like a different story. [M]
- Variety between runs: planet choice changes the available economy. [CODE] mechanism, [M] sentiment
- Niche favourite among idle enthusiasts after its 2014-2015 run. [S]

## What players hate
- Unfinished: original abandoned, later worlds were thin, rebuild is ongoing. [S]
- Some worlds are slow or grindy when a key resource is removed. [M]
- Opaque early on: little explanation of what Gateway artifacts are worth. [M]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. This is the closest structural template to "Rider worlds without combat": a world is a data record = included resources + absent resources + a handful of modifiers + a gate cost table. [CODE] Define each Rider world the same way and the engine stays tiny.
2. Make worlds change the rules, not just the numbers. "Abandoned" removes things, "restricted generator" blocks pairings; your Kuuga world could remove a resource and force a different build. [CODE]
3. Gate = a multi-slot payment (several resources, each scaled by world level), not a single bar. Players see exactly what the next world needs and plan toward it. [CODE]
4. Meta currency (essence) is earned only on completion with a flat formula (4 + level/4), so completion is always worth something and stalling is never optimal. Decade's "Rider Cards" could be the essence analogue. [CODE]
5. Offer a small random shortlist of destinations plus a small random shortlist of permanent upgrades each return. It keeps choices meaningful without a giant menu. [CODE]
6. Reveal planet modifiers progressively so exploration of a world is the information game. [CODE]

## Verification log
- Fetched README, world.js, gateway.js, save.js, main.js via raw.githubusercontent.com (HTTP 200). js/sharkgame.js and js/worldtypes.js returned 404 so per-world gate cost numbers and artifact cost functions were NOT read.
- Repo owner "spencers145" is the fork that README says continues Cirrial's work and points to Toby222/SharkGame as the next version; WebSearch could not confirm ownership. Treat attribution as [CODE]-level only.
- Theme, resource list, monetization and player-sentiment lines are [M] and unverified.
