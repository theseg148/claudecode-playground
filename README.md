# Idle-game research → Kamen Rider Decade idle design
Autonomous research project (started 2026-10-18 08:10:47 UTC, see START_TIME.txt / NOTES.md for the log).

## Read first
- **SUMMARY.md** — the 20 most important findings (with confidence tags C/P/H).
- **DESIGN_RULES.md** — concrete numeric rules R1–R42 with evidence level (C confirmed in code/primary data, P published/convergent, H hypothesis from our sim — play-test).
- **DECADE_IDLE_DESIGN.md** (+ **DECADE_WORLD_TABLES.md**) — the game design: loops, layers, reset table, nine worlds, systems roll-out, pacing plan, monetisation (default none), IP caution.
- **REVIEW_1.md / REVIEW_2.md** — adversarial reviews and what was fixed (kept for transparency).

## Evidence
- `research/` — foundations (math of idle games, design talks/postmortems, psychology, player complaints), `formula_tables.md` (source-verified formulas), `events_and_choices.md`, `ui_and_numbers.md`, `retention_monetization.md`, `decade_worlds.md` (lore, [S]/[M] tagged).
- `games/` — 47 game files in one template (24 carry [CODE]/[SRC] source-code evidence) (core loop, formulas, prestige, offline, monetisation, loves/hates, lessons) with [CODE]/[S]/[M]/[E] tags and verification logs. `_TEMPLATE.md` is the template.
- `analysis/` — cross-game analyses: growth curves, prestige designs, beloved patterns, anti-patterns, sequential-world freshness.

## Simulation (`sim/`, Python + matplotlib/numpy)
`sim.py` (greedy-payback player), `sweep.py`, `prestige_sweep.py`, `sessions_sweep.py`, `worlds.py`, `decade_model.py` (v1 toy models), `campaign.py` / `campaign3.py` (sessions + stepped offline + rides + carry sources + calibrated T_w and gates), `campaign_sweep.py`, `population.py`, `builds3.py`, `offline_lever.py`, `events.py`, `robustness.py`, `pacing_report.py` (PASS/FAIL checklist), `test_sim.py`. Results and caveats: **sim/results.md**.

## Prototypes (`prototypes/`, single-file HTML, open in a browser)
`milestones`, `offline`/`offline_v2`, `prestige` (v2), `unlock_tree`, `world_transition` (v2), `decade_slice_v2` (integrated 2-world slice with telemetry, Clock Up, mastery tree, Photo Windows) + `EVALUATIONS.md`.

## Limits (be honest)
Web access was limited to search snippets and raw GitHub files, so many game numbers are [M]/[E]; Guava Juice's game ("Tub Tapper") has almost no public data; all simulations are a toy greedy-player model, not validated against real players; the Kamen Rider lore hooks are fan-wiki sourced (Agito unverified). This is a fan project design — no Toei/Bandai assets.
