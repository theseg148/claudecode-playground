# Evolve
**Sources:** (URLs, required)
Tags: [SRC] = read from open-source code this session; [MEM] = recalled, unverified; [EST] = my estimate.
- https://raw.githubusercontent.com/pmotschmann/Evolve/master/src/functions.js (calcPrestige, getResetConstants, costMultiplier) [SRC]
- https://raw.githubusercontent.com/pmotschmann/Evolve/master/src/resets.js (reset handlers) [SRC]
- https://raw.githubusercontent.com/pmotschmann/Evolve/master/README.md (project description; game is a "civilization from primordial ooze to spacefaring empire" incremental) [SRC]
- https://pmotschmann.github.io/Evolve/ (live game), https://github.com/pmotschmann/Evolve, https://www.reddit.com/r/EvolveIdle/ (community; reddit only reached via a search snippet saying plasmids soft-cap around 400-500 and the cap is raised by Phage)
- https://evolve-wiki.fandom.com (wiki; not reachable from the sandbox)

## Core loop
- Start as RNA/DNA in a "warm little pond", evolve a species (organelles -> nucleus -> eukaryotic -> ... -> sentience), choose a race, then found a city.
- City loop: assign citizens to jobs (farmers, lumberjacks, miners, scientists...), build houses/factories/labs, research techs which unlock further buildings and eras (primitive -> discovery -> industrialized -> globalized -> early space -> deep space -> interstellar -> ...).
- Heavy micromanagement: power, morale, stability, army and government. The game explicitly mixes clicker and idler. [SRC README]
- Every run ends in a reset (MAD / Bioseed / Cataclysm / AI / Big Bang / Ascension...), buying permanent bonuses with the reset currency to make the next run faster and reach a new reset.

## Resource types
- Early: RNA, DNA, Food, Lumber, Stone, Furs, Copper, Iron, Aluminium, Cement, Coal, Oil, Uranium, Steel, Titanium, Alloy, Polymer, Iridium, Helium-3, Neutronium, Elerium, Nano tubes, Graphene, Stanene, Bolognium, Vitreloy, Orichalcum. [MEM]
- Knowledge (science), Money, Mana, Soul gems, Infernite etc.
- Meta currencies: Plasmids (and Anti-plasmids), Phage, Dark Energy, Harmony Crystals, Artifacts, Cores, Supercoiled, Genes ("Genome" strands). [SRC: calcPrestige returns plasmid, phage, dark, harmony, artifact, cores, supercoiled, pdebt]

## Cost & production growth formulas (public or estimated; mark which)
- Structure cost = `base * multiplier ^ count` with the multiplier typically between ~1.1 and ~1.35 depending on building [MEM]; `costMultiplier(structure, offset, base, multiplier, cat)` applies trait modifiers like small/large/compact/tunneler/housing_reduction to the multiplier. [SRC functions.js:776]
- RNA/DNA costs are cut by 20% when the "evolve" gene is owned (`Math.round(cost*0.8)`). [SRC adjustCosts]
- Plasmid gain on reset: `new_plasmid = round(pop / pop_divisor)`, plus one plasmid for each step in a knowledge ladder: `while (know > k_inc) { plasmid++; know -= k_inc; k_inc *= k_mult }`. [SRC calcPrestige]
- Reset constants (pop_divisor, k_inc, k_mult, phage_mult, plasmid_cap): [SRC getResetConstants]
  - MAD: 3, 100000, 1.1, 0, 150 (synthetic races: 5, 125000, ., ., 100)
  - Bioseed/Cataclysm: 3, 50000, 1.015, 1, 400
  - AI: 2.5, 45000, 1.014, 2, 600
  - Vacuum/Big Bang: 2.2, 40000, 1.012, 2.5, 800
  - Ascend/Terraform: 1.15, 30000, 1.008, 4, 2000
  - Matrix: 1.5, 32000, 1.01, 3.2, 1800
  - Retired: 1.15, 32000, 1.006, 3.2, 1800
  - Eden: 1, 18000, 1.004, 2.5, 1800
