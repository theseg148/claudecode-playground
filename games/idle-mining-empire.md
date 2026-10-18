# Idle Mining Empire
**Sources:** (URLs, required)
VERIFICATION UPDATE 2026-10-18: 'Idle Mining Empire' is a browser HTML5 game on CrazyGames (June 2021), NOT a confirmed mobile F2P title with gems/ads; the monetization, gems, 'Empire' prestige and offline sections below were written for a mobile tycoon and are UNVERIFIED for this game. See Verification log.
CONFIDENCE WARNING (LOW): sandbox could only fetch raw.githubusercontent.com; no page on Idle Mining Empire was fetchable. Details are [MEM-LOW] or [EST] and may be mixed with similar mining tycoons (Idle Miner Tycoon). Verify before using.
- https://www.crazygames.com/game/idle-mining-empire (browser game listing, via search snippets) [S]
- https://www.thefictionaddiction.com/idle-mining-empire/ (review, via snippet) [S]
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i (genre math; not fetched; it surfaced via the part III search result)
- https://en.wikipedia.org/wiki/Idle_Miner_Tycoon (closest genre comparison; not fetched)

## Core loop
- Browser (HTML5, CrazyGames, June 2021) idle tycoon [S]: build mine shafts, elevators and warehouses; hire managers to automate each level; money flows from ore to market.
- You tap to boost; managers automate; upgrades multiply speed or capacity; each new shaft costs more but yields more.
- Periodic "Empire" reset trades the whole mine for permanent Prestige currency (names unverified) and unlocks new regions (coal, gold, gems, etc.). [MEM-LOW]
- Events and missions refresh engagement.

## Resource types
- Cash (soft), Gems/Super Cash (premium), Prestige currency, Boosts (time-limited multipliers), Managers (collectible, with tier and rarity), Artifacts or cards (permanent small bonuses). [MEM-LOW]
- Resource per mine: ore units carried -> elevator capacity -> warehouse transport -> market. [genre structure]

## Cost & production growth formulas (public or estimated; mark which)
- Not verified for this title. Known genre baselines (Idle Miner Tycoon-style):
  - Next shaft cost multiplier about x3-x10 per shaft early. [EST]
  - Level upgrade cost ~ base * 1.07-1.15^level (coefficient per Game Developer series). [EST]
  - Production: each level adds linear output; milestone levels (25, 50, 100, 200...) give x2 speed or x2 profit. [EST]
  - Manager multiplier x3 to x10+ for their shaft per tier. [EST]
- Prestige: new currency = floor((lifetime cash / 1e15)^0.5)-ish, each point +x% (often +2% or +10%). [EST]

## Prestige structure
- One main prestige ("Empire"/"Super Cash"?), after which regions reset but meta-bonuses remain. [MEM-LOW]
- Each prestige point typically gives a flat percent boost (e.g., +x% income per point) so the benefit is linear in points. [EST]
- Additional soft prestige by moving to the next mine/region. [EST]

## Unlock pacing
- [EST] First 5 minutes: manager hired and shaft 2 built; 1 hour: 5-10 shafts and first elevator upgrade; 1-2 days: first Empire reset; weekly: regional unlock and event cycles.
- Managers and shafts each unlock on a cost basis, so pacing is a purchase queue. [EST]

## Offline progress
- [MEM-LOW] Standard for the genre: returning shows "Idle earnings" computed from time away at a managed rate; managers must be hired for shafts to earn offline. Cap often 8-24 h. Doubling by rewarded ad. [EST]

## Monetization effects
- F2P with rewarded ads, premium currency purchases, no-ads pack, and "boosters". [MEM-LOW]
- Time-limited sales; event passes. [EST]
- The main retention loop: ad-double offline plus daily login rewards. [genre knowledge]

## What players love
- Satisfying automation: watch numbers and trucks flow.
- Simple, quick sessions; clear next goal (the next manager).
- Regular events and collectibles.

## What players hate
- Ads and premium paywall pressure; resets that feel slow.
- Duplicate content between mining tycoons (little originality). [EST]
- Numbers inflate so notation hits e-notation quickly. [EST]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Manager-like automation purchases (hire a "Rider helper" per world) are a satisfying early milestone: one purchase changes manual to automatic.
2. Milestone-level multipliers (x2 at levels 25/50/100/200) beat smooth growth for dopamine; implement on every upgrade line.
3. Prestige with flat percent per point (+x% per Dimension Crystal) is easy for players to understand; use it for world 1-2 prestige.
4. Show the production flow visually (cards moving from shaft to market becomes Rider Cards moving from world to Decade's belt).
5. Offline: cap at 8-24 h, require automation purchased to earn offline, an incentive for buying managers.
6. Rewarded "double" optional; no mandatory ads.
7. Avoid cloning mining-tycoon structure verbatim; the genre is saturated, and the Decade IP differentiator is the sequential worlds.
8. This file is low-confidence; do not cite its numbers as facts.

## Verification log (2026-10-18)
Method: WebSearch snippets only.
Confirmed [S]:
- CrazyGames lists Idle Mining Empire as HTML5, desktop+mobile web, June 2021, rating 9.1: start from scratch and build a fully automated mining operation; click your worker to produce resources to sell; digging deeper unlocks new shafts that earn more; managers are added to each part of the workflow; upgrades make each part faster and more profitable. https://www.crazygames.com/id/game/idle-mining-empire
- Review (thefictionaddiction.com): cute low-stress background game; miners start at a couple of dollars and quickly reach millions, trillions and beyond. https://www.thefictionaddiction.com/idle-mining-empire/
Not the same game: App Store 'Mining Empire Idle Tycoon' (https://apps.apple.com/app/id6479964188; managers, offline income, weekly events, an elevator-bug fix note), 'Idle Mining Company: Tycoon' (managers, prestige), 'Mine Empire: Idle Tycoon' (Android, prestige, 100+ miners). Their features must not be attributed to the CrazyGames title. A Chrome extension with the same name also exists.
Unverified: any prestige/'Empire' reset, premium currency, ads/IAP, offline cap, all formulas (all remain genre [EST]); the 'Lazy Panda' developer guess was NOT confirmed and is dropped. Lessons below that rely on mobile monetization are generic design advice, not evidence from this game.
