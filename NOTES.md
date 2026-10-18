# NOTES

## Run 1 (started 08:10:47 UTC)
- Built sim/ (sim.py, sweep.py, worlds.py, results.md v1). Launched 6 subagents (math, psychology/complaints, 4 game batches).
- Key: cost_ratio/rate_ratio ~1.2-1.5 best; world time ~ (cost_scale/carry)^n.
- 08:14 psychology.md (155 lines) + player_complaints.md (171) done by subagent (its handback text said only 'placeholder'; files verified OK, cited, evidence-tagged [V]/[B]/[P]).
- 08:16 ENVIRONMENT LIMIT: WebFetch/curl are blocked (DNS/proxy) for wikis, reddit, wikipedia; only WebSearch snippets work. Game files from batches A,B (16 games) carry tags [S]=search snippet, [M]=memory, [E]=estimate. Only Cookie Clicker cost formula is source-confirmed. DESIGN_RULES must label evidence strength honestly. Guava Juice game = "Tub Tapper" (Roi Fabito, 2018), no public formulas.
- 08:16 raw.githubusercontent.com WORKS via curl -> source-code formula mining agent launched ([CODE] tag). Batch C (10 zone games) done; only Progress Knight formulas from source.
- 08:17 verify batch 2 done: Paperclips MegaClipper 1000*1.07^n [S]; CC 1.15^n, cube-root prestige [S]; Guava Juice Tub Tapper launched by Studio 71 per Tubefilter 2018-05-24 (otherwise little public).
- 08:18 verify batch1 done: AD DimBoost uses 8th dim 20+15/boost; CH monster HP x1.145/zone; Melvor offline cap 24h; Egg Inc soul egg +10% linear. Several earlier [M] numbers corrected.
- 08:19 math_of_idle_games.md (273 lines) + design_talks_postmortems.md (262) done. Key: r 1.07-1.15; AdCap r drops .01/tier, base x12/tier; milestone M~r^S; prestige reset when pending>=50-200% of current; targets first buy 60s, automation 3min, first prestige 10-15min (blog opinions).
- 08:20 analysis/growth_curves.md + prestige_designs.md done. Only ~11/37 games have confirmed cost formulas.
- 08:23 source mining round1 done (AD costs, Kittens ratios, Trimps, Synergism, Evolve, Bitburner, PK) -> research/formula_tables.md. Round 2 launched.
- 08:24 Phase 3 complete (5 analysis files). Next: DESIGN_RULES, DECADE_IDLE_DESIGN, SUMMARY drafts, then improve.
- 08:25 DESIGN_RULES, DECADE_IDLE_DESIGN, SUMMARY v1 drafted. Elapsed ~15 min; now improvement loop: contradictions, more sim, more games, prototype upgrades.
- 08:27 decade_slice.html built & headless-tested (94% goals in band). robustness sim done.
- 08:28 decade_worlds.md verified by agent; design doc patched (Kabuto upgrades, IP caution).
- 08:28 Round2 mining: AD IP=10^(log10(AM)/308-0.75), EP=5^(log10(IP)/308-0.7), RM=1000^(log10(EP)/4000-1); Kittens paragon=kittens-70; Cookie Clicker mirror ozh/cookieclicker has main.js (CC NOT closed source: price base*1.15^n, prestige cbrt(c/1e12), golden cookie 5-15min/13s); Paperclips AutoClipper 1.1^n+5, Mega 1000*1.07^n, trust at Fibonacci x1000 clips; Synergism offline 72h(+8h) ; Prestige Tree formulas.
- 08:29 batch E: 10 more games (now ~47 files). Shark Game worlds = data records w/ gate cost table; Idle Loops banks offline time as 5x spendable speed; Prestige Tree layers = worlds w/ order choice. 
Lessons added to world design: world = data record; multi-slot gate payment; offline time banked.
- 08:34 REVIEW_1 applied: DESIGN_RULES v2 (42 rules w/ C/P/H confidence), DECADE_IDLE_DESIGN v2 (reset table, objectives, world gates). Campaign sim v2 reconciles world length: ratio 1.0-1.2 => 27-48 d.
- 08:38 retention_monetization.md + ui_and_numbers.md done; decade_slice_v2 built (found/fixed post-hop soft-lock). R39: default no monetisation; R40a: doubles suffice.
- 08:41 events_and_choices.md done (342 lines). events.py: windows 2.5-3.6% of daily progress, ~+30% active session; form deck best +17.6% vs median; ach mult x10 at 144.
- 08:43 population.py: campaign days ∝ 1/sessions per day (gentle variant 99/49/33/26/21 d for 1/2/3/4/6 sessions). Rules updated. Waiting on REVIEW_2 + 2 weak-game upgrade agents.
