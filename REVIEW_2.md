# REVIEW_2 - second adversarial review (DESIGN_RULES v2, DECADE_IDLE_DESIGN v2, sim v2, slice v2)

Scope: REVIEW_1.md, DESIGN_RULES.md (DR), DECADE_IDLE_DESIGN.md (DD), DECADE_WORLD_TABLES.md (WT), SUMMARY.md (SU), sim/results.md (SR), sim/{campaign,builds,events,test_sim,campaign_sweep}.py, prototypes/{EVALUATIONS.md,decade_slice_v2.html}, research/{events_and_choices.md s5, retention_monetization.md, ui_and_numbers.md}. No other file was edited.
Sim claims below were re-run (scratch copies of campaign.py with patched ride threshold K, unique-goal counting, uneven session gaps, extra carry; the prototype script was run headless in node with a stubbed DOM). Priority: P0 = invalidates a headline number or rule, P1 = fix before building, P2 = polish. Line refs are file:line of the current files.

Headline: v2 fixed many text-level problems from REVIEW_1, but the three numbers everything hangs on (per-point bonus ~8 %, T = 1e6 with a 1e18 gate, carry c about s/1.0-1.2) are tuned in a sim that leaves out most of the carry sources the design itself adds. With the designed carry the "flat 27 d / 48 d" campaign collapses to 12-18 d, and with the archive bonus in the reset table it collapses to 5 d. Details in section 2.

---

## 1. REVIEW_1 issues: resolved vs papered over