- Soft cap: `plasmid_cap = floor(rc.plasmid_cap * (1 + (achievementLevel-1)/8))`; any gain above the cap becomes `cap + floor(overflow/(overflow+cap)*cap)`, so the overflow can at best double the cap. [SRC]
- Phage: `floor(log2(plasmids) * e * phage_mult)`. [SRC]
- Dark Energy (Big Bang): `ln(1 + 40*exotic) + log2(mass - 7)/2.5`; (Vacuum collapse): `log2(mana gen)/5`. [SRC]
- Harmony (Ascend): `min(achievement level,5)` times universe multiplier (micro x0.25, heavy x1.2, antimatter x1.1). [SRC]
- Apotheosis gives a fixed `(256>>4)**4 - 65535` plasmids (a joke constant). [SRC]
- Dark-energy and plasmid power effects use log curves (`Math.log(50+x)-3.912...`) i.e. strong diminishing returns. [SRC functions.js ~904, 1286-1341]

## Prestige structure
- MAD (Mutual Assured Destruction): first reset; gives Plasmids (Anti-plasmids in anti-universe); makes the next run faster. [SRC/MEM]
- Bioseed: leave the planet, gives plasmids + Phage; Cataclysm variant for the cataclysm challenge. [SRC]
- Black Hole / Vacuum collapse / Big Bang: Dark Energy, which strengthens universe-specific bonuses. [SRC]
- AI Apocalypse -> Cores; Matrix, Retired, Eden, Terraform, Descend (artifacts), Apotheosis (Supercoiled, end-of-chain). [SRC]
- Genes (CRISPR-like "Genome" system) allow keeping traits across resets, with challenge-mode multipliers `challenge_multiplier()` applied to every reward type. [SRC]
- Universes (standard, heavy, micro, antimatter, magic) change rates and resets. [SRC partial]
- Run-length targets: first MAD ~1-3 hours of play; later resets compress to 20-60 minutes once plasmids stack. [EST]

## Unlock pacing
- [MEM/EST] Evolution phase 5-10 min; early civic game ~30 min; Industrial ~1 h; first MAD reset 2-4 h; space tech 3-5 h; Bioseed/Black Hole days; Ascension and AI weeks; Apotheosis months.
- Resets are the way to unlock: plasmid thresholds gate new traits and the Phage cap, which gates challenge genes. [MEM]
- Challenges ("Genes") add +multiplier to all reset currency, so veterans re-run early eras under handicap for more gain. [SRC/MEM]

## Offline progress
- [MEM] Evolve does not simulate offline gameplay; it stores accumulated "time warp" ticks that the player can spend to fast-forward ("Time Skip", up to a cap, accrual about 1 tick per 5 minutes of real offline time... exact constants unverified). [MEM, EST]
- Because production depends on tunable assignments, closed-form offline would be unsafe, so the design is "bank time, spend later".
- Browser tab must stay open for real-time income. [MEM]

## Monetization effects
- Free, open-source browser game (GitHub Pages) with no ads or purchases. [SRC README]
- Contribution policy: "features that only make the game easier will not be accepted" - a design stance against shortcuts. [SRC README]
- Sustained by Patreon/donations (not verified). [MEM]

## What players love
- Real strategic depth: governments, races/traits, and how era choice changes the run.
- Reset layers each introduce a mechanic (not just a bigger number).
- Meaningful theorycrafting community and an in-game wiki.
- Open source and no monetization pressure.

## What players hate
- Overwhelming micromanagement (job assignment, power, morale) early in each run.
- Steep learning curve; long first runs.
- Plasmid softcaps feel punitive when you're behind. [community snippet: soft-caps in the 400-500 range]
- Slow late runs that need real-time attention.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Each reset type should have its own constants table (divisor, ladder step, softcap, bonus multiplier), exactly like getResetConstants: easy to balance and tune per world.
2. Gain = population-like term + milestone ladder (k_inc, k_mult): rewards both breadth and depth in one run.
3. Soft-cap with overflow `cap + overflow/(overflow+cap)*cap` is cheap and keeps the number from exploding while still rewarding overshoot.
4. Use `log2(x)*e*mult` style secondary currency (Phage) from a primary one (plasmids) for a second, slower progression layer.
5. Let a challenge-multiplier apply uniformly to all reset rewards, so "harder" modes feel worth it without new content.
6. Cut early micromanagement for a no-fighting game: drop job assignment; keep the *choice of build* as one-time picks per world (Rider form), not continuous juggling.
7. Offline: "bank time and spend later" suits games with complex interactions; for a simple upgrade idle, a capped closed-form is better.
8. Keep rule: no easy-mode shortcuts in the base game; sell cosmetics only (Rider suit skins) if monetized.
