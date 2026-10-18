# Bitburner
**Sources:** (URLs, required)
Tags: [SRC] = read from the open-source code this session; [MEM] = recalled, unverified; [EST] = my estimate.
- https://raw.githubusercontent.com/bitburner-official/bitburner-src/dev/src/Hacking.ts [SRC]
- https://raw.githubusercontent.com/bitburner-official/bitburner-src/dev/src/Constants.ts [SRC]
- https://raw.githubusercontent.com/bitburner-official/bitburner-src/dev/src/Server/formulas/grow.ts [SRC]
- https://raw.githubusercontent.com/bitburner-official/bitburner-src/dev/src/Server/data/Constants.ts [SRC]
- https://raw.githubusercontent.com/bitburner-official/bitburner-src/dev/src/Server/ServerPurchases.ts [SRC]
- https://raw.githubusercontent.com/bitburner-official/bitburner-src/dev/src/Hacknet/formulas/HacknetNodes.ts and Hacknet/data/Constants.ts [SRC]
- https://raw.githubusercontent.com/bitburner-official/bitburner-src/dev/src/Augmentation/AugmentationHelpers.ts [SRC]
- https://github.com/bitburner-official/bitburner-src and https://bitburner-official.readthedocs.io (docs, not reachable from sandbox)

## Core loop
- A text-terminal, JavaScript-programming incremental: you write scripts (`hack`, `grow`, `weaken`) that run on rooted servers and steal money from NPC servers.
- Money buys home RAM, purchased servers, hacknet nodes, programs (BruteSSH etc.), and later Augmentations from factions.
- "Install augmentations" is the prestige reset: you buy augmentations, install them, and restart with permanent multipliers.
- BitNodes (the outer prestige): destroying a BitNode resets everything and grants Source Files that give permanent bonuses and unlock new APIs (Singularity, Corporation, Gang, Bladeburner, Stock market etc.).
- Player skill is *automation*: the best income comes from writing batching scripts (HWGW) with exact timing.

## Resource types
- Money, hacking/strength/defense/dex/agility/charisma XP, Reputation (faction/company), Favor, Karma, Intelligence XP, Hash (hacknet servers), Corporation funds/shares, Gang respect, Bladeburner rank/skill points, Neuroflux Governor levels, Source-File levels, Netscript RAM (script cost). [MEM]

## Cost & production growth formulas (public or estimated; mark which)
All formulas below are [SRC] unless marked.
- Hack success chance: `chance = ((skillMult - reqSkill)/skillMult) * ((100 - difficulty)/100) * mults * intBonus`, with `skillMult = max(1, 1.75*hackingSkill)`, clamped [0,1].
- Hack money fraction stolen: `((100 - difficulty)/100) * ((skill - (reqSkill - 1))/skill) * mults / 240`, clamped [0,1].
- Hack XP: `(3 + baseDifficulty*0.3) * mults`.
- Hack time (s): `5 * (2.5*reqSkill*difficulty + 500) / (skill + 50) / (speedMults * intBonus)`. Grow time = 3.2x hack time; Weaken time = 4x hack time.
- Grow: `log growth = log1p(0.03/difficulty) * (serverGrowth/100) * growMult * coreBonus * threads` (capped at log1p(.0035) per thread), new money = `(money + threads) * exp(logGrowth)`, clamped to moneyMax.
- Security: each hack/grow adds 0.002 per thread, weaken subtracts 0.05 per thread. (ServerFortifyAmount / ServerWeakenAmount)
- Purchased server cost: `ram * 55000 * costMult * softcap^(log2(ram)-6)`; max RAM 2^20 GB; home RAM base 32000 per GB. [SRC Server consts]
- Hacknet node: purchase cost multiplier x1.85 per node; level upgrade `500 * sum(1.04^(lvl-1))`, RAM upgrade x1.28, core upgrade x1.48; income per second `level * 1.5 * 1.035^(ram-1) * (cores+5)/6 * mult`; max 200 levels, 64 RAM, 16 cores (legacy nodes). [SRC]
- Augmentation cost: each aug purchased in a run multiplies the price of *all remaining augs* by `1.9` (MultipleAugMultiplier). [SRC]
- NeuroFlux Governor: level cost multiplier `1.14` per level, infinite sink. [SRC]
- Other constants: Max skill level 975 without multipliers; TOR router 200k; travel 200k; corp faction rep 400k; donation: 1M money = 1 rep (before multipliers), favor needed to donate 150. [SRC Constants.ts]
- Coding Contract rewards: base faction rep 2500, company rep 4000, money 75M. [SRC]