| REVIEW_1 item | Status | Evidence |
|---|---|---|
| P0-1 world length vs ratio (R18/R19) | PARTIAL | R23 DR:34 / R25 DR:36 now carry real v2 numbers (27/33/48 d). But R23 is stated as a law ("length proportional to ratio^n") and the sim does not obey it (see 2.4); DR:36 still says "or <=5 days long" while the recommended ratio 1.2 ends at 8.7 d; DD:4 "world 3-4 days" and DD:8 "4.5 weeks flat" (27 d = 3.9 weeks). |
| P0-2 first prestige timing | RESOLVED in text (R10 10-15, R16 7-15, sim 6.6 min at T=1e6), but the first ride now gives only x1.08 (see 2.5) and in worlds 4-9 at ratio 1.2 the first ride is at 480 min, not in session 1 (2.4). R10 says 10-15 min while the sim/DR:25 say 7. |
| P0-3 per-point bonus | PARTIAL | DR:24 now says tune 2-10 % and cites 1-2 %. But headline sim numbers are all at 8 %; DD:12 says 5 % "initially"; at 5 % world 1 takes 4.0 d, not 3.0 (+33 %), at 2 % 7.0 d. DR:24 "keeps final mult 2e2-6e3" is false for the campaign (final x1.1e5, 2.5). |
| P0-4 automation timing | NOT RESOLVED | DR:16 R10 "first automation ~3 min"; DR:30 R21 "first-ride shop contains automation"; DD:84 "7:00 first automation" and "10:00 first ride"; research/events s5.8 explicitly overrides R10 ("3 min is too early"); prototype auto-buys only after the first ride. Four statements, three answers. |
| P1-5 layers/currencies | PAPERED OVER | DD:44 declares <=3 currencies (Shots, world currency, Form Energy) and hides cards/Driver "in the album". Still on screen: Charge (DD:24, WT:7), mastery points (EVALUATIONS:39, 1 per ride), Exposures (DR:55), Swap Tokens (DD:77), re-pick token (DD:78), Time Skip charge (DD:30), Ride Cards. That is 8-9 counters. R26 (DR:37) says world-local currency "from world 2-3" but Kabuto has Charge in world 1. |
| P1-6 offline model | RESOLVED (stepped curve simulated, test_sim.py:19-22), but R33 text is stale (DR:46 "1.5-2x longer", sim v2 shows +10 %, see 3.3) and R33/R34 now disagree on the 8->24 h effect (x1.1 vs x1.3). |
| P1-7 R24 active reward | PAPERED OVER | R34 (DR:47) rewritten, but DD:52 still says "Active <=1.5x (R34)", R34 itself says sessions give 4.2x, Photo Op (prototype +33 %) and Clock Up (about x1.67 duty-cycle average in the prototype) are not inside any budget (2.7). |
| P1-8 monetisation | RESOLVED (R39 default none; DD:62). Leftover: prototypes/EVALUATIONS.md:12 still keeps the "x2 claim" ad placeholder on offline.html. |
| P2-9 smaller mismatches | MOSTLY OPEN | SU:4 still says the cost/rate ratio "kept 97 % of goals ... holds for noisy and lazy players" (one config; 10-min checkers were 28 %, SR:61). R7 DR:11 still tags "augment x1.9" [C] as an endless sink (REVIEW_1: it is a one-off ladder). R20 DR:29 still says AD/Synergism show 4+ layers confuse (they are beloved games). R13b/R11 tallies still [P]. games/kittens-game.md:59 and games/trimps.md:101 still stale. R3 "200 untested" is fixed (campaign uses 200). |
| Sec.2 evidence tags | PARTIAL | New C/P/H scheme is clearer, but R8 DR:12 is tagged [C] while its second half is [Sim H]; R33 "Bitburner 75 % [CODE]" is still offline scripts only. |
| Sec.3 "interactions never simulated" | RESOLVED in spirit (campaign.py) - but see section 3: the sim omits offline auto-buy, every carry source except c, and counts repeated goals. SR header still "draft v1" with no "not validated" banner (SR:1). |
| Sec.4 missing rules | RESOLVED as text (R13, R14, R30, R35, R40-R42 ...). Several have no mechanism (R13 fork, see 2.6; R22 cliff awareness has no design). |
| H1 reset table | RESOLVED (DD:17-27) - but the archive bonus it defines breaks the economy (2.2) and "free respec" is still there (DD:56), which REVIEW_1 said removes the trade-off. |
| H2 L2 formula | RESOLVED (R24) but then re-introduced as a formula inside the reset table (archived Form Energy x(1+0.02*sqrt(total)), DD:21). |
| H3 rides per world | RESOLVED (8-12) but "rides per session <=2" (DD:53) and "each ride >=2x faster" (DR:25, DD:53) fail in the sim (2.5). |
| H4 world objective | RESOLVED for the sim (DD:46-47), not for the slice: prototype gate resets with every ride (4.3). |
| H5 endgame / L3 | STILL THIN: L3 "log-scaled formula" (DD:14) has no reset/payout definition. |
| H6 decisions | PARTIAL (builds sim exists, flawed, 2.6). |
| H7 upgrade-family matrix | NOT DONE; DD:73-84 is a systems roll-out, not a family x world matrix, and conflicts with DD:84 (2.3). |
| H8 s and c numbers | PARTIAL: s=3, c=3/2.5 given (DD:50), but "passive income of cleared worlds" (DR:40 R29) has no number and is not in the sim. |
| H9 Kabuto rule | PARTIAL: Cast Off moved to 40 (good). "Phylloxera Mirror (ride that copies build)" is still a fourth reset-like object (DD:35, WT:7); Cast Off "sheds a tier" (DD:35) is implemented as a plain multiplier in both builds.py and the prototype. |
| H10 lore claims | RESOLVED (DD:65). |

---

## 2. Priority issues

### P0-1. Carry sources not in the sim make the pacing plan false (R23, R25, R29, R38c, DD:21, DD:50)
- campaign.py:13-14 models carry only as `c**w`. The design adds, on top of c: Ride Cards +10 % each (prototype line 37), archived Form Energy x(1+0.02*sqrt(total)) (DD:21, prototype line 37), achievements 1.05^rows*1.01^count up to x10.1 (DR:56, SR:105), mastery cross-world nodes, Driver forms, "cleared worlds raise passive income" (DR:40). SR:105 even says "cap near x10 so it doesn't overwhelm world carry (c about 2.5-3)" - it does.
- Re-run (3 sessions/day, goal 1e18, T0=1e6, 8 %/pt), days per world W1..W9:
  - ratio 1.0, c only: 3.0 x9 = 27 d (DD:50)
  - ratio 1.0 + cards: 3.0 ... 2.0 (22 d); + achievements: 3.0 ... 0.7 (15 d); + both: 3.0, 2.3, 1.7, 1.3 ... 0.3 (12 d)
  - ratio 1.2, c only: 3.0 -> 8.7 (48 d); + cards + achievements: 3.0 -> 1.3 (18 d)
  - ratio 1.0 + the DD:21 archive bonus (sim seals, ~1.4e6 per world, sqrt gives x24 after W1) + cards: W1 3.0 d, then 0.3 d for every other world (5 d total).
  - Raising T0 to 1e10 to shrink seals instead: W1 = 136 d. T0 sensitivity is x2 per x10 (SR:91), so "tune T_w in play-test" is a very sharp knob.
