# Anti-patterns from disliked, weak or reworked games and player complaints

Scope: all 37 `games/*.md` ("What players hate" sections and lessons), `research/player_complaints.md` (C1-C12), `research/psychology.md`, `research/math_of_idle_games.md`, `sim/results.md`.

## Method and honesty notes
- The repo has no sales, uninstall or review-score data, so there is no proven "failed game". "Disliked/weak" here means: (a) the file records heavy complaints or reworks, (b) the file itself calls the game shallow, a clone or a weak reference, or (c) it is mobile-first with a monetisation-driven loop.
- **Weak/disliked reference set used for citations:** Clicker Heroes 2 (delays, prestige rework, bugs: `games/clicker-heroes-2.md`), Swamp Attack ("the weakest reference", not truly idle: `games/swamp-attack.md`), Guava Juice Tub Tapper (charted on brand; depth/retention unknown: `games/guava-juice-tub-tapper.md`), Idle Mining Empire (genre clone: `games/idle-mining-empire.md`), Mr. Mine, Farm Away, Idle Miner Tycoon, AFK Arena, Tap Titans 2, Cell to Singularity, Egg Inc, AdVenture Capitalist (heavy ad/IAP complaints), Magic Research, Reactor Incremental, Factory Idle.
- Many files are `[M]/[E]` only (Mr. Mine, Farm Away, Idle Mining Empire, Magic Research, Factory Idle, Reactor, Swamp Attack are "LOW confidence"; their "hate" lists are estimates). Counts are therefore "as recorded in the files".
- `research/player_complaints.md` itself is built from ~25 search snippets and mirrors; its frequencies are qualitative judgment, not survey data.
- Denominators: 37 games unless stated. Complaint ids C1-C12 refer to `research/player_complaints.md`.

## Anti-pattern table

| # | Anti-pattern | Games citing it | Complaint id |
|---|---|---|---|
| A1 | Grind walls / slow mid-game | ~30 of 37 | C1 (VERY COMMON) |
| A2 | Ads, IAP, paywall, gacha pressure | 14 of 37 (11 of 12 mobile-first) | C2, C3 |
| A3 | Opacity, complexity, UI sprawl, wiki dependence | 20 of 37 | C9 (weak evidence), C5 |
| A4 | Not really idle: babysitting, chores, must keep client open | 12 of 37 | C4 |
| A5 | No meaningful choice / shallow / clone | 12 of 37 | C5 |
| A6 | Prestige mistimed, underpaid or confusing | 15 of 37 | C6 |
| A7 | Offline progress missing, gated or inconvenient | 10 of 37 | C7 |
| A8 | Balance churn, bugs, reworks, power creep | 9 of 37 | C11 |
| A9 | Punitive failure states | 4 of 37 | (no id) |
| A10 | Number inflation | 3 of 37 | C8 |
| A11 | Save loss | 2 of 37 (+ C11 review snippet) | C11 |
| A12 | Fragmented economies, events that feel mandatory | 5 of 37 | C2/C3 |

## A1. Grind walls and slow mid-game (~30 of 37; C1)
- Files recording it: AFK Arena (wall stages), AD (Break Infinity -> Eternity "long with little change"), ADR/Candy Box 2 (slow opening), Bitburner (RAM waits), Cell to Singularity (metabit grind), CH1 (zone walls), CC (slow chips), Egg Inc, Evolve, Factory Idle, Farm Away, Idle Breakout, Idle Miner Tycoon, Idle Mining Empire, Idle Slayer, Idle Wizard, Increlution, KG ("very long mid-game walls"), Leaf Blower, Magic Research, Melvor, Mr. Mine ("grindy mid-game and slow second prestige"), NGU, PK ("mid-game plateau"), RG, Swamp Attack, Synergism, Tap Titans 2, UP (quantum-chip waiting).
- Complaint file: NGU summaries "hundreds to thousands of hours", Slot Grind "devolves into a grind after a couple of hours".
- Sim: ratios rate_ratio > cost_ratio skip the early game; cost/rate ratio > 2 creates walls (max gap > 2 h); carry x2, cost x10 gives 8.4 -> 1047 min (`sim/results.md`).
- Note: some players defend slow pacing as intentional (Steam CC thread, C1).

## A2. Monetisation friction (14 of 37; C2, C3)
- Games: AdCap (heavy ad/IAP), AFK Arena (gacha, pay walls), Cell to Singularity (ad nudges), Egg Inc (ad volume, subscriptions, Pro Permit gating), Farm Away, Guava Juice (`[E]`), Idle Miner Tycoon ("ad and IAP pressure", event mines mandatory), Idle Mining Empire, Mr. Mine (gem paywalls), Swamp Attack ("grind-wall-to-sell-currency"), Tap Titans 2 (clan pay pressure), CH1 (rubies overpriced), Melvor (expansions as paywall), Synergism (paid convenience reads as pay-to-skip).
- Complaint file: "Excessive forced advertisement"; "Remove ads" that does not; ads play when the player declines; "Progression stalls on purpose to sell you the fix" (C2, C3 quotes).
- Mobile-first set (12): AdCap, AFK Arena, Cell to Singularity, Egg Inc, Farm Away, Guava Juice, Idle Miner Tycoon, Idle Mining Empire, Mr. Mine, Swamp Attack, Tap Titans 2, Idle Slayer. 11 of 12 carry this complaint (all but Idle Slayer); the other 3 of the 14 are CH1, Melvor (expansions) and Synergism (PCoin).
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
- None or gated: CC base game (offline is a 1-chip upgrade), PK, UP, Idle Champions, Evolve (banked skip), ADR (state frozen), Candy Box 2, Idle Breakout, Reactor, Increlution.
- Other direction: "numbers when I come back are too big and I'm catching up instead of playing" (C7). Sim: offline efficiency 0 -> 0.25 speeds a casual player ~9x, 0.25 -> 1.0 only ~2x.

