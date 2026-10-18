# Increlution
**Sources:** (URLs, required)
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii (general prestige and variation math)
- https://itch.io/post/11613541 (forum context, loops subgenre; low quality)
- https://ui.lemm.ee/post/22865493 (thread placing Increlution next to Stuck in Time and Cavernous; commenter: speed improvements are polynomial)
- Honest note: Increlution's wiki was not reachable and no dedicated guide came back in search. Most mechanics below are [EST] from memory of the game (Steam, by Gilles? / "Sam" unknown). Treat as low confidence. Legend: [PUB] source-attested; [EST] estimate.
## Core loop
- Time-loop incremental: you queue actions (gather, craft, explore, fight-less training) that use up a daily/loop clock; the loop ends and you restart with permanent progress.
- Actions have progress bars; repeated actions level up and speed up; some unlock new actions.
- Each loop you decide an order of actions (a mini routing puzzle), then rewatch it play out.
- The game belongs to the "loops" subgenre with Stuck in Time and Cavernous [PUB].
## Resource types
- Action XP, Action levels, Stats (strength, etc.), Items/materials, Knowledge points, "Increlution" currency (Mastery/Evolution) [EST].
- Age/time budget per loop; Karma-like permanent stat [EST].
- Premium/none: Steam paid [EST].
## Cost & production growth formulas (public or estimated; mark which)
- Speed improvements are polynomial [PUB, forum commenter], not exponential: action speed ~ level^p with p > 1? [EST].
- Action XP requirement: `base * level^2`-ish [EST].
- Prestige gain ~ sqrt of loop progress [EST].
- Time budget per loop grows additively with upgrades [EST].
- General approach: polynomial progress keeps numbers small and readable (contrast with Cell to Singularity's exponentials).
## Prestige structure
- The loop itself is the prestige: reset on loop end; permanent upgrades carry (stats, unlocked actions, autos) [EST].
- Larger resets ("evolve") reset everything for bigger multipliers [EST].
- Each loop reveals new knowledge, so planning improves.
- Layer count: 2-3 [EST].
## Unlock pacing
- First loop: minutes. Early loops introduce a new action or mechanic each time [EST].
- Unlocks are knowledge-gated (discover item/location) rather than only currency.
- Automation unlocks let you queue longer plans [EST].
- Pacing feels like a puzzle campaign: each new area adds routing choices.
## Offline progress
- Probably limited; game is session-oriented with queue automation [EST].
- Queues running offline at partial rate [EST, unverified].
## Monetization effects
- Paid Steam game, no IAP [EST].
- No pressure.
## What players love
- The routing/queue puzzle plus steady, understandable progression [PUB sentiment on loops subgenre].
- Fresh reveals per loop.
## What players hate
- Slow late loops; repetitive re-execution [EST].
- Sparse documentation (hence little wiki coverage).
## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Make each Rider world a "loop": a timed segment whose end is a reset, with knowledge unlocked permanently.
- Knowledge-based unlocks keep worlds fresh without bigger numbers.
- Polynomial speed growth keeps pacing steady; consider polynomial rather than exponential for per-world upgrades.
- Queue/ordering as the player's only "action", ideal for no-fighting design.
- Offline: let queues run when idle.
