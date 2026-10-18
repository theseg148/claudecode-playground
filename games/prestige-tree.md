# The Prestige Tree (Jacorb) / Prestige Tree Rewritten
**Sources:**
- https://raw.githubusercontent.com/Jacorb90/Prestige-Tree/master/README.md (describes The Modding Tree as a modified Prestige Tree)
- https://raw.githubusercontent.com/Jacorb90/Prestige-Tree/master/js/mod.js (modInfo, getPointGen, version)
- https://raw.githubusercontent.com/Jacorb90/Prestige-Tree/master/js/layers.js (about 500 KB; 31 addLayer calls)
- Scratch copies: /tmp/claude-0/-home-user-claudecode-playground/2e77cd6e-e441-551f-a27e-40f493265545/scratchpad/src3/Jacorb90_Prestige-Tree_master_js_*.js (untrusted data, read only)
- https://gitee.com/loader3229/multitree (search hit: mirror of The Modding Tree) [S]
- Tags: [S] search snippet, [CODE] source, [M] memory, [E] estimate.

## Core loop
- Start with 10 points, buy the first upgrade, then points/sec accrue. Reset points for "prestige points" (P), buy upgrades, repeat. [CODE] (initialStartPoints 10; `canGenPoints = hasUpgrade("p", 11)`)
- Each new layer is a reset of the layers below that produces a new currency, new upgrades, and often a new minigame (boosters, generators, time, enhance, space, hindrances, quirks...). [CODE]
- Points per second = 1 * multipliers from upgrades, achievements, and every unlocked layer's effect. [CODE] (mod.js getPointGen)
- Game ends at e3.14e16 points in v1.3 ("The Expansion Update"). [CODE] (modInfo.endgame, VERSION)

## Resource types
- Points (base), then per layer: prestige points (p), boosters (b), generators (g), time capsules (t), enhance points (e), space energy (s), super boosters (sb), super generators (sg), hindrance spirit (h), quirks (q), solarity (o), subspace (ss), magic (m), balance (ba), phantom souls (ps), honour (hn), nebula (n), hyperspace (hs), imperium (i), mastery (ma), ghosts (ge), and more. [CODE] (layer ids/resource strings)
- Secondary currencies inside layers: time energy, generator power, space buildings, subspace, quirk energy. [CODE]
- Achievements are a layer ("a") with multiplicative boosts (e.g. x1.1, x1.5, x2 to prestige gain). [CODE]

## Cost & production growth formulas (public or estimated; mark which)
- Layer types: "normal" (gain depends on base resource: roughly (base / requires)^exponent * gainMult, floored) and "static" (cost of Nth unit = requires * base^(N^exponent)). Comment in source says "normal: cost to gain currency depends on amount gained. static: cost depends on how much you already have". [CODE] for the comment, [M] for exact TMT formulas
- Prestige (p): requires 10 points, exponent 0.5 (0.75 when mastered). [CODE]
- Boosters (b) and Generators (g): static, requires 200 points, exponent 1.25, base 5. [CODE]
- Time capsules (t): static, exponent 1.85, base 1e15; requires 1e120 * 1e180^(unlockOrder^1.415038). [CODE]
- Enhance (e): normal, exponent 0.02, same unlock-order requirement. [CODE]
- Space (s): static, exponent 1.85, base 1e15 (1e10 with an upgrade). [CODE]
- Hindrance spirit (h): normal, requires 1e30 time energy, exponent 0.125. [CODE]
- Quirks (q): normal, requires 1e512 generator power, exponent 0.0075. [CODE]
- Subspace energy (ss): static, requires 28-30 space energy, exponent 1.1, base 1.15. [CODE]
- Exponent shrinks with depth (0.5 -> 0.125 -> 0.0075), which is why late layers need absurd base values. [E] consequence of the numbers above

## Prestige structure
- 31 layers across rows 0-6 (row counts 1,2,5,4,5,6,5 from a grep of `row:`). [CODE] approximate
- Row order: P -> (B, G) -> (T, E, S) -> (H, Q, SB/SG, O...) -> deeper rows. [CODE] (`layerShown` conditions) 
- `unlockOrder`: the first of T/E/S you unlock is cheap; each later one costs 1e180^(order^1.415) more, and boosters/generators cost 5000x more if taken second. This forces a path choice and a replay reason. [CODE]
- Layers keep things through resets via milestones (`keep` lists, passiveGeneration). [CODE]
- "Mastery" (ma) layer re-runs earlier layers with buffed exponents (e.g. p exponent 0.5 -> 0.75, b base 5 -> 1.5). [CODE]

## Unlock pacing
- P always shown; B and G need P unlocked; T/E need B and G; S needs G; SB needs T, E, S; H needs T plus a Q milestone; later layers chain off several previous ones. [CODE] (`layerShown`)
- Each layer reveal is a screen-level event (a new node on the tree), which is the main pacing beat. [M]
- Total length is days to weeks for a first run. [M]

## Offline progress
- `offlineLimit: 1` (hours). [CODE]
- Players can also use passive generation milestones instead of waiting. [CODE]

## Monetization effects
- None; free, open source. [M]

## What players love
- The tree view and the sense of discovering a structure; endless layering. [M]
- Spawned TMT, a modding framework and many fan trees. [S] (README line)

## What players hate
- Hard walls where nothing progresses without a new layer; huge numbers become meaningless. [M]
- Heavy reading and many interlocking effects late on. [M]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. A world is a layer: each Rider world = one layer with its own currency, 10-20 upgrades, one small minigame. [CODE]
2. Show the whole map early as dimmed nodes; unlocking a node is the reward beat, not a combat victory. [CODE] (`layerShown`)
3. Let the player choose the order for a few worlds (unlockOrder penalty) so Decade's "world hopping" feels like a decision and creates replay. [CODE]
4. Use a "mastery" replay: revisit an earlier world later with changed rules, so old worlds stay relevant. [CODE]
5. Keep exponents shrinking per depth so currency gain slows naturally, then reset the scale with a new currency. [CODE]
6. Cap offline small (1 h here) only if you have other automation; for a casual mobile-style game I would be more generous. [E]

## Verification log
- mod.js, README.md, layers.js fetched from raw.githubusercontent.com (HTTP 200). I did NOT read the TMT core (js/game.js, js/technical/*), so the exact normal/static formulas are [M], not [CODE].
- Search for the repo returned nothing useful; the URL Jacorb90/Prestige-Tree was guessed from memory and verified by successful fetch (author = "Jacorb" in mod.js).
- Layer count (31) and row distribution were counted by grep; treat as +-1.
- Layer unlock details for layers past row 4 were only sampled.
