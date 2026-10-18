# Soda Dungeon (AN Productions / Armor Games)
**Sources:**
- https://www.giantbomb.com/games/3030-51231/ and https://giantbomb.com/wiki/Games/Soda_Dungeon [S]
- https://www.tvtropes.org/pmwiki/pmwiki.php/VideoGame/SodaDungeon [S] (listed, not opened)
- No source repo (Flash/Unity). No code read.
- Tags: [S] snippet, [CODE] source (none), [M] memory, [E] estimate.

## Core loop
- Upgrade a tavern, buy sodas, attract new adventurers, and send them raiding a dungeon for loot. [S]
- Free-to-play dungeon crawler RPG. [S]
- Adventurers run dungeon floors automatically; the player chooses party and upgrades between runs. [M]
- Combat exists (auto-battle), so this game is not no-fight; the interesting part is the town loop. [M]

## Resource types
- Gold, sodas (reputation items), loot/equipment. [S]/[M]
- Reputation: ten sodas from Peasant Pop (+1) to Drink Zero (+90). Different sodas attract different adventurer classes. [S]
- Premium currency (gems) and tickets/keys. [M]

## Cost & production growth formulas (public or estimated; mark which)
- Soda reputation values range +1 to +90 across ten tiers. [S]
- Class unlocks: patron = tavern reputation + a specific soda, e.g. Fighter needs 250 Reputation and Grappling Grape, Conjurer 400 and Cherry Charm; Gnomes upgrade gives +5% Essence per Gnomes level up to level 6 [S https://sodadungeon.fandom.com/wiki/Tavern_upgrades]. Stools and tables raise reputation [S]. Other costs not found. [E]
- Likely escalating gold costs per tavern upgrade and per class unlock. [E]

## Prestige structure
- Original game has dimension resets: tavern upgrades are PERMANENT and survive entering a new dimension [S https://sodadungeon.fandom.com/wiki/Tavern_upgrades]; resetting is described as trading the game state for rare powerful items [S giantbomb]. A 2017 Steam thread argues there is no true outer-loop prestige and resets run out at the Warrior's Dimension [S https://steamcommunity.com/app/564710/discussions/0/133261907136068020].
- Soda Dungeon 2 FAQ: each new dimension grants a relic of your choice (first five portals give a bonus relic) but you lose gold, dungeon progress, most equipment and most materials; a Blacksmith upgrade keeps some materials; final dimension is D11 Warrior's Dimension [S https://www.magicgameworld.com/?p=124638].
- Sequel Soda Dungeon 2 released on the same three platforms. [S]
- Town buildings (blacksmith, etc.) persist across runs. [M]

## Unlock pacing
- Tavern reputation threshold unlocks new classes and new dungeon areas. [S]/[M]
- Dungeons progress in themed zones with bosses. [M]
- New soda each rep step gives a short-term goal. [S]

## Offline progress
- Soda Dungeon 2 store text: players earn Battle Credits while away and redeem them later for loot [S https://apps.apple.com/app/id1454882086]. Original game offline behaviour not found [M] low confidence.

## Monetization effects
- Soda Dungeon 2: free with IAP; store says no timers, lives or paywall and everything buyable with in-game currency; mobile shows ads removable via in-game currency or a $8.49 Starter Bundle (2020 early-access review) [S https://apps.apple.com/app/id1454882086, https://mobilesyrup.com/?p=760570]. Original game monetization not verified [M]. Gem-as-premium-currency not confirmed (FAQ mentions gems only as equipment gem slots).

## What players love
- Humor and charm; many character classes. [M]
- Soda tier list as a visible reputation ladder. [S]

## What players hate
- Ads and mobile friction. [M]
- Grindy later floors. [M]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. A single "reputation ladder" of ten consumables with named steps gives a clear mid-game spine; use named Rider Cards as the rungs. [S]
2. Different rungs attract different characters; unlock allies per world rather than per level. [S]
3. A hub (tavern/town) that persists across runs is the safe place for upgrades; Decade's Photo Studio can be that hub. [M]
4. This game's progression is dungeon floors with combat; to avoid fights, replace floors with world-gate quests. [E]
5. Tie rewarded ads (if any) to an optional boost, never to the gate. [M]
6. Keep the humor in the item names; it carried this game. [M]

## Verification log (refreshed 2026-10-18)
- Refreshed 2026-10-18: 3 more WebSearch queries. Wiki tavern/patron numbers and SD2 FAQ reset rules are [S] snippets; no source repo. 
- Mixed evidence: dimension-reset details for the ORIGINAL come from forum/wiki snippets, the relic/D11 details from the SD2 FAQ; do not treat SD2 as equal to the original. Premium currency, ad boosts and original offline remain [M]/unknown.

### Previous log (superseded, kept for history)
- Search gave only the soda/rep detail and basic genre facts. Prestige, offline, and monetization lines are from memory and flagged low confidence.
- Search for the town wiki returned unrelated Elder Scrolls Blades pages; ignore them.
- Confidence ranking: prestige/offline/monetization lines are memory, flagged low confidence above.
