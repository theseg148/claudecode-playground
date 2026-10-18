# Swamp Attack
**Sources:** (URLs, required)
- https://swamp-attack.fileplanet.com/apk (store-style description: 70+ missions in four chapters)
- https://en.wikipedia.org/wiki/Incremental_game (general genre context)
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii
- Honest note: Swamp Attack (Chillingo) is a tower-defence/shooter with stage progression, NOT a true idle game and has no confirmed prestige. Search found no wiki data. Everything beyond the 70+ missions / four chapters claim is [EST] (recollection) and low confidence.
## Core loop
- Player defends a swamp shack from waves of zombie-like critters; fire weapons with taps (active), use grenades/airstrikes/turrets.
- Missions come in sequence across four chapters (~70+ missions total) [PUB-ish].
- Earn cash and stars/XP per mission; spend on weapons, upgrades, characters (e.g. Duke vs Bubba?), and gadgets [EST].
- Retry missions for more cash; difficulty rises smoothly with new enemy types.
## Resource types
- Cash (soft), Gems/Gold (premium), Stars (ratings) [EST], Ammo consumables / items [EST].
- Weapon upgrade tiers and unlocks.
- Chapters' map of missions with 1-3 star rating [EST].
## Cost & production growth formulas (public or estimated; mark which)
- No published formulas. [EST] Weapon upgrade cost curve ~1.3-1.6x per tier (typical mobile shooter), each upgrade +10-20% damage.
- Enemy HP per mission: linear-to-quadratic rise inside a chapter with a reset at new chapter boss [EST].
- Rewards per mission scale about linear with mission index [EST].
- Using genre math (gamedeveloper link): with geometric costs of rate r and linear production, time-to-next-upgrade grows; devs relieve with grind missions.
## Prestige structure
- None found. The sequential structure is the only "reset": completing a chapter moves to a new environment and enemy roster [EST].
- Replaying missions is optional grinding, no multiplier carryover.
- Comparison role in this research: shows how a non-idle stage game keeps content fresh without prestige.
## Unlock pacing
- Weapons and enemies unlock by mission index; new enemy type roughly every 3-5 missions [EST].
- Chapter transitions swap setting palette and introduce a boss [EST].
- Optional challenge ("star") conditions increase replayability.
- Paywalled speed: buying items "passes levels faster" [PUB via description].
## Offline progress
- None known; session-based play [EST].
- Energy timers on some modes [EST].
## Monetization effects
- Premium currency buys weapons/upgrades and passes levels faster [PUB-ish].
- Ads for double rewards [EST].
- Pay-to-win pressure grows in later chapters [EST].
## What players love
- Satisfying weapon variety and clear escalation.
- Short missions suit mobile.
## What players hate
- Grind walls and monetization push [EST].
- Repetition within chapters [EST].
## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- A chapter system (4 groups of ~15-20 steps) makes the world feel sequential: group content into themed chapters with a boss-like capstone (here, a non-combat "final build" milestone).
- New enemy every 3-5 missions maps to "new mechanic/card type every few steps".
- Don't copy the grind-wall-to-sell-currency pattern.
- Without prestige, freshness comes from varied content; idle needs stronger reuse via carryover.
- This is the weakest reference; weight other files more.
