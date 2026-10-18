# Adventure Capitalist
**Sources:** (WebFetch was blocked by DNS in this session, so all numbers are from recall of the wiki and community spreadsheets; verify before relying on them.)
- https://adventure-capitalist.fandom.com/wiki/Adventure_Capitalist_Wiki
- https://adventurecapitalist.fandom.com/wiki/Angel_Investors
- https://store.steampowered.com/app/346900/AdVenture_Capitalist/
- https://en.wikipedia.org/wiki/AdVenture_Capitalist
- Hyper Hippo Games (developer) https://www.hyperhippo.com/

## Core loop
- Buy the first business, tap it to produce cash, and buy more of it.
- Buy a manager for each business so it runs automatically.
- Buy milestone-level multipliers; save up for the next business; repeat up to the 10th.
- When earnings stall, reset for Angel Investors, and a bigger multiplier makes the next run much faster.
- The Event/Planet system (Earth, Moon, Mars, then more) gives a separate parallel loop with its own currencies.

## Resource types
- Cash (per planet).
- Angel Investors (the prestige currency; each gives a percentage bonus and can be sacrificed for Angel Upgrades).
- Gold (premium currency): from events and purchases, used for time warps and boosts.
- Megabucks / Mega Tickets in event modes (this changed a lot across versions; treat as estimate).
- Planet-specific currencies after Mars (e.g. Lunar and Martian currencies).

## Cost & production growth formulas
Public community-spreadsheet values for the Earth economy (from recall; treat the 7-digit coefficients as estimates):

| Business | Base cost | Coeff | Base revenue | Cycle |
|---|---|---|---|---|
| Lemonade Stand | $4 | 1.07 | $1.67 | 0.6s |
| Newspaper Delivery | $60 | 1.15 | $60 | 3s |
| Car Wash | $720 | 1.14 | $540 | 6s |
| Pizza Delivery | $8,640 | 1.13 | $4,320 | 12s |
| Donut Shop | $103,680 | 1.12 | $51,840 | 24s |
| Shrimp Boat | $1,244,160 | 1.11 | $622,080 | 96s |
| Hockey Team | $14,929,920 | 1.10 | $7,464,960 | 384s |
| Movie Studio | $179,159,040 | 1.09 | $89,579,520 | 1,536s |
| Bank | $2,149,908,480 | 1.08 | $1,074,954,240 | 6,144s |
| Oil Company | $25,798,901,760 | 1.07 | $12,899,450,880 | 36,864s |

- Cost of the n-th purchase: `cost(n) = base * coeff^n`. Coefficient drops from 1.15 to 1.07 as tiers rise, so late tiers stay affordable in bulk. [public]
- Revenue per cycle is `owned * base_revenue * multipliers`. [public]
- Milestone speed-ups: at 25, 50, 100, 200, 300, 400... owned the cycle time is halved or revenue is doubled (varies by version). 25/50/100 are most commonly quoted. [public, version-dependent]
- Manager costs run from $1,000 for Lemonade up to about $100B for Oil (each roughly 10 to 15x the last). [estimate]
- Angel Investors on reset (community-derived, mark as estimate): `angels = floor(150 * sqrt(lifetime_earnings / 1e15))` minus angels already owned. Early versions used a different base. [estimate]
- Each Angel Investor gives +2% to all profit by default (up to +x for upgrades), with sacrifice giving a larger multiplier but burning the angel count. [public]
- Because of the square-root, 4x lifetime earnings gives 2x angels. [follows from the formula above]

## Prestige structure
- "Claim Angel Investors" resets cash, businesses and managers, and keeps the angels, gold and upgrades.
- Typical optimum is to reset when pending angels exceed about 100% of current angels (estimate; community rule of thumb).
- Each planet has its own prestige, with unlock of the next planet via the previous planet's angel total.
- Angel upgrades (cost in angels) give permanent multipliers and cheaper managers, and some unlock "all businesses x3" style boosts.

## Unlock pacing
- Lemonade stand is available immediately; Newspaper after around 1 minute.
- All Earth businesses are reachable in 1 to 3 hours of the first run. [estimate]
- First Angel Investors about 1 to 2 hours in; the Moon after you have enough angels (approx. 1e12 total angels in community play-through, estimate).
- Mars opens after the Moon's progress and is aimed at multi-week players. [estimate]

## Offline progress
- Managers keep working offline, and the game awards the full income for the idle time (capped by time-warp options and later by an optional "hours cap" in some versions).
- Time warp (premium) lets players skip ahead 1h to 7 days of profit.

## Monetization effects
- Free-to-play with gold packs, ad-based boosts (2x for 4h), VIP / Angel packs, and time-warp items.
- Gold lets you buy time warps and instant Angel Investors; this directly competes with the free loop but is balanced by caps and the long arc.
- Steam version is a mostly free version with optional premium DLC boosts.

## What players love
- Instant clarity: ten businesses, simple managers, readable numbers.
- Satisfying "number goes up" from the milestone speed-ups.
- Short sessions pay out thanks to offline earnings.

## What players hate
- Heavy ad/IAP pressure and event content that fragments the economy.
- Planet resets feel like a restart of a simplified game with a few new numbers.
- Stagnation: there are few active decisions once all managers are bought.
- Frequent balance changes that invalidate community spreadsheets.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Map the 10 businesses to Rider worlds: decreasing coefficient (1.15 down to 1.07) keeps late worlds affordable in bulk.
- Milestone doublings at 25/50/100 owned are a cheap, clear reward loop; show the next milestone on every card.
- Use a square-root prestige so players can see "angels pending" and decide between resetting now or later.
- Give each world a manager-like auto-unlock (a Rider ally) so the early manual phase ends quickly.
- Avoid planet-style parallel economies; they fragment the player base.
- Keep premium to time-skips and cosmetic Rider forms; avoid selling the prestige currency.