- Proposed edits: DR:34 R23 and DR:40 R29: "The ratio is s / (c x all other permanent multipliers). Compute total permanent carry per world, including cards, archive, collections and tree, and budget them inside c; the sim must include every one." DD:21: replace the archive formula with a bounded bonus, e.g. +1 % per cleared world (flat), or make it replace part of c rather than add to it. DR:56 R38c: apply the achievement multiplier only inside its own world (or cap at x2 total) and re-run. Add to campaign.py a `extra_carry(w)` hook and include cards and archive in the reported table.

### P0-2. Per-point bonus, T and the 1e18 gate are mutually inconsistent across documents (R15)
- Campaign (campaign.py:61, SR:75): T0=1e6 with a 1e18 gate gives about 1.4e6 Seals per world and a final ride multiplier of 1+0.08*1.4e6 = about 1.1e5 (my run: seals 1.37e6).
- DR:24 says "5-10 %/pt keeps final mult 2e2-6e3"; SR:26 calls 9e4 "explodes"; research/ui_and_numbers.md:157 assumes "T sized so a world needs about 100 points, multiplier about 6". Three incompatible regimes (6, 6e3, 1e5) all cited as supporting the same rule.
- R16 (DR:25) "each ride >=2x faster than the last run's start" does not hold. Ride multiplier ratios in world 1: x1.08, x1.22, x1.55, x2.02, x6.0 ... (first 3 rides under 2x; the first ride is +8 %, i.e. almost nothing, and the R17 "pending >= 2x current" test is vacuous when current is 0, campaign.py:43).
- Proposed edits: DR:24 R15 - drop the "2e2-6e3" claim, state "campaign sim gives ~1e5 at 8 %/pt, T0=1e6, gate 1e18 (about 6 orders of magnitude of Seals); either reduce exponent/bonus or accept and cap with per-world display". DR:25/DD:53: add "ride 1 must pay >= x2 (give R21's first-ride bonus a number, e.g. x2 flat for the first ride) and require pending >= 2x current AND >= 5 Seals". Re-run campaign with a first-ride bonus.

### P0-3. Goal counting inflates the "goal density" and "dry session" results (R25, SU:13)
- campaign.py:40 appends an event for every first purchase of a tier and every milestone count in every run, so rides re-count the same ladder: world 1 logs 343 goals; only 55 are distinct (8 tier unlocks + 40 milestones + 11 rides; matches the "about 60" in SR:87/DD:51 only because it was computed by hand, not by the code). SR:75/87 percentages come from the 343 repeated events.
- With unique goals only (patched copy), ratio 1.2: W4 83 % of sessions, W9 62 % with 5 dry sessions in a row (the repeated-goal metric gives 69 %, max dry 5). SR:80-81 only reports W1-W4 (`[:4]` slice at campaign.py:79, so the table shows 83-100 % and max dry 2 for ratio 1.2 and 79-100 % / 2 for ratio 1.25). Full per-world data: ratio 1.2 max dry [0,1,1,2,2,2,3,4,5]; ratio 1.25 max dry up to 7 and 56 % of sessions with a goal in W9. The recommendation "ratio 1.0-1.2" (DR:34) therefore ends with 1.7 days of nothing in W9.
- Proposed edits: campaign.py: count a goal once per world (set of (tier,count)) plus rides; remove `[:4]` in the print and show W1-W9. SR:80-84, DR:34, DR:36 and SU:12-13: replace "83-100 % / 2 dry sessions" with the full range; DR:36: "ratio >1.1 needs a content-beat schedule for W6-W9 (>= 6 unique beats per session-day)".

