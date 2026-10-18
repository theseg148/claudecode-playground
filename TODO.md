# TODO

## Phase 1: Foundations -> research/
- [x] research/math_of_idle_games.md
- [x] research/psychology.md (compulsion loops, variable rewards, goal gradient, numbers go up)
- [x] research/player_complaints.md (reddit, reviews, quit reasons)
- [x] research/design_talks_postmortems.md

## Phase 2: Games -> games/<name>.md (30+; template in games/_TEMPLATE.md)
- [x] Cookie Clicker
- [x] Adventure Capitalist
- [x] Egg Inc
- [x] Antimatter Dimensions
- [x] Realm Grinder
- [x] Clicker Heroes
- [x] NGU Idle
- [x] Melvor Idle
- [x] Universal Paperclips
- [x] Idle Miner Tycoon
- [x] Kittens Game
- [x] A Dark Room
- [x] Trimps
- [x] Idle Slayer
- [x] Leaf Blower Revolution
- [x] Guava Juice's game
- [ ] Others (world/zone progression): AFK Arena, Idle Heroes, Swamp Attack, Cell to Singularity, Idle Breakout, Candy Box 2, Evolve, Progress Knight, Increlution, Spaceplan, Clicker Heroes 2, Hero Wars idle, Tap Titans 2, Idle Champions, Bitburner, Synergism, Magic Research, Idle Wizard, Cultist Simulator-ish, Farm idle, Egg Inc already, Mr. Mine, Idle Mining Empire
## Phase 3: Analysis -> analysis/
- [x] growth curves compare
- [x] prestige designs
- [x] beloved patterns / anti-patterns
- [x] sequential worlds freshness
## Phase 4: Simulation -> sim/
- [ ] sim.py
- [ ] sweeps
- [ ] Decade world model
- [ ] sim/results.md
## Phase 5: Prototypes -> prototypes/
- [ ] prestige, offline, unlock tree, world transition, milestones + evaluations
## Phase 6: Final
- [ ] DESIGN_RULES.md
- [ ] DECADE_IDLE_DESIGN.md
- [ ] SUMMARY.md

## Added (run 1)
- [ ] Verification pass: use WebSearch (standard) to confirm [M]/[E] formulas per game (Egg Inc, AD, AdCap, Trimps, Kittens); upgrade tags to [S]; clean Egg Inc soul-egg sentence
- [ ] Guava Juice Tub Tapper: search more (reviews, App Store text, dev interviews) for mechanics
- [ ] Decade world content: verify Kabuto/Den-O etc. mechanics via WebSearch
- [ ] Prototype evaluations (prototypes/EVALUATIONS.md)
- [ ] Sim: add offline/active-play modes, per-world prestige inside worlds, Decade world model with real Rider order
- [ ] 30+ games total (currently 16 + batches C/D pending)

## Improvement backlog (run 1, after v1 deliverables)
- [ ] Review DESIGN_RULES for contradictions (fixed R18 ratio direction); cross-check each rule vs sources
- [ ] Sim: active-layer (golden-cookie-style events) model; in-world prestige + world hops combined; multi-seed robustness (random player strategies, not just greedy)
- [ ] Sim: sensitivity of goal-gap band to number of tiers (4,6,8,10) and per-world 'new mechanic' unlock cadence
- [ ] Sim: model the "wall" rate vs. players abandoning (retention proxy)
- [ ] More games (target 45): Idle Heroes, Egg Inc done, Hades Star?, Cell Lab?, Clicker Heroes done, Fallout Shelter idle?, Tap Tap Plane?, Soda Dungeon, Realm Grinder done, Derivative Clicker, Idle Loops, Universal Paperclips done, "Reddit: top 20 incrementals" list, Gnorp Apologue, Orb of Creation, Shark Game(Fishing), Sandcastle Builder, Doodle Farm?
- [ ] Prototype: full vertical slice combining milestones+ride+offline+tree (prototypes/decade_slice.html), with a pacing telemetry overlay
- [ ] Verify Kabuto/other Rider world details by WebSearch (names of Zecters etc.)
- [ ] Re-run verification where web access allows; review [M]/[E] tags
- [ ] Charts embedded in sim/results.md (png references)
