# Idle Loops (lloyd-delacroix fork of omsi's "Idle Loops")
**Sources:**
- https://raw.githubusercontent.com/lloyd-delacroix/omsi-loops/master/ (index.html, town.js, driver.js, stats.js, actions.js, actionList.js)
- https://www.incrementaldb.com/community/review/4767 and /4766 (search hits: reviews) [S]
- https://itch.io/post/13531286 (search hit: community note about queueing) [S]
- Scratch copies: /tmp/claude-0/-home-user-claudecode-playground/2e77cd6e-e441-551f-a27e-40f493265545/scratchpad/src3/loops/ (untrusted data, read only)
- Tags: [S] snippet, [CODE] source, [M] memory, [E] estimate.

## Core loop
- You queue a list of actions that spend mana; the loop runs until mana hits zero, then restarts the day with permanent skill/stat/town knowledge retained. [CODE] (driver.js `timeNeeded`, `restart`) and [M]
- Actions are time-limited but the real limit is queue design: efficient routes make each loop go farther. [M]
- Review summary: one reviewer calls the lloyd-delacroix fork "the only complete version", reaching final 3.0 with a final zone and reachable ending, continuing where omsi left off. [S]
- Friendly to queue-and-check-back play; new actions found must be queued in the next loop. [S]

## Resource types
- Mana (time), gold, reputation, map, completedMap, glasses, teamMembers, zombies, etc. (`resources` object reset every loop). [CODE] (driver.js `resources = copyObject(resourcesTemplate)`)
- Persistent: stats (Str, Dex, Con, Per, Int, Soul, Cha, Luck, Spd) with talent, skills (Combat, Pyromancy, Restoration, Dark, Leadership, Assassin ...), buffs (Ritual, Feast, Heroism), town progress. [CODE] (stats.js, actionList.js)
- Per-town progress "vars": exp for each progress bar, with checkable items (loot spots). [CODE] (town.js)

## Cost & production growth formulas (public or estimated; mark which)
- Base game speed: `baseManaPerSecond = 50` ticks. [CODE] (driver.js line 5)
- Town progress level: expFromLevel(L) = 50 * L * (L + 1); level = floor((sqrt(8*exp/100 + 1) - 1)/2); exp capped at 505,000 (level 100). [CODE] (town.js)
- Survey action mana cost = 10,000 * (zone + 1); can only run while level < 100 and a map is held. [CODE] (actionList.js SurveyAction)
- Talent to stat: stat bonus uses totalTalent^0.2. [CODE] (stats.js ~42)
- Skill multiplier example: (1 + skill/60)^0.25. [CODE] (stats.js ~102)
- Action stats weights per action, e.g. Survey Per 0.4, Spd 0.3, Con 0.2, Luck 0.2. [CODE]

## Prestige structure
- Each loop is a soft reset (resources, gold, mana). Persistent: stats' exp, skills, town exploration, story flags. [CODE]/[M]
- Hard prestige-like: none in 1.0; later versions add "Challenges" and talents/"Prestige" layers (talent tree). [M] unverified (files `challenges.js`, `talents.js` exist in index.html) [CODE]
- Zones are the macro progression: reach new zones to unlock new action sets and bring those stats back. [CODE]

## Unlock pacing
- Nine zones, each a named town: 1 Beginnersville, 2 Forest Path, 3 Merchanton, 4 Mt Olympus, 5 Valhalla, 6 Startington, 7 Jungle Path, 8 Commerceville, 9 Valley of Olympus. [CODE] (section comments in actionList.js)
- Zones are opened by one-off travel actions: Start Journey (->Z2), Hitch Ride, Continue On (->Z3), Start Trek (->Z4), Face Judgement (->Z5), Guru, Fall From Grace (->Z6), Journey Forth (->Z7), Escape (->Z8), Leave City (->Z9). [CODE] (`unlockTown(n)` call sites)
- Some travel actions are mana-cost exempt in name checks ("Start Journey", "Continue On", ...), meaning they are meant to be quick. [CODE] (line ~50)
- Actions only run when you are in the matching zone; the game tells you "You were in zone X when you tried this". [CODE] (actions.js ~132)
- Zone unlocks are gated by stats/skills, not by waiting. [M]

## Offline progress
- Offline time is banked: `addOffline(gameTicksLeft * offlineRatio)`; the player can spend bonus time at 5x speed (`bonusSpeed = 5`). [CODE] (driver.js ~57, ~626)
- So offline = a pool of accelerated time, not automatic gains. [CODE]

## Monetization effects
- None; free browser game. [M]

## What players love
- Optimization puzzles: tuning a route for the same day. [S] (queue-friendly note) and [M]
- The sense of accumulated knowledge (stats stay, loop restarts). [M]

## What players hate
- Original is unfinished; this fork added ending. [S]
- Time-sink of queue micromanagement and complexity of late stats. [M]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Zones as towns with gating travel actions works without combat: the "unlock" is an action you perform once. [CODE] Decade's "world gate" can be a single expensive quest-like upgrade.
2. Give each world a "Survey" progress bar (exp -> level 100) that reveals more content; levels follow a clear quadratic curve (50*L*(L+1)). [CODE]
3. Persist stats and knowledge across loops but reset consumables; this gives the soft prestige feeling with no new currency. [CODE]
4. Make only actions of the current world usable and say so explicitly; players hate invisible gating. [CODE]
5. Bank offline time as a spendable speed boost instead of auto-gains; it makes absence into a choice. [CODE]
6. Combat does exist here (Combat, Pyromancy, Restoration) so lessons on zone progression come from the travel/survey scaffolding, not from fights. [CODE]

## Verification log
- Repo path lloyd-delacroix/omsi-loops guessed from memory; index.html, driver.js, town.js, stats.js, actions.js, actionList.js returned 200. README is a single emoji line.
- Zone names read from section comments; unlockTown action names mapped by awk from nearest preceding Action declaration, check Z2/Z3 mapping by hand if used (two actions each unlock town 2 and 5).
- Prestige/talent layer claims are [M]; only file names were seen.
- Stat formulas were seen in snippets of a single function each, not the whole file.