### P0-4. R23 "world length proportional to (s/c)^n" is not what the sim shows, and "flat" is a tautology
- When s = c every world is an exact rescale of world 1 (cost, gate and T all multiply by s^w, production by c^w), so "3.0 d x 9" and test_sim.py:30-33 (`max/min < 1.5`) cannot fail. It is not evidence for anything.
- For s != c, 1.2^8 = 4.3x predicts 12.9 d in W9; the sim gives 8.7 d (2.9x). 1.25: predicted 6.0x, sim 3.8x. 1.07: predicted 1.7x, sim 1.33x. The law is sublinear (rides absorb the difference; T scales with cost but not with c). Also each world is quantised to 0.33 d (one 10-min session per 8 h), so 3.0/3.3/3.3/3.7 for ratio 1.07 are 1-session steps (11 % each), not trends.
- First-ride timing drifts with ratio: at ratio 1.2, first ride is at 6.6, 7.9, 9.5 min for W1-W3 and 480 min (session 2) for W4-W9 (T scales with s^w but production with c^w). DR:25 and DD:53 "first ride <= 15 min" and DD:7/R10 "<= 60 s first purchase" are only true for the first three worlds.
- Proposed edits: DR:34 "length grows about (s/c)^(0.65 n) [Sim H, quantised to one session]"; scale T_w with the carry (T_w = T0*c^w, equal to T0*s^w only when c = s; campaign.py:14 uses s^w) and re-run so first ride stays <=15 min in all worlds; replace test_sim.py:30-33 with a test at ratio 1.2 asserting the W1-W9 monotone sequence and a first-ride-time bound.

### P0-5. Stale rules from v1 numbering and contradictory budgets (R26 one-new-thing, R33/R34, active budgets)
- R26 (DR:37) "exactly one new rule/verb per world" vs the actual content: DD:35 W1 has Clock Up + Cast Off + Charge + Photo Window (DD:76) + mastery tree + Zecter roster; DD:76-77 W2 adds Contracts (rule) + Album + Form Deck + swap tokens; WT:10 W4 adds Advent Cards + Constraint Shoots; W5 adds Fusion + Studio Garden. That is 2-4 new systems in W1-W5. Also DD:77 puts Album/Form Deck in W2 while DD:84 (first 10 minutes) has "4:00 first Form" and "5:30 album entry" in W1.
- research/events s5.3 says the Garden board unlocks "at first Ride (min 8-10)", DD:80 puts it in W5; the board needs 9 cards while the campaign yields 1 Ride Card per world (about 4 by W5) plus about 0.2 card shards per day.
- R33 vs R34: DR:46 "cap beyond 8 h buys x1.1" and "stepped is 1.5-2x longer than flat"; DR:47 "x1.3 for 8->24 h". My runs: stepped vs flat 0.5/0.5 is 3.0 d vs 2.7 d (+10 %), not 1.5-2x (that was the no-prestige v1). 8->24 h: spd 1: 9.0->7.0 d (x1.29), spd 2: 4.5->4.0, spd 3 (gap 7.8 h < 8 h): no effect by construction (campaign.py:56). So "cap barely matters" is just a statement about gaps shorter than the cap; uneven schedules (12/12 h gaps) gain x1.1 from 24 h.
- Reference player is 3 sessions/day (DR:36, DD:4, tables), 2 sessions ("size for ~5.8 d", DR:47 - actually a median over mixed configs; the headline config at 2/day is 4.5 d) and 5.3 sessions/day (DD:62). At 1/day the flat campaign is 81 d, at 6/day 16 d. Pick one and say what the others get.
- Proposed edits: DR:37 "Each world adds exactly one new *rule*; additional systems are introduced at most one per world, listed in DD s12". Fix DD:84 so the timeline matches DD:73-81 (move Form/Album out of the first 10 minutes or move the roll-out). DR:46 delete "1.5-2x" (state +10 %). DR:47 change "x1.3 for 8->24 h" to "x1.3 at 1 session/day, ~x1.0 at >=3". DD:52 replace "Active <=1.5x (R34)" with the real R34 numbers.

