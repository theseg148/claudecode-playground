# DESIGN RULES (v1) — Decade idle game

Evidence tags: **[CODE]** read from open-source game code; **[S]** confirmed in search snippets; **[SIM]** our simulation (sim/results.md, toy greedy-player model); **[PUB]** published design article/blog (single-author, often via excerpts); **[OPINION]** community/blog heuristic; **[GUESS]** tuning placeholder, play-test it. Many per-game numbers in `games/` are memory-based; rules below rely on the tagged ones.

## A. Cost & production
**R1. Per-unit cost growth r = 1.12–1.15 for ordinary generators; use 1.07 only on late/bulk tiers.** Cookie Clicker 1.15 [CODE games/cookie-clicker.md, ozh mirror main.js], Kittens 1.12–1.15 [CODE research/formula_tables.md], Trimps 1.12–1.24 [CODE], Pecorella: typical 1.07–1.15, AdCap drops 0.01/tier [PUB research/math_of_idle_games.md]. Price doubles every ~5 buys at 1.15, ~10 at 1.07 [derived].
**R2. Tier base cost ×8–12 per tier; tier production ratio slightly smaller than cost ratio (cost/rate ≈ 1.2–1.5).** AdCap ×12 [PUB], AD cost steps [CODE]; sweep of 512 configs: best configs had ratio 1.2–1.5; ratio ≤1 produces <3 s goal bursts; ratio >2 produces walls >2 h [SIM].
**R3. Milestone doublers at 10/25/50/100(/200) owned, ×2 (not ×3).** AD ×2 per 10 bought [CODE]; AdCap speed-ups at 25/50/100/200/300/400 [S]; sim: ×2 beat ×3 on average, ×3 with first milestone at 5 was worst [SIM]. Choose multiplier M ≈ r^spacing [PUB].
**R4. Show the next milestone as a bar and a number ("×2 in 7").** Goal-gradient effect [research/psychology.md], bar prototype [prototypes/milestones.html].
**R5. Reveal tier N+1 when the player can afford ~1/3 of it or owns 5 of tier N.** Cookie Clicker 1/3 reveal [S]; sim unlock rule "5 owned" [SIM].
**R6. Permanent perks get hard level caps (5–15 levels).** Trimps perk caps [S], Leaf Blower combo caps [S]; creates "done" moments and eases balance [OPINION].
**R7. Optional endless sink with a steep ratio (×1.14–1.9/level) for late-game choice.** Bitburner NeuroFlux 1.14, augment price ×1.9 [CODE].

## B. Pacing
**R8. Time to next meaningful goal: 15–600 s median ~45 s early; never > 30 min within a session.** Sweep: best configs median 46 s, max gap 344 s, 97 % goals in band [SIM]. 
**R9. First purchase < 60 s; first automation ≈ 3 min; first prestige/ride unlock 10–25 min.** [PUB research/math_of_idle_games.md, single-author] and sim prestige sweep first prestige 20–40 min in good configs [SIM]. Players quit at early walls [research/player_complaints.md C1].
**R10. A new option/unlock at least every 2–5 minutes in the first hour.** 14/14 beloved games reveal something new every few minutes [analysis/beloved_patterns.md, manual tally].
**R11. Every wait ≤ one session length (~10 min) must have something to spend on or decide.** Anti-pattern: grind walls (≈30/37 files) [analysis/anti_patterns.md].

