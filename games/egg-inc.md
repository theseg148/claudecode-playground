# Egg Inc
**Sources:** (WebFetch was blocked by DNS in this session; numbers are from recall of the community wiki and spreadsheets, so verify.)
- https://egg-inc.fandom.com/wiki/Egg,_Inc._Wiki
- https://egg-inc.fandom.com/wiki/Soul_Eggs
- https://egg-inc.fandom.com/wiki/Prophecy_Eggs
- https://egg-inc.fandom.com/wiki/Contracts
- https://auxbrain.com/ (developer Auxbrain)
- https://wasmegg-carpet.netlify.app/ (community calculators/tools)

## Core loop
- Hatch chickens (spend on hatchery capacity), lay eggs at a rate per chicken, and sell eggs for money.
- Buy research (common and epic), vehicles (to carry eggs to market) and hab upgrades (to hold more chickens).
- Fill the farm, then "Prestige" (send chickens to heaven) to receive Soul Eggs, then restart faster.
- Move to higher-value egg types as farm value grows.
- Contracts add a cooperative layer with deadlines and rewards.

## Resource types
- Cash (earnings).
- Soul Eggs (prestige currency, passive bonus to earnings and to egg value).
- Prophecy Eggs (rare; from contracts, daily gifts, and milestones; they boost soul-egg strength).
- Golden Eggs (contract currency).
- Boost tokens and Tachyon / Quantum stones (modifiers).
- Piggy bank (stores part of earnings and unlocks for a purchase or at a threshold).
- Eggs of Truth (Enlightenment) and Artifacts (later system; crafting and missions).

## Cost & production growth formulas
- Egg value (public, wiki): Edible 0.1 -> Superfood 1.25 -> Medical 15 -> Rocket Fuel 150 -> Super Material 1,000 -> Fusion 10,000 -> Quantum 1e5 -> Immortality 1e6 -> Tachyon 1e7 -> Graviton 1e8 -> Dilithium 1e9 -> Prodigy 1e10 -> Terraform 1e11 -> Antimatter 1e12 -> Dark Matter 1e13 -> AI 1e14 -> Nebula 1e15 -> Universe 1e16 -> Enlightenment 1e17. [estimates from recall; many values are ~10x steps]
- Chicken lay rate base is approximately 1 egg per 1/30 minute, modified by research (+x% each). [estimate]
- Hab capacity: 4 habs, each with 4 upgrade tiers, final capacity per hab increases from 250 to 1M-ish with cost multipliers. [estimate]
- Hatchery capacity: internal hatchery rate research gives chickens per minute while online and offline. [public]
- Research costs follow an exponential schedule: cost = base * growth^level, with common research growth about 1.05 to 1.3 depending on the research. [estimate]
- Soul egg bonus: earnings multiplier is `(1 + soul_egg_bonus) ^ soul_eggs` is not used; the actual rule is linear: `bonus = soul_eggs * (0.10 + 0.01 * soul_food_level + 0.05 * prophecy_eggs_bonus_level ...)` percent per soul egg, with base 10% per soul egg. [public, version-dependent]
- Prophecy Egg bonus: each Prophecy Egg adds +5% (later 1% steps) to the soul egg effect (so 10% -> 10.5% per soul egg, compounding multiplicatively). [public]
- Soul egg gain on prestige is a function of lifetime earnings, roughly proportional to a power of earnings (earnings^0.5-ish at start, then affected by research "prestige: bonus"). [estimate]
- Result: Soul egg count is the main driver after a few prestiges; getting 1e9 soul eggs gives 1e8 percent bonus, and later numbers reach 1e20 and beyond.

## Prestige structure
- Prestige ("Resurrect farm") requires a minimum number of chickens/earnings (the first is available at around 1 hour of play). [estimate]
- Soul eggs accumulate; they are lost only if the player does not claim them.
- Prophecy eggs are not reset and are used for the "Prophecy bonus" and for "Enlightenment" farms.
- Epic research is permanent and funded by golden eggs.
- Enlightenment (the final egg) has separate scoring and "Eggs of Truth"; contracts rank at Pro Permit level.

## Unlock pacing
- Edible egg at start; Superfood after about 2 to 10 minutes (when farm value reaches threshold).
- Medical about 30 minutes; Rocket Fuel about 1 hour; Super Material about 2 hours. [estimates]
- Later eggs are gated by farm value and by the number of prestiges, with the final egg taking months for new players.
- Contracts unlock after a few prestiges; Pro Permit is a paid choice.
- Artifacts, missions and the Gusset / Chicken-One plus the Enlightenment farm come in the late game.

## Offline progress
- Eggs continue to be laid while the app is closed for a limited time (starts at 30 minutes and increases with research for several hours), which is the "idle" part.
- Internal hatcheries keep refilling chickens offline, which makes a boost useful when the player logs off.
- Pro Permit and Boosts extend farm output for several hours.

## Monetization effects
- Free to play with ad-driven boosts (watch a video for 2x earnings for a period), IAP for Pro Permit (contract access) and golden-egg packs, and subscriptions.
- Prophecy Eggs obtainable for free but slowly; a paid pack speeds this up; no pay wall to the main game.
- Piggy bank is a purchase-gated gate; part of it is monetized.

## What players love
- Satisfying visual farm and simple UI, easy to check in.
- Social contracts with co-op bonuses and a long-lived community.
- Deep late game with artifacts and meta-optimization.

## What players hate
- Ad volume and the pressure to buy subscriptions.
- Grindy contract schedule and daily chores.
- Gating of late features behind real-money Pro Permit.
- Version updates that invalidate old strategies.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- The egg tier ladder maps well to Rider worlds: each world unlocks a new "egg" with a 10x value step.
- Have a prestige resource that is a linear percentage (Soul Eggs) and a rarer meta multiplier (Prophecy Eggs) that scales its strength; two layers keeps depth without a second reset.
- Provide offline production with research-driven length, so upgrades extend how long the player can be away.
- Contracts translate to timed Rider missions (no fighting) with rewards that feed the premium-lite currency.
- Avoid paywalling later features; keep paid items to cosmetic or time convenience.
