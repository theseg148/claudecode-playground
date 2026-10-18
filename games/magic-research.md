# Magic Research
**Sources:** (URLs, required)
VERIFICATION UPDATE 2026-10-18: this file's title game is the Steam/mobile 'Magic Research' (2023) by Maticolotto, NOT a Kongregate/Flash original (unconfirmed). 'Retirement' is the reset; the Kongregate and 'mana/elemental' details below stay [MEM-LOW]. See Verification log.
CONFIDENCE WARNING (LOW): sandbox could only fetch raw.githubusercontent.com. I could not fetch any page about Magic Research (there are a Flash/browser original and a later "Magic Research 2" on Steam; I am not certain which details belong to which). All specifics below are [MEM-LOW] or [EST]. Treat as hypotheses.
- https://store.steampowered.com/app/2311680/ (Steam app id 2311680 from vaporlens/steamdb search results) [S]
- https://www.incrementaldb.com/community/interview/1 (interview with the creator, Maticolotto; seen in search results only)
- https://www.kongregate.com/games/ (original-era host, exact URL unverified)
- (magicresearch.fandom.com guess: not confirmed)

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

## Verification log (2026-10-18)
Method: WebSearch snippets only; no source code or wiki page reachable.
Confirmed [S]:
- Developer Maticolotto (Matias Ezequiel Colotto); on Steam (app 2311680; Steam release March 2023 per https://gg.deals/ca/game/magic-research/ , a Discord page says 2023-01-25, so exact date conflicts), Android and iOS (https://apkpure.net/magic-research/com.mcolotto.magicresearchfull).
- Premise (store text): "you are the headmaster of a newly-created institution of Magic with one goal: to learn as much as possible about this power", gain fame and win the Tournament of Magic. Over 100 spells, dozens of side stories. https://videogamegeek.com/videogame/394132/magic-research , https://inviocean.com/?p=2447
- Reset mechanic is called RETIREMENT, with retirement bonuses that speed up later runs; apprentices can be assigned to automate repeated spells; facilities/storage/land-type resource management. (inviocean / game-solver snippets)
- Reviews ~410, ~91% positive; estimated full completion 77-120 h (reviewer estimates, vaporlens/steamdb snippets: https://vaporlens.app/app/2311680/magic_research.md ).
- Patch v1.12.1 added one storyline and eight upgrades (steamdb patch notes, https://steamdb.info/patchnotes/11069169).
- Forum tip: casting create-iron-bar spell with mana yields more iron than gathering (applevis.com comment, https://applevis.com/comment/145694). Accessibility note: the game is text-based.
- Sequel Magic Research 2 (Steam 2864890): v1.3.2 added "Classic Mode"; reviewers call prestige/retirement an artificial extender. https://vaporlens.app/app/2864890/magic_research_2
Contradicted: the earlier assumption of a Flash/Kongregate original and a 'research tree as central screen' is unsupported; the game is text-based with spells, apprentices, land and storylines. 'Ascend/reincarnate' wording replaced by 'retirement'.
Unverified (keep [EST]): all cost/growth formulas, prestige currency formula, temporary spell multipliers, elemental resources, offline rules.
