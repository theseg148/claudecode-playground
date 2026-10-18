# Melvor Idle
> Verification pass 2026-10-18 (WebSearch snippets only; pages not opened). [S] = confirmed in a search snippet with the URL given; [unverified] = not confirmed, treat as a design placeholder. See "Verification log" at the bottom.
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
- XP gap between level L-1 and L is roughly floor(1/4 * (L-1 + 300 * 2^((L-1)/7))), cumulative XP is the floored sum; experience doubles about every 7 levels [S https://wiki.melvoridle.com/w/Experience_Table]. (RuneScape-style curve.)
- Level 99 requires 13,034,431 XP and level 120 requires 104,273,167 XP [S https://wiki.melvoridle.com/w/Experience_Table]. Level 120 is the cap per skill with the Throne of the Herald expansion; virtual levels past that are display only.
- Doubling pattern: XP between levels doubles about every 7 levels, so late levels dominate play time. [follows from the formula]
- Action speed: each action has a fixed interval (e.g. 3s for a basic woodcutting action) reduced by upgrades and the Mastery bonuses. [public]
- Mastery: each Mastery Pool has four checkpoints at 10%, 25%, 50% and 95% of the pool, which give passive skill-wide bonuses only while the pool holds that share [S https://wiki.melvoridle.com/w/V0.17]. Example 95% bonuses (Melvor realm): Thieving, Cooking +10% food healing, Firemaking +5% Mastery XP in all skills, Smithing/Herblore +10% double chance. Thieving's 95% checkpoint needs 16,150,000 of a 17,000,000 pool [S https://wiki.melvoridle.com/w/Thieving]. Per-item mastery 99 bonuses are skill-specific and the generic '5% more XP' guess is [unverified].
- Combat: damage is based on stats, with accuracy and max hit formulas inherited from RuneScape. [public concept]
- Equipment cost grows roughly geometrically across tiers, 5 to 10x per tier. [unverified]
- Shop upgrades use escalating prices, each tier several times the last. [unverified]

## Prestige structure
- Melvor has no prestige in the base game; the progression is "levels, mastery and gear".
- Adjacent resets: Mastery Pools and the Township (in Throne of the Herald) are persistent; there is an optional "Hardcore" and an "Adventure" mode with restrictions.
- A new-game-plus style 'Ancient Relics' system adds persistent rewards after exploring the Atlas. [unverified]

## Unlock pacing
- Early skills available immediately; Combat from the start.
- Skill levels: unlock items every few levels, and gear tiers around 1, 20, 40, 60, 80, 99. 
- Dungeons and Slayer unlock mid-game (about combat level 50+). 
- Hitting 99 in a skill takes tens of hours; completing all skills takes hundreds of hours. [unverified]
- Expansion content adds a second arc after the main game.

## Offline progress
- Offline progress is a core feature: the cap is currently 24 hours [S https://wiki.melvoridle.com/w/Offline_Progression]; it was 12 hours in V0.13 and raised to 18 hours in the v1.0 beta [S https://wiki.melvoridle.com/w/Full_Changelog]. The 'Unlimited Offline' mod lifts it. Township updates passively every 1 hour up to 24 hours offline. The earlier '18 hours' was out of date.
- Players log in to a summary of what happened offline.

## Monetization effects
- One-time purchase on Steam and mobile; expansions are paid DLC; there are no ads in the paid versions. 
- Browser version is a free demo with ads (older). [unverified]
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

## Verification log

Confirmed [S]:
- XP formula, level 99 = 13,034,431, level 120 = 104,273,167 (the RuneScape table, confirmed on the Melvor wiki); mastery pool checkpoints 10/25/50/95%; sample 95% bonuses and Thieving pool size; offline cap 24 h now (12 h at V0.13, 18 h at the v1.0 beta).
Unconfirmed [unverified]:
- Equipment/shop price growth, Ancient Relics details, time-to-99 estimates, free-demo/ads details, combat formula specifics (not searched), per-item mastery generic bonus.
Note: the XP Table page was last updated ~783 days before the search; check for later changes.