## C. Prestige / world ride
**R12. Prestige currency = floor((lifetime/T)^0.5), T so first gain lands at ~25 min; +5–10 % per point.** sqrt used by AdCap/Realm Grinder/Synergism [CODE/PUB]; sweep: 23/108 configs satisfied (first 20–90 min, ≥3 in 6 h); T=1e8, exp 0.5–0.7, 5–10 % → 8–14 resets in 6 h, final mult 2e2–6e3 [SIM]. 25 %/pt exploded to 9e4 [SIM].
**R13. Player should reset when pending ≥ 2× current; highlight it.** AdCap heuristic, Pecorella 50–200 % [PUB]; sim rebuy rule [SIM].
**R14. Always display pending gain and post-reset production preview.** [PUB; psychology.md loss aversion].
**R15. No prestige before 60 % of the world's tiers are seen.** [SIM guard; GUESS on 60 %].
**R16. At most 2–3 reset layers total.** 4+ layers cause confusion (Clicker Heroes, Synergism, AD) [analysis/prestige_designs.md]. Each deeper layer uses a smaller exponent (Synergism 0.5→0.03→0.01) [CODE].
**R17. First prestige shop must contain automation + a QoL perk, and the first reset should feel like a gain (bonus on first use).** [PUB; psychology.md]; CC Twin Gates etc.

## D. Worlds
**R18. World clear time ∝ (cost_scale / carryover)^n; choose cost_scale/carryover = 1.0 (equal worlds) to 1.3 (each world ~30 % longer); below 0.8 later worlds become trivial, above 1.5 they become walls.** [SIM sim/results.md]; examples carry×2/cost×3: 8.4→63.6 min; carry×2/cost×1: 0.3 min.
**R19. Target 3–5 days per world for a 3×10-min/day player, ~2 days for a heavy player; 9 worlds ≈ 5–8 weeks.** Sessions sweep [SIM]; GUESS on total campaign length.
**R20. Each world adds exactly one new rule/mechanic and (from world 3) one world-local currency; ≤3 visible currencies.** sequential_worlds.md S1/S2/S11 (tally of ~12 games) [analysis]; failure: skin-only restarts (AdCap planets).
**R21. Carryover stack: permanent unlocks/collection never reset; best-result multiplier 1+best/10 for revisits; cleared worlds lift passive income immediately.** Progress Knight 1+maxLevel/10 [CODE]; AFK Arena income grows with stage [S].
**R22. Gate the ride with a visible objective (challenge or cap), reveal next world at ~1/3 progress.** Synergism challenges, CC reveal [S/CODE].

## E. Offline & sessions
**R23. Offline: 50 % efficiency for the first 2 h, 25 % beyond, cap 8 h (extend via upgrades up to 24 h). Never 0 %.** Sim: eff 0→0.25 speeds 3×10 min/day player 9× [SIM]; Bitburner 75 % [CODE], Synergism cap 3 days [CODE], AFK Arena 12 h [S], Melvor 24 h [S].
**R24. Active play must be rewarded only mildly (≤1.5× progress for 4× the sessions).** [SIM sessions]; avoids pressure and "not truly idle" complaints (12/37 files) [analysis].
**R25. Show a "welcome back" card with what happened.** [prototypes/offline.html; PUB].

**R28. Define each world as a data record (included/absent resources, a few modifiers, a gate cost table) so adding a world is a data edit.** Shark Game worlds [CODE games/shark-game.md]; Evolve per-reset constants tables [CODE]. Engineering rule, supports R20.
**R29. Gate a world with a multi-slot payment (3–4 named costs shown up front) that always pays a flat reward on completion.** Shark Game gate cost slots [CODE games/shark-game.md]; Synergism challenges [CODE]. [GUESS on 3–4 slots]
**R30. Offer banked offline time as optional spendable speed (e.g. ×5) alongside automatic gains.** Idle Loops [CODE games/idle-loops.md]; keeps returning players in control.

## F. Monetisation & UX
**R26. Cosmetic-only or time-skip sold; never sell prestige currency or gate world progress.** 14/37 files cite ad/IAP pressure, 11/12 mobile-first [analysis/anti_patterns.md].
**R27. Real numbers in tooltips, bulk-buy (×1/×10/×max), no hidden formulas.** Wiki-dependence complaint (NGU, Realm Grinder, CH) [analysis]. 

## Open questions (need play-testing)
Exact world length, whether 9 worlds is the right count, active-layer content, whether the ride should reset generators.
