# Idle Miner Tycoon
**Sources:** (WebFetch was DNS-blocked this session; only search snippets readable. [S] seen in snippet, [M] recalled from memory unverified, [E] estimate.)
- https://www.kolibrigames.com/blog/economy-in-free-to-play-mobile-games-part-2/ (Kolibri on hard/soft currency design; Super Cash = primary hard currency) [S]
- https://www.appgamer.com/idle-miner-tycoon/strategy-guide/what-is-prestige-in-super-miner-tycoon (prestige explained) [S]
- https://idleminertycoon.fandom.com/wiki/File:Ancient_Boost.PNG and the wiki main pages (Super Cash, Managers, Mines) [pages not read]
- https://www.supercheats.com/idle-miner-tycoon-cheats-tips-strategy/walkthrough/ [S]
- https://www.bluestacks.com/de/blog/game-guides/idle-miner-tycoon/idt-currency-guide-de.html (research point = 200 Super Cash) [S]

## Core loop
- Vertical mine: Mine Shafts (miners dig ore), Elevator (moves ore up), Warehouse (carries to surface). Throughput = min of the three stages, so upgrade the bottleneck.
- Loop: spend cash to level each stage -> hire a Manager per stage (auto-run) -> buy a new shaft -> when the mine is deep enough, prestige.
- Boost layer: Super Cash buys time-warps, 10x boosts (ad-triggered), Ancient/Event boosts. Later: Continents/Mines unlocked (Earth, Moon, Mars, Gold... ) each own currency scale.

## Resource types
- Cash (soft, per-mine), Super Cash (hard), Managers (cards/levels), Boosts, Research points (200 Super Cash each [S]), Idle Cash on return (offline), mine-specific event currencies, Continental cash (Gold mine etc.).

## Cost & production growth formulas
- Exact constants are not in my retrieved sources. Pattern [M]: each shaft/elevator/warehouse level cost grows ~ `base * ~1.1x - 1.3x^level`-style (geometric), and output grows linearly with level plus x2 multipliers at fixed level milestones (every 25 / 50 / 100 levels, 10 / 25 / 50...) [E].
- Shaft k cost grows steeply: each new shaft costs roughly x2-3 of the previous plus bigger base ore value [E]. Number formats escalate K, M, B, T, aa, ab... (e.g. 3.61T, 162aa as research price examples [S]).
- Manager boosts: x3 / x5 / speed boosts per shaft; levelled with Super Cash/manager cards [M].
- Prestige gain: Super-Cash payout depends on the mine's total production rate at the time of prestige and the prestige number [S: "cost to prestige will gradually increase" / "5 prestiges per mine"]. Treat any closed-form as unknown.

## Prestige structure
- Per-mine prestige, up to 5 times in any mine [S]. Prestige resets that mine's cash/levels but earns Super Cash and a ~4x income boost [S per walkthrough; check, this may be x4 per first prestige only].
- Does not touch other mines, achievements, or Super Cash balance [S].
- Prestige availability requires reaching a production-rate threshold, which grows each time [S].

## Unlock pacing
- First 5 min: shafts 1-3, first managers. ~30-60 min: first mine complete (deep enough to prestige) [E]. Day 1-3: second mine (Earth), research unlocks. Week 1+: continents, event mines (limited time, with their own currency + Super Cash rewards [S]).
- Early game ordering is spoon-fed with a tutorial; every few minutes a new shaft/manager.

## Offline progress
- Yes, strong: managers keep working while away; returning grants "Idle Cash" with a Super Cash "x2" ad/booster doubling, capped by an offline-time limit [M]. Core to the game's session design.

## Monetization effects
- Hard currency Super Cash (IAP, plus daily, expedition, event rewards [S]); rewarded-ad x2 boosts; VIP/Starter packs; time-skips. Heavy F2P design: grindy slowdown at deep shafts nudges to skip. Super Cash spent to unlock shafts and speed up unlocks [S].

## What players love
- Cash-number-go-up satisfaction; lots of visuals of workers; clear bottleneck puzzle (shaft/elevator/warehouse); prestige per-mine means a lot of mini-resets; events.

## What players hate
- Ad and IAP pressure; huge number inflation; late-game becomes passive and slow; event mines feel mandatory; paywalled progress and nagging notifications.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. A 3-stage bottleneck chain (Collect -> Transform -> Deliver) maps to Rider world "Ride -> Card -> Finish" and gives upgrade decisions without combat.
2. Per-world prestige capped at a small count (5) with growing thresholds is a clean cadence; a 4x payoff is a good anchor [S/E].
3. Milestone multipliers at fixed levels (x2 at 25/50/100) give dopamine spikes - use them [E].
4. Offline earnings with a capped window and "welcome back" doubling hooks returning.
5. New location unlocks (Earth -> Moon -> Mars) are natural analogues to world-hopping; give each its own currency scale.
6. Avoid its late-game ad/IAP pressure if we want better reviews.


## Verification log
Search date 2026-10-18; WebSearch snippets only (pages not opened).
- Partly supported [S]: managers let you earn Idle Cash offline with a cap (idleminertycoon.fandom.com, bluestacks guides); manager upgrade discounts up to 70-80% for Executives; Super Cash buys shafts/speedups (kolibrigames.com blog).
- NOT confirmed: cost growth constants, 'Super Cash x2 offline' booster, milestone levels 25/50/100. Remain [M]/[E].
