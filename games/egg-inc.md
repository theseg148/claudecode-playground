# Egg Inc
> Verification pass 2026-10-18 (WebSearch snippets only; pages not opened). [S] = confirmed in a search snippet with the URL given; [unverified] = not confirmed, treat as a design placeholder. See "Verification log" at the bottom.
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
- Egg value per egg (wiki main-eggs table, units as the wiki lists them) [S https://egg-inc.fandom.com/wiki/Eggs]: Edible 0.25, Superfood 1.25, Medical 6.25, Rocket Fuel 30, Super Material 150, Fusion 700, Quantum 3,000, Tachyon 50,000, Graviton 175,000, Dilithium 525,000, Prodigy 1.5M, Terraform 10M, Antimatter 1B, Dark Matter 100B, AI 1T, Nebula 15T, Universe 100T [S https://egg-inc.fandom.com/wiki/Universe_Egg], Enlightenment 1e-7 (lowest; upgrading from Universe divides value by 1e21) [S https://egg-inc.fandom.com/wiki/Enlightenment_Egg]. The old ladder (0.1, 1.25, 15, 150, 1000 ... clean 10x steps) was wrong: steps are uneven. Immortality is deprecated (replaced by CRISPR) and its value was not found. Pages are ~445 days old, so current values may differ.
- Chicken lay rate base: [unverified] the 1/30 per minute figure was not found. A Path of Virtue page gives 2.1 eggs per chicken per minute, but only under a specific Colleggtible with no common research [S https://egg-inc.fandom.com/wiki/Egg_of_Curiosity]; Comfortable Nests +10% and Hen House A/C +5% lay rate are listed as common research [S https://egg-inc.fandom.com/wiki/Research].
- Hab capacity (before -> after 4 upgrades) [S https://egg-inc.fandom.com/wiki/Habitats]: Coop 250 -> 788, Shack 500 -> 1,575, Super Shack 1,000 -> 3,150, Short House 2,000 -> 6,300, Double Decker 20,000 -> 63,000. Max total capacity is cited as 11.34 billion with all upgrades and Chicken Universes (older revision, 1.10). Hatchery base capacity 250. The old '250 to 1M-ish per hab' was wrong.
- Hatchery capacity: internal hatchery rate research gives chickens per minute while online and offline. [public]
- Research costs follow an exponential schedule, growth about 1.05 to 1.3. [unverified]
- Soul egg bonus [S https://egg-inc.fandom.com/wiki/Earnings_Bonus/Soul_Eggs]: each Soul Egg gives +10% earnings by default (linear, not compounding). The Soul Food epic research adds +1 percentage point per level (level 140 max, 150% per egg). Earnings Bonus formula per the wiki: EB = (10 + Soul Food level + Soul Stone bonus)% x Soul Eggs x Prophecy factor x 1.01^(Eggs of Truth). Simplified, with maxed epic research and no artifacts: EB = 1.5 x SoulEggs x 1.1^(ProphecyEggs) x 1.01^(TruthEggs) [S https://egg-inc.fandom.com/wiki/Farm_Value].
- Prophecy Egg bonus [S https://egg-inc.fandom.com/wiki/Egg_of_Prophecy and its talk page]: each Egg of Prophecy multiplies the Soul Egg effect by 1.05 (5%); the Prophecy Bonus epic research adds +1 percentage point per level, up to 10% per egg. General form ((105 + PB)/100)^(prophecy eggs); e.g. 2 eggs give 1.1025x at 5% and 1.21x at 10% (older revision).
- Soul egg gain on prestige [S https://egg-inc.fandom.com/wiki/Prestige]: depends on earnings since the last prestige, with diminishing returns as the Soul Egg count grows (each further Soul Egg costs more). The Prestige Bonus epic research adds +10% soul eggs per level, 20 levels, up to +200%. The exact exponent (the earlier 'earnings^0.5-ish') is [unverified].
- Result: because each Soul Egg is +10% (linear), N soul eggs give a +10N% earnings bonus before research; counts reach very large numbers late game. (The earlier '1e9 soul eggs = 1e8 percent' arithmetic was wrong.)

## Prestige structure
- Prestige [S https://egg-inc.fandom.com/wiki/Prestige]: unlocks as soon as you obtain a Soul Egg from any source (including Challenges and the Daily Gift Calendar). No minimum chicken count or 'about 1 hour' threshold was found [unverified]. Prestige resets chickens, common research, habs, silos and vehicles and returns the egg to Edible; permits, epic research, golden eggs, boosts and artifacts persist.
- Soul eggs accumulate. (The earlier claim that they are lost if unclaimed was unsupported [unverified].)
- Prophecy eggs are not reset and are used for the "Prophecy bonus" and for "Enlightenment" farms.
- Epic research is permanent and funded by golden eggs.
- Enlightenment (the final egg) has separate scoring and "Eggs of Truth"; contracts rank at Pro Permit level.

## Unlock pacing
- Edible egg at start; later eggs unlock by farm value [S https://egg-inc.fandom.com/wiki/Eggs]: Superfood discovered at ~10M farm value (upgrade ~68M), Medical ~840M (~5.3B), Rocket Fuel ~38B (~240B), Super Material ~27T (~170T), Fusion ~8Q (~50Q), Quantum ~3.6 quintillion (~23 quintillion). Wall-clock minutes for Superfood are [unverified].
- Wall-clock pacing for Medical / Rocket Fuel / Super Material (30 min / 1 h / 2 h) is [unverified]; farm-value gates above are the confirmed part.
- Later eggs are gated by farm value and by the number of prestiges, with the final egg taking months for new players.
- Contracts unlock after a few prestiges; Pro Permit is a paid choice.
- Artifacts, missions and the Gusset / Chicken-One plus the Enlightenment farm come in the late game.

## Offline progress
- Eggs continue to be laid while the app is closed for a limited time that research and purchases can extend; the exact starting cap (30 min) and the 'several hours' are [unverified]. A PocketGamer piece confirms the game tells players they are capped and offers real-money or golden-egg upgrades to extend offline takings [S https://www.pocketgamer.biz/egg-inc-idle-games-gold-standard/].
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

## Verification log

Confirmed [S]:
- Egg values for all 19 main eggs except Immortality (replaced by CRISPR), plus farm-value discovery/upgrade thresholds for Superfood through Quantum; corrected the old 10x-step ladder. (https://egg-inc.fandom.com/wiki/Eggs, Universe_Egg, Enlightenment_Egg)
- Soul Egg = +10% each, linear; Soul Food +1 percentage point/level (max level 140, 150%); Earnings Bonus formula; Prophecy Egg 5% each (up to 10% with Prophecy Bonus) with ((105+PB)/100)^n form. Fixed the muddled soul-egg sentence accordingly.
- Prestige Bonus epic research +10%/level up to +200%; prestige unlocks on first Soul Egg; what resets/persists.
- Hab capacities for Coop, Shack, Super Shack, Short House, Double Decker.
Unconfirmed [unverified]:
- Base lay rate (1/30 per min), research cost growth 1.05-1.3, soul egg gain exponent, offline cap length and starting value, wall-clock unlock pacing, Immortality egg value, larger-hab capacities beyond Double Decker.
Caveat: search summaries of wiki pages ~445 days old; values may have changed since. Some search results were SEO spam and were ignored.
