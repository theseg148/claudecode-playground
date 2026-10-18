# DESIGN RULES (v2) — Decade idle game
v2 applies REVIEW_1.md. Each rule has a **confidence**: **C** = confirmed in open-source code or primary data; **P** = published design article/wiki or ≥3 independent games/complaints (secondhand but convergent); **H** = hypothesis from our toy simulation or author judgement — play-test before trusting. Sim = sim/results.md (greedy player; toy). Game files: games/*.md.

## A. Cost & production
**R1 [C] Per-unit cost growth r = 1.12–1.15 for main generators (1.07 only for late/bulk tiers).** Cookie Clicker 1.15 [CODE games/cookie-clicker.md], Kittens 1.12–1.15 [CODE], Trimps 1.12–1.24 [CODE], Synergism 1.25 [CODE]; Pecorella 1.07–1.15 [P research/math_of_idle_games.md]. At 1.15 price doubles every ~5 buys, at 1.07 every ~10.
**R2 [H] Tier base cost ×8–12 per tier; tier rate ratio ≈ cost ratio / 1.3.** AdCap ×12 [P]; AD steps 1e3…1e15 [CODE]. Sim of 512 configs: best ratio cost/rate 1.2–1.5, ≤1 → bursts, >2 → walls [Sim].
**R3 [P] ×2 milestone multipliers at 10/25/50/100/200(/300/400/500/700/1000 for late tiers).** Guava Juice Tub Tapper's guide lists milestone levels 5,10,25,50,100,200,300,400,500,700,1000 with automation unlocking at 50 [S games/guava-juice-tub-tapper.md];  AD ×2 per 10 bought [CODE]; AdCap halvings at 25/50/100/200/300/400 [P]; Pecorella M≈r^S. Sim: ×2 beat ×3; 200 was not swept [H].
**R4 [P] Show the next milestone as a bar and a count ("×2 in 7").** Goal-gradient effect (psychology.md, strong support for the effect, weaker for magnitude), prototypes/milestones.html.
**R5 [P] Reveal tier N+1 at ~1/3 of its price or 5 owned.** Cookie Clicker reveal [P]; sim uses 5 owned [H].
**R6 [P] Permanent perks have hard level caps (5–15).** Trimps perk caps [P games/trimps.md], Prestige Tree/Evolve softcaps [CODE]. (Leaf Blower combo caps unverified.)
**R7 [C] Offer one endless, gentle-ratio sink (×1.14 per level) for late choice; steep one-off ladders (×1.9 per augment, Bitburner) are finite and are not an endless sink.** NeuroFlux 1.14, augment ×1.9 [CODE].
**R8 [C] Resource growth between milestone breakpoints should be smooth; no unscheduled cost walls >2×.** AD cost blocks [CODE], sweep walls [Sim H].

## B. Pacing (within a session)
**R9 [H] Time between goals: median 30–60 s, 90th percentile ≤10 min, no gap >30 min *inside a session*.** Best sweep config: median 46 s, max 344 s, 97 % in 15–600 s [Sim]; the band itself is author-chosen [H]. Walls drive quitting [C1 research/player_complaints.md, P].
**R10 [P] First purchase <60 s; first *light* automation (auto-collect, auto-buy tier 1) ≈3 min — full payback auto-buy only in the first-ride shop (R21); first prestige/ride unlock 10–15 min (first ride available in session 1).** Blog pacing [P research/math_of_idle_games.md]; anti_patterns/complaints/postmortem say 25–35 min is too late. Sim v2: with T≈1e6 the first ride lands at ~7 min [Sim H].
**R11 [P] ≥1 new option/unlock every 2–5 min in the first hour.** 14/14 beloved games [analysis/beloved_patterns.md, manual tally].
**R12 [P] Never a wait longer than one session without something to spend/decide.** ~30/37 games get grind-wall complaints [analysis/anti_patterns.md].
**R13 [P] Build fork in the first 5 min with ≥2 viable builds; no "buy the next thing" only.** player_complaints C5, beloved B4.
**R13b [H] Builds: ≥2 viable exclusive builds; slowest ≤25 % slower than fastest (sim v3 exact-time: best 1.19× at Speed ×1.2/node, Cast Off ×1.5→×2, Recipes rides −70 %). Cap mastery points at ≈4 per world (+1 starting point so the first fork is before the first ride), respec costs points; never make a build that only changes offline efficiency. Gates must be calibrated *with* the build mix (builds clear 20–45 % faster than none).** [Sim builds3.py H]
**R14 [P] Idle means idle: automation early, no mandatory active play, no daily-streak loss.** complaints C4/C10, anti_patterns.

## C. Prestige (Final Form Ride, inside a world)
**R15 [P/H] Seals pending = floor(sqrt(run_lifetime/T_w)); production multiplier = (1+Seals)^0.5 (NOT +8 %/seal).** sqrt gain: AdCap/Realm Grinder [P], Synergism layer 1 [CODE]. Campaign sim v3: linear +8 %/seal explodes (≈30 rides/world, multiplier 6e6, REVIEW_2 P0-2); (1+Seals)^0.5 gives 9–11 rides/world and a final multiplier of 240–320 [Sim H]. T_w is auto-calibrated so the first ride lands ≈8 min into play in every world. (Earlier linear-bonus advice "5–10 %/pt, final mult 2e2–6e3" came from the pre-ride continuous sweep and does not hold in the campaign; postmortem blueprints quote 1–2 %/pt [P].)
**R16 [P/H] Teach the loop early: first ride in session 1 (≈8 min, calibrated per world via T_w), then ≈9–11 rides per 3.2-day world (≈1 per 7 h wall-clock), each ≥1.5× production by construction (ride only when gain ≥1.5×; typical 2–4× speed-up quoted in postmortems [P]).** Sim v2: rides cluster at session starts because offline accrual makes pending jump [Sim H]; 2–4× speedup [P design_talks_postmortems.md]. (Replaces the earlier "20–45 min cycles", which is continuous-time only.)
**R17 [P/H] Player rides when it raises production ≥1.5× (sim rule; equivalent to the AdCap/Pecorella "pending ≥ current" heuristic early on); highlight it and show before/after production.** AdCap heuristic, Pecorella [P]; sim v3 ride rule [Sim H]. The old "pending ≥2× current" test was vacuous at 0 Seals (REVIEW_2).
**R18 [P] Always show pending gain; second-run first 30 s visibly faster.** math_of_idle_games 3.2, design_talks 4.4. Loss aversion is contested (psychology.md) so frame as gain *and* show the preview.
**R19 [H] No ride before ≥60 % of the world's tiers are seen (≥4 of 6–8).** Guard from sim; threshold untested.
**R20 [P] ≤3 reset layers in the game; each deeper layer uses a smaller exponent.** Synergism 0.5→0.03→0.01 [CODE]; 4+ layers confuse (Clicker Heroes, Synergism, AD) [analysis/prestige_designs.md]. Dimension Ride is a *fixed-bonus* hop, not a formula (see R24).
**R21 [P] First-ride shop contains automation + a QoL perk; first ride gives a bonus.** Cookie Clicker Twin Gates etc. [P], psychology (endowed progress).
**R22 [P] Cliff awareness:** the prestige currency magnitude ≪ main currency; check the reward cliff so players don't time rides before a cliff. math_of_idle_games 6.7.

## D. Worlds
**R23 [H] World drift d = cost_scale s / total permanent carry (c × Ride Cards × archived-Seals bonus × achievements × tree). Budget *every* carry source inside c; keep d ∈ [1.0, 1.07].** Campaign sim v3: s=3 with cards (+10 %/card), archive (+1 %/world, bounded) and achievements (×10 at W9) needs c≈2.25 for d≈1.0 (total carry 6.3e3 vs 6.6e3 at W9); leaving them out of c collapses a 27 d campaign to 12 d, and an unbounded √archive bonus to 0.3 d/world (REVIEW_2 P0-1). World length grows sublinearly in d (≈d^(0.65 n), session-quantised, v2 data); d>1.2 gave dry-session streaks of 5–7 and needs extra beats. Campaign length ∝ 1/sessions-per-day (population sim: 1/day 81–147 d, 3/day 27–48 d, 6/day 16–33 d).
**R24 [H] Dimension Ride = fixed world-clear bonus (carry c) + a Ride Card, not a formula.** Only ~8 hops, objective-gated; formula-prestige only adds opacity. Review H2.
**R25 [H] Target ≈3.2 days per world for a 3×10 min/day player (≈29 d ≈ 4 weeks campaign); gates ≈ ×2.5–3.5 per world (6.2e15 → 4.0e19 in sim v3) and rides give only 55–64 % of sessions a goal — supply ≥1 further beat per session (mastery node, album entry, Photo Window, fusion discovery).** Sim v3 pow variant: 64–73 % of sessions with a new unique goal, max dry 2 (4 in W4); 18-day worlds had 34 % [Sim H]. Gates are *outputs* of the calibration (campaign3.py), not free parameters.
**R26 [P] Each world adds exactly one new *rule/verb*; additional systems are introduced at most one per world (DECADE_IDLE_DESIGN §12; World 1 also carries the tutorial set: Photo Window + tree); world-local currency from world 2–3; ≤3 visible currencies at once.** sequential_worlds.md S1/S2/S11 [P, tally of ~12 games]; skin-only restarts fail (AdCap planets).
**R27 [P] A world is a data record (included/absent resources, modifiers, gate table) so adding a world = data edit.** Shark Game [CODE], Evolve per-reset constants [CODE].
**R28 [P] Gate = 3–4 named costs shown up front; completing always pays a flat reward.** Shark Game gate slots [CODE]; slot count is [H].
**R29 [P] Carryover stack: collection/automation/forms permanent; per-world best memory 1+best/10 for revisits (Progress Knight XP, CODE); cleared worlds raise passive income immediately (AFK Arena, P).**
**R30 [P] Endowed progress at world entry: pre-filled bar with a stated reason (e.g. "carried-over Ride Cards").** psychology.md (Nunes & Drèze).
**R31 [P] Finite arc: world 9 ends in a finale + post-credits mode (replay with restrictions, optional "All Riders" challenge).** Paperclips/A Dark Room/Spaceplan arcs 2–10 h [P].
**R32 [P] Lull audit: worlds 4–6 must each contain a mid-world surprise; AD Break Infinity→Eternity lull is the counter-example.** anti_patterns.md.

## E. Offline & sessions
**R33 [H] Offline: 50 % for first 2 h, 25 % beyond, cap 8 h ⇒ average ≈0.31 for an 8 h gap; upgrades can raise both. Cap beyond 8 h buys little (×1.1 in world length).** Sim v1 (flat 0.5) said casual worlds take 4 d; the stepped curve takes ~1.5–2× longer unless worlds are re-sized (Sim v2 uses stepped). Competitors: Bitburner 75 % [CODE], Cookie Clicker 5–75 % with Twin Gates [CODE], Synergism 72 h cap [CODE], AFK Arena 12 h [P], Melvor 24 h [S].
**R34 [H] Frequent play is rewarded roughly in proportion to sessions/day once rides exist (1→6 sessions/day: 4.2× faster; sim v2) — the offline cap barely matters past 8 h (×1.3 for 8→24 h). Decide deliberately: size worlds for the 2-session median (~5.8 d) and add a ride cooldown or per-world ride cap if heavy play should not run away.** Sim v1 (no prestige) showed only 1.5× for 4× sessions; the difference is the ride cluster per session [Sim H]. Any Photo-Op active bonus must be counted inside this budget (≤1.2× average) [P/H].
**R35 [P] Welcome-back card: ignore absences <1–2 min, measure from saved quit time, cap + clamp boosters, offer 1–2 decisions, list what happened.** design_talks_postmortems 4.5, complaints C7.
**R36 [P] Banked offline time as optional spendable speed (×5) next to automatic gains.** Idle Loops [CODE games/idle-loops.md].
**R37 [H] Infrequent returners get bursts, not gaps — auto-spend/summary rather than 10 manual buys.** Robustness sim: 10-min checkers see 28 % in-band but batched goals [Sim].

## F. Engagement events
**R38 [P, superseded by R38b for 10-min sessions] Cookie Clicker golden cookies: spawn gap 5–15 min, lifetime 13 s.** Cookie Clicker golden cookies 5–15 min base, 13 s lifetime [CODE games/cookie-clicker.md]; variable reward psychology (delight only, no punishment).

**R38b [H] Event budget: Photo Window every 90–240 s foregrounded (first guaranteed at ~3 min), ≈119 production-seconds EV, banked offline "Exposures" 1 per 30 min (cap 6) at half value ⇒ +28–37 % of active-session gain but only 2.5–3.6 % of daily progress (sim/results.md events).** Cookie Clicker's 5–15 min spacing assumes hour-long sessions [CODE]; ours is 10 min. No negative outcomes (R14, R42).
**R38c [P/H] Collections: achievement multiplier ≈ 1.05^rows·1.01^count (×10 at 144 entries) applied to base Shots only; AD's 1.25^rows·1.03^count reaches ×3.9e3 and is too large for a 9-world game.** AD [CODE research/events_and_choices.md].

## G. Monetisation, UX, trust
**R39 [P] Default for this fan project: no monetisation at all (Toei IP exposure is the largest risk; Cookie Clicker's Steam $4.99 one-time model shows a clean option; deterministic Ride Card unlocks avoid loot-box rules; research/retention_monetization.md). If it ever became commercial: monetise with cosmetics; optional time-skip sales acceptable only if they never gate a world or sell Ride Cards/prestige currency; no mandatory ads; rewarded ads only as an opt-in bonus.** 14/37 games cite ad/IAP pressure, 11/12 mobile-first [analysis/anti_patterns.md]; note: time-skips change pacing like offline efficiency does [Sim], so treat them as pacing tools.
**R40a [C/E] Numbers: native doubles suffice — peak ≈6.6e21 (s=3, world 9, gate 1e18·3^8; 6.5e22 if s=4) vs 1.8e308 max; per-tick income must exceed one double step (≈8.4e6 at 6.5e22), compare with ≥, never use Shots as keys; no big-number library needed (research/ui_and_numbers.md).
**R40 [P] Number legibility: named ranks, capped notation (no e47), real numbers in tooltips, additive vs multiplicative labelled, bulk-buy ×1/×10/×max.** C8, anti_patterns.
**R41 [P] Trust: autosave from day one, versioned export string (AD/Cookie Clicker-style deflate+base64 with end marker, [CODE research/ui_and_numbers.md]), local+cloud dual save, versioned backups, constants in one file.** C11, A8/A11.
**R42 [P] Soft failure only; never destroy the card collection.** A9.

## Open questions (play-test)
Exact world length; whether 9 worlds is right; reward size of Photo Op; fixed carry multiplier per world; whether Cast Off should coincide with ×2 at 25 owned (design doc: shift Cast Off to 40 owned).
