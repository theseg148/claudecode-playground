# Incremental / Idle Game Design: Talks, Postmortems, Developer Interviews, and Usable Numbers

Companion to `math_of_idle_games.md` (formulas). This file collects talks, postmortems, interviews and design blog posts, then
extracts numeric design rules. Every claim has an inline source URL.

## 0. Provenance and confidence (read first)

- In this research session the egress proxy blocked nearly every site except GitHub (gamedeveloper.com, gdcvault.com, slideshare.net, wikipedia.org, fandom wikis, medium.com,
  substack.com and others returned connection refusals). Web search worked and returned page excerpts, so most entries below are **search-excerpt-level**, not full reads.
- Confidence tags: **[CODE]** = read directly from public source on GitHub (highest); **[EXCERPT]** = from a search-engine excerpt of the cited page; **[SECONDARY]** = a blog or vendor
  article that is itself summarising something else; **[DERIVED]** = my own arithmetic on cited numbers.
- Where a number comes from a single blogger or vendor, I say so. Treat those as starting points to be playtested, not industry standards.
- Verification backlog is listed in section 9.

---

## 1. Inventory of talks, articles and postmortems

| # | Item | Who / where | URL | Status |
|---|---|---|---|---|
| 1 | Idle Games: The Mechanics and Monetization of Self-Playing Games (GDC 2015, F2P Summit) | Anthony Pecorella, Kongregate | https://www.gdcvault.com/play/1022065/Idle-Games-The-Mechanics-and ; slides https://www.slideshare.net/slideshow/idle-games-gdc2015final/45563367 ; video https://www.youtube.com/watch?v=Lu-RjxeDpU8 ; archive https://archive.org/details/GDC2015Pecorella | excerpt |
| 2 | Idle Chatter: What We Can Learn From Self-Playing Games (GDC 2016) | Pecorella | https://kongregatedev.ghost.io/idle-chatter-gdc-2016/ ; https://www.slideshare.net/slideshow/idle-chatter-gdc-2016-59734260/59734260 | excerpt |
| 3 | Quest for Progress: The Math and Design of Idle Games (GDC Europe 2016) | Pecorella | https://www.gdcvault.com/play/1023876/Quest-for-Progress-The-Math ; https://media.gdcvault.com/gdceurope2016/presentations/Pecorella_Anthony_Quest%20for%20Progress.pdf | excerpt |
| 4 | The Math of Idle Games, Parts I-III | Pecorella | https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i (II, III similarly) | excerpt (see math file) |
| 5 | The Rise and Rise of Idle Games | Kongregate/Pecorella deck | https://www.slideshare.net/slideshow/the-rise-and-rise-of-idle-games-68916528/68916528 | listed only |
| 6 | Making a Hit Idle Game: Eight Lessons from Kolibri Games | Kolibri (Idle Miner Tycoon), GameAnalytics | https://www.gameanalytics.com/blog/making-a-hit-idle-game-eight-lessons-from-kolibri-games | excerpt |
| 7 | What we learned: Idle Miner Tycoon and Idle Factory Tycoon | Kolibri talk | https://www.youtube.com/watch?v=9VlkPFF02c4 ; https://www.slideshare.net/slideshow/what-we-learned-idle-miner-tycoon-and-idle-factory-tycoon-kolibri/182846509 | listed only |
| 8 | How Kolibri went from MVP to 70 million installs | PocketGamer.biz | https://www.pocketgamer.biz/how-kolibri-went-from-minimal-viable-product-to-70-million-installs-for-its-idle-games/ | listed only |
| 9 | Balancing Tips: How We Managed Math on Idle Idol | Idle Idol devs, Game Developer | https://www.gamedeveloper.com/design/balancing-tips-how-we-managed-math-on-idle-idol | excerpt |
| 10 | Interview with Hevipelle, creator of Antimatter Dimensions | Incremental DB | https://www.incrementaldb.com/community/interview/31 | excerpt |
| 11 | The State of Clicker Heroes 2 (postmortem-style) | Playsaurus | https://playsaurus.com/blog/index.php/2021/06/28/the-state-of-clicker-heroes-2/ | opening + secondary review |
| 12 | The Evolution of Clicker Heroes: Interview with Playsaurus | Clicker Heroes blog | https://blog.clickerheroes.com/the-evolution-and-success-of-clicker-heroes-interview-with-playsaurus/ | excerpt |
| 13 | Idle Game Design Principles | Eric Guan | https://ericguan.substack.com/p/idle-game-design-principles | opening only |
| 14 | Lessons of my first incremental game | Game Developer | https://www.gamedeveloper.com/design/lessons-of-my-first-incremental-game | listed only |
| 15 | Universal Paperclips design commentary | Frank Lantz | http://www.franklantz.net/universal-paperclips/ ; https://www.hey.gg/blog/frank-lantz | excerpt |
| 16 | Orteil / Cookie Clicker interviews (Waypoint via Vice, Polygon) | Orteil | https://www.vice.com/en/article/cookie-clicker-wasnt-meant-to-be-fun-why-is-it-so-popular-8-years-later/ | excerpt |
| 17 | How to Design an Idle Game: Formulas From 4 Shipped Games | Onirealms | https://onirealms.com/guides/how-to-design-an-idle-game/ ; https://onirealms.com/guides/prestige-rebirth-ascension-explained/ | excerpt |
| 18 | Player Engagement with Idle Games (academic) | eScholarship | https://escholarship.org/content/qt0b07v51w/qt0b07v51w.pdf | listed only |
| 19 | Playing to Wait (academic, CHI 2018) | ACM | https://dl.acm.org/doi/10.1145/3173574.3174195 | listed only |
| 20 | Idle game design blog posts: bugnet, GridInc, kastark, DEV Community, game-ace | various | see section 7 | excerpt |

