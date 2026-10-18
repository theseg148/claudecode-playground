# REVIEW_3 - third adversarial review (DESIGN_RULES v3, DECADE_IDLE_DESIGN, WORLD_TABLES, SUMMARY v3, sim v3, analysis refresh)

Scope read: REVIEW_2, DESIGN_RULES (DR), DECADE_IDLE_DESIGN (DD), DECADE_WORLD_TABLES (WT), SUMMARY (SU), README, sim/results.md (SR), analysis/*.md, prototypes/EVALUATIONS.md (EV), plus decade_slice_v2.html, sim/*.py, games/*.md spot checks. Nothing else was edited. Re-runs were done in the repo (test_sim, pacing_report, events, offline_lever, offline_autobuy, ride_cooldown, builds3) and in a scratch copy (campaign.py 1e18, campaign3.py 2.25, population.py), so committed JSON was not overwritten. Priority: P0 = a headline number or rule is wrong or contradicts another document, P1 = fix before building, P2 = polish. Lines are file:line of the current files.

Headline: v3 fixed the Seal economy, unique goals, T_w calibration, and most R-number drift, and the sim numbers largely reproduce. What is left is (a) the headline "3.2 d/world, 29 d campaign" is measured without three features the design itself specifies, (b) DD/WT still carry the v2 gate numbers (1e18) and several v2 sentences that now contradict v3, (c) a handful of terminology collisions, (d) stale evidence tallies.

---

## 1. REVIEW_2 items: status table

| REVIEW_2 item | Status | Evidence / what is left |
|---|---|---|
| P0-1 carry sources in sim | PARTIAL | campaign3.py:15-22 includes c^w, cards, bounded archive, achievements; DR:34 R23 rewritten; DD:22 archive now bounded. NOT in sim: mastery cross-world nodes (DD:22 "3 cross-world nodes pooled"), Driver forms (DD:26), R29 "cleared worlds raise passive income" (DR:40, still no number), Time Skip (DD:30). The prototype still has the old unbounded bonus: decade_slice_v2.html:40 `(1+.02*Math.sqrt(S.arch||0))` and :55 `S.arch+=S.seals`. DD:22 says archive is a flat +1 %/world independent of Seals, so "archived per world" Seals have no function. |
| P0-2 Seal economy / per-point bonus | RESOLVED in DR:24-26 (R15-R17), SR v3, EV:18. Leftovers: DD:12 says "the prototype slice still uses a DEV linear formula (+8 %/seal)" - false, decade_slice_v2.html:40 uses `Math.sqrt(1+S.seals)` (BONUS const at :29 is unused). R21 "first ride gives a bonus" (DR:30) still has no number. DD:35/47 and WT:7 still gate on 1e18 (see P0-2 below). |
| P0-3 unique goals / W1-W9 | RESOLVED in campaign3.py and SR v3 (51 goals, 64-73 %, dry 2/4). Leftovers: SR:75-84 v2 table still shows `[:4]` data and "83-100 %"; DD:51 arithmetic "8 tiers x (1+5) ~ 40" (it is 48; the sim's 51 = 40 reached tier/milestone goals + 11 rides, so say that); SU:13 and DD:51 say "rides alone give 64-73 %" but SR:128-132 table says rides alone = 55-64 %, 64-73 % includes tier/milestone goals (DR:36 gets it right). |
| P0-4 R23 sublinear, T_w follows carry, flat test tautological | MOSTLY RESOLVED (DR:34 d^(0.65n); T_w calibrated, first ride 8.0 min all worlds, reproduced). Still open: test_sim.py:30-33 `test_world_scaling_flat_when_ratio_one` is the same tautology; no test runs mode="pow" or checks the gate schedule. WT:21 still says "worlds 4-6 at ratio 1.2 are 4-6 days (dry streak 1-2)" - v2 data, wrong word (see terminology), and contradicts the v3 plan of 3.2 d for every world. |
| P0-5 systems per world, R33/R34, reference player | PARTIAL | R26 reworded (DR:37) and first-10-min timeline fixed (DD:85). But W1 still has two verbs (Clock Up + Cast Off, DD:35, WT:7) plus Phylloxera Mirror (a ride that "copies build", a fourth reset-like object, REVIEW_2 H9, still in DD:35, WT:7). DR:37 R26 tally "~12 games" vs analysis/sequential_worlds.md:15-16 (S1 = 17 games, S2 = 14). Active budget DD:52/DR:48 says Clock Up <=1.25x, but prototype Speed II makes it x3 with regen 1/4 s (decade_slice_v2.html:56, :91) = ~2.0x average for an active player. Time Skip (DD:30, offline_v2.html "20 % of time as x5") is not in any budget or sim. |
| P0-6 prototype slice | MOSTLY FIXED (EV:43-51: cumulative gate, offline for gaps, in-place render, number format, Cast Off tiers>=4, Photo Window added). Still open: carry formula (above); header comment :26 says "DESIGN_RULES v2"; slice has 6 tiers while design/sim have 8 (EV:61 uses it as evidence for "4 of 6" ride guard vs R19 "4 of 8"); EV:35 still documents Clock Up x3/10 s, Speed II x5, Cast Off x2/x3/x5 while EV:48 and the code say x2/8 s, x3, x1.5/x2 (the file contradicts itself); DD:68 still says `prototypes/decade_slice.html` (v1) is the slice. |
| P1-7 builds | MOSTLY RESOLVED (builds3.py, 1.19x reproduced, point cap 4, starting point). New contradiction: mastery tree is "~25 nodes/world" (DD:56, EV:23) while points are capped at 4/world (DR:20 R13b, DD:56) - 4 points cannot fill 25 nodes, so the tree is a menu, not a tree to complete; pick one. WT:10 (Ryuki "Press (offline)") and WT:11 (Blade "Heart (offline)") are offline-only branches, which R13b (DR:20) and SR:102 call a trap. |
| P1-8 events numbers | MOSTLY RESOLVED: events.py is seeded and reproduces DR:56 (33-52 %, 3.1-6.5 %, +17.5 %/+40.7 %). SR:105-107 was NOT updated: still 28-37 %, 2.5-3.6 %, +17.6/+41 %, "bank 450". DD:56 item 8 still describes R38 (13 s window every 5-15 min, <=1.2x) which DR:54 marks superseded. |
| P2-9 smaller mismatches | MOSTLY RESOLVED: s=3/4 peak shown in R40a, R19 note, "ratio" -> "drift" in DR/DD/SU, Form Energy -> Seals in DR/DD/SU. Left: research/ui_and_numbers.md:154-157 (1.15 growth, x10 tier, "Form Energy 5 %/pt", "range 2e2-6e3", c = s/1.1 = 3.64, gate 1e18*s^w) and sim/campaign3.py:3 docstring "Form Energy"; campaign.json committed is the 1e19 run (5.0 d W1), not the `campaign.py 1e18` run documented in SR:113 (running the command prints the SR table but also overwrites the json). |
| H5/H7/H9/H8 (L3, family matrix, Phylloxera, passive income) | STILL OPEN | L3 "All Riders" has no reset/payout (DD:14); no upgrade-family x world matrix; Phylloxera Mirror unchanged; R29 passive income has no number. |

---

## 2. Priority issues (the 8 most important first)

### P0-1. The headline pacing (3.2 d/world, ~29 d, 64-73 % goal density) is measured without auto-spend, builds, and Time Skip, all of which the design includes
- offline_autobuy.py (re-run, matches SR:167-175): auto-spend while away shortens world 1 by x1.26 (6/day) to x1.44 (1/day); builds3.py: any build clears 20-45 % faster than no build (3.22 -> 1.85-2.57 d); R37 (DR:51) says "calibrate gates with it on". R21 (DR:30) puts auto-buy in the first-ride shop, i.e. it is on from ride 1 in every world, and R13b (DR:20) says gates must be calibrated with the build mix. Neither is done: R25 (DR:36), DD:3, DD:8, DD:50, SU:12, analysis/sequential_worlds.md:140 all state 3.2 d / 29 d. Stacking the two measured factors (x1.27 and x1.2-1.7) gives roughly 1.7-2.1 d/world, 15-19 days for the campaign, and the "64-73 % of sessions have a goal / max dry 2" figure (measured at 3.2 d) is not valid either.
- Proposed edit: campaign3.py: add `auto_spend=True` and a build multiplier (e.g. Speed x1.2 x2 nodes) to `World`, re-calibrate G_w with both on, republish the gate schedule. Until then DR:36 R25: "3.2 d / 29 d is the spend-at-return, no-build upper bound; with R21 auto-spend and one build expect about 2 d / 18 d". Same caveat in DD:8, DD:50, SU:12.

### P0-2. Gate numbers contradict each other (v2 explosive regime still in DD and WT)
- DR:36 R25 / SR:126-135: W1 gate 6.2e15, W9 4.0e19 (pow, v3). DD:35 and WT:7 give W1 gate "Shots 1e18"; DD:47 "1e18 * s^w in the sim = ~3 days" (that was the lin +8 %/seal regime, 2.67e20 in campaign3 lin, not 1e18); DR:61 R40a and DD:71 peak "6.6e21 = 1e18*3^8" and research/ui_and_numbers.md:153. With the adopted pow variant the W9 gate is 4.0e19, so R40a's peak is 100x too high (harmless for doubles, but the player-facing numbers in the design, the notation table and the slice's DEV gates are all built on the wrong scale).
- Edit: DD:35 gate "Shots 6e15" (W1) and DD:47 "(a) lifetime Shots >= G_w (calibrated, 6.2e15 -> 4.0e19 = x2.5-3.5 per world, DR R25)"; WT:7 same; DR:61/DD:71 "peak ~4e19 gate x ~100 overshoot ~ 4e21".

### P0-3. Two different "Photo" mechanics share one name, and the R38 spec survived in DD
- DD:5 "tap 'Photo Op'" and DD:26 "Photo Op cooldown" (a button with cooldown, +10 % in the slice, decade_slice_v2.html:53) versus DD:56 item 8 "Photo Op: unscheduled 13 s window every 5-15 min, <=1.2x average (R38)" (that is the Photo Window event, and R38 is "superseded by R38b", DR:54). WT:3 adds a third "optional 'Photo Op' variant". R34c (DR:48) budgets "Photo Op <=1.1x" and "Photo Windows 1.05-1.1x" separately.
- Edit: DD:56 item 8: "Photo Op = tap button, 6 s of income per 60 s (+10 %, R34c); Photo Window = unscheduled event every 90-240 s foregrounded (R38b)". WT:3 delete the "Photo Op variant" or define it.

### P0-4. Terminology collisions: "Seals" vs Blade's "Undead Seals", "Form", "Photo", "ratio"
- WT:11 (Blade tier 5 "Undead Seals") collides with the L1 currency "Seals" (the main-screen counter, R15). Rename the tier ("Undead Cards" is also taken; use "Sealed Undead") or rename the currency (Exposures is also taken; "Shutter Points"?). Pick before content writing.
- "Form" still names five things: Final Form Ride, Driver forms (DR:40, DD:26), Form Deck (DD:77), Agito Forms (WT:13), Kabuto's "Rider Form". At least rename the deck ("Loadout") and Agito's mechanic.
- "ratio" for drift survives in WT:21, SR:80-84 (columns "cost scale / carry (ratio 1.00 ...)"), SR:78 header table, population.py output ("lengthening (3/2.5)"), EV:32. Search/replace to "drift d".
- Mastery "points", "Charge", "Exposures", "Swap Tokens", "Time Skip", "Ride Cards": DD:44 admits 8-9 counters exist; DR:37 R26 says world-local currency "from world 2-3" but DD:2b gives every world a local currency and W1 has Charge. Say "Charge counts as W1's one local counter" in R26.

### P0-5. Rides-alone vs total goal-density sentence is wrong in SU and DD
- SU:13 #11 "Rides alone give only 64-73 % of sessions a new goal" and DD:51 "only 64-73 % of sessions contain one": per SR:128-132 / campaign3_pow_only.json the 64-73 % is sessions with any new unique goal (tier, milestone or ride); sessions with a ride are 55-64 %. DR:36 states both correctly; analysis/anti_patterns.md:92 says "55-73 %". Edit SU:13: "Rides plus tier/milestone goals give a new goal in only 64-73 % of sessions (rides alone 55-64 %)".

### P1-6. Stale evidence tallies and unreproducible evidence totals
- DR:18 R12 "~30/37", DR:60 R39 "14/37 ... 11/12 mobile-first", SU:18 #16 "~30/37 ... 14/37 ... 11 of 12" - analysis/anti_patterns.md:16-17 now says ~34 of 47 and 17 of 47 (14 of 15 mobile-first); anti_patterns.md:29 and :35 section headings still say "~30 of 37" and "14 of 37" (the same file disagrees with itself). DR:37 R26 "tally of ~12 games" vs 17/14 in sequential_worlds.md.
- SU:22 #20: "24 carry code-read evidence and 22 only snippets": 47 - 24 = 23 (grep of games/*.md finds 24 files with [CODE]/[SRC], 23 without). The tag totals (812 confirmed / 681 estimated, "54 % confirmed") cannot be reproduced by grep (255 [CODE] + 60 [SRC] + 72 [PUB] + 389 [S] + 261 [M] + 351 [E] tags found); and "confirmed" adds [S] search snippets (486) to code reads (326), which inflates confirmation. Report code-read vs snippet vs estimate separately, as beloved_patterns.md:8 does, and drop the "54 %" headline or recompute with a stated grep.
- games/kittens-game.md:20 and :59 still say ratios [M]/"NOT confirmed" while :71 lists code line numbers; DR:5 R1 tags Kittens 1.12-1.15 as [CODE]. Edit the file header lines or tag R1's Kittens as [CODE (kittens-game.md:71)] after verifying.

### P1-7. R-number references: shifted-number audit
All R-references in DR, DD, WT, SU, analysis/*.md, README were checked against DR v3 and are correct, with these exceptions:
| Where | Reference | Problem |
|---|---|---|
| DD:1 | "Applies DESIGN_RULES.md v2" and title "(v2)" | v3 now; also WT:1 "v2" |
| prototypes/decade_slice_v2.html:26 | "DESIGN_RULES v2" | R-numbers there are v3; fix comment |
| prototypes/decade_slice.html:22,42,62 | R12 sqrt prestige, R24 active layer, R17 auto-buy, R23 offline | v1 numbering (v3: R15, R34c/R38b, R21, R33); file is superseded - delete it or mark "v1, numbering obsolete" |
| prototypes/EVALUATIONS.md:30 (decade_slice.html) | "R15/R17/R19 (... pending >=2x ...)", "R29", "R33/R35" | mixes v1 and v3 meanings (v3 R17 = >=1.5x rule) |
| sim/campaign.py:2,4 | "(R23)" offline, "(R13,R15)" ride rule | v1 numbers; offline is R33, ride rule R15-R17 |
| sim/builds.py:1 | "R13 target: each within +-15 % of median" | v3 R13b is slowest <=25 % slower |
| sim/test_sim.py:28 | "(R10)" first goal in 2 min | R10 says <60 s first purchase; test allows 120 s |
| DR:67 (Open questions) | "whether Cast Off should coincide with x2 at 25 owned (design doc: shift Cast Off to 40)" | already decided (DD:35, prototype, builds3) - delete |
| DR:7 R3 | "200 was not swept [H]" | REVIEW_2 said fixed; sweep.py:8 includes 200 in two milestone sets, campaign uses it - change to "200 swept in the milestone-set factor, not as a single factor" |
| SR:7-12 | refers to R2/R19 only through v1 text | fine, superseded banner exists |
Also analysis/*.md use "R2.1" for research/formula_tables.md section ids (beloved_patterns.md:61, prestige_designs.md:19,27) which look like DR rule numbers - write "formula_tables 2.1".

### P1-8. Remaining text-level contradictions (numbers)
| Item | Document A | Document B |
|---|---|---|
| Clock Up | DD:24 and WT:7: x3 for 10 s (WT) / "xN, 10 s" (DD) | DR:48: x2 / 8 s per 4 Charge; prototype :52 x2/8 s, x3 with Speed II; EV:35: x3/10 s, Speed II x5 |
| First Zecter | WT:7 "joins at 5 tiers" | DD:85 "5:30 first Zecter joins (tier 3)" |
| First ride timing | DR:16 R10 "first prestige/ride unlock 10-15 min" (and "~7 min" in the same sentence) | R15/R16, DD, SR: 8.0 min calibrated |
| First fork | DR:19 R13 "first 5 min" | DR:20 R13b "before the first ride", DD:56 "~2:00" - consistent but R13 should say 2:00 |
| Campaign length | DR:34 R23 "3/day 27-48 d" (v2 population, lin regime, 1e18 gate) | R25 / DD:8 / SU:12 "~29 d" (v3). 1/day 81-147 d and 6/day 16-33 d are quoted as "sim v3 + population sim" (DD:8) but come from population.py on campaign.py (v2 regime). v3-based values: 1/day ~82 d, 6/day ~19 d (offline_lever x9). |
| Sessions per day reference | DR:47 R34 ref player 3/day, 2/day = 4.5 d, 1/day ~9 d | DR:46 R33 "x1.47 at 1 session/day" fine; SU:11 #8 "1->6 sessions = 4x" fine |
| Mastery size | DR:20/DD:56: <=4 points/world | DD:56/EV:23: ~25 nodes/world |
| Goal count | DD:51 "8 x (1+5) ~ 40" | arithmetic 48; sim 51 includes 11 rides |
| Pacing report | SR:111 "bad config fails 7 of 9 checks" | re-run: 6 of 9 FAIL (R2, R9 median, R9 max, R9 in-band, R25 3-5 d, R16 rides) |
| Cast Off | DD:35 "sheds a tier for a stronger one" | prototype and builds3: plain multiplier on tiers >=4 at >=40 owned |
| campaign3 runtime | SR:126 "(about 25 min)" | whole script (lin + pow) finished in a few minutes in this environment |

### P1-9. pacing_report.py and test_sim.py still test the superseded regime
- pacing_report.py:5,17-24 imports campaign.play_world with lin +8 %/seal, T0=1e6, goal 1e18, "R25 world 3-5 days" and "R16 8-12 rides": the PASS lines certify the v2 explosive economy (final multiplier ~1e5) that R15 rejects, not the v3 plan (pow, calibrated T_w, 3.2 d). SR:111 says "Recommended config passes all" - true but misleading.
- test_sim.py: `test_unique_goals_and_ride_gain` and `test_first_ride_*` run campaign3 with its default mode (check `play` default); none exercise `mode="pow"` or assert the R25 gate schedule growth x2.5-3.5 or goal density; `test_world_scaling_flat_when_ratio_one` is a tautology (REVIEW_2 3.6, unchanged).
- Edit: pacing_report.py: use campaign3.World/play with mode="pow", T calibrated, gate from the schedule; test_sim.py: add `test_pow_mode_rides_every_ride_ge_1_5`, `test_gate_growth_between_2_and_4`, and delete/replace the flat test.

### P1-10. WT content defects
WT:98-102 style placeholders remain in a table that claims to "fill worlds 2-9": WT:8 "Imagin Pudding? [M]", WT:11 "Club ... pick 3" (4 suit branches, template says 3 branches, WT:3), WT:14 "Kiriya…". WT:10-11 offline-only branches (see P1-7). WT:7 W1 gate "1e18" (P0-2). WT:3 "T_w scaled by world cost" should say "calibrated so the first ride lands at 8 min" (DR:25). WT:21 stale (see table). Edits: replace placeholders with named items or "TBD [content]", re-map Press/Heart to ride-economy effects (Press: packs cost fewer Shots; Heart: rides need 30 % less T).

### P2-11. README accuracy
- README:12 "carry sources and calibrated T_w and gates" attributed to `campaign.py / campaign3.py`; only campaign3.py has these (campaign.py is v2).
- README Simulation list omits ride_cooldown.py, offline_autobuy.py, cc_ladder.py, builds.py/campaign3.py outputs and sim2.py; README research list omits kamen_rider_landscape.md; prototypes list omits decade_slice.html (v1, still in the repo) and offline_v2.html is listed only as "offline/offline_v2" (ok).
- README:5 "DESIGN_RULES ... R1-R42" - there are also R13b, R34c, R38b, R38c, R40a; and it should say v3.
- README:6 "REVIEW_1.md / REVIEW_2.md" -> add REVIEW_3.md.
- TODO.md: Phase 4-6 still unchecked although complete; either delete or tick.
- NOTES/README do not say that SR v1/v2 sections are superseded (SR banner does).

### P2-12. Evidence tags in DESIGN_RULES - 8 rules checked against cited files
Chosen set (shuf, seed fixed): R4, R5, R13, R14, R22, R26, R29, R34. Plus spot checks R1, R7, R3, R12, R20, R39 while verifying tallies.
| Rule | Tag | Cited | Verdict |
|---|---|---|---|
| R4 | P | psychology.md goal-gradient | OK (Kivetz et al. 2006 cited, psychology.md:57-59); magnitude caveat present |
| R5 | P | Cookie Clicker reveal | OK but weak: cookie-clicker.md:46 gives "1/3 to 1/2" as an estimate; "5 owned" is purely sim [H] - tag as P/H |
| R13 | P | complaints C5, beloved B4 | OK: player_complaints.md:67 C5 COMMON among enthusiasts; beloved B4 = 13 of 14 (manual tally, judgement-based set) - fine as P |
| R14 | P | complaints C4/C10 | OK for C4 (COMMON); C10 is "COMMON in press, RARE as quit cause" (player_complaints.md:97), so it supports "no daily-streak loss" weakly |
| R22 | P | math_of_idle_games 6.7 | Citation wrong: math_of_idle_games.md section 6 has numbered list items 1-9 (item 7 = prestige currency smaller magnitude), no "6.7"; "check the reward cliff" is not in that list. Cite "6 item 7" and mark the cliff awareness as [H] |
| R26 | P | sequential_worlds S1/S2/S11 "tally of ~12 games" | Tally stale: S1 17 games, S2 14, S11 5 (sequential_worlds.md:15-25) |
| R29 | P | Progress Knight 1+best/10 CODE; AFK Arena P | OK: progress-knight.md:26 "1 + maxLevel/10" [CODE]; AFK Arena part not verified (afk-arena.md has no [CODE]/[SRC]) |
| R34 | H | sims | OK as H; numbers reproduce (ride_cooldown 4.32 -> 2.92x; 24 h cooldown slows 3/day by 24 %) |
Other spot checks: R1 [C] - Kittens ratios are [M]/"NOT confirmed" in kittens-game.md:20,59 though :71 gives code lines (inconsistent file); Cookie Clicker 1.15 [CODE] ok; Trimps 1.12-1.24 ok (trimps.md:74-84); Synergism 1.25 ok (synergism.md:23). R7 [C]: bitburner.md:33-34 NeuroFlux 1.14 and aug 1.9 tagged [SRC] ok. R3 [P]: the late ladder 300...1000 rests on one guide (SU:22 admits it) - fine as P only for 10/25/50/100/200; tag the late ladder [S]. R20 [P] "Synergism 0.5 -> 0.03 -> 0.01 [CODE]": synergism.md:118 states it as a takeaway; verify the layer-2/3 exponents have a code line. R33 [H] "Bitburner 75 % [CODE]" was only scripts in REVIEW_2; still listed as [CODE] at DR:46. R38c "[P/H]" is fine.

---

## 3. Sim reproduction (section 5 of the brief)
| Claim (SR) | Re-run | Result |
|---|---|---|
| test_sim.py 7 tests | `python3 test_sim.py` | all pass (2 s) |
| pacing_report recommended passes all, bad fails "7 of 9" | `pacing_report.py`, `pacing_report.py 1.15 5 14` | recommended: all 9 PASS (46 s median, 97 %, 3.0 d, 11 rides, 7 min); bad: **6** of 9 fail |
| events.py (DR:56, DD:77) | `events.py` | spd3: 33/44/52 % of active gain, 3.1/4.8/6.5 % of daily; spd1: 6.5-11.4 %; deck +17.5 % / +40.7 %; achievements x1.29/2.16/4.67/10.09 - reproduces DR:56 and DD:77. **SR:105-107 still has the old values** (28-37 %, 2.5-3.6 %, +17.6/+41 %) |
| offline_lever (SR:149-157, DR:46) | `offline_lever.py` | identical to the table: 78/8.03/9.1/6.17, 39/4.02/4.55/4.22, 26/2.52/3.22/3.08, 26/2.7/3.07/3.07, 13/1.76/2.11/2.11; ratios x1.47, x1.08, <=x1.05 hold |
| offline_autobuy (SR:167-175) | `offline_autobuy.py` | identical (9.10->6.34, 4.55->3.34, 3.22->2.54, 2.11->1.67) |
| ride_cooldown (SR:177-186) | `ride_cooldown.py` | identical, ratios 4.32/4.12/3.92/3.67/2.92 |
| builds3 (SR:140-147) | `builds3.py` | identical (3.22/2.04/1.85/2.57; best spread 1.19 at f 1.2, (1.5,2), r 0.3) |
| campaign v2 table (SR:78-84) | `campaign.py 1e18` (scratch) | identical (27 / 33 / 48.3 / 57.3 d); but it prints W1-W4 only for goal density |
| campaign v3 (SR:126-139) | `campaign3.py 2.25` (scratch) | lin and pow reproduce campaign3_c2.25.json exactly (pow: 9-11 rides, mult 239-322, gates 6.24e15 -> 3.96e19, first ride 8.0 min, 64-73 % / dry 2, 4 in W4; lin: mult 5.5e6-8.5e6, gate W9 2.09e24). Note the lin gate steps are noisy (x1.92 at W6, x5.62 at W7) - gate "x2.5-3.5" is an output of bisection + session quantisation, not a smooth rule |
| population (SR:115-124) | `population.py` (scratch) | identical, v2 regime (lin 8 %, 2x rule) - not v3 |
Not reproducible from committed scripts: the claimed campaign.json (committed file is the 1e19 run); SU:22 tag totals (812/681/54 %); "1.17x" build claim is superseded by build v3 but still sits in SR:98-102 with "adopted in prototype" wording (the prototype's Cast Off/Speed are the v3 numbers, so just relabel as v2); R22/R3 citations as above.

---

## 4. Eight edits to do first
1. Recalibrate gates and report world length with R21/R37 auto-spend and one build on (P0-1); until then caveat R25/DD:8/SU:12 as upper bound.
2. Replace every 1e18 gate / 6.6e21 peak in DD:35,47,71, WT:7, DR:61 with the v3 schedule (P0-2).
3. Split Photo Op (button) from Photo Window (event) and fix DD:56 item 8, WT:3 (P0-3).
4. Rename "Undead Seals" (WT:11) or the L1 currency; rename Form Deck / Agito Forms; finish ratio -> drift in WT:21, SR tables (P0-4).
5. Fix SU:13 / DD:51 "rides alone 64-73 %" to 55-64 % rides / 64-73 % any goal (P0-5).
6. Bring decade_slice_v2.html in line: bounded flat +1 %/world archive (line 40, 55), 8 tiers, Speed II inside the R34c budget, v3 header comment; fix DD:12 "DEV linear" and DD:68 file name; reconcile EV:35 with EV:48 (P0-1, P1-8).
7. Update stale tallies and R-number comments: SU:18, DR:18, DR:37, DR:60, SU:22, anti_patterns.md:29,35, sim/campaign.py:2-4, builds.py:1, DD:1, WT:1, DR:67; and refresh SR:105-107 to events.py output (P1-6, P1-7).
8. Make pacing_report.py and test_sim.py test the v3 pow regime; replace the tautological flat test (P1-9); change WT Press/Heart offline branches and fill the placeholders (P1-10).
