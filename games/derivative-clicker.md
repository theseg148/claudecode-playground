# Derivative Clicker (gzgreg)
**Sources:**
- https://raw.githubusercontent.com/gzgreg/derivativeclicker/gh-pages/README.md (changelog 0.01 to 0.341)
- https://raw.githubusercontent.com/gzgreg/derivativeclicker/gh-pages/js/data.js (start state, building factors, costs)
- https://raw.githubusercontent.com/gzgreg/derivativeclicker/gh-pages/js/script.js (cost, reset logic)
- https://raw.githubusercontent.com/gzgreg/derivativeclicker/gh-pages/js/building.js
- Scratch copies: /tmp/claude-0/-home-user-claudecode-playground/2e77cd6e-e441-551f-a27e-40f493265545/scratchpad/src3/dc/ (untrusted data, read only)
- https://uncommonx.itch.io/idle-derivative-prototype (search hit: a Godot prototype that recreates Derivatives and Click Scholars) [S]
- Tags: [S] snippet, [CODE] source, [M] memory, [E] estimate.

## Core loop
- Earn money by clicking (starts at $0.10 after reset, so no-click runs are possible) and buy buildings; each tier builds the one below it ("generators that build more generators"). [CODE] (money 0.1), [S]
- Buildings are grouped in 7 tiers, 5 per tier: deriv(N), a click/other building, computer-like, worker, and a "famous mathematician" per tier. [CODE] (data.js comment indices 0-34)
- Names climb mathematically: high schooler, undergraduate, graduate student, postdoc, research scientist, lab manager, research lab; mathematicians Andrew Wiles, Kurt Godel, Bernhard Riemann, Carl Gauss, Leonhard Euler, Isaac Newton. [CODE]
- Click and autoclick are separate stats (moneyPerClick, moneyPerAutoclick, clickPower, "clicks to gain" for autobuilding). [CODE]

## Resource types
- Money, "proofs" (second currency with costPerProof 5), and tiered reset currency (6 tiers). [CODE]
- Infini-currency tracked after hitting infinite money; "currently do nothing" in v0.34. [CODE] (README)
- Statistics tracked: total money, ticks, clicks, manual clicks. [CODE]

## Cost & production growth formulas (public or estimated; mark which)
- Buying n of a building: price * ((factor^n - 1) / (factor - 1)), i.e. geometric series. [CODE] (script.js line ~79)
- Per-building cost factors (growth ratio): deriv1 1.1, combinatorics 1.1, computer 1.3, high schooler 1.1, mathematician 1.05, deriv2 1.2, probability 1.3, assembly line 1.8, ... up to deriv7 2.7 and Isaac Newton 4. [CODE] (`new Building(factor, moneyCost, proofCost)`)
- Base money costs jump by orders of magnitude per tier: $0.10, $500, $20,000, $20M, $1B, $10T, $500B, ... up to $1e27 for tier-7 mathematician. [CODE]
- Tier unlock upgrades cost 1e6, 1e9, 1e12, 1e15, 1e18, 1e21, 1e24. [CODE] (tierUpgradeCosts)
- Global multiplier from reset currency = 1 + 0.01 * resetCurr (per tier). [CODE] (script.js ~73)
- Thresholds for reset currency: proofs need 10 * (10 * (10 + n))^6 for the next unit; mathematicians 7000 * (10 + n)^6. [CODE]
- Reset currency buyables cost 10 to 100,000+ units of specific tiers (e.g. "Unlocks tier 5" = 10 tier-1 currency, "tier 7" = 100 tier-3). [CODE]

## Prestige structure
- Tiered resets: reset tier 1 and you gain tier-1 currency; every `resetCurrFactor` (5) of tier N converts into 1 of tier N+1, consuming them. [CODE] (script.js ~262)
- Tier-1 reset is cheap, "tier 2..6" resets need more of the earlier currency. [CODE]
- Reset currency buyables: unlock tiers 5/6/7, reduce the building price multiplier by /1.1, reduce clicks needed for autobuilding, reduce ticks between auto-builds. [CODE]
- Hitting infinite money triggers an automatic "infini-reset" that erases all reset currency. [CODE]

## Unlock pacing
- Tiers 1-4 at start, tiers 5-7 locked behind tier-1/2/3 reset currency purchases. [CODE]
- Sixth derivative arrived in v0.2, seventh tier in v0.22; chart, achievements, number suffixes were added across 2014. [CODE]
- First hour is clicking, then autoclickers, then first reset. [M]

## Offline progress
- No offline mechanic found. Version 0.17 fixed a bug where Chrome/Firefox throttle background tabs to once per second. [CODE] (README) 
- A `timeMult` (x10 at the 100 ms tick floor) speeds up play instead. [CODE]

## Monetization effects
- None. Hosted on GitHub Pages. [CODE]

## What players love
- The calculus theme: tier N produces tier N-1 like a derivative hierarchy. [M]
- Depth of reset layers for a tiny game. [M]

## What players hate
- Abandoned after 2015 (v0.341). [CODE]
- Number blindness and dense UI. [M]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Tier chain "each tier makes the tier below" gives natural era structure: Heisei Rider N produces Rider N-1 power. [CODE]
2. Tier unlock upgrades at costs 10^3 apart give a rhythm of one new tier per goal. [CODE]
3. Cheap lower-tier resets that convert 5:1 upward is a clean way to tie several prestige levels together. [CODE]
4. Let reset currency buy convenience (cheaper bulk, faster autobuild), not only multipliers; it widens upgrade space without more inflation. [CODE]
5. Offer an infini-style cap check so late currency overflow has a designed ending. [CODE]
6. Not much to learn about world/zone progression: the "world" is the tier. [E]

## Verification log
- All four files returned HTTP 200 from the gh-pages branch of gzgreg/derivativeclicker. The repo was guessed from a search snippet that linked gzgreg.github.io/derivativeclicker; WebSearch did not directly list the repo.
- Only parts of script.js read; per-building production values and exact achievement list were not.
- Offline claim is absence-of-evidence, not verified.
