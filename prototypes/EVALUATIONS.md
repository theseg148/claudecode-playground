# Prototype evaluations
_Rule numbers refer to DESIGN_RULES.md v2/v3 (older text in this file may use v1 numbers where flagged)._
Each prototype is a single HTML file (open in a browser; no build). Rules referenced come from research/*, games/*, sim/results.md. Evidence tags: [CODE] source code, [S] search-snippet, [SIM] our simulation, [M] memory.

## milestones.html — generator ladder with x2 milestone bars
Implements cost = base*1.12^owned, doublers at 10/25/50/100/200 owned, a progress bar to the next doubler, and tier N+1 hidden until 5 of tier N.
- Applies: Adventure Capitalist-style doublers [M]; Synergism x2 at 25/50/100/200 walls [CODE games/synergism.md]; goal-gradient bar (research/psychology.md); sweep winners (growth 1.12, cost/rate ratio ~1.33) [SIM].
- Works: the bar makes every purchase a step toward a visible goal.
- Change: show "x2 in N more" numerically, add bulk-buy (x10/x25/max) because late game is click-heavy, show per-second delta before buying. Rider theming: milestone = "Form Up" animation (Kabuto: Cast-Off at 25, Clock Up at 100).

## offline.html — "Time away" card
50 % efficiency for first 2 h, 25 % beyond, 8 h cap, optional x2 claim.
- Applies: sim finding that offline efficiency is the dominant pacing lever [SIM]; Synergism 3-day cap and Bitburner 75 % offline [CODE games/synergism.md, games/bitburner.md]; AFK Arena 12 h chest [S].
- Weak: never-zero soft cap is good, but the x2 claim as ad placeholder must stay optional (complaints: ads-as-wall, research/player_complaints.md).
- Change: show a breakdown of what was bought/would be bought; auto-spend on cheapest goal ("while you were gone Decade took photos of...").

## prestige.html — Rider Seal reset
Seals = floor((lifetime/1e6)^0.5), +25 %/seal, shows pending seals with "recommended" at >=2x current.
- Applies: sqrt prestige (Adventure Capitalist/Synergism [CODE]), readable pending gain, 2x-rule from prestige sweep [SIM].
- Weak: +25 %/seal is too strong per sweep (final mult ~1e5); use 5-10 %. First prestige threshold should land ~25 min [SIM].
- Change: reset keeps "form" unlocks; add a one-time bonus on the first reset so it feels like a reward, not a loss (loss aversion, psychology.md).

## unlock_tree.html — 3-branch mastery tree
Branches Clock Up / Zecter / Hyper with prerequisites, final node "Decade Link" unlocks next world.
- Applies: finite caps and visible 'done' moments (Trimps perks [S]); branching instead of linear to create planning (Bitburner augments [CODE]).
- Weak: only 12 points and 9 nodes — decisions are trivial. Need ~25 nodes/world with respec.
- Change: let the tree persist across worlds (carryover) and add one cross-world node per world.

## world_transition.html — Dimension Ride
Progress bar to goal, then a flash "ATTACK RIDE" transition, new palette, carryover x3.
- Applies: each world should have its own identity (Idle Wizard realms, Progress Knight layers [CODE/S games/progress-knight.md]); carryover ratio equals cost scale ratio to keep world length constant [SIM].
- Weak: transition is cosmetic only. Add: new rule per world, a card/photo reward, a recap screen ("Kabuto cleared in 3d 4h, kept: ...").

## decade_slice.html — integrated vertical slice (2 worlds)
Combines R1–R3 (growth 1.12, cost ×8/rate ×6, ×2 milestones with bars), R5 (tier reveal at 5 owned), R15/R17/R19 (sqrt Seals +8 %/pt, pending ≥2× highlight, ride needs 4 tiers seen), R21 (auto-buy after first ride), R29 (cards +10 % each persist), R33/R35 (offline 50 %/25 %, 8 h cap, welcome-back toast), R34c (Photo Op: now 6 s of income per 60 s = +10 %; was 15 s per 45 s = +33 % in the first version), plus live pacing telemetry (goal-gap bars, median/max/in-band %) and ×1/×10/×100 speed for tuning.
Headless test (Playwright + Chromium, greedy bot, ×100 speed, 25 simulated minutes, no JS errors): 18 goals, median gap 80 s, max 160 s, 94 % in the 15–600 s band — consistent with sim sweep [SIM].
Not yet good: only 2 worlds, no distinct per-world rule (only names), no mastery tree, ride gating is by tier count not an objective, Seals reset all generators (no preview of post-reset rate), world-2 cost scale hard-coded ×3 with carry ×3 (ratio 1.0 → equal-length worlds). Next: add per-world rule (Clock Up button), preview panel, mastery tree persistence.

## decade_slice_v2.html — adds Kabuto Clock Up, Cast Off at 40, mastery build fork, ride preview, archived Seals
Adds: Charge/Clock Up (×3 for 10 s, Speed II ×5), Cast Off ×2/×3/×5 at 40 owned (not 25, to avoid colliding with the ×2 milestone — review issue 7), a 6-node mastery tree (Speed / Cast Off / Recipes branches; 1 mastery point per Final Form Ride), before/after ride preview, Seals archived per world at Dimension Ride (reset table in DECADE_IDLE_DESIGN.md §2), offline 50→65 % via Recipes I.
Bug found by the headless bot and fixed in both slices: after a Dimension Ride the start gold was 15 while tier-0 cost scaled ×3, so world 2 soft-locked (no production, no purchases). Fixed by starting gold = cost of tier 0 (`cs(0)`). Lesson for the real game: **every reset path must leave the player able to buy something within seconds** (R10) — add an automated "no-soft-lock after reset" test.
Headless bot (greedy + clock + tree + rides + hop): world 1 → hop → world 2 buys generators within 70 s; no JS errors.
Still missing: second world rule, objective with 3 named costs (currently a single lifetime-Shots bar), tuning of T per world.

## offline_v2.html — welcome-back card (R35, R36, R38b)
Slider-driven card: ignores <2 min, measures capped time (8 h), stepped efficiency (50 %/25 %), Exposure bank (1 per 30 min, cap 6, half value), banked Time Skip (20 % of time as ×5 speed), auto-spend suggestion and two decisions (spend vs save, use Exposures now vs keep). Evaluation: implements every R35/R36 clause; the numbers (Time Skip 20 %, Exposure half value) are untested [H]. Missing: the cap upgrades (8→24 h), the ride-preview link, and a persisted quit timestamp (v2 slice has it).

## REVIEW_2 fixes applied to decade_slice_v2.html (all verified headless)
1. Gate counts world-lifetime Shots (`S.wlife`), not per-run `S.life` (a ride no longer erases gate progress). Gates remain DEV-sized (3e6 / 3e8) so a tester can finish a world in minutes — real gates are ~1e18–1e22 (sim/campaign3.py).
2. Hidden/throttled tab: any real-time gap >2 s goes through the offline model (50 %/25 %, 8 h cap) instead of being credited at 100 %.
3. DOM is rebuilt only when the structural signature changes (own counts, affordability, tree, charge), not every 100 ms — real mouse clicks registered 30/30 in Playwright.
4. Number format uses K/M/B/T… suffixes to 1e36 (R40); dimension-ride flash replaced by a 0.5 s brightness fade (no full-white flash).
5. Cast Off applies to tiers ≥4 only (matches builds.py); Clock Up now ×2 for 8 s for 4 Charge (regen 1/8 s ⇒ ≈×1.25 average), Speed II ×3; Photo Op +10 %: active tools stay inside the R34c budget (≤1.5× total).
6. Auto-buy after the first ride is payback-greedy like the sim (not cheapest-first). Separate localStorage key `decadeSliceV2`.
Known gaps: still two worlds, a single-bar gate instead of 3 named costs, no Photo Window event, no Album/Form Deck (they arrive in World 2 per DECADE_IDLE_DESIGN §12).
