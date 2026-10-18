# Increlution
**Sources:** (URLs, required)
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii (general prestige and variation math)
- https://itch.io/post/11613541 (forum context, loops subgenre; low quality)
- https://ui.lemm.ee/post/22865493 (thread placing Increlution next to Stuck in Time and Cavernous; commenter: speed improvements are polynomial)
- https://store.steampowered.com/app/1593350/Increlution/ , https://www.gamingonlinux.com/2021/05/check-out-the-demo-for-increlution-a-survival-idle-game-up-on-steam/ , https://www.dekudeals.com/items/increlution (store text via search snippets) [S]
- https://steamcommunity.com/app/1593350/discussions/0/4626981776940619365 (automation unlock requirement), https://steamdb.info/patchnotes/10359027 , https://steamdb.info/patchnotes/11414612 , https://steamdb.info/patchnotes/8866572/ (dev patch notes via snippets) [S]
- https://github.com/richardcocks/Increlution-Tools (README read: automation loadout editor) and https://github.com/lgl017temp/increlution-tools (README+package.json read) [CODE]; third-party fan tools, not game source; copies in /tmp/claude-0/-home-user-claudecode-playground/2e77cd6e-e441-551f-a27e-40f493265545/scratchpad/src5/increlution/
- Honest note: no official wiki found. The game's own source is not on GitHub. Developer name is NOT confirmed (earlier guesses removed). Legend: [S] snippet, [CODE] third-party tool code, [EST] estimate.
## Core loop
- Store text: minimalistic incremental time-management game inspired by roguelites; health declines faster over time until you die; death starts a new life and progress in previous lives raises your "instincts" [S dekudeals/gamingonlinux]. You queue actions step by step; the game pauses automatically when the queue is empty [S]. (Earlier "daily/loop clock" wording was a guess.)
- Actions have progress bars; repeated actions level up and speed up; some unlock new actions.
- Each loop you decide an order of actions (a mini routing puzzle), then rewatch it play out.
- The game belongs to the "loops" subgenre with Stuck in Time and Cavernous [PUB].
## Resource types
- Confirmed: health/time per life, instincts (carry across lives), reincarnation screen between lives [S]. Action categories in the automation editor: Jobs, Construction, Exploration, organised by chapter [CODE richardcocks README]. All other currencies listed earlier (Knowledge points, Mastery, Karma) were guesses and are UNCONFIRMED [EST].
- Age/time budget per loop; Karma-like permanent stat [EST].
- Premium/none: Steam paid [EST].
## Cost & production growth formulas (public or estimated; mark which)
- Automation unlock: completing an action about 400 times at level 8 was the requirement a player called too high (suggesting 150 and 3); another notes it is lowered in New Game+; a player asked for the hourglass action to automate after 1-2 completions instead of 10 [S steam thread above]. Chapter-5 tools and chapter-7 constructions reduce other automation requirements [S patch notes]. Automation priority levels: Off/Low/Regular/High/Top [CODE].
- Speed improvements are polynomial [PUB, forum commenter], not exponential: action speed ~ level^p with p > 1? [EST].
- Action XP requirement: `base * level^2`-ish [EST].
- Prestige gain ~ sqrt of loop progress [EST].
- Time budget per loop grows additively with upgrades [EST].
- General approach: polynomial progress keeps numbers small and readable (contrast with Cell to Singularity's exponentials).
## Prestige structure
- The loop itself is the prestige: reset on loop end; permanent upgrades carry (stats, unlocked actions, autos) [EST].
- Larger resets: New Game+ exists [S] (lowers automation requirements). Names such as "evolve" were guesses [EST].
- Each loop reveals new knowledge, so planning improves.
- Layer count: 2-3 [EST].
## Unlock pacing
- Free demo covers chapter 1 with Steam Cloud sync to the full game; Early Access since 13 Oct 2021; fan tooling referenced chapter 11 by June 2023 [S gamingonlinux; CODE lgl017 README]. Reviews 85% positive of about 1,233 at one snapshot [S steamdata.ai]. Early loops introduce a new action or mechanic each time [EST].
- Unlocks are knowledge-gated (discover item/location) rather than only currency.
- Automation unlocks let you queue longer plans [EST].
- Pacing feels like a puzzle campaign: each new area adds routing choices.
## Offline progress
- Dev patch notes: options added to accumulate offline time while a menu or the reincarnation screen is open, fast-forwarding until a paused state is reached; a later patch removed an internal cap limiting offline progress to 5% of total playthrough time [S steamdb patchnotes via snippet]. A mod article says offline time does not accumulate once the game pauses at an automation-locked action [S https://gamepretty.com/increlution-how-to-unlock-all-automations-with-mod/].
## Monetization effects
- Steam game with a free demo [S]; price and absence of IAP not verified [EST].
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

## Verification log (refreshed 2026-10-18)
- Refreshed 2026-10-18: 3 more WebSearch queries plus GitHub search. Replaced the earlier guesses with store text (health, death, instincts, queue, auto-pause), automation rules and offline patch notes [S], and automation structure from fan tool READMEs [CODE]. Raw files saved under /tmp/claude-0/-home-user-claudecode-playground/2e77cd6e-e441-551f-a27e-40f493265545/scratchpad/src5/increlution/.
- No official wiki or game source found; developer unconfirmed. Still [EST]: XP curves, prestige-gain formula, layer count, speed-polynomial exponent. The fan tool repos contain no game formulas that were read.
