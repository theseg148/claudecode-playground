# REVIEW_1 - adversarial review of DESIGN_RULES.md, DECADE_IDLE_DESIGN.md and sources

Scope read: DESIGN_RULES.md (DR), DECADE_IDLE_DESIGN.md (DD), SUMMARY.md (SU), sim/results.md (SR), analysis/*.md, research/formula_tables.md, research/{psychology,player_complaints,math_of_idle_games,design_talks_postmortems,decade_worlds}.md, prototypes/EVALUATIONS.md, sim/prestige_sweep.py, and spot checks of games/{cookie-clicker,kittens-game,trimps,leaf-blower-revolution,progress-knight,afk-arena,bitburner,synergism}.md. No other files were edited.
Line refs are `file:line`. Priority: P0 = contradicts or invalidates the plan, P1 = fix before v2, P2 = polish.

---

## 1. Contradictions between documents

### P0-1. World length: R18 (ratio 1.0-1.3) cannot coexist with R19 (3-5 days per world, 9 worlds = 5-8 weeks)
- DR:29 R18 says ratio cost_scale/carryover 1.3 means "each world ~30 % longer"; DR:30 R19 and DD:12 say 3-5 d per world.
- Arithmetic: ratio 1.3 over 9 worlds is 1.3^8 = 8.2x from W1 to W9. If W1 (Kabuto) is ~1 d (DD:12), W9 is ~8 d and the campaign is ~32 d. If W1 is 3 d, W9 is ~25 d and the total is ~96 d (14 weeks). Ratio 1.0 gives equal worlds, so only ratios of about 1.0-1.07 fit "3 to 5 d".
- 9 x 3-5 d = 27-45 d = 4-6.5 weeks (and ~1 d for Kabuto lowers it), but DR:30 and DD:12 say 5-8 weeks. SR:51 says "4-6 weeks". Three different totals.
- SR:18 gives the usable band as "[1.0, 1.5]" and SR:51 as "c ~0.8-1.0 s" (ratio 1.0-1.25). R18 says 1.0-1.3. Three different bands for the same parameter. R18's "above 1.5 become walls" has a single data point at ratio 5 (carry x2, cost x10, SR:17); 1.5-5 is untested.
- Proposed edit, DR:29: "R18. choose cost_scale/carryover in [1.0, 1.1] if worlds should stay within 3-5 d; ratio 1.3 doubles world length every ~2.6 worlds (x8 over 9 worlds) and is only acceptable if W1 is ~0.5 d. [SIM, toy]". DR:30: "Target ~3-5 d per world (ratio ~1.0-1.07); 9 worlds = 4-6.5 weeks". Make DD:12, SR:51 and SU:13 use the same numbers.

### P0-2. First prestige timing: 10-15 vs 10-25 vs ~25 vs 20-90 min
- DR:16 R9 says first ride unlock 10-25 min; DR:21 R12 says "first gain lands at ~25 min"; DD:9 says 25 min; SU:9 says 10-25 min; SR:23 uses 20-90 min as the "satisfying" band.
- analysis/anti_patterns.md:91 says first ride "within 10-15 minutes (C6 postmortem said 25-35 min was late)"; research/player_complaints.md:158 says the same; research/design_talks_postmortems.md:182 says "around 10-15 minutes". The project's chosen target (25 min) is exactly the value its own postmortem source calls "too late".
- The sim band 20-90 min was chosen by the author (research/../prestige_sweep.py: `20<=first_min<=90`), so "23/108 configs satisfy" is circular.
- Edit: DR:16 "first prestige/ride unlock 10-15 min (postmortem: 25-35 min too late); sim only shows T=1e8 gives ~25 min, so lower T to ~1e7 and re-run". DR:21 delete "so first gain lands at ~25 min" or change to ~12 min. Also prototypes/prestige.html uses T=1e6 which SR:24 calls a "tutorial reset" - note this.

### P0-3. Per-point prestige bonus: 5-10 % (DR) vs 1-2 % (source blueprint)
- DR:21 R12 and SU:8 say +5-10 %/point; research/design_talks_postmortems.md:233 says "bonus per point 1-2 % so the second run beats the first by 2x-4x"; research/math_of_idle_games.md:3.2 says the bonus must make 4x earnings arrive faster than the previous cycle.
- The 5-10 % came only from a sweep of {5, 10, 25 %}; no value below 5 % was tested, and the "25 % explodes" result (SR:26) is conditioned on exponent 0.7, which DR:21 drops.
- Edit: DR:21 add "(sweep tested only 5/10/25 %, exp 0.4/0.5/0.7; 25 % explodes at exp 0.7; Pecorella-style 1-2 %/pt untested) [SIM, hypothesis]".

### P0-4. Automation timing: first automation at 3 min (R9) vs only after first ride (R17, DD:34)
- DR:16 says first automation ~3 min; DR:26 R17 / DD:34 say auto-buy comes from the first Ride shop (~25 min). C4 ("not idle") in analysis/anti_patterns.md:93 says "unlock early". Pick one. Proposal: a cheap, priced "Zecter Hand" auto-buy for tier 1 at ~3 min (B10: automation as priced milestone), the full auto-buy-cheapest in the Ride shop.

### P1-5. Layers/currencies exceed the limits the rules set
- DR:25 R16: max 2-3 reset layers; DR:31 R20 and DD:28: <=3 visible currencies. DD:9-11 defines L1 Final Form Ride, L2 Dimension Ride, L3 All Riders, plus mastery tree, Ride Cards, Decade Driver forms (DD:33-37). Visible currencies: Shots, Charge (Kabuto, DD:19), world currency, L1 points, L2 points, Ride Cards = 5-6. Kabuto's table cell says currency "none" (DD:19) yet the rule spends "Charge".
- DR:31 R20 says world-local currency "from world 3", but DD:20 gives Den-O (world 2) Train Tickets.
- Edit: DD:28 add an explicit currency budget (e.g. Shots + one world currency; L1 points shown only on the ride screen; L2 = cards, not a currency), and fix DD:20 or DR:31.

### P1-6. Offline model: three versions
- DR:36 R23: 50 % for 2 h, 25 % beyond, cap 8 h; DD:35: efficiency 50 -> 75 %, cap 8 -> 24 h via upgrades; analysis/beloved_patterns.md:102 and anti_patterns.md:96: flat ~50 %, 8 h; research/math_of_idle_games blueprint (design_talks_postmortems.md:234): cap 2 h at start. The sim (SR:29-42, SR:44) used flat eff 0.5 capped 8 h. The stepped 50/25 curve of R23 was never simulated: for a 3x10 min/day player (about 8 h gaps) average efficiency is (2x0.5+6x0.25)/8 = 0.31, so R19's "~4 d" (SR:34, eff 0.5) becomes ~6-9 d (SR:34 eff 0.25 = 6.3 d).
- Edit: DR:36 either simulate the stepped curve or state "sim used flat 0.5; stepped 50/25 curve unsimulated, expect world length x1.5-2 for casual".

### P1-7. R24 is not a design lever and double-counts with the Photo Op
- DR:37 R24 "Active play must be rewarded only mildly (<=1.5x for 4x the sessions)" is the output of the toy sim (SR:39: 4x sessions = 1.5x faster) with zero active mechanic. Adding DD:38's Photo Op (<=1.5x) on top gives >1.5x total. Reword: "the active layer must add <=1.2x average on top of the ~1.5x the session count already gives" and cite a number (beloved_patterns.md:103 suggests x3 for 30 s per 5 min = ~1.2x average if always claimed).

### P1-8. Monetisation: R26 vs anti-patterns vs DD
- DR:41 R26 permits "time-skip sold"; analysis/anti_patterns.md:92 says never sell time-skips as main revenue; DD:47 allows a "rewarded x2 offline claim" (an ad hook) while research/player_complaints.md:C2-C3 says ad-gated progress is the biggest churn trigger and SR:36 shows offline efficiency is the dominant pacing lever (a x2 offline claim is therefore a pacing gate). Edit R26: "cosmetics only; any rewarded ad is a one-time, skippable x2 claim that never exceeds the free 50 %->75 % path".

### P2-9. Smaller number mismatches
- SU:4 (item 2) says the ratio band "kept 97 % of goals in a 15-600 s band" - that is one config (1.12/8/6/x2, SR:6-8), not "the ratio band"; SR:62-63 has the robustness table (84-97 %, 28 % for 10 min checkers).
- SU:6 (item 4) "walls >30 min correlate with quitting [SIM/complaints]": the sim has no quit data; the 30 min wall threshold is an author definition (SR:3).
- DR:8 R3 lists 10/25/50/100/200 but the sim only used 10/25/50/100 (prestige_sweep.py, SR:62 "good" config); 200 is untested.
- DR:7 R2 says tier cost x8-12 but the sim's best examples include 20/14 (SR:5) and the sim has 8 tiers while DD:8 has 6 (growth of the 3-h sweep horizon vs a 6-tier world may differ).
- DD:9 "8-14 times per world over its 3-5 days only if world is much longer; initial worlds use 3-6 rides" is incoherent (8-14 resets was a 6 h continuous-play result, SR:25) - rewrite with a concrete number (see DD hole 3 below).
- DR:6 R1 "Kittens 1.12-1.15 [CODE]" ok for field/most buildings, but hut 2.5 and barn 1.75 in the same source (formula_tables.md Kittens row); R1 should say "production buildings". games/kittens-game.md:59 still says ratios "NOT confirmed" (stale vs its own line 65 [CODE]).
- games/trimps.md:101 says "the cost curve, not a hard cap, is what limits perk levels", contradicting games/trimps.md:19-20,49 (caps 15 and 10) that DR:11 R6 relies on.

---

## 2. Evidence tags that overstate the support

| Rule | Tag in DR | What the sources actually say | Proposed tag |
|---|---|---|---|
| R3 DR:8 | "AD x2 per 10 bought [CODE]" for milestones at 10/25/50/100/200 | AD is x2 at every 10 (formula_tables.md Sec.2); 25/50/100/200 is AdCap, which is [S]/secondary (growth_curves.md:3 table; unverified x3/x4) | [CODE] for "x2 per 10", [S/PUB] for 25/50/100/200; 200 [GUESS] |
| R6 DR:11 | "Leaf Blower combo caps [S]" | games/leaf-blower-revolution.md:49 is a lesson/suggestion, the shop rows [S] show max levels only for "~624 shown max" and no cap; "5-15 levels" has no source | Trimps [S] only; "5-15" [GUESS] |
| R7 DR:12 | Bitburner "augment price x1.9/level" | x1.9 is per augmentation bought in a run (one-off), NeuroFlux 1.14 per level (formula_tables.md Sec.3) | Say "NeuroFlux x1.14 per level [CODE]; x1.9 per aug is a ladder, not an endless sink" |
| R8 DR:15 | [SIM] "97 % goals in band" | The band (15-600 s) and "wall" (30 min) are author-defined and the sweep score maximised in-band fraction (SR:3) - circular. Applies to the first 3 h, not to multi-day worlds | [SIM, self-defined band] + [GUESS] |
| R9 DR:16 | [PUB] and [SIM] for "10-25 min" | Single-author blogs say 10-15 min; sim band is 20-90 min | [PUB 10-15], see P0-2 |
| R12 DR:21 | "sqrt used by AdCap/Realm Grinder/Synergism [CODE/PUB]" | Only Synergism L1 is [CODE] (formula_tables.md Sec.3); AdCap/RG sqrt is [PUB] from a secondary GitHub synthesis; CC is cbrt [CODE], AD is log of log [CODE], Egg Inc 0.14. T=1e8 is a sim unit, not portable | [CODE] Synergism, CC cbrt; [PUB] others; T "tune to hit 10-15 min" |
| R13 DR:22 | [PUB] "2x" | math_of_idle_games.md 3.2 says secondhand excerpt of "+50 % to +200 %"; "2x" in sim is the player's rule, not a design requirement | [PUB, secondhand] |
| R15 DR:24 | "[SIM guard; GUESS on 60 %]" | SR:27 lists it as a rule of thumb, but the sweep did not vary it (6 tiers fixed); it is a code guard in the toy sim, not a finding | [GUESS] only |
| R16 DR:25 | "[analysis/prestige_designs.md]" "4+ layers confuse (CH, Synergism, AD)" | AD's EP/Reality layers and Synergism's 5 layers are among the *beloved* games (beloved_patterns.md:46: Synergism 5 layers, AD 3+); only CH2 is a recorded complaint. A3 evidence on complexity is "weak" (anti_patterns.md:41-43) | [OPINION], count "2-3" as a GUESS |
| R18 DR:29 | [SIM] | Pure closed form s/c with no player decisions, no in-world prestige (SR:19); example numbers are the model's own | [SIM-hypothesis] |
| R19 DR:30 | Flagged GUESS, but "~2 days for a heavy player" is claimed [SIM] | Decade model (SR:44-51) is quantised to 0.33 d, "world clear = top tier x25" is arbitrary, base cost 2e3 is a scale choice (SR:51) | [GUESS] |
| R21 DR:32 | "Progress Knight 1+maxLevel/10 [CODE]; AFK Arena income grows with stage [S]" | PK: multiplier applies to *XP of one task*, and PK Rebirth Two zeroes maxLevel (games/progress-knight.md:37); AFK Arena is [PUB-ish]/[EST] (games/afk-arena.md:10,22), not [S] | [CODE] for PK formula only; "best-result" meaning in Decade is undefined (hypothesis); AFK [PUB-ish] |
| R23 DR:36 | "Bitburner 75 % [CODE]" etc. | Bitburner 0.75 is for *offline scripts*; Synergism 3-day cap is buffed by PCoin purchases; AFK Arena 12 h [PUB]; the stepped 50/25 curve has no source | The curve itself [GUESS/SIM-untested] |
| R10/R11 DR:17-18 | "14/14", "~30/37" | beloved_patterns.md:8 and anti_patterns.md:8 say the tallies inherit [M]/[E] weakness and "belovedness" is a judgement | Add [TALLY, weak evidence] |
| R14 DR:23 | "psychology.md loss aversion" | psychology.md:83-91 cites Gal & Rucker 2018 against a general loss-aversion claim; table says "contested magnitude" | Cite endowed progress / Pecorella pending-gain readout instead |
| SU:7 (item 5) | "[CODE]" on sqrt for AdCap/RG | as above | [CODE/PUB] |

---

## 3. Rules resting only on the toy sim: relabel as hypotheses
The sim is greedy, single-player-strategy, 3-6 h horizon (except the sessions and decade models), no mid-world decisions, and optimises author-defined "goals" (first tier buy or milestone).
- R2 ratio 1.2-1.5, R3 (x2 vs x3, first milestone at 10), R8 (band, median 45 s), R9 (first-prestige band), R12 numeric parameters (T, 0.5-0.7, 5-10 %), R13 (2x rule), R15, R18, R19, R23 (eff 0.5), R24 -> tag them `[SIM-HYP]` and add to SR a header "Not validated against a human".
- Interactions never simulated: prestige inside worlds + carryover + offline together (SR:19 caveat, SR:44 has no prestige; SR:21 prestige has no offline/sessions). DD:9-12 combines all three and then quotes numbers (3-6 rides per world, 25-min first ride, 3-5 d) that no run produced. Run `decade_model.py` with prestige + 8 h/50 % offline + 3x10-min sessions before publishing v2.
- A 6-tier world with 5 milestones per tier gives roughly 6 + 30 = ~36 "goals" (+25 mastery nodes). Spread over 3-5 days (4,300-7,200 min) that is one goal per ~100-200 min on average, which breaks the R8 band (15-600 s, max 30 min). R8 is a first-3-hour result and cannot hold for a multi-day world. Either R8 should say "applies to the first hour of each world", or each world needs ~10x more goals (more milestone tiers, per-tier upgrades, mastery nodes with timed costs).
- Sim first prestige scales with the whole world cost; in a 3-5 day world the intended 20-45 min ride cycle (SU:8) is inconsistent with a 3x10-min/day player whose longest decision window is the 8 h offline cap. State rides per day instead (e.g. 1 per session).

---

## 4. Missing rules the research supports but DESIGN_RULES omits
Add these as R28+ (with source):
1. **Build fork in the first 5 min and >=2 viable builds** (player_complaints.md:158 item 4, C5; beloved B4; psychology.md:148; anti_patterns.md:94). DR has no choice rule at all, only pacing/numbers; DD's families (DD:31-38) are mostly "buy the next thing".
2. **Idle means idle: early automation, no mandatory active play, no daily-streak loss** (C4, C10, anti_patterns.md:93, :98). Only R24 touches it.
3. **Soft failure only / never destroy the card collection** (A9; reactor lesson 2).
4. **Endowed progress at each world entry (pre-filled bar, justified)** (psychology.md:65-72 and :149; Nunes & Dreze). R17 mentions bonus on first use only.
5. **Second run visibly faster in the first 30 s, 2-4x speedup per ride** (design_talks_postmortems.md:187; math_of_idle_games.md 3.2). Not in DR; R12 only sets the first-ride gain.
6. **Prestige-currency magnitude much smaller than main currency, and design the reward cliff** (math_of_idle_games.md:6.7, design_talks 4.4 "cliff awareness"). The cliff matters because the player will time the ride right before one.
7. **Welcome-back should offer 1-2 decisions and ignore short absences (<~1-2 min); measure from the saved quit timestamp, cap, clamp boosters** (design_talks_postmortems.md:4.5, player_complaints.md:C7 / implication 6). R25 only says "show a card".
8. **Number legibility: named ranks, capped notation, no e47, show additive vs multiplicative** (C8, anti_patterns.md:97, psychology.md:147). R27 covers tooltips only.
9. **Trust: cloud + local dual save, versioned backups, autosave from day one; one-file constants** (C11, A8/A11, anti_patterns.md:99-100). Not in DR.
10. **Surprise/"bumpy" events** (math_of_idle_games.md:6.9 and design_talks Idle Chatter; beloved B9; psychology variable reward "delight only") - DD:38 Photo Op has no frequency or reward size. Specify e.g. spawn gap 5-15 min (CC golden: formula_tables.md Sec.R2.3), lifetime 13 s, <=1.2x average.
11. **Throttle systems: one new system per world, show <=3 resources, one screen per world** (A3, B12, S11). Partially in R20; add the UI half.
12. **Finite arc + post-credits mode** (SU:19-20; games Paperclips/ADR/Spaceplan). Not a rule but needed for world 9 (see below).
13. **Raising prestige gain by "cliff" and "reset when growth slows to 10-20 % of peak"** (math_of_idle 3.2) - alternative to the 2x rule, for a rule R13b.
14. **Mid-game lull between layers (AD Break Infinity -> Eternity)** (anti_patterns.md:80): add a "lull audit" rule for worlds 4-6 where the DD rules are weakest.

---

## 5. Design holes in DECADE_IDLE_DESIGN.md

### H1. What resets at each ride is undefined (P0)
- DD:9 (Final Form Ride) never states what is lost. DD:10 says Dimension Ride "keeps Ride Cards, forms, automation, Decade Driver; resets generators". Not stated for: Shots, tier counts, milestone progress (do x2 milestones reset? they must, or the ladder is skipped), mastery tree (DD:33 says it "persists via best-result memory" - but PK's best-result is a per-task multiplier, not tree persistence; prototypes/EVALUATIONS.md:unlock_tree says the tree persists across worlds), world-local currency (does it survive a Final Form Ride? a Dimension Ride?), Charge, L1 points (do they survive the Dimension Ride or convert to L2?), offline cap/efficiency upgrades, Photo Op state.
- DR:45 lists "whether the ride should reset generators" as open; DD:10 asserts it resets them. These conflict; settle it.
- Proposed edit, new DD table in section 2:

| Thing | Final Form Ride (in-world) | Dimension Ride (to next world) |
|---|---|---|
| Shots, generators, tier unlocks, milestones | reset | reset |
| L1 points ("Form Energy") | kept, +gain | converted to permanent x(1+0.05*sqrt(total)) or archived per world (so old worlds do not dilute) |
| Mastery tree | kept | kept per world; 3 "cross-world" nodes pooled |
| World currency | kept | frozen in the old world |
| Automation, offline upgrades, cards, Driver | kept | kept |
| Photo Op progress | n/a | n/a |

### H2. L2 "smaller exponent ~0.14-0.25" (DD:11) is unsupported and incoherent
- Unsourced: R16/Synergism fall 0.5 -> 0.03 -> 0.01 (DR:25), Egg Inc 0.14 is the only match (math_of_idle_games.md:5, and it is flagged unresolved in :7). More important: a prestige-formula only makes sense when the player decides when to reset. L2 is gated by an objective (DR:33 R22, DD:10), and there are only 8 hops in the whole game. A formula with an exponent adds nothing here; use a fixed "world clear" bonus (the carryover c in sim).
- Edit DD:11: "L2 is not a formula-prestige; each cleared world gives a fixed carry multiplier c and a card; the exponent text is deleted. L3 'All Riders' is the only layer with a formula."

### H3. How many rides per world and the rhythm of a 3-5 day world (P0)
- DD:9 gives no number; the sim's 20-45 min cycles (SR:25) assume continuous play. For a 3x10-min/day player, define "one ride per 1-2 sessions in the early worlds" and a count (e.g. 4-6 per world), then check that each ride is >=2x faster (design_talks 2-4x) and that the sum of cycles matches the world length. Add a check table to DD.

### H4. World objective (what ends a world) is never defined (P0)
- DD:10 "gated by an objective (R22)", DD:41 "reveal next world's card at ~1/3 of the objective", but there is no objective in section 3's table. The sim used "own 25 of top tier" (SR:44). Specify per world, e.g. W1 "own 25 of tier 6 + complete the Zecter roster", W2 "lay the full Rail map", etc. Without it, R22's "challenge or cap" is empty and R18/R19 cannot be checked.

### H5. World 9 / endgame (P0)
- DD:44 "ending sequence; post-game 'All Riders' challenge layer (L3), Another-World replay with restrictions" - nothing else. Missing: what the last objective is (Kuuga is last in the table, DD:27, but DD:14 says order is free: pick and justify, the show order starts with Kuuga; decade_worlds.md:8), what L3 resets and pays, what the player decides after the credits, whether numbers keep growing (cost scale s^8 at W9; with s=3, 6,561x W1 costs, i.e. e-notation, against C8), whether there is a final number cap, and what "Another-World replay with restrictions" restricts (R6-style caps? challenge modifiers à la Synergism, which R16 already warns about). Add: finite arc 40-60 h total, endgame = 9 challenge modifiers (one per world rule) giving cosmetic/Driver rewards only, no new prestige currency.

### H6. What the player decides (P1)
- Sections 3-4 list ~60 themed upgrade names but most are one-line renames of "buy a multiplier". Missing: the build fork in the first 5 min (C5, B4), which generator/rule synergy to run, at least one trade-off per world (e.g. Kiva: night vs day allocation; Ryuki: which 3 of N cards in slots - these exist in the table but no cost/benefit numbers). Add one decision per world with 2 viable options, a stated opportunity cost, and a free respec rule (DD:33 says respec free, which removes the tradeoff; restrict respec to between rides, not mid-ride).
- Mastery tree "~25 nodes, 3 branches, free respec" (DD:33) comes from the prototype critique (EVALUATIONS.md unlock_tree) not from any measured design; with 6 tiers per world and 25 nodes, the 25 nodes dwarf the 6-tier ladder (see Sec.3 goal-count issue).

### H7. Upgrade types per world are not specified (P1)
- DD:31-38 lists 8 families but not which exist in which world. Provide a matrix (rows = 8 families, columns = 9 worlds) with introduction world and cadence: e.g. generators W1, milestone bars W1, mastery tree W1 (small) growing to 25 nodes by W3, automation W1 (cheap) + W2 (full), offline upgrades W2, cards W1, Driver W3, active layer W2. As written, R20 (one new rule per world) is the only introduction schedule and nothing says when the 7 non-rule families appear.

### H8. Carryover c and cost scale s are never given numbers
- DD:10 and DR:32 refer to "cleared worlds lift passive income" and "best-result multiplier", but DD has neither c nor s, nor what "passive income" does inside the new world (converts to Shots? to local currency?). sim/decade_model uses c^w as a multiplier on all production. Add `s = 3, c = 2.9` (ratio ~1.03) as starting values, define passive income as a constant fraction (e.g. 2 % per cleared world) of current Shot rate, and state whether it applies from the first second (R9: first purchase < 60 s on arrival).

### H9. Kabuto rule is mechanically inconsistent with R3
- DD:19: "Cast Off at 25 owned sheds a tier for a stronger one" collides with R3's x2 at 25 and with R5's "tier N+1 revealed at 5 owned of N" (what is shed? does it break the cost ladder and the 60 % rule R15?). "Clock Up: spend Charge" adds a currency while the table says "none". "Phylloxera Mirror (prestige reset that copies your build)" is a fourth reset-like object outside L1/L2/L3. Resolve before building the tutorial world.

### H10. Lore verification claims are stronger than research/decade_worlds.md
- DD:56 says Kabuto, Kiva, Ryuki, Blade, Faiz, Kuuga, Hibiki and Den-O hooks "were checked against ... [S]". decade_worlds.md: Hibiki gameplay hooks (Ongekibou, Tachibanaya) have "No snippet [?]" (line ~87-88), Blade "Fusion" is [M], Kiva day/night is [M], DenLiner as Decade's vehicle is [M], Hikari Studio unconfirmed. Edit DD:56 to "world names and device names [S]; mechanics themes are design, not lore".
- The IP paragraph (DD:57-58) is sound; keep "Rider War" reframing.

### H11. Other
- DD:47 "optional rewarded x2 offline claim": see P1-8.
- DD:7 header cites R5, R8-R11 but the doc never says how R10 (new unlock every 2-5 min in the first hour) is met in Kabuto; add an unlock timeline for minutes 0-60.
- DD:50-53 risk list should add: (a) sim only covers 1 world with no mid-world prestige combined with carryover; (b) goal-density in multi-day worlds (Sec.3); (c) 5-6 currency count.

---

## 6. Proposed concrete edits (summary list)
1. DR:15 R8 -> "applies to the first hour of each world; later per-world goal density to be set by H7 matrix".
2. DR:16 R9 -> "first purchase <60 s; priced tier-1 auto-buy ~3 min; first ride 10-15 min [PUB]; sim currently lands ~25 min with T=1e8 -> retune T".
3. DR:21 R12 -> "floor((lifetime/T)^0.5), T tuned for a 10-15 min first ride; per-point bonus 5-10 % [SIM] vs 1-2 % [PUB], untested lower range".
4. DR:25 R16 -> relabel [OPINION]; explicitly count Final Form Ride, Dimension Ride, All Riders as the 3 layers and Mastery/Cards/Driver as non-resetting meta.
5. DR:29-30 R18/R19 -> numbers from P0-1.
6. DR:36 R23 -> add "stepped curve unsimulated; sim = flat 0.5, cap 8 h; casual expectation x1.5-2 longer".
7. DR:37 R24 -> as P1-7.
8. DR:41 R26 -> as P1-8.
9. Add R28-R37 from Sec.4 (choice fork, idle-means-idle, soft failure, endowed progress, 2-4x second run, welcome-back details, number legibility, trust/saves/constants, bumpy events, UI throttle).
10. DD sections 2 and 5: add the reset table (H1), objectives (H4), endgame (H5), matrix (H7), numbers for s and c (H8), ride count (H3).
11. SU:4, SU:6, SU:7, SU:9: fix tags/claims as in Sec.1 P2-9, P0-2.
12. SR: add "toy model - hypotheses, not findings" banner at SR:1; add the missing run (prestige + offline + sessions + carryover) as an explicit TODO.