## Prestige structure
- Tier 1: Install augmentations (soft reset): resets money/skills/servers, keeps augmentations (permanent multipliers), reputation resets but "favor" accumulates for faster later rep. A typical run uses ~10-30 augmentations installed in batch because of the x1.9 compounding. [SRC/MEM]
- Tier 2: BitNode destruction: need to hack the `w0r1d_d43m0n` server (requires hacking level ~3000 in the base node, scales per BitNode) and then choose the next BitNode. Awards Source File levels (up to 3, with some to 1 for BN12 infinite). [MEM]
- BitNode multipliers (`currentNodeMults`) change nearly every rate: e.g. server growth, cloud server cost/limit, hacknet income. [SRC references]
- Exploits / Intelligence give semi-permanent small buffs. [MEM]

## Unlock pacing
- [MEM/EST] First 30 minutes: learn `scan`, `nuke`, `hack`, write first script; ~2 hours to automate with purchased servers; first augment install at 3-6 hours; first BitNode destruction typically 12-30 hours in the first node.
- Faction unlocks are sequenced by hacking skill (CSEC ~ 51, NiteSec ~ 202, The Black Hand ~ 340, BitRunners ~ 505, Daedalus 2500+), roughly [MEM]. 
- Subsystems unlock via Source Files from BitNodes (Bladeburner BN6/7, Gang BN2, Corporation BN3, Stock market via purchases, Singularity BN4, Sleeves BN10, Grafting BN10, Stanek's Gift BN13...). [MEM]

## Offline progress
- Scripts continue to be simulated: "Multiplier for hacking income earned from offline scripts" = `0.75` i.e. offline hacking income is 75% of online equivalent. [SRC: OfflineHackingIncome]
- Time-based work (training, working) is processed from stored time; game also provides Bonus Time (`MillisecondsPer20Hours` style constants) for fast-forwarding catch-up while tab is open. [SRC consts]
- Game engine cycle is 200 ms per cycle. [SRC: MilliPerCycle]

## Monetization effects
- Free, open source, on Steam as a one-time purchase (no microtransactions). No ads, no energy. [MEM]
- Because it is a programming game, "paywalls" are replaced by RAM cost limits.

## What players love
- The game IS a programming puzzle: optimal play comes from your own code.
- BitNodes keep each new playthrough different, with special mechanics.
- Open-source, moddable, tweakable (Netscript API), and a strong Discord.
- Satisfying "my script stole $1e12 while I slept".

## What players hate
- Programming literacy required; bounces non-coders. [MEM]
- Some BitNodes (e.g. Bladeburner, Corporation) feel like separate grinds.
- Long early waits for RAM; the x1.9 augmentation compounding feels tough to plan. [MEM]
- Hacknet nodes are weak after the first hour (income vs cost). [MEM]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Cost compounding on *purchases within a prestige* (x1.9 per augment) gives a great "buy the right set before reset" decision without extra UI. Apply to "Rider Card" slot purchases per world.
2. An infinite, exponent-mild sink (NeuroFlux x1.14/level) keeps every number useful at the end.
3. Pair a small ladder of multipliers (1.85 node, 1.28 RAM, 1.48 cores) so each upgrade type has a distinct cost slope - cheap to implement, feels rich.
4. Hard-code constants in one file (Constants.ts) so balancing is a one-file diff; do likewise.
5. Offline at 75% of online rewards is a clean rule that keeps active play more valuable while respecting returning players.
6. Each BitNode changes global multipliers (`currentNodeMults`): model each Rider world as a multiplier table; only a few tuned numbers per world yields strong variety.
7. Unlock new subsystems only through the outer prestige (Source Files) to keep each loop simple at first.
8. Skip scripting; give a lightweight automation option (auto-buy toggles) so players still feel "I optimized this".