### P0-6. Prototype slice v2 does not implement what the sim assumes, and has gameplay bugs
(line numbers: prototypes/decade_slice_v2.html)
1. Gate resets with every ride (line 50 `S.life=0`; gate test line 63 `S.life<gl`): the sim gates on cumulative `life`, the slice on one run. Headless (node, stubbed DOM, cheapest-affordable bot): world 1 gate (3e6, line 27) is cleared at 14.3 min after only 2 rides, not 3 days; world 2 (3e8) is reachable in the first 3 h. GOALMULT [3e6,3e8] vs sim 1e18*3^w: the slice cannot be used to judge world length, and EVALUATIONS.md:35 "94 % in band" is an in-band result of a 25-minute run.
2. Hidden/background tab bypasses the offline model: tick (line 73) credits `(performance.now delta)*prod` at 100 % with no 8 h cap and no 50/25 curve; `offline()` (line 55) only runs at load. A throttled tab earns more than a closed tab. Fix: clamp dt (e.g. `Math.min(dt, 1)`) and route longer gaps through the offline function on `visibilitychange`.
3. `render()` rebuilds `#gens` and `#tree` via innerHTML every 100 ms (lines 66-68, 76): a click with mousedown/mouseup spanning a rebuild is lost, and touch taps often miss; headless bots call the handlers directly, so EVALUATIONS.md:35 never saw it. Fix: update text/disabled in place, or re-render only on state change.
4. `carry` (line 37) stacks cards (+10 % each) and sqrt(archived Seals) on 3^w, so effective ratio is below 1 (the "trivial" region of R23). See P0-1.
5. Clock Up (lines 49, 72-73): Charge +1 per 6 s, cost 5, lasts 10 s x3 (x5 with Speed II) means a duty cycle of about 33 % -> average x1.67 (x2.3) for an active player, plus Photo Op +33 % (15 s of income per 45 s). Together about x2.2 active vs 0 offline, against R34 "<=1.2x" and DR:55's 1.03-1.06. Neither is in builds.py or events.py.
6. Cast Off (line 35) multiplies every tier at >= 40 owned; builds.py:28 only tiers >= index 3. The values "adopted in the prototype" (SR:100) were not what was simulated.
7. Smaller: stale rule numbers in the header comment (line 25 "R12 ... R15 ... R23", v2 numbering is R15/R19/R33), same localStorage key as decade_slice.html (line 31 / v1:27 - loading a v1 save in v2), `fmt` prints 2.50e+13 (violates R40 "no e47"), white full-screen flash on Dimension Ride (line 51; ui_and_numbers.md:148 "no flashing"), auto-buy always picks the cheapest affordable item (line 75) which is not the payback-greedy policy the sim uses (so sim timings do not apply after ride 1).

### P1-7. Build balance (R13b) rests on an under-powered measurement
- builds.py:14 gives every build `pts=min(len(rides),3)` all in its own branch; a real player earns about 11 mastery points per world (rides) and the tree costs 9 in the slice (EVALUATIONS.md:39), so by about ride 8 the player owns all three branches. There is no fork after the first third of the world; "first fork within 5 min" (DD:56, DR:19) is also impossible because points arrive only from rides (first ride 7-10 min).
- builds.py:28 `castoff` changes `prod` but the greedy `g` in campaign.py:30 does not see the Cast-Off bonus, so the bot undervalues that build.
- The claimed "1.17x spread" (DR:20, SR:99) is exactly one session of quantisation (2.0 d vs 2.33 d, 6 vs 7 sessions; the third scenario is 1.33 vs 1.33 d). It cannot distinguish "balanced" from +-17 %.
- DD:56 keeps "free respec"; at 3 branches and abundant points that removes the decision entirely.
- Edit: DR:20 R13b: "measured with a 3-point budget and one-session resolution; real point supply (about 11/world) makes the fork transient; either cap points at 3-4 per world or make nodes mutually exclusive". Make the first fork a Crew/Approach choice at 2:00 (events s5.5) or drop "within 5 min". Run builds with greedy `g` that includes the build multiplier and with 0.1-day resolution.

