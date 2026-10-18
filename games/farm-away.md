# Farm Away! (idle farming)
**Sources:** (URLs, required)
CONFIDENCE WARNING (LOW): the sandbox could only fetch raw.githubusercontent.com. Farm Away! (a mobile idle farm with a virtual-farm-in-the-background style) could not be looked up. Everything is [MEM-LOW] or [EST]. I also was unsure whether to cover Farm Away! or "Idle Farming Empire"; I chose Farm Away! per the brief's first option.
- https://play.google.com/store/apps/details?id=com.fugu.farmaway (id from memory, unverified)
- https://apps.apple.com/us/search?term=farm%20away (search; not fetched)
- https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii (genre math; not fetched)
- https://adventure-capitalist.fandom.com/wiki/Adventure_Capitalist_Wiki (genre-prototype wiki; not fetched)

## Core loop
- Tap or auto-harvest crops, sell for coins, buy more plots and faster crops, hire farmhands, unlock animals/crafting. The farm is the visible progress meter.
- The structure is Adventure Capitalist-like: several producers (wheat, corn, ... livestock) each with a cycle time; managers automate each; multipliers at owned thresholds.
- Prestige ("sell the farm"/"move to a bigger farm") resets the farm for a permanent bonus.
- Seasonal events and orders (deliver X crops for a reward) add short goals.

## Resource types
- Coins, Gems (premium), crops (wheat, corn, carrots...), animal products (eggs, milk, wool), Workers, Boosters, Prestige currency ("golden tokens" etc.; naming unverified). [MEM-LOW]
- Seeds or crop tokens may be spent to plant. [EST]

## Cost & production growth formulas (public or estimated; mark which)
- Not verified for this title. For Adventure Capitalist-style structures (which it follows), established values: [genre MEM]
  - Cost of the nth unit = base * coefficient^n with coefficient between 1.07 and 1.15 (Adventure Capitalist uses 1.07 for lemonade up to 1.15 for oil). [MEM from Game Developer series]
  - Revenue per cycle = count * base revenue * multipliers; cycle time fixed per producer (1 s ... hours).
  - Milestone speed-ups: x2 at 25, 50, 100, 200, 300, 400 owned etc. [MEM]
- Prestige: points = floor(150 * sqrt(lifetime earnings / 1e15))-ish in Adventure Capitalist (Angel formula), each point +2% income. [MEM; in AdCap, 150*sqrt(earnings/1e15) is the commonly cited formula; unverified for Farm Away]
- Crop value tiers grow ~5-10x per tier with cycle time growing ~2-4x. [EST]

## Prestige structure
- One main reset: farm expansion/reset giving permanent bonus tokens. [MEM-LOW]
- Players typically prestige when projected tokens double the current stock. [genre]
- Additional, later layer (trading/pro farm) possible. [EST]

## Unlock pacing
- [EST] 0-5 minutes: first crops and plots; 30-60 min: managers and animals; 1 day: prestige; 1 week: later crops, events.
- Unlock tiers by total owned/profit so each crop appears around 10-20x the previous crop's cost.

## Offline progress
- [MEM-LOW] Returns "while you were away" coins, with managers required; capped to hours; bonus for watching an ad. Exact values unknown. [EST]

## Monetization effects
- F2P: rewarded ads (double rewards, speed-ups), IAP gems, no-ads. [MEM-LOW]
- Timers/energy not needed in this genre; monetisation is largely boosters and time skips. [EST]

## What players love
- Calm, cosy theme; progress you can see (the farm fills up).
- Lots of automation; short check-ins.
- Cosmetic variety (decorations).

## What players hate
- Ads and pushy offers; slow mid-game. [EST]
- Little meaningful choice; all upgrades are eventually bought. [EST]
- Time-skip IAP making the base game feel slow. [EST]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. A known template: several parallel producers with manager automation. For Decade, each world could be a producer line, and "managers" are allied Riders.
2. Producers with differing cycle times provide variety in a no-fighting game: fast (1 s) vs slow (1 h) lines make check-in rhythm.
3. Milestone speed-ups at 25/50/100/200 owned are a reliable dopamine pattern.
4. Prestige formula 150*sqrt(earnings/1e15) (Adventure Capitalist, unverified) is a good starting point; each point +2% income. [EST]
5. Orders/delivery goals give short-term targets when the number go up is slow.
6. Visible growth (farm fills up) maps to a diorama of Rider worlds filling up in the Studio.
7. Avoid time-skip IAP as the main monetization; sell cosmetics.
8. Low confidence: re-research before relying on numbers.
