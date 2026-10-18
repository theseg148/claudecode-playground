# Mr. Mine
**Sources:** (URLs, required)
VERIFICATION UPDATE 2026-10-18: developer (Playsaurus), platforms, Steam id, and the depth/milestone structure are now confirmed; all numeric formulas remain unverified. See Verification log.
CONFIDENCE WARNING (LOW): the sandbox could only fetch raw.githubusercontent.com; no store, wiki or forum page about Mr. Mine could be fetched. Everything is [MEM-LOW] or [EST]. Verify before using.
- https://store.steampowered.com/app/1397920/MrMine/ (Steam, free to play; text via search snippets) [S]
- https://apps.apple.com/app/mr-mine/id1257552996 (App Store; unverified)
- https://mrmine.fandom.com/wiki/File:3.png (front page of the Mr. Mine wiki; section list seen in snippet) [S]
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii (genre math reference; surfaced by search, not fetched)

## Core loop
- Vertical-mine idle by Playsaurus (also made Clicker Heroes) [S: https://blog.mrmine.com/ search snippets, https://mrmine.fandom.com/wiki/File:3.png]. (Earlier 'Playgems' was WRONG.) Mr. Mine digs deeper automatically; depth in meters is the central number.
- Tap to dig, hire workers (miners, lamps, drills...), collect resources (Coal, Copper, Iron... gems) and sell them for cash. Spend cash on upgrades to dig and carry faster.
- Beyond a depth, special layers appear (Lava, Cave Monsters? [MEM-LOW]) and new resources/items drop. A "Dwarf" crafting and "Dig Dungeon"/events layer in later updates. [MEM-LOW]
- Prestige: "Reinforcement/Prestige" resets depth and cash for permanent boosts. [MEM-LOW]

## Resource types
- Cash/Coins, ores (Coal, Copper, Iron, Silver, Gold, Diamond... ), Gems/Rubies (premium), Artifacts, Prestige currency, Mission tokens. [MEM-LOW]
- Depth (m) acts as a progress resource driving unlocks of ore types. [MEM]
- Miners/boosters have energy or are limited by time. [EST]

## Cost & production growth formulas (public or estimated; mark which)
- No verified formulas. Estimated shape:
  - Depth unlocks are roughly geometric: each new ore tier appears at ~2-3x the previous depth. [EST]
  - Upgrade costs: base * 1.1-1.2^level; production per level linear +x%. [EST]
  - Sell price of ore grows ~3-5x per tier; mining speed upgrades are +10-25% steps. [EST]
- For comparison, the Game Developer series notes miner/worker economy usually uses cost multiplier c in 1.07-1.15, production linear in count (https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii). [genre reference, not fetched]
- Prestige formula guess: points = floor(sqrt(lifetime cash / 1e9))? [EST, not from the game]

## Prestige structure
- One main reset giving a permanent multiplier ("Mr. Mine's something"); some versions have an additional "Rebirth/Era" step. [MEM-LOW]
- Reset keeps premium currency and some unlocked skills. [EST]
- First reset roughly after 1-3 days casual play; later resets faster. [EST]

## Unlock pacing
- [EST] Minutes 0-10: tap digging, first workers; 1 h: first new ore tier; 1 day: first big-depth layer and missions; 1 week: prestige loops and events.
- Content drip tied to meters (depth) is the pacing: every 100-500 m a fresh resource or character appears. [EST]

## Offline progress
- [MEM-LOW] Mr. Mine pays offline earnings when you return; the player can double it by watching an ad. Offline cap and rate unknown (typical for the genre: 2-12 hours at 50-100%). [EST]

## Monetization effects
- Free to play with rewarded video ads (double offline income, boosts) and IAP gem packs. [MEM-LOW]
- Premium gem currency speeds upgrades and unlocks special dwarves. [EST]
- Ad-doubling of offline income is the central retention hook of the genre. [genre knowledge]

## What players love
- Visual, satisfying: you can *see* the digging and the depth meter ticking.
- Simple core, charming art, regular events.
- Progress even when closed.

## What players hate
- Ad pressure and gem paywalls late. [EST]
- Grindy mid-game and slow second prestige. [EST]
- Limited depth of strategy; just buy the next upgrade. [EST]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Use one big visible progress number (depth in Mr. Mine; "dimension distance" for Decade) that gates unlocks. It makes pacing readable for players and designers.
2. Show the economy visually: a Dimension Door corridor lengthening is the analogue of the mine shaft.
3. Drip new resource types every 100-500 units of the progress meter, each with ~3-5x higher value.
4. Rewarded-ad-doubled offline income is effective; implement as an optional, never mandatory bonus. If ads are not wanted, use a free daily "double" token.
5. Add an event layer (limited-time world) to keep returning players engaged without new core content.
6. Keep premium currency off the critical path to avoid the mid-game gem-wall complaint.
7. Second-prestige pace: aim for roughly one-third the time of the first.
8. This file is low-confidence; verify numbers before using.

## Verification log (2026-10-18)
Method: WebSearch snippets only (wiki/Steam pages not fetchable).
Confirmed [S]:
- Developer Playsaurus; Steam (free), browser and phones; originally 2012, remastered for Steam. https://store.steampowered.com/app/1397920/MrMine/ , https://blog.mrmine.com/?p=74
- Steam text: manage a team of miners and upgrade a drill; 100+ drill upgrades; hire scientists to find rare relics; chests with hidden upgrades; unique buildings; quests and achievements; secret encounters; features unlock the deeper you go.
- Wiki sections: Materials, Milestones, Super Miners, Scientists, Caves, Forge, Monsters/Weapons, Reactor/Buff Lab, Chests, Quests, Upgrades, Blueprints. https://mrmine.fandom.com/wiki/File:3.png
- Milestone depths (unofficial blog.mrmine.com, treat as medium confidence): trading post 15 km, cave building 45 km, Chest Compressor 700 km, Reactor ~1133-1134 km (World 2 101-102 km), Buff Lab 1,135 km, Robot MK2 1257 km (drill parts 24-26). https://blog.mrmine.com/?p=40 , ?p=109
- Worlds: Earth -> Moon -> ... Titan; Einsteinium and Fermium come from the Reactor, not mining (blog snippet).
- Super miners boost drill speed, auto-sell ores and speed all miners in a mineshaft (snippet).
Contradicted: 'Playgems', 'Dwarf crafting', 'Dig Dungeon', ore list (Coal/Copper/Iron...) and 'energy/time-limited miners' are not confirmed; wiki indicates Forge, Caves, Monsters, Reactor instead.
Unverified: whether a prestige reset exists (no snippet mentioned it; worlds/'timelapses' may serve that role), all costs, growth multipliers and offline values; the 2-3x depth geometric claim is [EST].