### P1-8. Events numbers (R38/R38b) do not reproduce
- SR:104 / DD:77 "best deck +17.6 % vs median, +41 % vs worst": events.py:43-56 only computes top-1 vs top-3 (mean 1.1 %, p90 1.9 %; np.random is not seeded). The 17.6/41 numbers are not produced by the committed code (my runs 1.1 %).
- events.py:15,31: the windfall is `min(0.15*bank_s,600)` with `bank_s=450` fixed; at session start after a night the bank is thousands of production-seconds, so a windfall is up to 613 s (7x the modelled 80 s) and first-window EV is much higher; the exposure bank (line 31) is added once per day regardless of sessions/day. research/events s5.1 says "EV about 10 min of production each" while the code says 119 production-seconds (5x apart); the "+40-60 % active" in s5.1 matches the code, the 10 min does not.
- R38 (DR:53) 13 s window, 5-15 min spacing, while R38b (DR:55) is 90-240 s foregrounded; DD:56 still describes the 5-15 min version; s5.1 uses a 15 s lifetime.
- Edit: delete or recompute the +17.6/+41 figures (SR:104, DD:77); add a seed and the median/worst computation to events.py; in DR:53 label R38 as superseded by R38b; make the windfall depend on actual stock.

### P2-9. Smaller number and wording mismatches
- DR:60 R40a and DD:71 use s=4 for the 6.5e22 peak; the plan uses s=3 (gate 6.6e21 at W9, DD:50, ui_and_numbers.md:153).
- DR:28 R19 "60 % of tiers" = 4.8 of 8; campaign.py:43 uses maxtier>=3 (4 of 8, 50 %); prototype 4 of 6.
- campaign.json in the repo is from a different goal (1e19: 5.0 d, 12 rides, 392 goals); SR's 3.0 d table needs `python3 campaign.py 1e18` which is not recorded (default goal_mult is 1e9 -> 0.7 d/world). Record the argument in the header and write the JSON name by argument.
- SR:44-51 (v1 decade model: "1.3 d per world", "c about 0.8-1.0 s") and SR:12-19 ("[1.0, 1.5]") still sit above the v2 section that supersedes them; SU:10-11 (item 8) still quotes the v1 "0->25 % = 9x, 4x sessions = 1.5x" next to the v2 "4.2x" in one bullet.
- DD:12 vs DR:24: 5 % per point vs sim 8 %. DD:53 "rides per session <=2": world 1 has 3 rides in one session (day 2, minutes 1440/1443/1448).
- Terminology drift: "Form" now names Form Energy, Final Form Ride, Driver forms, Form Deck, Agito forms and Kabuto's Rider Form; sim/prototype call the L1 currency "Seals". Rename (e.g. Form Energy -> Film Points or keep "Seals") before content writing.
- research/ui_and_numbers.md:154 uses growth 1.15 and tier x10 while the design is 1.12 and x8; the 1.4e12 / 1e8 figures should be recomputed (200 owned at 1.12 = 6.8e9 multiplier, top tier unit about 2e17*s^8).
- prototypes/EVALUATIONS.md still uses v1 R-numbers (R12-R15, R17, R21, R23, R24) throughout.

---

## 3. Sim code review (answers to the specific questions)
1. Greedy bot: payback greedy, omniscient (acts at the exact second a purchase is affordable, 100 % attention for 10 min), never plans for tier unlocks, buys nothing during offline (campaign.py:56-57), so R21 auto-buy and R37 auto-spend are not modelled; with auto-buy the offline gold would compound and worlds would be shorter. Ride policy: tested K (ride when pending >= K x Seals): K=1..5 give 3.0-3.3 d (robust), K=10 5.7 d, K=30 8.7 d; with no rides (T=1e30) the gate is not cleared in 400 days. Rides are mandatory for clearing; a player who rides rarely loses 2-3x.
2. Goal counting: repeated goals (P0-3).
3. Quantisation: the world is cleared at the next session start after the gold arrives (a player must log in to hop, so this is defensible), but resolution is 0.33 d (11 %): all differences below that (ratio 1.0 vs 1.07, builds spread) are noise. Uneven schedules matter more: gaps 4/6/14 h -> 3.2 d, 12/12 h -> 4.5 d, 5/19 h -> 5.0 d (vs 3.0 d for 8/8/8), because the 8 h cap wastes the long gap.
4. T scaling: T = T0*s^w (campaign.py:14) assumes c = s; see P0-4.
5. "ratio" is used for two things: R2 cost/rate per tier (1.2-1.5, 8/6 = 1.33) and R23 cost_scale/carry (1.0-1.2). SU:4 and SU:12 use the same word. Rename the second "world drift" (d = s/c).
6. test_sim.py: five tests pass; none exercises rides, the stepped-offline edge past the cap with a ride, events.py or builds.py; `test_no_softlock_after_reset` (line 23-27) ends with `assert W.done() or W.t>0 and ...` which is always true, and `W.events[0] < 120` is true because the world starts with exactly the first tier's cost. Add: monotone W1-W9 at ratio 1.2; first ride < 15 min in every world; unique-goal count per world; ride multiplier ratios.
7. Robustness section (SR:53-63): claims "good/bad ranking independent of strategy" - only for the pre-ride 3 h model; it was never repeated in the campaign model.