---

## 2. Anthony Pecorella (Kongregate): what the three talks add beyond the articles

### 2.1 GDC 2015: core and meta loops
- Abstract framing: examine the core and metagame loops of idle games and why they retain players so well. Source: https://www.gdcvault.com/play/1022065/Idle-Games-The-Mechanics-and [EXCERPT].
- Slide claim: idle games were among the best-retaining games on Kongregate.com with ARPU "well above" most single-player games on the site; a Game Developer write-up repeats that they were
  some of the most-played games on the site in 2015. Sources: https://www.slideshare.net/slideshow/idle-games-gdc2015final/45563367 and https://www.gamedeveloper.com/business/video-the-mechanics-and-monetization-of-self-playing-games [EXCERPT].
  Exact retention percentages were not retrievable; see section 7 for third-party benchmark bands.

### 2.2 GDC 2016 "Idle Chatter": design lessons
From the excerpt of https://kongregatedev.ghost.io/idle-chatter-gdc-2016/ and the SlideShare deck https://www.slideshare.net/slideshow/idle-chatter-gdc-2016-59734260/59734260 [EXCERPT]:
1. Progress without interaction: offline progress gives a reward on every return, so forced appointment mechanics (energy timers) become unnecessary.
2. Rising costs act as a natural energy system: the player accepts waiting because "I will have more later".
3. Prestige is a strategic reset that lets the designer rein in growth.
4. "Make it bumpy": smooth curves feel flat; add surprise and delight moments (random events, golden-cookie-style spawns).
5. The deck is 127 slides and covers how the genre grew and expanded in a year.

