# Prototype evaluations
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
