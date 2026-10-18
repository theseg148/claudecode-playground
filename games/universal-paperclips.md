# Universal Paperclips
**Sources:** (WebFetch was blocked by DNS errors in this session; only WebSearch snippets were readable. Tags: [S] = seen in a search snippet from the URL listed, [M] = recalled from memory of the game's public JS/wiki and NOT re-verified, [E] = my estimate.)
- https://en.wikipedia.org/wiki/Universal_Paperclips (design: Frank Lantz, 2017, exponential growth plateaus that force investment in the next phase) [S]
- https://universalpaperclips.fandom.com/wiki/Trust (Trust milestones start at 2000 clips, later ones follow Fibonacci) [S]
- https://universalpaperclips.fandom.com/wiki/WireBuyer (costs 7,000 ops, appears after 15,000 inches of wire bought) [S]
- https://universalpaperclips.fandom.com/wiki/MegaClippers (unlock after 75 AutoClippers) [S]
- https://universalpaperclips.fandom.com/wiki/Ops (ops caps per phase) [S]
- Game itself ships unobfuscated JS (decisionproblem.com/paperclips/) - the formulas below tagged [M] come from reading it; re-verify there.

## Core loop
- Phase 1: click "Make Paperclip" -> sell via price/demand -> buy wire -> buy AutoClippers -> buy Marketing -> raise Trust via milestones -> spend Trust on Processors/Memory -> Ops fund Projects.
- Two interlocking currencies: money (wire, clippers, ads) and Ops/Creativity (projects). Player tunes price: demand falls as price rises, so there is an optimum price slider.
- Phase 2 (after "Release the HypnoDrones"-style takeover): Earth matter is converted; you manage Swarm Computing, Quantum computing, factories, harvester/wire drones, power farms.
- Phase 3: Space - Von Neumann probes, speed/exploration/replication/hazard-remediation/combat sliders and Yomi (strategic tournaments), until all matter is paperclips.
- The "game" is mostly a chain of projects that each unlock the next economy; there are no player-facing prestiges within a run.

## Resource types
- Paperclips (score), Funds ($), Wire (inches), Ops (processors x memory cap), Creativity (grows at max ops), Trust (non-spendable-except on processors/memory), Yomi (tournaments), Honor, Clips-per-sec, Matter (Earth/space), Power, Drones, Probes.
- Ops cap = memory x 1000 [M]. Phase gates on max ops from search: 70,000 / 120,000 / 150,000 / 200,000 for the four project tiers [S - interpretation unclear; the snippet labels them "Phase 1-4"].

## Cost & production growth formulas
- AutoClipper cost [M]: `1.07^level + 5` dollars (roughly; starts ~$5, so slow exponential). Production per clipper = 1 clip/sec x multipliers.
- MegaClipper cost [M]: `1.07^level * 1000`; each MegaClipper = 500 AutoClippers of output. Only unlocked after 75 AutoClippers [S].
- Wire: 1000-inch spool, price does a random walk around ~$15-30 [M]; WireBuyer automates for 7,000 ops [S].
- Marketing level n cost [M]: approx doubles each level (~`100 * 2^(n-1)`); each level multiplies demand by 1.1 [E on exact constants].
- Demand: `0.8 * marketing_mult * 1.1^(marketing-1) * 1.1^... / price_factor` - effectively linear-falling in price; optimum price found by hand [M, vague].
- Trust: +1 at 2000 clips, then Fibonacci-spaced clip thresholds [S]; +1 per project, etc.
- Space phase costs are huge fixed-number multiples (factories ~ 100M clips, probes 1e? ) [E - not verified].

## Prestige structure
- None within a run. The game ends when matter is exhausted. On completion the player may start over ("Universe Next Door" / Universe -1) with a small carried bonus [M]; no real meta-currency. Total clip count at end ~3.0e55 [M, likely 30 septendecillion clips].

## Unlock pacing
- Minute 0: clip button. ~1-3 min: first wire + AutoClipper. ~5-10 min: Marketing, first Trust and Processor. ~30-60 min: Creativity, first big projects, WireBuyer (needs 15k inches purchased [S]).
- Phase 1 ends ~2-3 hr (money ~ $ millions); Phase 2 and 3 push the total typical clear to ~6-10 hours of real play [E - community reports vary; mark estimate].
- Projects appear when Ops/Trust/clip thresholds are met; constant "ding" of new thing every few minutes.

## Offline progress
- None in the base browser version: the page must stay open (tab throttling slows it). Mobile ports vary. Design implication: Ops accrue only while open.

## Monetization effects
- Free browser game (no monetization) by Frank Lantz (NYU Game Center). Paid mobile/iOS ports exist [M]. Zero pay-to-win - the game is a case study in "narrative-first incremental".

## What players love
- Strong narrative arc with horror: ever-escalating scope from desk to universe; surprise phase changes.
- Every few minutes a new mechanic; no filler waiting; player-tuned price/slider mini-decisions; Yomi strategy tournaments; ending with a real "oh no".
- Short, finite (~8 hours), completable.

## What players hate
- Quantum Computing chip waiting (Phase 2 busywork, clicking for chips in time windows).
- Phase 3 Drift/Combat tuning is opaque; no offline play; Trust/Honor grind in space.
- Wire price random-walk frustration early.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Treat each Rider world as a "stage" that swaps the core verb (like clips -> drones -> probes) and recontextualises earlier upgrades.
2. Gate with milestone ("Trust"-like) thresholds on Fibonacci-ish totals rather than timers.
3. Make a new mini-decision every few minutes (slider/price analogue = Ride-Booker/form-selection) to avoid pure waiting.
4. Finite 8-10 hr arc with a satisfying world-collapse finale suits Decade (destroyer-of-worlds) theme.
5. Exponential cost `base*1.07^n`-style curves for first-tier buyers, with a 500x "Mega" tier unlocked after n=75, is a neat pattern for "Final Form Ride" bulk upgrades.
6. Keep an automation unlock (WireBuyer-like, 7k ops) as a priced milestone: automation = reward.
