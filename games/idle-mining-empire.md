# Idle Mining Empire
**Sources:** (URLs, required)
CONFIDENCE WARNING (LOW): sandbox could only fetch raw.githubusercontent.com; no page on Idle Mining Empire was fetchable. Details are [MEM-LOW] or [EST] and may be mixed with similar mining tycoons (Idle Miner Tycoon). Verify before using.
- https://play.google.com/store/search?q=idle%20mining%20empire (search; not fetched)
- https://apps.apple.com/us/search?term=idle%20mining%20empire (search; not fetched)
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i (genre math; not fetched; it surfaced via the part III search result)
- https://en.wikipedia.org/wiki/Idle_Miner_Tycoon (closest genre comparison; not fetched)

## Core loop
- Mobile idle tycoon: build mine shafts, elevators and warehouses; hire managers to automate each level; money flows from ore to market.
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
