# DECADE IDLE — Design document (v2)
Applies DESIGN_RULES.md v2 (R-numbers) and REVIEW_1.md. Fantasy: Tsukasa travels the Rider worlds in sequence, photographing each one and *restoring* it by upgrading it — no fighting. Lore hooks are verified in research/decade_worlds.md ([S] vs [M]); fan project, see §9.

## 1. Loops
- Seconds: auto-collect + tap "Photo Op"; buy; watch the ×2 bar fill.
- Session (10 min): 1–2 rides' worth of decisions: welcome-back card → spend → build choice → optional Final Form Ride.
- World (3–4 days): ~8–12 Final Form Rides, gate completed, Dimension Ride.
- Campaign: 9 worlds ≈ 4.5 weeks flat or ≈ 7 weeks lengthening (R23, R25), then finale + post-game.

## 2. Structure
**Ladder per world:** 8 tiers (names per world), cost ×8–12 per tier, rate ratio = cost ratio/1.3, growth 1.12 (R1–R2). ×2 milestones at 10/25/50/100/200 owned (R3) shown as bars (R4). Tier N+1 visible at 5 owned of N (R5).
**Layer 1 — Final Form Ride (in-world, R15–R19):** Seals pending = floor(sqrt(run_lifetime/T_w)); production multiplier = (1+Seals)^0.5 (sim v3; linear +8 %/seal explodes). Player rides when it raises production ≥1.5× (highlighted, with before/after preview). T_w is calibrated so the first ride lands ≈8 min into play in every world (R10, R16). Rhythm: ≈9–11 rides per 3.2-day world (≈3.4/day), each ≥1.5× production by construction. The prototype slice still uses a DEV linear formula (+8 %/seal) for quick feel-testing.
**Layer 2 — Dimension Ride (to next world, R24):** NOT a formula: a fixed carry multiplier c per cleared world (c ≈ cost-scale s / 1.0–1.2) plus one Ride Card; gated by the world objective (§4). Number of hops: 8.
**Layer 3 — "All Riders" (post-game, R31):** only layer with a formula (log-scaled), unlocked after world 9.
Layers ≤3 (R20).

