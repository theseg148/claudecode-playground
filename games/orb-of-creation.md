# Orb of Creation (MarpleGames)
**Sources:**
- https://store.steampowered.com/app/1910680/ (store page, via search snippet) [S]
- https://steamcommunity.com/app/1910680/discussions/0/3274688023488676144 [S]
- https://www.dlcompare.fr/actualites-gaming/orb-of-creation-le-jeu-incrementiel-sans-temps-d-attente-79667 [S]
- https://vaporlens.app/app/1910680/orb_of_creation.md [S]
- No repo; commercial game. No code read.
- Tags: [S] snippet, [CODE] source (none), [M] memory, [E] estimate.

## Core loop
- Described on Steam as a "non-idle incremental-puzzle game" where you recreate the world with magic and ingenuity. [S]
- Spell-casting system where how you set up and cast spells greatly affects the result. [S]
- Sandbox of magic, artifacts and alchemy that synergize. [S]
- A player says it is "not really an idle game, more an incremental". [S]
- A French article calls it a "clicker without waiting" ("sans attente"). [S]

## Resource types
- Mana and spell-related resources, alchemy materials, artifacts. [S]/[M]
- Exact currency list not verified. [E]

## Cost & production growth formulas (public or estimated; mark which)
- No public formulas found. [E]
- Likely polynomial/exponential spell upgrade costs as in other incrementals. [E]
- Synergy between layers (each layer intertwines with the last) implies multiplicative interactions. [S]

## Prestige structure
- Search found nothing about prestige or realm mechanics specifically. [S]
- "Constantly expanding gameplay, every new layer intertwines with the last" suggests layer-style progression. [S] (store text) and [E]
- A dlcompare article (search snippet) says the full 1.0 released 23 June 2026 and adds an advanced replay feature called Prestige [S https://www.dlcompare.com/gaming-news/orb-of-creation-redefining-non-idle-incremental-games]; snippet cut off before explaining it, and the Steam/itch pages seen still say "in development", so 1.0 status and prestige rules are UNCONFIRMED.

## Unlock pacing
- Expanding layers over time; new mechanics introduced progressively. [S]
- No numbers known. [E]
- A beta branch exists whose saves are not compatible with the main branch. [S] Dev MarpleGames posted a v0.6.0 beta branch (Aug 2023) needing a fresh save; Steam release followed v0.5.4 on itch [S https://marple.itch.io/orb-of-creation]. Itch prototype had no save/load or offline idling and ended at "Unlock: The World" [S https://marple.itch.io/orb-of-creation-prototype]. Dev 0.4.0 content ended at two upgrades costing 1 billion of a scarce resource [S https://marple.itch.io/orb-of-creation/devlog/294294/orb-of-creation-dev-040].

## Offline progress
- Marketing says no waiting [S]. Prototype explicitly had no offline idling [S]; a Steam commenter says one must pause/unpause constantly to progress [S https://steamcommunity.com/app/1910680/discussions/0/3805031898647217128]. Current offline behaviour not found [E].

## Monetization effects
- Paid on Steam; no known microtransactions. [M]

## What players love
- Intricate interlocking mechanics; "many different mechanics all affecting each other". [S]
- Active play instead of waiting. [S]

## What players hate
- Not enough evidence in snippets. Players asking whether it is idle suggest expectation mismatch. [S]
- Beta save incompatibility. [S]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Spells whose setup matters turn "upgrade" into "arrange"; a Decade Card deck/order puzzle can add depth without combat. [S]
2. Layers that intertwine with earlier ones keep old content alive; a new Rider world should reuse an earlier world's resource. [S]
3. Be clear in the store text whether the game is idle or active; reviews show mismatch. [S]
4. A "no waiting" promise means progress must come from decisions; if your game is idle, state that. [S]
5. Zone progression here is layers of systems, not locations; a world could be a system layer with a name and a Rider. [E]
6. Keep beta saves compatible or warn loudly. [S]

## Verification log (refreshed 2026-10-18)
- Refreshed 2026-10-18: 3 more WebSearch queries (wiki, patch notes, 1.0). No wiki or patch-note text retrievable; no repo (commercial). New [S]: dev name, beta v0.6.0, prototype limits, 1.0/Prestige claim from one article.
- Conflict: dlcompare says 1.0 shipped 23 June 2026; Steam/itch snippets still say in development. Prestige rules, currencies and formulas remain unknown. Still lowest-confidence file.

### Previous log (superseded, kept for history)
- Only search snippets; none of the cited pages were opened. Everything about prestige, realms or currencies is explicitly unknown and not invented.
- Lowest-confidence file of the batch; worth a second pass with a page-opening tool.
- Confidence ranking: Orb of Creation is lowest of this batch; all claims rest on store and forum snippets.
