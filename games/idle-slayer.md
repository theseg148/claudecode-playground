# Idle Slayer
**Sources:** ([S] = snippet, [M] = memory unverified, [E] = estimate. WebFetch DNS-blocked; no exact ascension formula located.)
- https://idleslayer.fandom.com/wiki/FAQ?oldid=381 [S]
- https://idleslayer.fandom.com/wiki/Critical_Culling [S]
- https://idleslayer.fandom.com/wiki/Endgame_Strategy [S]
- https://idleslayer.fandom.com/wiki/Strategy_Guide [S]
- https://steamcommunity.com/app/1353300/discussions/0/4418676236153552668/ and /3035977580520219725 and /3110266679785950552 (Steam threads on souls, stacking) [S]
- https://steamcommunity.com/app/1353300/discussions/0/3075369490061519519/ [S]
- https://www.reddit.com/r/idleslayer (via mirror redlib.hbubli.cc/r/idleslayer/comments/1kzbv6a/) [S]

## Core loop
- Side-scrolling runner: the Slayer auto-runs, jumps, and slays enemies/collects coins. The player taps to jump and chains kills (active play), while Idle upgrades automate it. Coins -> upgrades -> bonus stages -> quests -> Ascension (souls) -> repeat. Random Boxes (flying) and Rage mode add active spikes.
- Hybrid idle/active: the character runs automatically but manual jumps/Rage collect much more.

## Resource types
- Coins, Souls (ascension currency), Slayer Points (SP; ascension upgrades), Armory items/Bonus, Random Box rewards, Dimensions/Portals tokens later, Bonus Stage keys, Silver/Gold/Rainbow coins, Mana. Quests/Rookie Quests.

## Cost & production growth formulas
- Critical hits yield 200% souls with a 15% base chance per enemy kill; Hyper Critical +50%, Critical Mushrooms +30% on crit soul gain [S].
- Soul Reaper and Soul Reaper II stack additively [S, player observation]. Whether ascension bonus is additive/multiplicative is debated [S].
- Souls -> bonus: each soul adds a % bonus to coin income (commonly cited ~+X% each), later with diminishing/multiplicative bonuses from Slayer Points shop [M/E].
- Upgrade costs: typical `base * 1.1x-1.2x^level` with level cap and coin multiplier tiers [E - not verified].
- Random Box chance: community calculator (linked from Strategy Guide) [S]; exact spawn math not retrieved.

## Prestige structure
- Ascension: unlocked after finishing the first two Rookie Quests, buying their upgrades, and earning a Slayer Point [S]. First ascend advice: wait until Permanent Slayer + Soul Gatherer Bundle + Permanent Quests are affordable together [S].
- Ascension resets coins/upgrades, grants souls + Slayer Points; permanent upgrades persist (Permanent Slayer, Permanent Quests...). Later "Dimensions"/Armory layers add second-tier prestige [M].

## Unlock pacing
- First ascension within a few hours of play (~2-4 hr) [E]; subsequent ascensions every 20-60 min early, lengthening later [E]. Bonus Stage, Armory, Portal tiers unlock over days/weeks. Endgame strategy page treats Rage Mode as a playstyle-changing upgrade [S].

## Offline progress
- Yes: offline coins accumulate at a fraction of active rate, with a cap tied to upgrades (Offline progress upgrade) [M/E].

## Monetization effects
- Steam: free-to-play [S: raijin.gg/nodal.gg listings; earlier text here said paid ~$5-10, which snippets contradict - likely was paid before the v3.0.0 F2P switch, unverified]; on mobile free with ads (rewarded ads for boosts) and IAP for bundles [M].

## What players love
- Active/idle hybrid; satisfying chain upgrades; the Random Box/Rage surprise moments; frequent ascension cadence; lots of quests; nostalgic pixel art.

## What players hate
- Grind between ascensions after the bonus slows [S: players say random boxes/multipliers needed after the slowdown]; confusing additive vs multiplicative bonuses [S]; late-game timers.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Gate prestige behind a quest chain + one purchase (earn first Slayer Point) - the unlock *is* the tutorial.
2. Show explicitly whether bonuses are additive or multiplicative; players debate it [S].
3. Random Box analogue: a "Rider Card drop" event with a visible chance upgrade.
4. Crit-for-souls is a nice example of a second "prestige" stat with its own upgrade line.
5. Advise a first-ascension checklist in-game (affordable trio) to prevent premature resets.
6. Keep a hybrid: auto progress + optional active bursts (Rage) so no fighting is required but engagement exists.


## Verification log
Search date 2026-10-18; WebSearch snippets only (pages not opened).
- Confirmed [S]: Slayer Points formula '12 + lifetimeSP*4' (wiki snippet, exact context unclear); crits give 200% souls; Critical Mushrooms +30% crit souls; % souls bonus is additive; Rage Mode added in v3.0.0 with free-to-play Steam (idleslayer.fandom.com).
- CORRECTION [S]: Steam is free-to-play (not paid $5-10 as stated in Monetization); mobile free with ads + IAP (Remove Ads $3.99 1 month / $9.99) per App Store listing. Fixed in Monetization line.
- NOT confirmed: soul-to-coin %, upgrade cost ratios, ascension timings, offline fraction.
