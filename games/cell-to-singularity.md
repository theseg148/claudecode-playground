# Cell to Singularity
**Sources:** (URLs, required)
- https://en.wikipedia.org/wiki/Cell_to_Singularity (entropy as currency, eras)
- https://cell-to-singularity-evolution.fandom.com/wiki/MetaBits (Metabits as prestige, reboot via first Singularity; seen in search snippet, page itself failed to fetch)
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii (general prestige math)
- Legend: [PUB] from sources above; [EST] my recollection/estimate, unverified. Exact numeric formulas were not retrievable here.
## Core loop
- Tap to generate Entropy; buy "generators" (life nodes) that generate entropy per second.
- Spend entropy to unlock Milestones along an evolution tree: Cell -> Multicellular -> Fish -> Land animals -> Mammals -> Humans (Anthropocene) -> Industrial -> Information Age -> Singularity [PUB general].
- Each tree entry is an "upgrade card" with an educational description of an evolutionary milestone.
- Ideas (a secondary currency) come from Humans/tech nodes and unlock the later eras [EST].
- Periodically you "Reboot" for Metabits.
## Resource types
- Entropy (main), Ideas (tech era), Metabits (prestige) [PUB], Trilobites / Dark Matter / Black Holes in the "Singularity" or Reality Engine layer [EST].
- Reality Engine: Metabits upgrade it (global multipliers) [PUB].
- Mesozoic Valley: a sub-game (stage/area) with its own mini-puzzle currencies [EST].
- Premium currency: Trilobites/Dino bucks? ("Vault" gems) [EST].
- Animals/Species count as collection (Biome).
## Cost & production growth formulas (public or estimated; mark which)
- Generator cost: standard idle form `cost_n = base * r^n` with r near 1.07-1.15 [EST].
- Entropy per second per node: base x level x milestone multiplier (x2 at preset levels) [EST].
- Metabits gain: nonlinear in entropy earned; "each metabit requires more entropy and ideas than the last" [PUB, fandom comment] => likely `floor(c * (E/E0)^k)` with k < 1 [EST].
- Singularity: cumulative; first purchased Singularity enables reboot [PUB].
- Era unlock costs jump ~1e3-1e6 each era (heavy step) [EST].
- Time-based "Mesozoic Valley" costs use different arcs.
## Prestige structure
- Reboot (Simulation Reboot): reset entropy, ideas, generators; gain Metabits proportionate to run [PUB].
- Metabits buy Reality Engine upgrades, permanent global multipliers [PUB].
- After reboot, the tree is rebuilt faster because multipliers apply from the start.
- Extra layers: "Dark Matter"/"Eternal Reboot" in late updates [EST].
- Second layer by Singularity: crossing it triggers "ending" and a new loop on a different timeline (Interstellar) [EST].
## Unlock pacing
- Early: new tree node every 30-60 seconds, new era every ~20-40 min [EST].
- Each era is thematically new (cell, fish, mammal, human, machine), with its own art/background and educational text. So the same "buy generator" mechanic reads as different worlds.
- Later eras gate on Ideas, a currency that appears after earlier content.
- Metabits unlock quality-of-life (auto-buy, speed) fairly early so repeated runs don't repeat grind.
- Achievement-style "Milestones" keep fresh goals every few minutes.
## Offline progress
- Entropy accrues offline at a fraction of rate; offline cap exists (hours) [EST].
- Ad-boost doubles offline earnings (watch ad) [EST].
- Offline plus daily check-ins is core to its mobile retention.
## Monetization effects
- Rewarded ads for 2x boosts, speed-ups; IAP for Trilobites (premium), removing ads [EST].
- "Dino bucks"/Trilobites buy Tree Instant unlocks and cosmetics [EST].
- Ad boost must be used to hit pacing; non-payers still progress [EST].
## What players love
- Educational and thematic: evolution timeline gives meaning to each upgrade [PUB].
- Strong visual evolution of the biome as you progress.
- Frequent unlocks, easy to understand.
## What players hate
- Metabit grind: each reboot yields less relative gain; slow late game [PUB comment].
- Ads/premium nudges [EST].
- Some updates break balance / lag [EST].
## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Era = world: each Rider world is a themed era with its own art background and descriptive card text; same engine, new skin and new "ideas"-like secondary currency.
- Teach through cards: each upgrade is a "Rider card" with lore, so reading is part of reward.
- Use a secondary currency that first appears in a later world to make it feel mechanically new (Ideas analogue: "Hero Memory").
- Prestige should rebuild the tree faster: provide auto-buy and starting multipliers early.
- Metabit sublinear payout: model it as sqrt/log of progress; communicate the next-reward threshold.
- Keep a visible "milestone" list for constant micro-goals.
- Avoid ad-pressure: pacing should not require ad-boosts.
