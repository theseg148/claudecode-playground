# Candy Box 2
**Sources:** (URLs, required)
VERIFICATION UPDATE 2026-10-18: author, release date, tech stack, game version and wiki location are now confirmed. The compiled/TypeScript game code could NOT be fetched (candybox2.js and sources/* return 404 on raw), so NO numeric formula is verified. See Verification log.
CONFIDENCE WARNING: the sandbox could only reach raw.githubusercontent.com. Wikipedia, the fandom wikis and the game site timed out/ENOTFOUND, and no Candy Box 2 source repo was reachable. Everything below is [MEM] (recalled, unverified) or [EST]. Re-verify with the URLs before using numbers.
- https://candybox2.github.io/ (official game; not fetched)
- https://en.wikipedia.org/wiki/Candy_Box_2 (not fetched)
- http://candybox2.gamepedia.com (wiki link taken from the game's own index.html; not fetched)
- https://github.com/candybox2/candybox2.github.io (source repo; link from the game's index.html) [CODE-partial]
- https://raw.githubusercontent.com/candybox2/candybox2/master/index.html and .../faq.html (read) [CODE]

## Core loop
- ASCII-art browser game by aniwey (a student from Caen, France), released 2013-10-24 as sequel to "Candy Box!". [S: https://en.wikipedia.org/wiki/Candy_Box!] The ORIGINAL Candy Box! gives candies at 1 per second [S, same page]; that rate for Candy Box 2 is unconfirmed [MEM].
- Spend candies on nothing visible at first -> the game rewards patience: tools, shops and areas appear as total candies grows (the Candy Box! trick: "do nothing, then things appear").
- Then branch: eat/throw candies, buy lollipops, farm lollipops, feed the cauldron, forge equipment, go on quests.
- Quests are small ASCII adventures (fight, collect candies, find chocolate bars/pain au chocolat) that return candies and items; items unlock more quests and a map.
- Finally the story arc ends in several "worlds" (castle, desert, hole, sea, giant beanstalk, wishing well, dragon...). [MEM]

## Resource types
- Candies (main), Lollipops (production-gate), Chocolate bars (rare crafting), Pain au chocolat, Candy "hearts"/health, Gold-like "candies" used as item currency, Cauldron ingredients, Wishing-well candies, Time-limited candy production bonuses from items. [MEM, partially EST]
- Equipment: sword/armour/boots, "Great items", staff, bow etc. gating quests. [MEM]

## Cost & production growth formulas (public or estimated; mark which)
- No public closed forms found. Estimates based on how the game plays:
  - Base candy income: 1 candy/sec at start. [MEM]
  - Shop prices grow roughly 3-10x between tiers (e.g. 10 -> 100 -> 1,000 candies then thousands to millions late). [EST]
  - Lollipop farm: each lollipop planted yields over time (a timed growth mini-system); costs roughly 10x per tier. [EST]
- Because quests (not buildings) drive income, growth is *additive via equipment* rather than exponential via buildings. [EST]
- The cauldron uses recipes (mix X candies + Y lollipops -> item), thus sink costs are linear in ingredients rather than geometric. [MEM/EST]

## Prestige structure
- None in the classic sense. There is no reset layer that gives a currency; a single playthrough ends in a finite story (final boss then ending). [MEM]
- A few parts reset locally (e.g. completing a quest then re-running for candies; "Candy Box 1" sub-game inside). [MEM]
- That means replay value comes from secrets, achievements/ASCII art, and optional challenges. [MEM]

## Unlock pacing
- [EST] First 5-15 min: nothing to do but wait/eat; shop appears; first quest around the 15-45 min mark; map/town and cauldron within ~1-2 hours; full completion about 8-20 hours with secret hunting.
- The "reveal as you wait" pacing (a new UI element appears after crossing a candy threshold) is the signature; each unlock introduces a new element in the same ASCII page, so the page itself grows. [MEM]

## Offline progress
- [MEM] Income continues only in a running tab; saving is manual (save to file or cookie/local storage), no explicit offline catch-up formula. [EST based on the original Candy Box design]
- Time-based timers (lollipop growth) are tied to real-time elapsed since last open, which acts as lightweight offline progress. [EST]

## Monetization effects
- Free, no ads, no purchases. Made as a hobby game; released as web game, later with a Steam port. [MEM; Steam port unverified]
- Because it is non-monetized, the design is purely about curiosity and discovery.

## What players love
- Surprise: the game conceals most of its content until you play long enough.
- ASCII art charm, humour, and Easter eggs (e.g. hidden quests, secret ending).
- Quests are compact, readable and different, not another idle number.
- Nostalgia from the first Candy Box!, which many consider the origin of the 2013 incremental wave.

## What players hate
- Tedious waiting at the start with no hints. [MEM]
- Combat is basic; mis-built characters can get stuck needing candies grind. [EST]
- No persistent meta-progression, so replays feel same. [MEM]
- Manual saves can lose progress. [MEM]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Reveal UI progressively: each Rider world's panel appears only when the previous milestone is crossed (Candy Box's "page grows" trick). Cheap to implement; strong sense of discovery.
2. A first-minute hook can be a tiny passive income plus ONE obvious thing to do, then the first unlock within about 60 seconds. (Candy Box's weakness: too slow; fix it.)
3. Use mini-systems (cauldron-style recipes) as upgrade sinks; recipes = linear cost, a nice break from geometric costs.
4. Story arc with a finite ending is fine for a Decade game: each world is a chapter, and Decade's "ride through worlds" (the Dimension Door) is a natural map.
5. Replace quests with non-combat puzzle events (collect Rider Cards, assemble a Kamen Ride sequence) to keep the exploration feel with no fighting.
6. Hidden easter-egg unlocks (secret cards, hidden forms) reward curiosity and give community talking points.
7. Include auto-save from day one; manual-save loss is a recurring complaint.
8. Treat its absence of prestige as a deliberate option: first release can ship world 1-3 as a campaign and add prestige later.


## Source-verified formulas
No verified source code could be fetched this session: the candidate raw URLs for the Candy Box 2 repository (`candybox2/candybox2.github.io`, `candybox2/candybox2`, `aniwey/candybox2`) returned 404 on raw.githubusercontent.com, and the GitHub tree API is not available in this sandbox. No [CODE] tags are claimed for this game; all numbers elsewhere in this file remain [MEM]/[EST]. Retry later with the correct owner/repo.

## Verification log (2026-10-18)
Local copies (untrusted, read only): /tmp/claude-0/-home-user-claudecode-playground/2e77cd6e-e441-551f-a27e-40f493265545/scratchpad/src4/candy-box-2/
Confirmed:
- [CODE] index.html in https://github.com/candybox2/candybox2.github.io (mirror candybox2/candybox2, branch master) shows "Version 1.2.3", links to wiki http://candybox2.gamepedia.com, blog candybox2.wordpress.com, IRC, and the source repo, and the original at candybox2.github.io/candybox/. The game is HTML + jQuery 1.9.1 + one bundled script candybox2.js.
- [CODE] faq.html (same repo): "The game is written in TypeScript ... compiles to javascript using tsc"; says octopus-king behaviour and "the squirrel's game" are NOT bugs (so those exist); contact aniwey. cacheManifest.mf lists candybox2.js, so the game works offline once cached (browser cache, not idle catch-up).
- [S] Release 2013-10-24 and developer aniwey: https://en.wikipedia.org/wiki/Candy_Box! (search snippet).
- [S] Walkthrough snippets (https://www.arrpeegeez.com/2014/08/candy-box-walkthrough.html): crossing the desert (needs health and an iron axe, ~400 candies) unlocks the lollipop farm, time ring and leather gloves. The desert/lollipop farm/castle exist, which matches Core loop. A gameskeys walkthrough says the shop sells lollipops at 60 C (three total) but its text is garbled; treat as weak.
Contradicted/unverified: "Steam port" is still unverified; "~1 candy/s" is only confirmed for Candy Box 1. Cauldron, wishing well, sea, beanstalk, shop price ladder, growth multipliers and the 8-20 h completion time remain [MEM]/[EST]; no search result mentioned the cauldron. Retry: find the compiled candybox2.js through a different mirror (e.g. aniwey/candybox2 on another host), then grep for candiesPerSecond-style values.
