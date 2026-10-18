# (the) Gnorp Apologue
**Sources:**
- https://steamcommunity.com/app/1473350/discussions/0/4038104133466644335/ (player discussion on prestige bar) [S]
- https://steamcommunity.com/app/1473350/discussions/0/4039230885224209873 [S]
- https://vaporlens.app/app/1473350/the_gnorp_apologue (review summary) [S]
- https://destructoid.com/?p=441359 (Compression event article) [S]
- No source repository exists (commercial Steam game); no code read.
- Tags: [S] snippet, [CODE] source (none), [M] memory, [E] estimate.

## Core loop
- A rock sheds shards; Gnorps collect them as currency; you build machines and routes to move shards, and eventually trade the run for talent points. [S]
- A run ends when the player chooses to trade progress for "talent points" used for strategic upgrades. [S]
- Visual/physical idle: you watch and place things in a small world rather than click numbers. [M]
- Talents can be re-spent each run, so builds are chosen per run. [S]

## Resource types
- Shards (base currency from the rock). [S]
- Talent points (prestige currency). [S]
- Zybellium (upgrade material that resets on prestige). [S]
- Gnorps themselves are a purchasable resource; one player advises that over 25 runners are unnecessary. [S]
- Compression bar: fills when a shard pile is built faster than it is collected. [S]

## Cost & production growth formulas (public or estimated; mark which)
- No public formulas found. [E]
- Compression Events have ten tiers; later tiers need you to be further along via prestige. [S]
- Player reports that prestiging does not lower the next requirement; talents just make hitting it likelier. [S] (disputed by other posts)
- Typical idle scaling (exponential costs, additive/multiplicative boosts) is assumed. [E]

## Prestige structure
- Prestige bar: white = new progress, grey = banked progress from earlier runs; you can prestige without filling the bar if you add something to the white part. [S] (players disagree on details)
- Each prestige grants talent points; spending them unlocks build-defining talents (missiles, rockets, ice-fire are the cited viable builds). [S]
- Zybellium upgrades and Compression tiers reset on prestige. [S]
- Reviews say progress can stall after about two prestiges. [S]

## Unlock pacing
- Early game introduces Gnorps and shard routes; later systems (Compression, talents) are gated by prestige count. [S]/[M]
- Compression tiers unlock more as you progress through prestiges. [S]
- No world/zone sequence known. [E] An "Epilogue" update added a new mode with extra mechanics and a new ending; dev design rules for talents: not openly synergistic, open new exploration, carry a workable downside [S https://steamdb.info/patchnotes/13036305 via search snippet]. Achievements exist for first Compression event, first prestige, prestiging with 10 talent points, 3 unspent Zybellium [S https://steamcommunity.com/id/emuapple/stats/1473350/achievements].

## Offline progress
- No offline-gain description found. [E] Verified save behaviour: the "Saving Update" added cloud saving, a quit button and a default-on "Save on quit"; saves got much smaller but projectiles and shards are no longer fully stored, and a "Recover save" button grants talent points based on Steam achievements [S https://steamdb.info/patchnotes/13914174].

## Monetization effects
- Paid Steam game; no microtransactions known. [M]

## What players love
- Novel physical, tactile idle mechanics and strategic builds. [S]/[M]
- Reassignable talents each run. [S]

## What players hate
- Only a few builds are viable; wrong investments can brick a run. [S]
- Confusing prestige bar semantics (three conflicting player explanations). [S]
- Stalling after two prestiges. [S]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Do not hide how banked progress works; Gnorp's bar caused three conflicting explanations. Show "banked / new / needed" with numbers. [S]
2. Respec-free talents per run give replayable builds; for Decade, a loadout of Rider Cards per world run. [S]
3. A secondary meter (Compression) that rewards a specific play pattern, not only time, adds variety; keep the unlock tied to prestige count. [S]
4. Avoid build bricking: if a choice can lock a run into a dead end, warn or allow undo. [S]
5. Keep the world physical and visible; for zone progression, each Rider world could be a small scene that changes as the economy grows rather than a menu entry. [E]
6. One-line unlock rule ("prestige N times to open Compression tier N") beats hidden gating. [S]

## Verification log (refreshed 2026-10-18)
- Refreshed 2026-10-18 with 3 more WebSearch queries (wiki, offline, patch notes). No wiki or formulas exist in indexed results; no source repo (commercial). Added only save/Epilogue/achievement facts from SteamDB patch notes and Steam achievement lists [S].
- Still unknown: prestige formula, Compression numbers, offline behaviour. Previous caveats stand; ten tiers and 25 runners remain snippet-only.

### Previous log (superseded, kept for history)
- Only WebSearch snippets (summaries of Steam forum threads, a review aggregator, and a Destructoid article) were used. I did not open the pages. All numbers (ten tiers, 25 runners) come from the snippets.
- No official docs; no source. Everything else is [M] or [E] and should be re-checked in-game before design decisions.