### 2.3 GDC Europe 2016 "Quest for Progress": the math deck
From https://media.gdcvault.com/gdceurope2016/presentations/Pecorella_Anthony_Quest%20for%20Progress.pdf [EXCERPT]:
- Standard model: exponential costs against linear/polynomial production; `x^k` is never exponential and `k^x` always wins eventually.
- "What if generators produced generators?" derivative model with the Taylor series of `e^x` (Part II material).
- Prestige currency typically grows at a lower order of magnitude than primary currency; prestiges can be nested.
- Reset rule of thumb (as excerpted): reset when you would gain roughly +50% to +200% prestige currency. Cited by third-party summaries (https://bugnet.io/blog/how-to-design-an-idle-or-incremental-game, via search excerpt).
- Worksheets (CC BY 4.0) with formulas and iterative models of idle progression systems: https://archive.org/details/idlegameworksheets .

---

## 3. Game-by-game design notes

### 3.1 Antimatter Dimensions (Hevipelle) 
- Design lineage: Hevipelle wanted a game he himself would play; he liked the polynomial growth of Derivative Clicker, took layered prestige from Realm Grinder, automation from Transport Defender and challenges from Idle Wizard.
  Source: https://www.incrementaldb.com/community/interview/31 [EXCERPT].
- Structure: dimensions feeding dimensions, then Infinity (1.79e308 antimatter), then Eternity, then Reality; a review notes the first act's tightness does not survive intact into later layers.
  Source: https://playwanderer.online/game-reviews/antimatter-dimensions [EXCERPT].
- Community-estimated pacing (not developer-stated): first Infinity a few hours to ~2 days; first Eternity ~2 days to a week; first Reality a week to a month; completion 1-3 months.
  Sources: https://antimatter-dimensions.fandom.com/wiki/Guide ; https://antimatter-dimensions.fandom.com/wiki/BubbaCow%27s_Antimatter_Dimensions_Guide [EXCERPT].
- Hard numbers from source code [CODE] (https://github.com/IvarK/AntimatterDimensionsSourceCode):
  - Dimension base costs 10, 100, 1e4, 1e6, 1e9, 1e13, 1e18, 1e24; per-batch cost multipliers 1e3, 1e4, 1e5, 1e6, 1e8, 1e10, 1e12, 1e15 (src/core/dimensions/antimatter-dimension.js).
  - x2 output per 10 purchases of a dimension ("buy ten multiplier").
  - Tickspeed: base cost 1000, x10 per purchase (src/core/tickspeed.js); each upgrade speeds ticks by 1/0.8 (=1.25x) after 3 galaxies, 1/1.1245 with none.
  - Galaxy requirement `80 + 60n` 8th dimensions (src/core/galaxy.js); dimension boost requirement starts at 20 and adds 15 per boost for the 8th tier (src/core/dimboost.js).
  - IP: `10^(log10(antimatter)/308 - 0.75)`; EP: `5^(log10(IP)/308 - 0.7)` (src/game.js).
  - [DERIVED] Each prestige layer is "308 orders of magnitude wide", the same distance as the mandatory wall; the pacing consistency, not the specific constants, is the design.
- Source repo carries the whole game's content: https://github.com/IvarK/AntimatterDimensionsSourceCode . The README says run with `npm ci` and `npm run serve`.

### 3.2 Cookie Clicker (Orteil)
- Origin: created 8 August 2013, a second version on a new URL by 24 August (the first became "Classic"). Source: https://cookieclicker.fandom.com/wiki/Cookie_Clicker [EXCERPT].
- Orteil's stated philosophy: the game's satirical reading was "accidental"; "if it's fun and people enjoy it, that's kind of enough". Source: https://www.vice.com/en/article/cookie-clicker-wasnt-meant-to-be-fun-why-is-it-so-popular-8-years-later/ [EXCERPT].
- Warning: pages claiming Orteil "invented prestige" or giving "exclusive" quotes (cookie-clicker2.org, playcookieclicker.com) could not be corroborated; do not cite them. Noted in the same search result.
- Numbers: building price `ceil(base * 1.15^(owned - free))`, price doubles about every 5 buildings; Classic used 1.1. Source: https://cookieclicker.wiki.gg/wiki/Buildings and https://cookieclicker.wiki.gg/wiki/Building_(Cookie_Clicker_Classic) [EXCERPT].
- Prestige: chips = floor(cbrt(cookies / 1e12)); +1% CpS per prestige level; needs 1e12 * M^3 cookies for M chips. Source: https://cookieclicker.fandom.com/wiki/Heavenly_Chips [EXCERPT].
- Design role of random events: Golden Cookies reward active play; one player reports 3-4 hours a day watching for them (Vice link above). Buff stacking can reach very large clicking multipliers (Frenzy x7 with Click Frenzy x777 = x5,439) per https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md [SECONDARY].
- Offline: ~2 hours is cited for Cookie Clicker context in a Part III summary; unverified.

### 3.3 Clicker Heroes (Playsaurus)
- Origin: heavily influenced by Cookie Clicker; the founders (Fragsworth, Doogog, with CEO Austin Oblouk) re-skinned the idle loop as an RPG; the studio was a three-person operation near folding and shipped quickly to experiment.
  Source: https://blog.clickerheroes.com/the-evolution-and-success-of-clicker-heroes-interview-with-playsaurus/ [EXCERPT].
- Balance is the hardest part of making idle games and player feedback set the pace: https://www.coolmathgames.com/blog/discover-the-dev-playsaurus [EXCERPT].
- Numbers: hero cost uses 1.07 growth; x4 DPS per 25 hero levels from level 200; x10 at 1000, 2000 ... 8000. Source: https://clickerheroes.fandom.com/wiki/Formulas [EXCERPT, community wiki].
- Ascension: Hero Souls `floor(pow(((level-100)/5+4)/5, 1.3) * bonus)`; +10% DPS per soul; first ascension advised at zone 100 minimum, zone 130 ideal (official blog). Sources: https://clickerheroes.fandom.com/wiki/Hero_Souls ; https://blog.clickerheroes.com/ascension-in-clicker-heroes-the-ultimate-guide/ ; https://www.coolmathgames.com/clicker-heroes-tips-tricks-guide [EXCERPT].
- Primal bosses every 10 zones from 100 give extra souls (blog above), an example of a "reward cliff" placed at the reset decision point.
- Transcendence (second layer): Ancient Souls = floor(5 * log10(total hero souls)). Source: https://blog.clickerheroes.com/clicker-heroes-ancient-souls-master-the-ultimate-currency/ [EXCERPT, single-source].
- Clicker Heroes 2 postmortem ("The State of Clicker Heroes 2", June 2021): the team is unhappy with the state of the game and lists mistakes. A 2026 review summarises four: staying on Flash too long, mechanics drifting from what made the original work, an Early Access launch with only a few days of content, and charging for a sequel to a free game. The game was removed from sale in March 2024.
  Sources: https://playsaurus.com/blog/index.php/2021/06/28/the-state-of-clicker-heroes-2/ ; https://playwanderer.online/game-reviews/clicker-heroes-2 [EXCERPT / SECONDARY].
  Lesson: the sequel failed through scope growth and drift from the core loop, not through math.

### 3.4 Egg, Inc. (Auxbrain)
- Prestige: sends the player back to the first egg, keeps golden eggs, soul eggs, eggs of prophecy, epic research. Source: https://en.wikipedia.org/wiki/Egg,_Inc. [EXCERPT].
- Official FAQ: soul eggs get "continuously more difficult" to earn (the prestige counter is non-linear). Source: https://auxbrain.freshdesk.com/support/solutions/folders/47000774544 .
- Bonus per soul egg base 10%; Soul Food research +1 percentage point per level (24% at level 14, max 150% total per one guide); prophecy-egg bonus compounds 5-10%.
  Sources: https://egg-inc.fandom.com/wiki/Earnings_Bonus/Soul_Eggs ; https://jzr.uz/blog/egg-inc-mystical-eggs-math ; https://tap-guides.com/2025/10/24/egg-inc-prestige-soul-eggs-guide/ [SECONDARY].
- Gain formula per Pecorella Part III: `(c_R / 1e6)^0.14` (earnings since reset); a community approximation uses farm value^0.21.
  Sources: https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii ; https://everycalculators.com/egg-inc-prestige-calculator.html [EXCERPT/SECONDARY].
- Guide timing thresholds (old, opinion): wait for ~50+ soul eggs, or "a few hundred" is efficient, or prestige as soon as progress slows. Sources: tap-guides link above; https://www.touchtapplay.com/egg-inc-how-to-prestige/ [SECONDARY].
- Egg, Inc. design relevance: because gain is based on since-reset earnings with a tiny exponent, the "how long do I run" decision is flattened, which discourages marathon runs.

### 3.5 AdVenture Capitalist
- See math file tables. Angels: +2% each; 150*sqrt(lifetime/1e15); heuristic "reset when pending angels >= current". Sources: https://adventure-capitalist.fandom.com/wiki/Angel_Investors ; https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md [EXCERPT/SECONDARY].
- Angel spending thresholds (community guide): <=20% of angels for x2, 30% for x3, 40% for x4, 50% for x5-x9, 60% for x10+. Source: https://adventure-capitalist.fandom.com/wiki/Angel_Upgrades [EXCERPT].
- Pecorella notes later layering to rein in numbers ("Mega Bucks") in Part III: https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii [EXCERPT].

### 3.6 Realm Grinder (Divine Games)
- Layers: Abdication (basic reset), Reincarnation (gems), Ascension. Reincarnation can be done when enough gems are acquired and loses gems for extra bonuses and a free Reincarnation Power upgrade.
  Source: https://realm-grinder.fandom.com/wiki/Reincarnation ; https://en.wikipedia.org/wiki/Incremental_game [EXCERPT].
- Formula (Part III): `p = (sqrt(1 + 8 c_M / 1e12) - 1)/2` on max currency; doubling needs 4x earnings; resetting at the same point earns nothing new. Source: https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii [EXCERPT].
- Divine Games is known for developer diaries and frequent updates; started on Kongregate in May 2015. Source: https://www.divinegames.it/discuss/viewtopic.php?id=395 [EXCERPT]. No formal postmortem was found.

### 3.7 Kittens Game (bloodrizer / nuclear-unicorn) [CODE]
Source: https://github.com/nuclear-unicorn/kittensgame
- priceRatio distribution across js/buildings.js, space.js, etc.: 49 entries at 1.15; the rest at 1.10, 1.12, 1.18, 1.25, 1.35, 1.5, 1.75, 2, 2.5.
  Examples: field 1.12, mine 1.15, barn 1.75, hut 2.5 (js/buildings.js).
- Bulk cost: `resPrice * (priceRatio^num - 1)/(priceRatio - 1)` (game.js).
- Paragon: +1% production each, capped by a diminishing-returns limiter; +10% storage per 100 paragon (js/prestige.js).
- The repository also holds `combat-balance.md`, a developer balancing document (not read in full): https://github.com/nuclear-unicorn/kittensgame/blob/master/combat-balance.md .

### 3.8 Universal Paperclips (Frank Lantz)
- Deliberately short: a full playthrough about 4-6 hours (author's own site), an "intense thing you do" rather than a long hobby game.
  Sources: http://www.franklantz.net/universal-paperclips/ ; https://www.hey.gg/blog/frank-lantz [EXCERPT].
- Pacing lesson: escalate the stakes gradually; end-state planned so the player can disengage.

### 3.9 Idle Idol (balancing postmortem)
- Problem statement: costs grow exponentially, rewards linearly; their chart had costs pass rewards at ~level 35.
- Start value 1.1 growth for both cost and reward (11%-19% increase from prior level); exponent tweaks are extremely sensitive.
  Source: https://www.gamedeveloper.com/design/balancing-tips-how-we-managed-math-on-idle-idol [EXCERPT].

### 3.10 Kolibri Games (Idle Miner Tycoon, Idle Factory Tycoon)
- Prototype with no 3D art, IAP, social, localization, ad mediation, long-term motivation or cloud saves reached 63%-81% D1 retention vs ~40% typical.
  Source: https://www.gameanalytics.com/blog/making-a-hit-idle-game-eight-lessons-from-kolibri-games [EXCERPT].
- Idle Miner Tycoon released July 2016 after eight weeks of development. Source: https://en.wikipedia.org/wiki/Kolibri_Games [EXCERPT].
- 70 million installs across idle titles reported by PocketGamer.biz (title only): https://www.pocketgamer.biz/how-kolibri-went-from-minimal-viable-product-to-70-million-installs-for-its-idle-games/

---

## 4. Numeric design rules extracted

### 4.1 Cost multipliers
| Rule | Value | Evidence |
|---|---|---|
| Standard production generator | 1.07-1.15 per owned | AdCap tiers 1.07-1.15 (https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md), Cookie Clicker 1.15, Clicker Heroes 1.07 (links in 3.2, 3.3) |
| Beginner-friendly default | 1.10-1.15 | Idle Idol 1.1; kastark sample `10 * 1.1^n` (https://kastark.co.uk/articles/incrementals.html [EXCERPT]) |
| Late-level flattening | 14% -> 12.5% -> 11.5% | Idle Ronin via https://onirealms.com/guides/how-to-design-an-idle-game/ |
| Capacity/housing structures | 1.75-2.5 | Kittens Game [CODE] |
| Production structures in Kittens | 1.12-1.15 | Kittens Game [CODE] |
| Tier-to-tier base cost | x12 (AdCap), x10 to x1e15 (AD) | math file section 5 and 4 |
| Upgrade (not generator) price | steeper: x3 to x10 per step | Antimatter Dimensions tickspeed x10 [CODE]; Cookie Clicker upgrade tiers (not sourced) |

### 4.2 Milestone multipliers
| Game | Rule | Source |
|---|---|---|
| AdCap | thresholds 25, 50, 100, 200, 300, ... 1100 owned; multipliers x2 up to x11-ish; global x3 at 100 of everything | https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md [SECONDARY] |
| Antimatter Dimensions | x2 per 10 bought of that dimension | [CODE] |
| Clicker Heroes | x4 per 25 hero levels from 200; x10 at 1000, 2000..8000 | https://clickerheroes.fandom.com/wiki/Formulas |
| Cookie Clicker | buildings have upgrade tiers at ownership counts (1, 5, 25, 50, 100...); not verified here | n/a |
- [DERIVED] With r = 1.07-1.15, 10-25 purchases raise a generator's price ~2x-33x. A x2 milestone every ~10 purchases at r=1.07 (price x1.97) or every ~5 at r=1.15 (price x2.01)
  keeps per-currency efficiency constant; a x4-x5 per 25 purchases (Clicker Heroes) compensates a price rise of x5.4 at r=1.07.
  Design formula: choose milestone multiplier M and spacing S so that `M ~ r^S`.

### 4.3 Pacing targets (first session onward)
Single-author rules of thumb, not standards:
- First purchase within ~60 seconds; first automation within ~3 minutes; first prestige around 10-15 minutes; a visible leap every few minutes.
  Sources: https://bugnet.io/blog/how-to-design-an-idle-or-incremental-game and https://dev.to/aguier/i-built-7-idle-games-in-30-days-what-i-learned-about-incremental-design-5d3f [SECONDARY, flagged as one builder's heuristics].
- First session active play 15-60 minutes for new players, shrinking over time (reengagement frequency). Source: https://ericguan.substack.com/p/idle-game-design-principles [EXCERPT].
- Stagger complexity: hook in first 30 minutes, daily habit, then long-term depth; add one variable (currency, automation, prestige) at a time. Source: https://gridinc.co.za/blog/idle-games-best-practices [EXCERPT].
- Prestige second run should feel "visibly faster" in the first 30 seconds; well-tuned prestige gives about 2x-4x faster second run. Sources: bugnet link above, https://onirealms.com/guides/how-to-design-an-idle-game/ [SECONDARY].
- Long-form games: Antimatter Dimensions first Infinity hours, first Eternity days, first Reality 1-4 weeks (community, see 3.1). Short-form: Universal Paperclips 4-6 hours total (3.8).
- Retention bands for healthy soft-launch idle titles: D1 35-45%, D7 15-20%, D30 5-10% (vendor blog, single source): https://game-ace.com/blog/idle-game-development/ ; Kolibri prototype D1 63-81% (3.10).

### 4.4 Prestige timing rules
- Reset when gain >= +50% to +200% of current prestige currency (Pecorella slides, via https://bugnet.io/blog/how-to-design-an-idle-or-incremental-game).
- Reset when progress falls to ~10-20% of peak speed, or when the next milestone takes longer than re-reaching it with new bonuses (https://gridinc.co.za/blog/idle-games-best-practices [SECONDARY, unverified]).
- Do not prestige exactly at 100%/the first moment possible; wait until growth slows drastically (Exponential Idle guide cited in a search result for https://exponential-idle-guides.netlify.app/guides/1-ee2k/).
- Make the first prestige early and clearly worthwhile; show a preview. A vendor case study reports a drop-off before the prestige unlock fixed by a tooltip/animated preview, +19% retention past D7 (vendor claim; treat with caution). Source: bugnet link above.
- Cliff awareness: players time resets just before reward jumps (Idle Ronin stage 200; Clicker Heroes primal bosses every 10 zones from 100). Sources: onirealms link; Clicker Heroes blog link.
- Doubling multiples to model: sqrt formulas need 4x earnings, cbrt 8x, exponent 1/7 needs 128x (math file section 3.1).
- Failure mode: an income-doubling upgrade that scales too fast made a prestige loop reach endgame after only 3 prestige points; fix by lowering the multiplier effect and re-gating unlocks.
  Source: https://itch.io/t/5446445/feedback-prestige-loop-accelerates-to-endgame-levels-at-3-prestige-points [EXCERPT].

### 4.5 Offline progression numbers
- Caps in the wild: Idle Ronin 8 h; Idle AI Factory starts at 2 h and research raises it to 8 h; Idle Summoner welcome-back up to 24 h; general guidance 2-24 h.
  Source: summary in https://games.themindstudios.com/post/idle-clicker-game-design-and-monetization/ and the Onirealms guide (search excerpts; the specific per-game numbers appeared in a result for the query on offline caps).
- Implementation bugs to avoid: measure from saved quit timestamp (not "last resumed"), cap the window, clamp rate so boosters cannot create windfalls (Idle AI Factory postmortem, https://onirealms.com/guides/how-to-design-an-idle-game/).
- Reduced offline rate (e.g. 50%) keeps closing the app rewarding without making active play pointless. Source: https://lkowalskil.github.io/offline-idle-dungeon-game-android.html [SECONDARY].
- Ignore very short absences so app-switching does not show a reward screen (same sources).
- Formula: `offline = rate * min(elapsed, cap) * offline_multiplier` (https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md section 1.11).

### 4.6 Big-number engineering
- A 32-bit float overflowed and froze progress around stage 1000 in Idle Ronin/Idle AI Factory. Source: Onirealms guide above.
- Antimatter Dimensions stores quantities as Decimals and compares `log10`; its prestige formulas are linear in `log10`. [CODE] https://github.com/IvarK/AntimatterDimensionsSourceCode
- Use log-space or a Decimal library once a game passes 1e308.

---

## 5. Cross-cutting patterns across games

1. Mandatory first wall, optional later walls: AD forces the first reset at 1.79e308; AdCap, Cookie Clicker and Egg Inc make the first reset a player decision.
2. Layered resets reset the *meaning* of the previous layer (Realm Grinder abdicate -> reincarnate -> ascend; AD infinity -> eternity -> reality; Clicker Heroes ascend -> transcend).
   Sources: https://en.wikipedia.org/wiki/Incremental_game ; https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md section 1.3.
3. Cost growth shrinks as the tier price grows (AdCap), or as level grows (Idle Ronin), so late steps remain affordable.
4. Multiplier gates at fixed counts convert linear purchase counts into exponential production (all of AdCap, AD, Clicker Heroes).
5. Prestige currency exponents: 1/2 (AdCap, Realm Grinder), 1/3 (Cookie Clicker), 0.14 (Egg Inc), log-of-log (AD).
6. Active-play bonuses (Golden Cookies, Click Frenzy, Clicker Heroes clicks) are layered over idle income, with automation added progressively (AD automation from Transport Defender). 
7. Sequels and rebuilds are the biggest risk: Clicker Heroes 2 lost a decade of goodwill by drifting from the core loop (3.3).

---

## 6. Practical blueprint (synthesised, [DERIVED] from the above)

Starting parameters for a new incremental prototype:
- 8-10 generators; base cost ratio ~x12 per tier (AdCap) or x10-x1000 with batch multipliers (AD); cost growth r from 1.15 (tier 1-2) down to 1.07 (top tier).
- Milestones at 25/50/100/200/300 owned giving x2/x2/x3/x2/x2; check `M ~ r^S` consistency.
- Prestige: `gain = floor(k * sqrt(lifetime / T))` with T set to the earnings reached by minute 10-15 (first-prestige target) and bonus per point 1-2% so the second run beats the first by 2x-4x.
- Show pending prestige gain from the first moment it is >= 1; highlight when pending >= 50-100% of current.
- Offline cap 2h at the start, upgrade to 8h; offline rate 50%-100%.
- Second prestige layer once the first needs ~4^6 (4,096x) earnings, or when numbers approach 1e30-1e50 [DERIVED guideline: Pecorella notes later layers "rein in numbers"].
- Add "bumpy" events (random golden-style spawns) every few minutes of active play.

---

## 7. Other design blog posts (summaries, single-source unless noted)

- Reengagement clocks (Eric Guan): producers on timers (cheese every 30 min; 5-hour storage fill then stall) create return appointments. https://ericguan.substack.com/p/idle-game-design-principles [EXCERPT]
- Layered progression: keep introducing new currencies/prestiges/mechanics; one number climbing forever runs out of steam. Search summary for https://bugnet.io/blog/how-to-design-an-idle-or-incremental-game and https://dev.to/aguier/i-built-7-idle-games-in-30-days-what-i-learned-about-incremental-design-5d3f
- Percentage multipliers compound; a x2 multiplier can beat doubling the generator count (Steam discussion, unreliable).
- Currency economy: sources outpacing sinks -> inflation. https://dev.to/sam_novak_574b07811e18495/idle-game-economy-design-what-your-currency-sinks-actually-eat-1non [EXCERPT]
- Cost-scaling postmortem: late-game costs jumping 10x created a wall fixed by reworking scaling. (From the kastark search result.)
- Academic: "Playing to Wait" https://dl.acm.org/doi/10.1145/3173574.3174195 and "Player Engagement with Idle Games" https://escholarship.org/content/qt0b07v51w/qt0b07v51w.pdf were listed but not read.

---

## 8. Monetisation figures that touch design
- 62% of idle revenue from IAP, 38% from ads; paying players 2.6x lifetime value (secondary file; unattributed): https://github.com/ac2522/IdleFramework/blob/main/IDLE_GAME_MECHANICS_RESEARCH.md section 1.12.
- Typical ad boost: 2-4 hours of x2 production (same file). Permanent multipliers x2, x3, x5 as IAPs.

## 9. Verification backlog
1. Read the Quest for Progress PDF and confirm the +50%-200% reset rule and any pacing targets.
2. Read Kolibri's eight lessons in full (https://www.gameanalytics.com/blog/making-a-hit-idle-game-eight-lessons-from-kolibri-games).
3. Read the incrementaldb interview with Hevipelle for first-hand statements on pacing.
4. Read the Playsaurus CH2 post (https://playsaurus.com/blog/index.php/2021/06/28/the-state-of-clicker-heroes-2/) to confirm the four mistakes.
5. Confirm AdCap milestone table and the Egg Inc gain exponent against primary sources.
6. Locate Cookie Clicker's upgrade-tier thresholds; they were not retrievable here.
