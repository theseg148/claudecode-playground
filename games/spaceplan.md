# Spaceplan
**Sources:** (URLs, required)
VERIFICATION UPDATE 2026-10-18: developer/publisher, release date, price, premise, content counts, review share now [S] (see Verification log at bottom). Formulas, offline and prestige details remain unverified [EST]/[MEM]. Anything tagged [S] was read only as a web-search snippet (no page fetch available).
CONFIDENCE WARNING: sandbox network only reached raw.githubusercontent.com; no Spaceplan page could be fetched. All content below is [MEM] (recalled, unverified) or [EST]. Verify at the URLs before quoting numbers.
- https://store.steampowered.com/app/616110/SPACEPLAN/ (Steam; app id 616110 appeared in search results; page text only seen through search snippets) [S]
- https://www.cosmocover.com/newsroom/spaceplan-launches-on-app-store-google-play-and-steam/ (press release, via search snippet) [S]
- https://toucharcade.com/2017/05/08/spaceplan-review-delicious-potatoes/ (review, via search snippet) [S]
- (earlier guesses jhollands.itch.io and spaceplan.fandom.com are unverified; the old Steam id 1051770 was WRONG)

## Core loop
- Narrative incremental by Jake Hollands, published by Devolver Digital [S: cosmocover press release snippet]. You are a ship AI/pilot stranded after a failed escape; you click to produce Energy and unlock increasingly absurd tech.
- Click an energy source -> buy generators -> unlock research that auto-completes -> new "worlds" and story beats. Dialogue is sarcastic, with a computer voice commenting.
- Each story beat unlocks a new currency or building category: Energy -> Matter -> Planets/solar systems -> strange late-game systems (time, universe-scale building).
- Finite: the game has a clear ending after roughly 2-4 hours. [MEM/EST]

## Resource types
- Energy (initial click resource), Matter, Science/Data, Information, Dimensions, time-like resources late; also story "logs" and "directives". [MEM]
- Resource count is intentionally small at any one time (2-4 visible), not a complex economy. [EST]

## Cost & production growth formulas (public or estimated; mark which)
- No public formulas found. Estimates based on standard incremental structure:
  - Generator cost = base * 1.15^owned (typical genre default; the Game Developer "math of idle games" series recommends 1.07-1.15 for coefficients). [EST]
  - Production per generator multiplied by upgrade tiers (x2, x3... at owned thresholds like 10/25/50/100). [EST]
  - Story gates: some buildings are locked behind narrative events, not cost. [MEM]
- Total content is bounded so exponents rarely exceed e20-e30 before the finale. [EST]

## Prestige structure
- No prestige. One continuous run to an ending; replays are voluntary. [MEM]
- The game compensates with a final twist (the larger "plan" of the title) delivering the reveal. [MEM]

## Unlock pacing
- [EST] First 10 minutes: manual clicking and 2-3 unlocks; by 30 min: first big narrative reveal; by 1 hour: automation dominant; final 30-60 min mostly watching and reading.
- Every 3-10 minutes a new item/dialogue appears, which is the central tuning principle (always something new). [EST]

## Offline progress
- [MEM] The mobile/Steam versions give some offline income when closed; browser version has less. Exact formula unknown. [EST: capped, modest ratio like 50% rate]
- Since the game is story-driven, offline tends to be "wait for the next beat" rather than a big payout.

## Monetization effects
- Paid game on Steam/mobile (premium one-time price, roughly low single-digit dollars) with a free web demo/earlier version. [MEM/EST]
- No energy timers or ad walls. Story content is the product.

## What players love
- Humour and voice; the incremental is a vehicle for writing.
- Short and finished: players value an incremental that has an ending.
- Gentle difficulty, always something to click, no grinding walls.
- Pacing that matches a movie: setup, escalation, twist.

## What players hate
- Some report it feels too short and shallow for experienced incremental fans. [EST]
- Little replay value; no prestige or challenge layer.
- Late game becomes passive and loses the clicker interactivity. [MEM]

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. A narrator voice that reacts to each unlock gives a no-fight game personality. Decade's cheeky "passing-through photographer" tone fits (Tsukasa quips).
2. Cap visible resources at 2-4 at a time; add a new one per world, retire old ones into passive background.
3. Pace content in beats: a new thing every 3-10 minutes in the first hour, then stretch to 20-60 minutes per beat.
4. A finite campaign with a real ending is a legitimate product shape; Decade's "Rider worlds" can be chapters 1-10 with a finale, and prestige is a bonus mode after the credits.
5. Gate by narrative rather than cost in places: some unlocks trigger on a story event, which lets you control exact pacing.
6. Keep click interaction meaningful early (the first minutes) then transition to automation as a deliberate "ah, it's running by itself" story moment.
7. Because premium pricing works for a short narrative idle, don't force ad/energy monetization; consider one-time purchase or cosmetic DLC.
8. Offline: modest and capped is enough for a story pacing game; payouts should never skip the narrative.

## Verification log (2026-10-18)
Method: WebSearch snippets only (Steam/wiki pages not directly fetchable); no source code exists publicly that I could find.
Confirmed [S]:
- Developer Jake Hollands, publisher Devolver Digital; mobile + Steam launch 2017-05-04; Steam price EUR 2.99. https://www.cosmocover.com/newsroom/spaceplan-launches-on-app-store-google-play-and-steam/ , https://cosmocover.com/newsroom/spaceplan-set-to-unlock-the-mysteries-of-the-galaxy-via-potatoes-on-may-4
- Started as a web-based clicker prototype (MetaFilter, Aug 2016: https://metafilter.com/161529/maris-pipers ; press materials above).
- Official blurb: manual clicks plus passage of time create and launch potato-based devices and probes from a satellite orbiting a planet; "fifteen starchy items" to unlock; five planets across two realities; described as a "life-affirming, silly story". https://store.steampowered.com/app/616110/SPACEPLAN/ (via snippets)
- Steam app id is 616110 (earlier id 1051770 in this file was wrong). Reviews ~3,300, ~91% positive (gg.deals snippet, https://gg.deals/gb/game/spaceplan/).
- Story length: a store listing gives ~6 h 3 min for the main story (HowLongToBeat-style figure from a search snippet; source page not identified). The earlier "2-4 hours" is therefore likely too low [EST->contradicted].
- Early game: KinetGen click generator; Thing Maker items such as Repair Solar Cell (one example cost 26 power in an early 2016 build) and Potato raise power. https://wbgsv0a.gigazine.net/gsc_news/en/20160816-spaceplan-review (snippet; old build).
- No in-app purchases or ads (German press, appgefahren.de snippet). Premium one-time price matches the "Monetization" section.
- Google Play listing last updated 2025-12-05 (balance may have changed since old guides).
Still unverified: all cost/growth formulas (1.15^n is only a genre default), offline-income rules and ratio, resource names beyond Energy/watts, the claim 'Matter/Dimensions' resources, and the 'sarcastic computer voice' detail beyond the generic 'silly story'. "No prestige" is consistent with every description seen but not explicitly confirmed.
