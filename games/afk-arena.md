# AFK Arena
**Sources:** (URLs, required)
- https://afk.guide/level-caps/ (hero level caps by tier; Resonating Crystal)
- https://gamerempire.net/afk-arena-guide-tips-tricks-strategy/ (12-hour idle chest, daily 120-minute fast reward)
- https://afk-arena.fandom.com/ (community wiki, not fetched; DNS failed)
- https://www.sportskeeda.com/esports/afk-journey-beginners-guide-best-tips-start-strong (sequel AFK Journey: 12h -> 24h idle cap by stage)
- Legend: [PUB] in sources; [EST] my recollection/estimate.
## Core loop
- Auto-battler: build a 5-hero team from factions; battles are fully automatic; the player picks team, upgrades, skills and artifacts.
- Campaign: chapters of stages (Chapter 1 ... 40+); beating a stage raises your AFK income rate and unlocks next stage [PUB-ish].
- Each stage yields gold, hero XP and items continuously while you are away ("AFK rewards"); you collect a chest [PUB].
- Spend resources to level heroes (limited by level caps), ascend tiers, equip gear, and push the campaign again.
- Other modes (Kings Tower, Arena, Guild Hunts, Labyrinth) are side lanes of progress that feed currencies.
## Resource types
- Gold, Hero Essence, Dust (for ascending), Diamonds (premium), Scrolls (summon), Stargazer cards, Faction emblems [EST].
- AFK rewards: gold/XP/items per minute (rate depends on campaign stage) [PUB].
- Hero level cap tiers: Elite 100, Elite+ 120, Legendary 140, Legendary+ 160, Mythic 180, Mythic+ 200, Ascended 240 [PUB afk.guide]. Resonating Crystal raises the shared cap (+5 per extra ascended hero beyond five; max 465) [PUB].
- Stars do not increase level cap [PUB]. 
- Faction Towers and Kings Tower progress counters.
## Cost & production growth formulas (public or estimated; mark which)
- Hero level cost: gold + essence rise steeply after level 100; roughly exponential ~ x1.02-1.05 per level [EST].
- AFK income per minute: stage-indexed lookup table, increasing mostly linear-to-superlinear by chapter [EST].
- Idle chest cap: 12 hours of production [PUB]; AFK Journey extends 12h -> 24h as stages clear [PUB, sibling game].
- Daily quick AFK reward: 120 minutes of resources instantly [PUB].
- Enemy power per stage: approx +3-5% per stage with chapter jumps ~+10-20% [EST]; "wall" stages appear where team power is lower than enemy power.
- Hero power: base stats x level x tier multipliers; Resonating Crystal shares levels of the top five to others [PUB].
## Prestige structure
- No classic prestige reset. Progress is a monotonic campaign plus tiers.
- Soft prestige analogues: Hero ascension (merge duplicates to upgrade tier), hero "Reset" refunds invested resources, season resets in Arena / Kings Tower [EST].
- Season-based "Dream Realm" and Arcane Labyrinth reset periodically [EST].
- Hero levels via Resonating Crystal are the persistent power.
## Unlock pacing
- Campaign gates features by stage: Arena, Guild, Kings Tower, Labyrinth, Artifacts unlock at stage markers [PUB-ish].
- Level caps per tier force you to collect heroes of higher rarity, not just grind gold.
- Story chapters new each major update; new factions (Celestial, Hypogean, Dimensional) arrive over time [EST].
- First week: very fast; after ~30 days: daily loops dominate [EST].
## Offline progress
- Core design: AFK chest accrues up to 12 hours [PUB]; collecting more often is optimal; idle rate = stage-based [PUB].
- Pushing campaign raises idle rate permanently so progress compounds without a reset.
- Daily free quick-AFK (120 min) and purchased quick-AFK extra [PUB].
## Monetization effects
- Diamonds buy summons (hero gacha), VIP levels increase AFK quality/speed [EST].
- Monthly cards, bundles, quick-AFK purchases [EST].
- Gacha pull rates drive pay-to-power; the idle chest is the free baseline.
## What players love
- Low-effort play: set team, collect, upgrade; satisfying campaign progress.
- Hero collection and faction synergy.
- Cute/pretty art, new chapters as fresh content.
## What players hate
- Wall stages that need pay or long waits; gacha RNG.
- Daily chores (many modes) become bloat [EST].
- Level cap tiers feel like gating.
## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Sequential chapters with idle income tied to furthest stage: each new world immediately raises passive income, which gives instant reward and no reset needed.
- Cap hours of offline accumulation (e.g., 12h) to encourage check-ins; extend cap by progress (AFK Journey).
- Level caps by tier: force upgrades from different systems (collect Rider Forms) rather than one currency.
- A single shared cap bonus (Resonating Crystal) is an elegant carryover: past worlds' heroes lift the current cap.
- Avoid gacha; use deterministic unlock (card recipes).
- Provide a "quick collect" daily item (120 min) as friendly pacing.
- Wall stages should be signposted with a "what you need" hint (e.g., required forms).
