# Melvor Idle
**Sources:** (WebFetch was blocked by DNS in this session; figures are recalled from the wiki, so verify. The XP table is well known and likely accurate.)
- https://wiki.melvoridle.com/w/Melvor_Idle_Wiki (the official wiki)
- https://wiki.melvoridle.com/w/Experience
- https://wiki.melvoridle.com/w/Mastery
- https://wiki.melvoridle.com/w/Offline_Progress
- https://melvoridle.com/ (the game)
- https://store.steampowered.com/app/1267910/Melvor_Idle/ (verify app id)

## Core loop
- Pick one skill action at a time (woodcutting, fishing, mining, smithing, etc.); it runs on a timer and gives XP, items and mastery.
- Combat is automatic: pick equipment, select an enemy and the combat style, and the game fights for you.
- Convert gathered items into gear and consumables; sell for GP; unlock new areas, dungeons and slayer tasks.
- Mastery (per item) and Mastery Pool give permanent bonuses.
- Expansions (Throne of the Herald, Atlas of Discovery, Into the Mist) add new skills and worlds.

## Resource types
- GP (gold), Slayer Coins, Raw materials, Processed items, Food, Potions, Runes, Equipment, Mastery XP and Mastery Pool XP, Prayer Points, Summoning marks, Shards of the event, and Township resources in the first expansion.
- Combat yields drops (bones, loot), and dungeon-specific items.

## Cost & production growth formulas
- XP to level `L` (public, wiki): `XP(L) = floor( 1/4 * sum_{n=1}^{L-1} floor( n + 300 * 2^(n/7) ) )`. [public; this is the RuneScape curve]
- Level 99 requires 13,034,431 XP, and level 120 (virtual) about 104 million. [public]
- Doubling pattern: XP between levels doubles about every 7 levels, so late levels dominate play time. [follows from the formula]
- Action speed: each action has a fixed interval (e.g. 3s for a basic woodcutting action) reduced by upgrades and the Mastery bonuses. [public]
- Mastery: item mastery level costs scale with the skill's item count; at mastery 99 an item gets bonus (e.g. 5% more XP?). Pool checkpoints (10, 25, 50, 95%) give skill-wide boosts. [public structure; exact numbers are estimate]
- Combat: damage is based on stats, with accuracy and max hit formulas inherited from RuneScape. [public concept]
- Equipment cost grows roughly geometrically across tiers (bronze -> rune -> dragon); 5 to 10x per tier. [estimate]
- Shop upgrades (e.g. axes, bank slots) use escalating prices where each tier costs several times the last. [estimate]

## Prestige structure
- Melvor has no prestige in the base game; the progression is "levels, mastery and gear".
- Adjacent resets: Mastery Pools and the Township (in Throne of the Herald) are persistent; there is an optional "Hardcore" and an "Adventure" mode with restrictions.
- A new-game-plus style "Ancient Relics" system adds persistent rewards after exploring the Atlas. [estimate]

## Unlock pacing
- Early skills available immediately; Combat from the start.
- Skill levels: unlock items every few levels, and gear tiers around 1, 20, 40, 60, 80, 99. 
- Dungeons and Slayer unlock mid-game (about combat level 50+). 
- Hitting 99 in a skill takes tens of hours; completing all skills takes hundreds of hours. [estimate]
- Expansion content adds a second arc after the main game.

## Offline progress
- Offline progress is a core feature: the game simulates up to 18 hours of offline skilling and combat (the cap, public), with some actions and combat results at reduced efficiency. [public/recall]
- Players log in to a summary of what happened offline.

## Monetization effects
- One-time purchase on Steam and mobile; expansions are paid DLC; there are no ads in the paid versions. 
- Browser version is a free demo with ads (older). [estimate]
- There is no premium currency, so progress is time-based only.

## What players love
- Familiar RuneScape-like feeling with a true idle experience.
- Offline progress that respects time away.
- Great variety (skills, mastery, combat) and a one-time price.

## What players hate
- Long grind to 99 and mastery completion.
- Combat is only automatic; less depth for some players.
- Expansions can feel like a paywall to the best content.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- An XP curve that doubles about every 7 levels gives smooth long-term pacing without a prestige reset.
- Offer a strong offline cap (e.g. 12 to 18 hours) with a summary screen; players value it.
- Use mastery-style per-item progression to give a permanent upgrade feel.
- A one-time purchase and no ads is a viable model for an idle game with a loyal audience.
- If prestige is skipped, deliver long-term goals using breadth (new worlds and skills).