---

## 4. SUMMARY / DESIGN_RULES numbers that do not match results
| Claim | Where | Actual |
|---|---|---|
| ratio 1.25 -> "3 -> 11.3 d with 2 dry sessions" | DR:34, SR:84 | W9: 56 % of sessions with a goal, 7 dry sessions in a row; ratio 1.2 W9: 69 %, 5 dry |
| "final mult 2e2-6e3" at 5-10 %/pt | DR:24, SU:7 | campaign W1 x1.1e5 at 8 %/pt |
| "8->24 h x1.3" | DR:47 | x1.29 only at 1 session/day; x1.0 at >=3; DR:46 says x1.1 |
| stepped offline "1.5-2x longer than flat" | DR:46 | +10 % in sim v2 (3.0 vs 2.7 d at 8 %/pt) |
| "size worlds for the 2-session median (5.8 d)" | DR:47, SU:10 | median over 144 mixed configs; headline config at 2/day = 4.5 d |
| "4.5 weeks flat" | DD:8 | 27 d = 3.9 weeks (4.5 weeks = ratio 1.07, 33 d) |
| "about 60 goals, >=1 goal in 90-100 % of sessions" | DD:51, SR:87 | code counts 343 (repeats); unique 55; W4+ at ratio 1.2 drops to 83 % then 62 % |
| best deck +17.6 % vs median / +41 % vs worst | SR:104, DD:77 | not computed by events.py (top1-vs-top3 = 1.1 %) |
| Active <= 1.5x | DD:52 | R34 says sessions give 4.2x; no active budget exists |
| builds within 17 % | DR:20, SR:100 | one-session resolution; 3 points; prototype uses different Cast Off |
| peak 6.5e22 | DR:60, DD:71 | s=4; plan uses s=3 (6.6e21) |

---

## 5. Eight items to do first (proposed edits, in order)
1. Add every permanent carry source to campaign.py (cards, archive, achievements, tree, passive income) and re-publish the world-length table; replace the DD:21 archive formula with a bounded bonus. (P0-1)
2. Fix the Seal economy: choose T so a world yields ~100-1000 Seals (not 1e6), give the first ride a numeric bonus, and update R15/R16/R17 claims (final multiplier, "each ride >= 2x"). (P0-2)
3. Count unique goals, report W1-W9, and drop "ratio 1.2 is fine" unless W6-W9 get a beat schedule. (P0-3)
4. Rewrite R23 as sublinear and make T_w follow c^w so first ride stays <=15 min in all worlds; replace the tautological flatness test. (P0-4)
5. Reconcile R26/DD:73-84 (systems per world, first-10-minutes timeline) and R33/R34/DD:52 (offline, sessions, active budgets); pick one reference player. (P0-5)
6. Fix the slice: cumulative gate, dt clamp/visibility handling, in-place render, same Cast Off as builds.py, world goals from the sim. (P0-6)
7. Redo builds with correct points supply, build-aware greedy and finer resolution; drop "free respec" or the 5-minute fork claim. (P1-7)
8. Remove or recompute unreproducible events numbers (+17.6/+41, windfall bank) and mark R38 superseded; add the missing stale-ref clean-ups (EVALUATIONS R-numbers, SU:4/SU:10, SR banner "not validated against humans"). (P1-8, P2-9)
