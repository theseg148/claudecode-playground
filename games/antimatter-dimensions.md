# Antimatter Dimensions
**Sources:** (WebFetch was blocked by DNS in this session; formulas are from recall of the wiki and open source repo, so verify.)
- https://antimatter-dimensions.fandom.com/wiki/Antimatter_Dimensions_Wiki
- https://antimatter-dimensions.fandom.com/wiki/Infinity
- https://antimatter-dimensions.fandom.com/wiki/Eternity
- https://antimatter-dimensions.fandom.com/wiki/Reality
- https://github.com/IvarK/AntimatterDimensionsSourceCode (the source is public; ground truth for formulas)
- https://ivark.github.io/ (the game)

## Core loop
- Buy Antimatter Dimensions: the 1st makes antimatter, the 2nd makes 1st dimensions, and so on up to the 8th.
- Buy tickspeed upgrades, Dimension Boosts and Antimatter Galaxies.
- Reach Infinity (about 1.79e308 antimatter), spend Infinity Points on upgrades, then repeat.
- Higher layers: Eternity, Reality, then Celestials. Each layer re-teaches the same loop with new rules.

## Resource types
- Antimatter, Infinity Points (IP), Infinities, Eternity Points (EP), Eternities, Time Theorems and Time Dimensions, Replicanti, Reality Machines, Perk Points, Glyphs, Relic Shards, Celestial-specific currencies (Teresa's Reality Machines pour, Effarig's relic shards, Enslaved's Hint, V's Achievements, Ra's memories, Laitela's Dark Matter, Pelle's Remnants).

## Cost & production growth formulas
- Base dimension costs (public, wiki): 1st 10, 2nd 100, 3rd 1e4, 4th 1e6, 5th 1e9, 6th 1e13, 7th 1e18, 8th 1e24. [public]
- Per-purchase cost multipliers after each batch of 10: 1e3, 1e4, 1e5, 1e6, 1e8, 1e10, 1e12, 1e15 respectively. [public]
- Each batch of 10 bought doubles that dimension's multiplier (x2 per 10), and dimension N produces dimension N-1 per second. [public]
- Production per second: `D_n_amount * multiplier * tickspeed` feeding the one below. [public]
- Tickspeed: starts with 1000 ms per tick; each upgrade multiplies the interval by 0.89 (cost starts at 1e3 and rises by x10 each purchase). Antimatter Galaxies improve the multiplier by +0.02-ish (0.89 to 0.87, ...). [public, approx values]
- Dimension Boosts: first needs 20x 4th dimension, then 15 more of the next dimension per boost; each boost gives x2 to the lowest dimensions and unlocks the next tier. [public]
- Galaxies: first Galaxy needs 80x 8th dimensions, each next needs +60. [public]
- Infinity: reached at 2^1024 = 1.7976931348623157e308. [public, exact]
- IP gain: `IP = floor(10^(log10(AM)/308 - 0.75))`-style (one IP at Infinity growing about 10x per 308 orders more AM). [public approx]
- Eternity: needs 1.79e308 IP. EP gain = `5^(log10(IP)/308 - 0.7)` (approx) which scales with the log of IP. [estimate; see source code]
- Reality: needs about 1e4000 EP and maxed Time Studies (roughly 1.5 e3 hours of play to the first one). [estimate]
- Replicanti: grows with `1 + chance` per interval and has a cap at Infinity with galaxies; costs 1e140 IP to unlock. [public, approx]

## Prestige structure
- Infinity: resets Dimensions and Antimatter; keeps IP, Challenges and Achievements.
- Eternity: resets Infinity-related upgrades; keeps EP, Time Studies, Eternity Challenges.
- Reality: resets almost everything; keeps Glyphs, Perks, and Reality Machines and unlocks Celestials.
- Each Celestial has a Reality-gated challenge with its own rules and unique rewards (e.g. Teresa's Perk Shop).
- Doomed (Pelle) is a final reset that restarts the entire game in a hostile mode (Endgame update).

## Unlock pacing
- First Infinity: about 30 minutes to 2 hours for a fresh player. [estimate]
- Challenges unlock by Infinity count; Break Infinity (breaking the 1.79e308 cap) is around hour 3 to 8. [estimate]
- Eternity: first at about 1 to 3 days; Reality: about 1 to 3 weeks; Celestials: weeks to months. [estimates]
- There is a 12-normal-challenge, 8-infinity-challenge and 12-eternity-challenge stack for the first three layers.
- Achievements: 150+ with row-by-row reward bonuses (e.g., Row 1: +x1.1 multipliers).

## Offline progress
- The game simulates offline time with a chunked tick, with the number of ticks configurable in settings (default 1000 ticks per session). Real speed is a "Game speed" multiplier.
- Players can set "offline progress" on or off; Time Dimensions continue to work offline. [estimate on defaults]

## Monetization effects
- None. Free, no ads, no premium currency; Steam version is free. Developer funded by donations/Patreon (Antimatter Dimensions: Steam).

## What players love
- Every layer reinvents the game; the first few hours feel like discovery.
- Big-number satisfaction and many puzzles (challenges).
- Open source, active modding and community spreadsheets.

## What players hate
- Mid-game (Break Infinity to Eternity) can feel long with little change.
- Late layers require wiki reading; it is opaque and math-heavy.
- Endgame content is paced in weeks, and Doomed restarts are polarizing.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- A natural prestige cap (like 1.79e308) is a good "world complete" gate: the player sees a clear finish line for each Rider world.
- Each new layer should change rules (new challenge type) rather than just add a bigger number.
- Use multiples-of-10 purchases that double output; it gives readable breakpoints.
- Provide a pre-prestige preview (IP pending) and show log-scale progress.
- Keep an achievement ladder with small multipliers so every session ends with something earned.
- Free and ad-free play builds trust, so consider placing premium in cosmetics only.