### Reset table (answers REVIEW H1)
| Thing | Final Form Ride | Dimension Ride |
|---|---|---|
| Shots, generators, tier unlocks, milestone progress | reset | reset |
| Seals (L1 points) | kept (+gain) | archived per world; each cleared world adds a *bounded flat* +1 % permanent bonus, counted inside the carry budget (REVIEW_2: an unbounded √-formula collapses later worlds to 0.3 d) |
| Mastery tree nodes | kept | kept for that world; 3 cross-world nodes pooled |
| World currency | kept | frozen in old world (visible in the album) |
| Charge (Kabuto's Clock Up resource) | reset to full | reset |
| Automation, offline upgrades, Ride Cards, Driver forms | kept | kept |
| Photo Op cooldown | continues | continues |
Rule: nothing the player earned by *decision* (tree, cards, forms) is ever lost; only the generator run resets (R42).

## 2b. World as data (R27–R28)
World record = {name, tier names, ratio table, rule id, local currency, gate (3–4 named costs), per-world T_w, carry c}. Engine = one generic ladder + rule plug-in. Gate pays a flat Ride Card. Offline time banks into a "Time Skip" charge (×5 speed) alongside automatic gains (R36).

## 3. Worlds (order free, Kabuto first, Kuuga last as the finale; show order is Kuuga…Hibiki but fixed here)
| # | World | New rule (verb) | Themed upgrades (no combat) | Gate (3 named costs, examples) |
|---|---|---|---|---|
| 1 | **Kabuto** | *Clock Up*: spend Charge for ×N speed 10 s; *Cast Off* at **40** owned sheds a tier for a stronger one | Clock Up Prep Station, Hyper Clock Up time-skip, Cast Off / Put On, Zecter Roster (Kabuto, Gatack, Drake, Sasword, Hercus, TheBee as worker types) [S], Grandma's Recipes menu, ZECT Logistics, Phylloxera Mirror | Shots 1e18 · 3 Zecters collected · Hyper Clock Up unlocked |
| 2 | Den-O | *Contracts*: assign Imagin to generators | DenLiner route map, Rider Pass stamps, Imagin contracts (Momotaros, Urataros, Kintaros, Ryutaros) [S], Climax fusion, Time Table | Shots · 4 Imagin contracts · Route length 8 |
| 3 | Faiz | *Routing*: link tiers for adjacency bonus | Mission Memory slots, phone-keypad macros, Photon-blood channels, Laundry Express [M] | … |
| 4 | Ryuki | *Advent Cards*: 3 slots, card packs by milestone | Contract-monster feeding (income), deck slot, mirror polish, ORE Journal press run [M]; Rider War reframed as card collecting | … |
| 5 | Blade | *Fusion*: combine two cards | Rouze Card sorting by suit (set bonuses), BOARD archive, Rouzer maintenance | … |
| 6 | Kiva | *Day/Night*: night boosts rare tier, day boosts base | Castle Doran greenhouse, Fuestle set collection, Violin varnish [M], Kivat duet | … |
| 7 | Agito | *Forms*: Ground/Flame/Storm/Trinity | G3 suit mk, Altering ring, Unknown patrol [all M — Agito unverified] | … |
| 8 | Hibiki | *Training rhythm* (optional taps) | Onkaku tuning, Ongekibou practice, Oni retreat, Tachibanaya cafe [M] | … |
| 9 | Kuuga (finale) | *Colour switch*: Mighty/Dragon/Pegasus/Titan rotation | Arcle upgrades, Amadam polish (= offline cap), Pegasus eye (auto-collect radius) | All 8 previous Ride Cards + 3 named costs |
Worlds 3–9 gates are placeholders to fill during content design. **Main-screen counters ≤3:** Shots, Seals, and one per-world counter (World 1: Charge; later worlds: the world currency). Everything else lives on its own screen: mastery points (tree), Exposures (event strip), Swap Tokens (deck), Time Skip (offline card), Ride Cards (album) — REVIEW_2 counted 8–9 counters in total, so the screens, not the count, are what keeps the UI legible (R26, R40).

## 4. World objectives (the ride gate)
Each gate = 3 named costs (R28): (a) lifetime Shots ≥ goal·s^w (the pacing-controlled one: 1e18·s^w in the sim = ~3 days), (b) a collection requirement ("3 Zecters"), (c) a mechanic requirement ("use Hyper Clock Up once"). Completing pays a Ride Card (flat). Reveal the next world's card at ~1/3 of the gate (R30 endowed progress when you arrive: bar starts at the carried-over card value, with the reason shown).

## 5. Pacing plan and check table (from sim/results.md campaign v3)
- **Recommended (sim v3): s=3, total carry budget c≈2.25 plus cards/archive/achievements so that drift d≈1.0; gates ×2.5–3.5 per world (6.2e15 → 4.0e19 for 3.2-day worlds); ≈29 d (≈4 weeks) for a 3-session/day player; 1 session/day ≈ 80–150 d, 6 sessions/day ≈ 16–33 d (population sim).** Every permanent carry source must be inside the budget (R23).
- Per world (sim v3, unique goals): ≈51 distinct goals (8 tiers × (1 + 5 milestones) ≈ 40 + ≈11 rides); only 64–73 % of sessions contain one, max dry streak 2 (4 in W4). The remaining sessions must contain a *beat* from other systems (mastery node, album entry, Photo Window reward, fusion discovery) — at least one per session (R25, R32).
- Offline: stepped 50 %/25 %, cap 8 h (upgradable to 24 h) (R33). Active-tools budget (R34c): Clock Up ≤1.25× average, Photo Op ≤1.1×, Photo Windows ≈1.05–1.1× of daily progress; all together ≤1.5× in an active session.
- Checks (automate in test_sim.py): each ride ≥1.5× production (by construction); first ride ≤15 min in every world (≈8 min calibrated); gates grow ×2.5–3.5 per world; no soft-lock after any reset (start gold = tier-0 cost); ≥1 beat in every session.

## 6. Upgrade families (what the player decides — R13)
1. Generators (spine). 2. ×2 milestones. 3. Mastery tree (~25 nodes/world, 3 branches; points capped at ≈4 per world so builds stay exclusive; respec costs 1 point per node moved — free respec removes the decision): **branch choice = build** (e.g. Kabuto: Speed vs Cast-Off vs Recipes — each must reach the gate on its own; first fork at ≈2:00 by picking one of three root nodes with a *starting* point granted at world entry, since ride points only arrive after ≈8 min — REVIEW_2 P1-7; R13). 4. Automation (first ride shop, R21). 5. Offline upgrades. 6. Ride Cards (earned only). 7. Driver forms (cross-world, small). 8. Photo Op: unscheduled 13 s window every 5–15 min, ≤1.2× average (R38).

## 7. Transition moments
Pre-ride card reveal (1/3), ride flash + recap card (time, kept, reset — see reset table), arrival with endowed bar and a ≤60 s first purchase (R10), new-rule tooltip (3 steps), cleared-world income bump visible (R29). Finale: Kuuga clear plays the ending; unlocks Another-World replay (restrictions) and "All Riders".

## 8. Monetisation (R39)
Default: **none** (fan project, Toei IP; research/retention_monetization.md: Apple/Google/Belgium loot-box rules avoided by deterministic unlocks; Cookie Clicker Steam is a clean one-time model). Design for ~5 short sessions/day (GameAnalytics 2020 idle benchmark, 5.3 sessions × 8 min, vendor/[S]). If commercialised later: Cosmetic Driver skins/photo frames; optional opt-in rewarded boost; time-skip packs only if they never gate a world (treated as pacing, per sim); no sale of cards/Seals.

## 9. Lore & IP (research/decade_worlds.md)
Verified [S]: Kabuto (Clock Up, Cast Off, Hyper Zecter, Zecter roster), Den-O Imagin, Kiva Fuestles/Castle Doran, Blade Rouze Cards, Faiz Mission Memories, Hibiki Onkaku. Unverified: Agito; "Tenshi", "Misaki Kaoru" (dropped); Hikari Studio framing. Fan project: no assets/logos/card images; consider renaming mechanics before release; non-commercial.

## 10. Risks / next
Greedy toy sim; unknown real session behaviour; nine rules = content cost (ship 3 worlds first: Kabuto, Den-O, Faiz); tuning T_w, bonus/pt, c need play-tests. prototypes/decade_slice.html implements a 2-world slice with telemetry for tuning.

## 11. Technical notes (research/ui_and_numbers.md)
Native doubles suffice (peak ≈6.5e22 vs 1.8e308 limit). Named-short notation to 1e33; log-scale gate bar; versioned `DECADE1:` export string; autosave + backup slots.

## 12. Systems roll-out (from research/events_and_choices.md; one new system per world — R26)
| World | New system introduced | Notes (numbers [H]) |
|---|---|---|
| 1 Kabuto | Photo Window event (first at ~3:00, then every 90–240 s foregrounded; banked offline Exposures) + Clock Up | windows ≈ +30 % of active-session gain, ≈3 % of daily progress (sim/results.md events) |
| 2 Den-O | Album (16 entries/world; achievement ×1.05^rows·1.01^count on base Shots) + Form Deck (3 slots 3:2:1, swap tokens, switch cost 1 top-tier unit) | best deck +17.6 % vs median; several near-equal decks |
| 3 Faiz | Approach pick at world entry (Documentary/Portrait/Landscape: +25 % one tier family, −10 % other; one re-pick token) | build fork per world (R13b) |
| 4 Ryuki | Constraint Shoots (2 optional challenges/world; first clear = automation or ×1.15; ≤ ×3.1 total from multipliers) | unlocked after base verb used ≥5 times |
| 5 Blade | Studio Garden (3×3 card-adjacency board, 5-min tick, 1 tick/30 min offline, max 12 banked; +20–25 % for 9 cards, cap +35 %) | fusion discoveries 6–8 per world |
| 6–9 | No new system; deepen existing (board 4×4→5×5, more forms, harder shoots) | lull audit R32 |
Crew/jobs layer (Kittens-style): optional alternative to the generators-only fork at 2:00 of world 1 — decide after play-test; skip if it adds a 4th currency.
Never copy: negative golden-cookie outcomes, offline penalties, hidden slot interactions, gifted-boost economies (events_and_choices §5.10).
First 10 minutes of World 1 (target, [E]; Forms/Album arrive in World 2, so they are NOT in this timeline): 0:00 Photo Op, 0:20 tier 1, 0:45 first ×2 bar, 1:30 tier 2 (visible at 5 owned), 2:00 first fork (Approach-lite: pick Speed / Cast Off / Recipes root), 3:00 first light automation (auto-collect + auto-buy tier 1 only) and first Photo Window, 4:00 Clock Up unlocked, 5:30 first Zecter joins (tier 3), 8:00 ride preview, ≈8–10:00 first Final Form Ride (≥×1.5 production, R16). Full payback auto-buy comes with the first-ride shop (R21).
