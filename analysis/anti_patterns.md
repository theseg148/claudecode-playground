# Anti-patterns from disliked, weak or reworked games and player complaints

Scope: all 47 `games/*.md` (the original 37 plus derivative-clicker, fallout-shelter, gnorp-apologue, idle-heroes, idle-loops, orb-of-creation, ordinal-markup, prestige-tree, shark-game, soda-dungeon; "What players hate" sections and lessons), `research/player_complaints.md` (C1-C12), `research/psychology.md`, `research/math_of_idle_games.md`, `sim/results.md`.

## Method and honesty notes
- The repo has no sales, uninstall or review-score data, so there is no proven "failed game". "Disliked/weak" here means: (a) the file records heavy complaints or reworks, (b) the file itself calls the game shallow, a clone or a weak reference, or (c) it is mobile-first with a monetisation-driven loop.
- **Weak/disliked reference set used for citations:** Clicker Heroes 2 (delays, prestige rework, bugs: `games/clicker-heroes-2.md`), Swamp Attack ("the weakest reference", not truly idle: `games/swamp-attack.md`), Guava Juice Tub Tapper (charted on brand; depth/retention unknown: `games/guava-juice-tub-tapper.md`), Idle Mining Empire (genre clone: `games/idle-mining-empire.md`), Mr. Mine, Farm Away, Idle Miner Tycoon, AFK Arena, Tap Titans 2, Cell to Singularity, Egg Inc, AdVenture Capitalist (heavy ad/IAP complaints), Magic Research, Reactor Incremental, Factory Idle.
- Evidence recount (tags in games/*.md): 326 code-read, 486 [S], 77 [PUB], 681 estimated. "What players hate" lists are still mostly [M]/[E]/[S]: after the verification passes the files for Mr. Mine, Farm Away, Idle Mining Empire, Magic Research, Factory Idle, Swamp Attack and Orb of Creation say their formulas/monetisation are unverified (Farm Away's and Idle Mining Empire's AdCap-style formulas belong to other games; Idle Mining Empire is a CrazyGames browser title, not a mobile F2P game, so its ad/IAP complaint is generic). Reactor Incremental is the only weak game with code-read numbers (the cwmonkey clone). Counts are therefore "as recorded in the files"; the 10 added games were tallied by hand from their "What players hate" and Monetization sections.
- `research/player_complaints.md` itself is built from ~25 search snippets and mirrors; its frequencies are qualitative judgment, not survey data.
- Denominators: 47 games unless stated (previous version: 37). Complaint ids C1-C12 refer to `research/player_complaints.md`.

## Anti-pattern table

| # | Anti-pattern | Games citing it | Complaint id |
|---|---|---|---|
| A1 | Grind walls / slow mid-game | ~34 of 47 (was ~30 of 37; +Gnorp, Fallout Shelter, Soda Dungeon, Prestige Tree) | C1 (VERY COMMON) |
| A2 | Ads, IAP, paywall, gacha pressure | 17 of 47 (14 of 15 mobile-first; was 14 of 37, 11 of 12) | C2, C3 |
| A3 | Opacity, complexity, UI sprawl, wiki dependence | 26 of 47 (was 20 of 37; +Gnorp, Ordinal Markup, Derivative Clicker, Prestige Tree, Idle Loops, Shark Game) | C9 (weak evidence), C5 |
| A4 | Not really idle: babysitting, chores, must keep client open | 14 of 47 (was 12 of 37; +Orb of Creation, Idle Loops) | C4 |
| A5 | No meaningful choice / shallow / clone | 13 of 47 (was 12 of 37; +Gnorp: only a few viable builds) | C5 |
| A6 | Prestige mistimed, underpaid or confusing | 18 of 47 (was 15 of 37; +Gnorp, Ordinal Markup, Soda Dungeon) | C6 |
| A7 | Offline progress missing, gated or inconvenient | 12 of 47 (was 10 of 37; CORRECTED: Idle Champions HAS offline progress, so it is removed from the list; +Derivative Clicker, Orb of Creation, Idle Heroes 8 h cap) | C7 |
| A8 | Balance churn, bugs, reworks, power creep | 12 of 47 (was 9 of 37; +Idle Heroes, Orb beta saves, Gnorp save changes) | C11 |
| A9 | Punitive failure states | 6 of 47 (was 4; +Fallout Shelter incidents, Gnorp run-bricking) | (no id) |
| A10 | Number inflation | 6 of 47 (was 3; +Ordinal Markup, Derivative Clicker, Prestige Tree) | C8 |
| A11 | Save loss | 4 of 47 (+ C11 review snippet; +Gnorp, Orb) | C11 |
| A12 | Fragmented economies, events that feel mandatory | 5 of 47 | C2/C3 |

## A1. Grind walls and slow mid-game (~30 of 37; C1)
- Files recording it (new in this refresh: Gnorp Apologue stalls after about two prestiges, Fallout Shelter late-game stagnation, Soda Dungeon grindy later floors, Prestige Tree hard walls without a new layer): AFK Arena (wall stages), AD (Break Infinity -> Eternity "long with little change"), ADR/Candy Box 2 (slow opening), Bitburner (RAM waits), Cell to Singularity (metabit grind), CH1 (zone walls), CC (slow chips), Egg Inc, Evolve, Factory Idle, Farm Away, Idle Breakout, Idle Miner Tycoon, Idle Mining Empire, Idle Slayer, Idle Wizard, Increlution, KG ("very long mid-game walls"), Leaf Blower, Magic Research, Melvor, Mr. Mine ("grindy mid-game and slow second prestige"), NGU, PK ("mid-game plateau"), RG, Swamp Attack, Synergism, Tap Titans 2, UP (quantum-chip waiting).
- Complaint file: NGU summaries "hundreds to thousands of hours", Slot Grind "devolves into a grind after a couple of hours".
- Sim: ratios rate_ratio > cost_ratio skip the early game; cost/rate ratio > 2 creates walls (max gap > 2 h); carry x2, cost x10 gives 8.4 -> 1047 min (`sim/results.md`, v1 toy). Campaign sim v3: with total carry about equal to cost scale (world drift d about 1.0) worlds are equal-length; leaving carry sources out of the budget collapses worlds, and long worlds without extra beats give dry-session streaks (18-day worlds: only 34 % of sessions had a goal). Cookie Clicker's own price/CPS ratio (1.4-2.9 per tier, from the CODE table) sits above the sim band and is offset by upgrades.
- Note: some players defend slow pacing as intentional (Steam CC thread, C1).

## A2. Monetisation friction (14 of 37; C2, C3)
- Games: AdCap (heavy ad/IAP), AFK Arena (gacha, pay walls), Cell to Singularity (ad nudges; premium currency is Darwinium), Idle Heroes (gacha, weekly subscription), Fallout Shelter (lunchboxes, rush risk), Soda Dungeon (ads on mobile), Egg Inc (ad volume, subscriptions, Pro Permit gating), Farm Away, Guava Juice (`[E]`), Idle Miner Tycoon ("ad and IAP pressure", event mines mandatory), Idle Mining Empire, Mr. Mine (gem paywalls), Swamp Attack ("grind-wall-to-sell-currency"), Tap Titans 2 (clan pay pressure), CH1 (rubies overpriced), Melvor (expansions as paywall), Synergism (paid convenience reads as pay-to-skip).
- Complaint file: "Excessive forced advertisement"; "Remove ads" that does not; ads play when the player declines; "Progression stalls on purpose to sell you the fix" (C2, C3 quotes).
- Mobile-first set (15): AdCap, AFK Arena, Cell to Singularity, Egg Inc, Farm Away, Guava Juice, Idle Miner Tycoon, Idle Mining Empire (caveat: the CrazyGames title is browser-only; mobile-tycoon features were unverified), Mr. Mine, Swamp Attack, Tap Titans 2, Idle Slayer, Idle Heroes, Fallout Shelter, Soda Dungeon. 14 of 15 carry this complaint (all but Idle Slayer); the other 3 of the 17 are CH1, Melvor (expansions) and Synergism (PCoin). Clicker Heroes 2 is a commercial case of its own: paid Early Access (16 July 2018), delisted 14 March 2024, no updates for a long time.
- Of the 12 clean beloved games in `analysis/beloved_patterns.md` B1, only Melvor has any monetisation complaint (expansion paywall).

## A3. Opacity, complexity and UI sprawl (20 of 37; C9, C5)
- Games: AD (late layers need the wiki), CH1 (spreadsheets), CH2 (4+ confusing layers), Evolve (micromanagement), KG (hidden formulas, tooltips clutter), Leaf Blower (the wiki needed a "No Gem Upgrade" guide), NGU ("Required wiki use"), RG ("new players cannot tell what upgrades do"), Synergism ("new players bounce by hour 3"), Trimps (spreadsheet UI, needs AutoTrimps), Tap Titans 2, Idle Champions, Idle Wizard, Factory Idle (late UI clutter), Reactor (spreadsheet late game), PK (opaque late unlocks), Increlution and Magic Research (thin docs), Idle Slayer (additive vs multiplicative confusion), CC (opaque ascension timing).
- Complaint file notes C9 evidence is weak (inferred); still the most repeated item in the game files.

## A4. Not really idle (12 of 37; C4)
- CC (click fatigue, must be present for golden cookies), Evolve, KG (job micromanagement), Synergism (babysitting early layers), UP (no offline, quantum-chip chore), AFK Arena and Egg Inc (daily chores), Idle Champions (client must stay open), CH1 (idle vs active burnout), Trimps (needs a bot), ADR/Candy Box 2 (fire-stoking tedium), Bitburner (programming literacy).
- Complaint quotes: "you MUST babysit the automation"; "a ton of busywork that's not exactly 'idle'" (C4).

## A5. Shallow choice, clones (12 of 37; C5)
- AdCap ("few active decisions once all managers are bought"), Candy Box 2 (grind), Factory Idle (bottleneck hunting repeats), Farm Away ("all upgrades are eventually bought"), Guava Juice (tap-and-upgrade shell), Idle Breakout, Idle Mining Empire ("little originality"), Mr. Mine ("just buy the next upgrade"), Swamp Attack (repetition within chapters), Increlution, PK (identical lives), Spaceplan (little replay).
- Lessons in the files say the same: Guava Juice lesson 1 "depth is what retains"; Idle Mining Empire lesson 7 "genre is saturated".

## A6. Prestige mistimed or underpaid (15 of 37; C6)
- Too much repeat for too little: AdCap ("planet resets feel like a restart of a simplified game with a few new numbers"), Cell to Singularity ("each reboot yields less relative gain"), CC ("a bad ascension feels wasted"), Idle Breakout, Idle Mining Empire, Mr. Mine ("slow second prestige"), Magic Research ("soft walls at the second prestige"), Factory Idle ("long reset cycles").
- Too confusing: CH1 (ascension mandatory), CH2 (rework, 4+ layers), KG, Leaf Blower (prestige vs Gold Leaf split), RG (reincarnation grind), Evolve (plasmid soft caps punish players who are behind), PK (Rebirth Two zeroes max-level multipliers).
- Sim support: only 23 of 108 prestige configs hit the satisfying band; threshold 1e6 is a tutorial reset, 1e10 pushes it past 90 min or never; 25%/pt bonus makes numbers outrun content (`sim/results.md`).
- Complaint file: "reset mechanics = laziness to create infinite progress"; first prestige at 25-35 min was too late in one postmortem (C6).

## A7. Offline problems (10 of 37; C7)
- None or gated: CC base game (offline needs the Twin Gates or Perfect idling upgrade; nothing without them `[CODE]`), PK, UP, Evolve (banked skip), ADR (state frozen), Candy Box 2, Idle Breakout, Reactor (clone replays ticks, no cap found), Increlution, Derivative Clicker (none found), Orb of Creation (prototype had no offline idling), Idle Heroes (8 h cap, 10 h per one review). **Idle Champions was removed from this list: the App Store text says champions keep fighting while the game is closed [S]; cap and rate unknown.**
- Other direction: "numbers when I come back are too big and I'm catching up instead of playing" (C7). Sim v1: offline efficiency 0 -> 0.25 speeds a casual player ~9x, 0.25 -> 1.0 only ~2x. Campaign sim v3 (Offline lever): no offline makes a 3-session/day world ~10x longer (26 d vs 2.5-3.2 d), stepped 50/25 % is only 13-28 % slower than flat 50 %, and an 8 -> 24 h cap matters only to players with gaps over 8 h.

## A8. Balance churn, bugs, reworks (9 of 37; C11)
- CH2 (delays, prestige rework, bugs), Cell to Singularity (lag, broken balance), AdCap (balance changes invalidate spreadsheets), RG (updates favour veterans), Egg Inc (updates invalidate strategies), Idle Champions (power creep, FOMO), Magic Research, Factory Idle (recipe patches), PK (forks with differing numbers).

## A9. Punitive failure states (4 of 37)
- Reactor meltdown wipes components; ADR exploration starvation/item loss; CC wrinklers/Grandmapocalypse; Evolve plasmid soft caps; Fallout Shelter incidents scale with room upgrades (a guide has to warn about it); Gnorp Apologue wrong investments can brick a run.
- Design counter-measure already recorded: soft failure (a heat meter that only throttles) in `games/reactor-incremental.md` lesson 2.

## A10-A12. Smaller items
- A10 Number inflation: Idle Miner Tycoon, Idle Mining Empire (e-notation quickly), Ordinal Markup (notation unreadable for non-mathematicians), Derivative Clicker (number blindness), Prestige Tree (huge numbers become meaningless), plus C8 quotes ("exponent gibberish with no sense of scale").
- A11 Save loss: PK (cache clears), Candy Box 2 (manual saves), Gnorp Apologue (save-size change; "Recover save" grants talent points), Orb of Creation (beta save incompatibility); C11 snippet (Farmer Against Potatoes rollback).
- A12 Fragmented economies/mandatory events: AdCap planets and events, Idle Miner Tycoon event mines, Idle Champions FOMO, Egg Inc contracts, Idle Mining Empire events.

## Sequential-world-specific failures (cross-reference)
- Skin-only new world: AdCap planets (A6), Swamp Attack repetition inside chapters.
- Carryover that trivialises the next world: sim "carry x2, cost x1: 8.4 -> 0.3 min"; in v3 terms, world drift d < 1 (carry sources such as Ride Cards, archived Seals and achievements left outside the budget: 27 d campaign became 12 d, an unbounded sqrt(archive) bonus 0.3 d per world).
- Walls between worlds: sim "cost x10"; in v3 terms d > 1.2 gives dry-session streaks of 5-7.
- Too many layers: CH2 4+, Synergism sprawl, NGU system count.
- Diluted older worlds: handled in CH2 by per-world prestige points so "prestige in World N doesn't dilute World N-1" `[EST]`.
- Mid-game lull between layers: AD Break Infinity -> Eternity.
- Full wipe with no carry: Ordinal Markup factor shift; confusing banked-progress semantics: Gnorp Apologue prestige bar.

## Cross-cutting findings
1. The loop is liked; the wrapper is hated (A2 vs `research/player_complaints.md` pattern 1).
2. Walls, mistimed prestige and offline gaps are one problem at three time scales (pattern 2): the player runs out of satisfying next actions.
3. Enthusiasts quit over choice and legibility (A3, A5, A10); casuals over ads/grind (A1, A2). A licensed-IP game sits nearer the casual side (pattern 4).
4. Trust items (A2, A11, ad-removal that does not remove ads) are one-star triggers (pattern 6).

## Implications for Kamen Rider Decade world-progression idle game
Aligned with DESIGN_RULES.md (R-numbers) and DECADE_IDLE_DESIGN.md.
1. **Never gate on a wall without a side option (A1; R9, R12, R25, R32).** Median gap between goals 30-60 s, 90th percentile at most 10 min, no gap over 30 min inside a session, nothing longer than a session without something to spend or decide. Rides alone give a new goal in only 55-73 % of sessions, so supply at least one further beat per session (mastery node, album entry, Photo Window reward, fusion discovery); worlds 4-6 each get a mid-world surprise (lull audit, AD Break Infinity -> Eternity is the counter-example). Cost/rate ratio 1.2-1.5, growth 1.12-1.15, x2 milestones.
2. **First ride in session 1 (A6; R10, R16, R19):** first purchase under 60 s, light automation about 3 min, first Final Form Ride about 8 min (T_w calibrated per world; 25-35 min is too late), then 9-11 rides per 3.2-day world, each at least 1.5x; no ride before at least 4 tiers have been bought. Replaces "20-45 min cycles" and "60 % of tiers".
3. **Ship ad-free (A2; R39).** Default: no monetisation at all (fan project, Toei IP exposure). If it ever became commercial: cosmetics only, never sell Seals/Ride Cards, time-skips only if they never gate a world (they act like offline efficiency on pacing), rewarded ads only as an opt-in bonus. Deterministic collection, no gacha (Idle Heroes, Fallout Shelter lunchboxes are the cautionary cases).
4. **Idle means idle (A4; R14):** auto-collect and auto-buy tier 1 early, full payback auto-buy in the first-ride shop (R21); active tools (Clock Up, Photo Op, Photo Windows) accelerate within the R34c budget (all together at most 1.5x in an active session) but are never required; no daily-streak loss.
5. **Do not clone tycoon structure (A5; R13, R13b, R26):** differentiator is sequential worlds with one new rule each and at most one extra system per world; a build fork in the first 5 minutes with at least two viable builds, slowest at most 25 % slower; avoid Gnorp-style run-bricking choices (respec costs mastery points but is never blocked).
6. **Prestige must feel like a gain (A6; R15-R18, R20, R24):** show pending gain and before/after production, never destroy the card collection, keep at most 3 layers (Final Form Ride, Dimension Ride, post-game All Riders). Seals = floor(sqrt(run_lifetime/T_w)), multiplier (1 + Seals)^0.5; the earlier "per-point bonus at most about 10 %" is replaced because a linear +8 %/seal explodes in the campaign (about 30 rides per world, multiplier 6e6). Show "banked / new / needed" explicitly (Gnorp lesson) and keep one item per reset (Ordinal Markup lesson).
7. **Offline (A7; R33, R35):** stepped 50 % first 2 h, 25 % beyond, cap 8 h (average about 0.31 for an 8 h gap), never 0 and never gated behind a late upgrade (CC complaint); offline production is existential, the cap a light-player upgrade; welcome-back card ignores absences under 1-2 minutes, offers 1-2 decisions and lists what happened.
8. **Legibility (A3, A10; R26, R40):** at most 3 visible currencies on the main screen, other systems on their own screens, formula breakdowns with additive vs multiplicative labelled, bulk-buy x1/x10/x max, named ranks and capped notation instead of e47; native doubles suffice (peak about 6.6e21).
9. **Soft failure only (A9; R42):** no world-clock penalty that destroys cards; no negative event outcomes.
10. **Trust (A11; R41):** autosave from day one, versioned export string, local+cloud dual save, versioned backups.
11. **Reduce balance churn (A8):** all constants in one file (Bitburner `Constants.ts`); worlds as data records (R27).
12. **Caveat and open items:** the "hate" lists are largely [M]/[E]/[S] and counts are hand tallies; re-verify with first-hand review sampling. Open: the sessions-per-day advantage (4.3x heavy vs light): a ride cooldown is a poor lever (24 h cooldown only 4.3x -> 2.9x and slows the 3/day player about 24 %, R34), so give heavy players optional content instead; gates must be calibrated with offline auto-spend on, which shortens worlds 26-44 % (R37), play-tested drift tolerance (R23), event spacing at real session lengths (R38b).