## A8. Balance churn, bugs, reworks (9 of 37; C11)
- CH2 (delays, prestige rework, bugs), Cell to Singularity (lag, broken balance), AdCap (balance changes invalidate spreadsheets), RG (updates favour veterans), Egg Inc (updates invalidate strategies), Idle Champions (power creep, FOMO), Magic Research, Factory Idle (recipe patches), PK (forks with differing numbers).

## A9. Punitive failure states (4 of 37)
- Reactor meltdown wipes components; ADR exploration starvation/item loss; CC wrinklers/Grandmapocalypse; Evolve plasmid soft caps.
- Design counter-measure already recorded: soft failure (a heat meter that only throttles) in `games/reactor-incremental.md` lesson 2.

## A10-A12. Smaller items
- A10 Number inflation: Idle Miner Tycoon, Idle Mining Empire (e-notation quickly), plus C8 quotes ("exponent gibberish with no sense of scale").
- A11 Save loss: PK (cache clears), Candy Box 2 (manual saves); C11 snippet (Farmer Against Potatoes rollback).
- A12 Fragmented economies/mandatory events: AdCap planets and events, Idle Miner Tycoon event mines, Idle Champions FOMO, Egg Inc contracts, Idle Mining Empire events.

## Sequential-world-specific failures (cross-reference)
- Skin-only new world: AdCap planets (A6), Swamp Attack repetition inside chapters.
- Carryover that trivialises the next world: sim "carry x2, cost x1: 8.4 -> 0.3 min".
- Walls between worlds: sim "cost x10".
- Too many layers: CH2 4+, Synergism sprawl, NGU system count.
- Diluted older worlds: handled in CH2 by per-world prestige points so "prestige in World N doesn't dilute World N-1" `[EST]`.
- Mid-game lull between layers: AD Break Infinity -> Eternity.

## Cross-cutting findings
1. The loop is liked; the wrapper is hated (A2 vs `research/player_complaints.md` pattern 1).
2. Walls, mistimed prestige and offline gaps are one problem at three time scales (pattern 2): the player runs out of satisfying next actions.
3. Enthusiasts quit over choice and legibility (A3, A5, A10); casuals over ads/grind (A1, A2). A licensed-IP game sits nearer the casual side (pattern 4).
4. Trust items (A2, A11, ad-removal that does not remove ads) are one-star triggers (pattern 6).

## Implications for Kamen Rider Decade world-progression idle game
1. **Never gate on a wall without a side option (A1).** Pair every long wait with a new thing: a Side Rider card, a detour world, a form unlock. Sim: keep goal gaps in the 15-600 s band and max gap < 30 min; aim cost/rate ratio 1.2-1.5, growth 1.10-1.15, milestone doublers at x2 not x3.
2. **First world-ride within 10-15 minutes** (C6 postmortem said 25-35 min was late), then 20-45 min cycles; do not allow a ride before ~60% of the world's tiers are seen (sim rule).
3. **Ship ad-free or strictly opt-in (A2).** If IAP: cosmetics only (suits, henshin sounds) and a one-time remove-ads that works; never sell the prestige currency or time-skips as the main revenue (Farm Away lesson 7, AdCap lesson 6).
4. **Idle means idle (A4).** Auto-henshin/auto-card-ride unlocks early; "Attack Ride" burst accelerates but is never required; no daily-streak loss mechanics.
5. **Do not clone tycoon structure (A5).** The differentiator is sequential worlds with a rule per world; include a build fork in the first 5 minutes and >= 2 viable builds.
6. **Prestige must feel like a gain (A6).** Show before/after production, keep the card collection across resets, use sqrt/cbrt with a pending-gain readout, and keep layers to 2-3 (CH2/Synergism warning). Do not let per-point bonuses exceed ~10% (sim: 25%/pt explodes to 9e4x).
7. **Offline ~50%, 8 h cap, "welcome back" with 1-2 decisions (A7).** Never gate base offline behind a late upgrade (CC complaint).
8. **Legibility (A3, A10).** One screen per world, <= 3 visible currencies, in-game formula breakdowns (additive vs multiplicative labelled, Idle Slayer lesson 2), a first-purchase shopping list (Leaf Blower lesson 3), named ranks instead of e47.
9. **Soft failure only (A9).** No world-clock penalty that destroys cards.
10. **Trust (A11).** Cloud plus local dual save, versioned backups, auto-save from day one (Candy Box 2 lesson 7).
11. **Reduce balance churn (A8).** Keep all constants in one file (Bitburner `Constants.ts` lesson) so rebalancing is a one-file diff.
12. **Caveat:** for several anti-patterns the evidence is weak (`[M]/[E]` hate lists, search-snippet complaints). Re-verify with first-hand review sampling (see "Gaps" in `research/player_complaints.md`) before treating counts as ratios.
