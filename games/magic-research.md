# Magic Research
**Sources:** (URLs, required)
CONFIDENCE WARNING (LOW): sandbox could only fetch raw.githubusercontent.com. I could not fetch any page about Magic Research (there are a Flash/browser original and a later "Magic Research 2" on Steam; I am not certain which details belong to which). All specifics below are [MEM-LOW] or [EST]. Treat as hypotheses.
- https://store.steampowered.com/search/?term=Magic+Research (search page, not fetched)
- https://www.kongregate.com/games/ (original-era host, exact URL unverified)
- https://magicresearch.fandom.com (guess; unverified)

## Core loop
- Wizard-themed idle: you gather mana, research spells and upgrades, and summon helpers (apprentices, golems, towers... [MEM-LOW]) that produce mana and other magical resources.
- Research is a tree: spending resources unlocks buildings or multipliers, which unlock further research.
- Periodically you "ascend/reincarnate" the wizard (the prestige) to gain permanent bonuses and open the next tier of the tree. [MEM-LOW]
- The "research" word in the title makes the *tech tree* the central screen, not buildings.

## Resource types
- Mana (basic), plus several elemental/arcane resources (e.g. fire, water, etc.) and Research points. [MEM-LOW]
- Prestige resource(s) (names unverified). [MEM-LOW]
- Time/ritual timers for spells with cooldowns. [EST]

## Cost & production growth formulas (public or estimated; mark which)
- No verified numbers. Genre-standard estimates for planning:
  - Building cost = base * r^owned with r around 1.10-1.20. [EST]
  - Research cost steps by roughly x3-x10 per tier, and unlocks multiply production x2-x5. [EST]
  - Prestige currency = floor(sqrt(lifetime mana / threshold)) or cube-root variants (Game Developer's "math of idle games part III" says most games use a fractional exponent like sqrt or cbrt). [EST, with the Game Developer article as the genre reference: https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii]
- Spell effects are temporary multipliers (x2-x10 for tens of seconds to minutes) driving active play. [MEM-LOW]

## Prestige structure
- One main prestige loop (ascension) with a permanent multiplier and gated tech; later versions add additional layers. [MEM-LOW]
- Possibly an equivalent of "unlock the next realm/tier" on first prestige. [EST]
- Typical genre design: first prestige at 30-90 min, second 1-3 days. [EST]

## Unlock pacing
- [EST] Minute 0-5 tutorial of mana gathering; 15-30 min first research branch; 1-2 hours first prestige available; the full tree is a multi-day affair.
- Research gating is the pacing mechanism: you cannot buy stronger buildings until their prerequisite research completes. [MEM-LOW]

## Offline progress
- [EST] Probably standard: production for the time away at a reduced rate, capped (typical 8-24 h). I could not confirm.
- Research timers (if timed) keep counting while away. [EST]

## Monetization effects
- Original was free browser/Flash-era game with ads on host portal; the Steam sequel is a paid game. [MEM-LOW]
- Mobile-style monetization (speed-ups) not recalled. [EST]

## What players love
- A real tech tree with meaningful branching; wizard theme.
- Active spells give moments of agency in an otherwise idle game. [MEM-LOW]
- Prestige permanent bonuses are clearly felt. [EST]

## What players hate
- Early game slow before first research completes. [EST]
- Balance issues typical of small-team indie idles (soft walls at the second prestige). [EST]
- Lack of documentation; wiki thin. [EST]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Make the *tech tree* the main screen: since the game is upgrade-focused with no fighting, "Rider Cards / Forms / Kamen Ride unlocks" as a tree gives a clear loop (spend, unlock, see new thing).
2. Use timed active "spells" (e.g. Attack Ride flash: x3 production for 30 seconds, 5-minute cooldown) as optional active play without combat.
3. Prestige currency via sqrt of lifetime currency (genre baseline); tune the divisor so first prestige lands in 30-60 minutes. [EST]
4. Research costs step x3-x10 per tier; building costs r = 1.12-1.15. [EST]
5. Let each prestige open the next branch of the tree (a new Rider world), not only a multiplier, to feed the "sequential worlds" fantasy.
6. Provide a thorough in-game help/wiki page since small idles are criticised for poor docs.
7. Avoid second-prestige soft walls by playtesting the transition: ensure the second layer's first purchase is affordable in about 10-15 minutes.
8. Record uncertainty: this file is low-confidence; re-research before copying numbers.
