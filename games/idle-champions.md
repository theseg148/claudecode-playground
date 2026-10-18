# Idle Champions of the Forgotten Realms
**Sources:** (URLs, required)
- https://idlechampions.fandom.com/wiki/The_Forbidden_City (adventure page: gem rewards, patron objectives by area)
- https://idlechampions.fandom.com/wiki/The_Witchlight_Carnival (patron objective pattern)
- https://idlechampions.fandom.com/wiki/Seeking_Allies (campaign adventure)
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii
- Note: fandom pages fetched only via search snippets; favor formula pages not retrievable here. Legend: [PUB] seen in sources; [EST] recollection/estimate.
## Core loop
- Assemble a formation of champions (up to 10 slots) on a grid; they auto-fight through areas (levels) of an adventure; you level champions with gold, unlocking abilities at specific levels.
- Areas progress in groups of 5 with a boss/mini-boss every 5th area; adventures are 50-ish areas for short ones up to hundreds in later variants [EST].
- The player is designing formations and synergies (buff placement), not dodging; combat is automatic. (For your game: the "fight" is an engine, the player's actions are upgrades.)
- Adventures end by completing an objective area or by resetting at a chosen area.
## Resource types
- Gold (in-adventure only, resets), Gems (premium; also earned from adventure rewards, e.g. Icon Gems x450 on Forbidden City [PUB]).
- Favor per patron (Mirt, Vajra, Strahd, Zariel, Elminster...) [PUB], used to buy patron upgrades and powers; amount scales with area reached [EST].
- Patron "Influence" and coins (Ruby Coin etc.) from patron objectives [PUB].
- Chests, Tokens, Blacksmith contracts, Modron cores, Trials of Mount Everest tokens [EST].
- Champion feats, loot (gear), and "Specializations" choices at certain levels.
## Cost & production growth formulas (public or estimated; mark which)
- Enemy health per area: exponential; common community figure ~x1.2-1.3 per few areas, boss multiplier x10-ish [EST].
- Champion level cost: geometric, `base * 1.07^level`-style with discounts for gold find [EST].
- Favor earned: grows ~ exponentially in highest area reached (power ~ area^k) [EST]; patron objective rewards are fixed per area threshold [PUB].
- Patron objectives per adventure at specific areas, e.g., Mirt at area 325 in Forbidden City [PUB]; harder variants raise area thresholds and reward amounts [PUB].
- Damage multiplier stacking: many sources multiply; synergy between slots multiplies [EST].
## Prestige structure
- Per-adventure reset: you "Reset" an adventure at an area; gold and champion levels reset; Favor and champion gear persist [PUB-ish].
- Patron Favor is the real prestige currency: reaching deeper areas earns more Favor, which buys permanent patron boosts.
- Resetting an adventure converts the run into Divine Favor for that campaign; unspent Favor passively raises gold find, and Favor spent on a Blessing stops counting toward it [S https://earlyguides.com/idle-champions-of-the-forgotten-realms]. Extra familiars unlock bench slots which, paired with the Modron Core, auto-load a saved formation at the start of each adventure [S Steam forum https://steamcommunity.com/app/627690/discussions/0/2148721524004872020]. The Split the Party adventure unlocks multi-party and modron cores and is a separate campaign with no Favor [S https://idlechampions.fandom.com/wiki/Split_The_Party]. Exact reset timing and core automation rules not found [EST].
- Variants: constrained versions of the same adventure (restrictions, e.g., only X champions) that re-skin the same levels with new rules and extra rewards [PUB].
- Seasonal/Event adventures give limited-time champions.
## Unlock pacing
- Campaign adventures unlock sequentially (Tomb of Annihilation, Mad Mage, Descent into Avernus, Icewind Dale, Witchlight...), each with new champions and gimmick.
- Within an adventure, objectives (kill X, reach area Y) give rewards; epic/variant versions unlock after beating base [PUB].
- Champion unlock via chests, events, or gems.
- Time to first patron: hours; to Modron automation: weeks of play [EST].
## Offline progress
- CONFLICT: App Store text says champions keep fighting until defeated even when the game is closed [S https://apps.apple.com/app/id1339874088], contradicting the earlier guess of no offline progress. Cap and rate not found; earlier claim withdrawn [EST]. Offline chest/Blacksmith timers [EST].
- Modron core and Briv-style skip-ahead champions let you automate while the client is open.
## Monetization effects
- Free with IAP; the premium currency in store listings is Platinum, spent on Champions, Familiars, potions and skins; bundles such as 8,000 Platinum plus 1,333 bonus; Teen rating for random items [S https://store.epicgames.com/web-shop/idle-champions-of-the-forgotten-realms-8000-platinum-f8c89b]. Chests with champions/gear, events, sales [EST].
- Pay-to-power via champion unlocks and gear; free route slow but possible [EST].
## What players love
- Formation puzzle and synergy discovery; each new champion changes optimal builds.
- Each campaign introduces new tuning and visuals, keeping the same loop fresh [PUB pattern].
- Variants with restrictions extend value of old content.
## What players hate
- Complexity creep, power-creep of champions, FOMO events [EST].
- Must keep client running; heavy RAM [EST].
- Patron/loot systems opaque to new players.
## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Each Rider world is an "adventure" with a fixed length and a few objective thresholds (patron-style) that pay out rewards at given depths; the thresholds provide goals between resets.
- Variants: replay the same world with a restriction (e.g., "only Form X cards") for extra reward; re-use art/content.
- Per-world "patron" favor: each Rider offers favor which buys permanent boosts specific to that Rider's cards.
- Formation/slot synergies = card deck synergies (no fighting needed): "Attack Ride" slots with adjacency bonuses.
- Automate resets once the player proves mastery (Modron analog = "Decade Driver auto").
- Introduce one new gimmick per world; do not just increase numbers.

## Verification log (refreshed 2026-10-18)
- Refreshed 2026-10-18: 2 more WebSearch queries. Added Divine Favor/Modron/Split the Party facts, fixed premium currency (Platinum) and the offline conflict [S]. Wiki formula pages still not retrievable; no code (commercial).
- Still [EST]: enemy HP scaling, level cost ratio, Favor formula, area counts per adventure, chest rules, Modron automation timing. Forum bug reports about automation after reset are anecdotal.
