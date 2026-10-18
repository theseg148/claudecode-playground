# Patterns shared by the most-beloved idle/incremental games

Scope: all 47 files in `games/` (the beloved set below is still the original 14; the 10 later files are used as supporting evidence, see "Additions"), plus `research/psychology.md`, `research/player_complaints.md`, `research/math_of_idle_games.md`, `sim/results.md`.

## Method and honesty notes
- No sales, retention or review-score data exists in this repo. "Beloved" is a judgment from the "What players love" sections, longevity, community tooling (wikis, calculators, mods) and absence of complaints about monetisation. It is not a measurement.
- **Beloved set (N = 14):** Antimatter Dimensions (AD), Cookie Clicker (CC), Universal Paperclips (UP), A Dark Room (ADR), Kittens Game (KG), Evolve, Synergism, Trimps, Melvor Idle, Progress Knight (PK), Bitburner, Realm Grinder (RG), NGU Idle, Spaceplan.
- Evidence strength per game file (recounted after source mining rounds 1-2 and the verification passes; tags in games/*.md: 326 code-read, 486 [S], 77 [PUB], 681 estimated across 47 files; 24 of 47 games carry code-read tags): **code-read = AD (17 [CODE]/[SRC]), Bitburner (25), Evolve (31), Synergism (35), PK (24), Kittens Game (15), Cookie Clicker (9; public mirror ozh/cookieclicker `main.js`, NOT closed source), Universal Paperclips (8), Trimps (6), A Dark Room (4)**. Snippet-level = Melvor `[S]`, RG `[S]`, NGU `[S]`, Spaceplan `[S]` (developer, price, ~6 h length, no formulas). So 10 of the 14 beloved games now have code-read evidence (previously 5 strong); only Melvor, RG, NGU and Spaceplan remain snippet/estimate-level. Counts below still come from manual reading of the files; treat "9 of 14" as "9 of 14 as far as the files record".
- Counts are manual tallies from the files, not keyword matches. Where a game only partly fits I say so.
- Companion files: `analysis/anti_patterns.md`, `analysis/sequential_worlds.md`.

## Pattern table (counts out of the 14 beloved games)

| # | Pattern | Count |
|---|---|---|
| B1 | Non-predatory monetisation (free, open source, or one-time purchase) | 12 of 14 clean, 2 partial |
| B2 | Something new appears every few minutes, and the UI is revealed progressively | 14 of 14 |
| B3 | Each stage/layer changes the rules, not only the numbers | 14 of 14 (10 via prestige layers, 4 via phases/genres/beats) |
| B4 | Real decisions (build, route, price, allocation), not just "buy the next thing" | 13 of 14 |
| B5 | Inspectable math (open source, readable JS, or deep community wiki/calculators) | 10 of 14 |
| B6 | Prestige/gains compressed by sqrt, cbrt, log or falling exponents so numbers stay readable | 7 of 14 |
| B7 | Strong voice/theme (humour, horror, lore) that makes each unlock a story beat | 9 of 14 |
| B8 | Offline or catch-up progress exists | 9 of 14 (5 do without) |
| B9 | Optional active spikes layered on an idle base | 5 of 14 |
| B10 | Automation is itself a priced reward/milestone | 5 of 14 |
| B11 | Milestone or achievement ladders giving frequent small wins | 6 of 14 |
| B12 | Small number of visible resources early, more added later | 6 of 14 |

## B1. Non-predatory monetisation (12 of 14 clean, 2 partial)
- Clean: AD "None. Free, no ads, no premium currency" (`games/antimatter-dimensions.md`); CC Steam one-time, no IAP (`games/cookie-clicker.md`); UP free browser, "zero pay-to-win" (`games/universal-paperclips.md`); ADR free, mobile ~$0.99 no IAP (`games/a-dark-room.md`); KG free, donations (`games/kittens-game.md`); Evolve free, README rejects "features that only make the game easier" (`games/evolve.md`); Trimps free (`games/trimps.md`); Melvor one-time purchase, "no premium currency, so progress is time-based only" (`games/melvor-idle.md`); PK free (`games/progress-knight.md`); Bitburner Steam one-time, RAM limits replace paywalls (`games/bitburner.md`); NGU Steam one-time, "mostly free of pay-to-win" `[unverified]` (`games/ngu-idle.md`); Spaceplan premium one-time, no ad walls (`games/spaceplan.md`, `[MEM]`).
- Partial: Synergism PCoin upgrades buff offline cap and quark gain, which some read as pay-to-skip (`games/synergism.md`, `[SRC]` + `[MEM]`); RG has optional IAP on Kongregate/mobile, one-time on Steam (`games/realm-grinder.md`, `[unverified]`).
- Supports: `research/player_complaints.md` pattern 1 "The loop is liked; the wrapper is hated" and pattern 6 "Trust".

## B2. A new thing every few minutes, revealed progressively (14 of 14)
- ADR: each button appears only when relevant; each new tab is a story beat (`games/a-dark-room.md`). Village stage names (Lonely Hut -> Raucous Village) tie to counts.
- UP: "Every few minutes a new mechanic; no filler waiting" (`games/universal-paperclips.md`).
- Spaceplan: "Every 3-10 minutes a new item/dialogue appears" (`games/spaceplan.md`, `[EST]`).
- CC: later buildings revealed at about 1/3 to 1/2 of price so the next tier is always visible (`games/cookie-clicker.md`).
- AD: each layer "re-teaches the same loop with new rules"; 150+ achievements (`games/antimatter-dimensions.md`).
- Synergism: each layer unlocks a new building set and minigame (`games/synergism.md`).
- KG, NGU, Evolve, Bitburner, Trimps, RG, PK, Melvor: heavy unlock ladders (NGU "a fixed number of features each day"; Bitburner subsystems unlock via Source Files; Trimps new permanent layers at zone thresholds; PK unlock tree "level X in job Y"; Melvor items every few levels). See each file's "Unlock pacing".
- Psychology: dense goal gradients plus endowed progress (`research/psychology.md` sections 5-6).
- Sim support: the best configs gave 32 goals in 3 h, median gap 46 s, max gap 344 s (`sim/results.md`, sweep).

## B3. Each stage changes the rules (14 of 14)
- Via prestige layers (10): AD (Infinity/Eternity/Reality, Celestials with their own rules), Evolve (each reset type has its own constants table and mechanic), Synergism (5 layers, each a new subsystem), Trimps (Heirlooms, Nature, Universe 2), RG (factions, abdication, reincarnation), Bitburner (BitNodes change `currentNodeMults`), KG (karma/paragon/time layers, challenges), NGU (rebirth, titans, challenges), PK (rebirth one/two), CC (heavenly tree plus Garden/Grimoire/Stock mini-games).
- Via phases/genres/beats (4): UP (clips -> drones -> probes), ADR (village economy -> map -> shooter), Spaceplan (new currency per story beat), Melvor (expansions add skills/worlds).
- Players' words: AD "Every layer reinvents the game"; Evolve "Reset layers each introduce a mechanic (not just a bigger number)".
- Detail in `analysis/sequential_worlds.md`.

## B4. Real decisions (13 of 14)
- RG faction choice; Evolve race and government; Bitburner writing the scripts; KG job assignment; NGU energy/magic allocation; Trimps perk purchases; PK "what to train in a limited life"; AD challenges and time studies; Synergism ants/runes/corruptions; CC golden-cookie combos; Melvor skill/mastery choices; UP price slider and Yomi tournaments; ADR supply-chain jobs (hunter -> charcutier).
- Exception: Spaceplan (writing is the product; "shallow for experienced fans", `games/spaceplan.md`).
- Maps to `research/player_complaints.md` C5 ("no meaningful choices is the sole reason your earlygame is boring") and SDT autonomy (`research/psychology.md` section 2).

## B5. Inspectable math (10 of 14)
- Source or code available and now actually read: AD (GitHub), Bitburner, Evolve, KG (`game.js`, `buildings.js`), Synergism, Trimps (`main.js`, `config.js`; plus AutoTrimps/Perky), PK, CC (`main.js` in the public ozh/cookieclicker mirror; the game is not closed-source), UP (unobfuscated JS, ianfixes mirror), ADR (open source, MPL-2.0, `room.js`).
- Even without code, RG and NGU have heavy wiki/spreadsheet culture. The counter-case: the community built spreadsheets because the game would not explain itself (see anti-patterns A3).

## B6. Compressed gains keep numbers readable (7 of 14)
- AD IP = `10^(log10(maxAM)/308 - 0.75)`, EP = `5^(log10(IP)/308 - 0.7)`, RM = `1000^(log10(EP)/4000 - 1)` `[CODE]` (`src/game.js` L89-163, `machines.js`; `games/antimatter-dimensions.md`, `research/formula_tables.md` R2.1).
- CC `cbrt(C/1e12)`, +1% CPS per level `[CODE]` (`main.js` L4185-4192).
- Synergism exponents fall per layer: 0.5 -> 0.03 -> 0.01 `[SRC]`.
- Evolve: log curves plus plasmid soft cap `cap + overflow/(overflow+cap)*cap` `[SRC]`.
- PK: income `1 + log10(level+1)`, lifespan and speed on log33/log13 `[CODE]`.
- KG: paragon (+1 % production per paragon x ratio, limited-DR cap 2x; reset gives kittens - 70; +1 paragon per 1000 years) with `getLimitedDR` diminishing returns `[CODE]` (`prestige.js` L549-576, `game.js`).
- RG: sqrt formula (`research/math_of_idle_games.md` 3.1).
- Player evidence: "I want the numbers to rise because I made them rise" (`research/player_complaints.md` C8).

## B7. Strong voice and theme (9 of 14)
- ADR atmosphere and late twist; UP "ever-escalating scope... ending with a real 'oh no'"; Spaceplan sarcastic computer voice; CC jokes on every upgrade; PK dark humour and evil path; KG text charm; Evolve "from primordial ooze to spacefaring empire"; AD celestial narrative; Trimps flavour. Sources: each game's "What players love".
- Psych support: Deterding says progress mechanics work even as satire (`research/psychology.md` section 1).

## B8. Offline progress (9 of 14; 5 without)
- With: AD (chunked simulation; `ipOffline` upgrade pays 50 % of best IP/ms `[CODE]`), CC (needs Twin Gates: 5 % for 1 h, up to 75 % from angel tiers and 91 % with all extras, unlimited at 100 % with Perfect idling; nothing without them `[CODE]`), KG (capped catch-up), Melvor (24 h cap `[S]`), Bitburner (0.75 multiplier `[CODE]`), Synergism (72 h base + 4 h per research 31/32, 200-tick simulation `[CODE]`), Trimps, NGU, RG (small).
- Without or banked: ADR (state frozen), UP (page must stay open), PK (tab open; Time Warping skill instead), Evolve (banked "time skip"), Spaceplan (modest, `[MEM]`).
- Reading: offline is not a requirement for being loved, but all five no-offline games are either finite (ADR, UP, Spaceplan) or session-based by design (PK, Evolve). Open-ended games have it (`sim/results.md`: eff 0 -> 0.25 makes a 3x10 min/day player about 9x faster).

## B9. Optional active spikes (5 of 14)
- CC golden cookies (spawn gap 5-15 min base, lifetime 13 s, `main.js` L5934-6000, L5617 `[CODE]`; Frenzy x7), RG spells, UP price slider and projects, NGU Adventure mode, Synergism automation toggles/challenges. Active play accelerates; the base keeps running. Matches `research/player_complaints.md` cross-cutting pattern 5 ("active play accelerates, idle play never stalls").

## B10. Automation as a reward (5 of 14)
- UP WireBuyer costs 7,000 ops (`games/universal-paperclips.md`, `[S]`); AD Break Infinity requires a 0.1 s Big Crunch autobuyer `[S]`; Synergism auto-prestige credited offline as `timeAway / fastestPrestige` `[SRC]`; Bitburner (automation is the game); Trimps (the community built AutoTrimps, which doubles as a complaint).

## B11. Milestone and achievement ladders (6 of 14)
- AD 150+ achievements with row rewards; CC achievements and milk; Synergism "hundreds of achievements"; Evolve achievement level raises the plasmid cap `[SRC]`; UP Trust milestones on Fibonacci-spaced clip counts `[S]`; ADR village stage names by count.

## B12. Few visible resources early (6 of 14)
- Spaceplan 2-4 visible resources (`[EST]`); UP money plus ops; ADR wood first; AD one currency, eight dimensions; CC cookies; PK coins only. Counter-case: KG, NGU, Synergism show many resources and are the most-cited for complexity.

## Cost-curve facts shared by the beloved set
- Core production-building ratios sit in 1.07-1.15 (CC 1.15 `[CODE]`, KG 1.12-1.15 `[CODE]`, Trimps 1.12-1.24 `[CODE]`, UP 1.07-1.1 `[CODE]`, RG likely 1.08-1.15 `[unverified]`), with outliers by design: Synergism 1.25-3 per tier `[CODE]`, PK `1.01^level` polynomial `[CODE]`, ADR linear (`10 + 10n` traps, `100 + 50n` huts, caps 10 and 20; `[CODE] room.js`; pacing from timers), Melvor XP doubling every ~7 levels `[S]`.
- Sim result: the *shape* (cost ratio between tiers slightly above rate ratio, ~1.2-1.5, plus x2 milestones) matters more than the growth constant (`sim/results.md`). Cookie Clicker's own ladder is steeper (price/CPS 1.4-2.9 per tier, derived from the CODE table), an open calibration item.

## Additions from the 10 later game files (not counted in N = 14)
- **Shark Game [CODE]:** a world is a data record (included/absent resources, modifiers, gate slots); flat essence on completion; random shortlist of next worlds (supports B3, R27, R28). **Prestige Tree [CODE]:** each layer is a new resource, upgrades and minigame; unlock-order choice; `offlineLimit` 1 h (B3, B2). **Idle Loops [CODE]:** offline time is banked and spent at x5 speed (B8 variant, R36). **Derivative Clicker [CODE]:** reset currency buys convenience as well as multipliers (B10). **Orb of Creation, Gnorp Apologue, Ordinal Markup, Soda Dungeon, Idle Heroes, Fallout Shelter:** [S]-level only; they contribute cautions (see anti_patterns.md) more than beloved patterns.
- Adding Shark Game, Prestige Tree and Idle Loops would not change any B-count above (B3 and B8 would only gain examples).

## Implications for Kamen Rider Decade world-progression idle game
Aligned with DESIGN_RULES.md (R-numbers) and DECADE_IDLE_DESIGN.md. Superseded advice from the first version is noted inline.
1. **Be the "wrapper-clean" game (B1, R39).** 12 of 14 beloved games have no predatory monetisation. Default for this fan project: no monetisation at all (Toei IP exposure); if it ever became commercial, cosmetics only, no sale of Ride Cards or Seals, time-skips only if they never gate a world, no mandatory ads. `research/player_complaints.md`: fandom will not forgive forced ads on a licensed property.
2. **Reveal, don't dump (B2, B12; R11, R26).** One number and one button at the start, at most 3 visible currencies on the main screen (Shots, Seals, one per-world counter); at least one new option or unlock every 2-5 minutes in the first hour; at most **one extra system per world** on top of the world's rule (World 1 also carries the tutorial set: Photo Window and the mastery tree).
3. **Every world must change a rule (B3, R26, R27).** Use `research/decade_worlds.md` hooks (Kabuto Clock Up/Cast Off, Den-O contracts, Ryuki cards, Faiz routing, Blade fusion, Kiva day/night, Agito forms, Hibiki rhythm, Kuuga colour forms) and store each world as a data record (Shark Game, Evolve).
4. **Ship real choices (B4, R13, R13b).** A build fork inside the first 5 minutes (the first fork at about 2:00 using a starting mastery point) with at least two viable exclusive builds; the slowest build at most 25 % slower than the fastest (sim v3: 1.19x), never a build that only changes offline efficiency.
5. **Compress prestige (B6, R15-R17).** Seals = floor(sqrt(run_lifetime / T_w)), multiplier **(1 + Seals)^0.5** (not 5-10 %/pt and not "final multiplier 2e2-6e3": that came from the pre-ride sweep; linear +8 %/seal explodes to 6e6), ride when it raises production at least 1.5x, show pending gain and before/after, first ride about 8 min (T_w calibrated), 9-11 rides per 3.2-day world, gates x2.5-3.5 per world. Not "first gate about 25 min, then 20-45 min cycles".
6. **Give the game a voice (B7).** Tsukasa's quips as narrator reacting to each unlock.
7. **Offline (B8, R33, R36).** Production while away is existential (about 10x faster than none); the cap is minor. Stepped 50 % for 2 h, 25 % beyond, cap 8 h (average about 0.31 for an 8 h gap), never 0; 8 -> 24 h cap as a light-player upgrade; optional banked x5 time (Idle Loops). Welcome-back card with 1-2 decisions (R35).
8. **Active spikes optional and budgeted (B9, R34c, R38b).** Not a x3 "Attack Ride": use the Photo Window (every 90-240 s foregrounded, first at about 3:00, banked offline Exposures 1 per 30 min cap 6 at half value) and Clock Up; budget Clock Up at most 1.25x of average, Photo Op at most 1.1x, Photo Windows 1.05-1.1x of daily progress, all active tools at most 1.5x in an active session. No negative outcomes (the golden-cookie 5-15 min / 13 s timing is the reference, scaled for 10-minute sessions).
9. **Automation as milestone (B10, R10, R21).** Light auto-collect and auto-buy tier 1 at about 3 min; full payback auto-buy in the first-ride shop; collection automation as a milestone reward (Guava Juice level 50).
10. **Ladder of small wins (B11, R3, R4, R38c, R25).** x2 milestone bars at 10/25/50/100/200, an album/binder with an achievement multiplier of 1.05^rows x 1.01^count (about x10 at 144 entries, base Shots only, counted inside the carry budget c); beats supplied at least once per session because rides alone give a goal in only 55-73 % of sessions.
11. **World drift (R23).** Keep d = cost_scale / total permanent carry in [1.0, 1.07] with cards, archived Seals and achievements all inside c.
12. **Evidence caveat.** Code-read evidence now covers AD, Bitburner, Evolve, Synergism, PK, KG, CC, UP, Trimps and ADR; Melvor, RG, NGU and Spaceplan remain snippet/estimate-level. Open: pacing of golden-cookie-style events at real session lengths (R38b), and whether heavy players get enough optional content (a ride cooldown was simulated and rejected, R34); gates must be calibrated with offline auto-spend (R37, worlds 26-44 % shorter).
