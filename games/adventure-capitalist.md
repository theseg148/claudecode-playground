# Adventure Capitalist
> Verification pass 2026-10-18 (WebSearch snippets only; pages not opened). [S] = confirmed in a search snippet with the URL given; [unverified] = not confirmed, treat as a design placeholder. See "Verification log" at the bottom.
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

- Cost of the n-th purchase: cost(n) = base * coeff^n [S https://adventure-capitalist.fandom.com/wiki/Businesses]. Confirmed rows: Newspaper Delivery base 60, coeff 1.15; Car Wash base 720, coeff 1.14 (second one costs 829.92); Pizza Delivery base 8,640, coeff 1.13. The wiki's note implies about 1.07 for the cheapest business (snippet ambiguous). The coefficient falls as tiers rise, so the '1.15 to 1.07' range is plausible but other rows are [unverified].
- Revenue per cycle is owned * base_revenue * multipliers. [recall]
- Milestone speed-ups [S https://adventure-capitalist.fandom.com/wiki/Businesses]: cycle time is halved at 25, 50, 100, 200, 300 and 400 owned per business, and again at the same marks owned across all businesses; at most 12 halvings (1/4096 of the start time). A forum post cites an x3 profit unlock at 100; x4 and 500+ milestones were not found [unverified].
- Manager costs ($1,000 Lemonade to ~$100B Oil, 10-15x steps) were not found in any source [unverified].
- Angel Investors on reset: community formula angels = floor(150 * sqrt(lifetime_earnings / 1e15)) minus angels owned. Not seen stated directly; a Steam post quoting the wiki lists lifetime-earnings thresholds of 44.444B, 177.78B and 400B for the first three angels [S https://steamcommunity.com/app/346900/discussions/0/364039531219683031], which match this formula (my own arithmetic). Treat as consistent, not directly confirmed.
- Each Angel Investor gives +2% to all profit by default, boosted by upgrades; the bonus applies to the base rate so it matters less with many angels [S Steam threads, e.g. https://steamcommunity.com/app/346900/discussions/0/364039785169128886]. Sacrificing angels for a large multiplier (x3 etc.) only pays off past a break-even (one calculation ~250,000 angels). Spent angels are lost on reset.
- Because of the square-root, 4x lifetime earnings gives 2x angels. [follows from the formula above]

## Prestige structure
- "Claim Angel Investors" resets cash, businesses and managers, and keeps the angels, gold and upgrades.
- Typical optimum is to reset when pending angels exceed about 100% of current angels (estimate; community rule of thumb).
- Each planet has its own prestige, with unlock of the next planet via the previous planet's angel total.
- Angel upgrades (cost in angels) give permanent multipliers and cheaper managers, and some unlock "all businesses x3" style boosts.

## Unlock pacing
- Lemonade stand is available immediately; Newspaper after around 1 minute.
- All Earth businesses are reachable in 1 to 3 hours of the first run. [unverified]
- First Angel Investors about 1 to 2 hours in; the Moon after you have enough angels (approx. 1e12 total angels in community play-through, estimate).
- Mars opens after the Moon's progress and is aimed at multi-week players. [unverified]

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

## Verification log

Confirmed [S]:
- Cost coefficients and base costs for Newspaper (1.15, 60), Car Wash (1.14, 720), Pizza (1.13, 8,640); halving milestones at 25/50/100/200/300/400 with 12 max halvings; +2% per angel; first-three-angel thresholds consistent with the 150*sqrt(L/1e15) formula.
Unconfirmed [unverified]:
- Lemonade/Donut/others coefficient rows, manager costs, x3/x4 milestone details beyond a forum mention, exact angel formula text, Earth/Moon/Mars pacing, offline behavior.
