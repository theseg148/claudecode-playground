# Guava Juice (Tub Tapper) - the YouTuber's idle/mobile game
**Sources:** (Very little public information was found. [S] = search snippet, [E] = estimate. WebFetch was DNS-blocked, so no page was read in full.)
- https://en.wikipedia.org/wiki/Guava_Juice (Roi Fabito, Filipino-American YouTuber; Guava Toys, album, animated show) [S]
- https://www.tubefilter.com/2018/05/24/influencers-mobile-games-guava-juice-tub-tapper/ (trade press on influencer games; names the game) [S - title only, article body not read]
- https://archive.advertisingweek.com/events/ny/2018/speakers/?id=11105 (his bio: game got 120K+ downloads in week 1, #3 in App Store Simulation, peaked #26 overall free apps) [S, self-reported]
- https://www.moregameslike.com/guava-juice-tub-tapper/steam/ (third-party listing: adventure/idle clicker; build bathtubs to boost bubbles, coins unlock upgrades, mini-games Pop Bubbles and Blowup Bath Bombs) [S]
- https://businessinsider.nl/roi-fabito-on-his-guava-juice-youtube-channel-merch-business-2020-2/ (business context) [S]

## Update 2026-10-18 (deeper search)
- Tubefilter 2018-05-24 [S, snippet]: Studio 71 (media co. repping ~1,300 influencers) launched Guava Juice: Tub Tapper (~May 2018) as a mobile title built on Roi Fabito; framed against Kim Kardashian: Hollywood (~$200M reported gross). Gameplay described: tap as many on-screen bubbles as possible, build and automate bathtubs, quick-play challenges. #3 App Store Simulation and #26 overall free in week 1 per Studio 71. https://www.tubefilter.com/2018/05/24/influencers-mobile-games-guava-juice-tub-tapper/
- Third-party listing [S, low reliability, contains unrelated text]: hundreds of bathtubs, Endless Upgrades, Show off your Swag, Forty Costumes, Unique Power-ups, genres Adventure/Idle Clicker. https://www.moregameslike.com/guava-juice-tub-tapper/steam/
- Publisher: a search suggested PopReach (Toronto) published it, but no source ties PopReach to the game; UNVERIFIED, do not cite.
- Not found by any search: App Store / Google Play text, review text, YouTube video coverage, ad/IAP structure, current availability (likely delisted; unknown). Searches for the exact title return unrelated Tapper games.

## Which game is it
- "Guava Juice" is Roi Fabito's YouTube channel. The game identified is **Guava Juice: Tub Tapper**, a mobile idle/clicker, launched around May 2018 [S]. Launched by Studio 71 per Tubefilter [S]; actual developer/publisher still UNVERIFIED. Other games with similar names (e.g. "Guava Juice R2" on itch.io) appear unrelated.

## Core loop
- Tap the bathtub to produce bubbles -> earn coins -> buy upgrades and additional tubs ("building bathtubs to boost bubbles") -> unlock "crazy upgrades" themed on the channel [S]. Mini-games interrupt the loop: Pop Bubbles and Blowup Bath Bombs [S].

## Resource types
- Bubbles (production), coins (soft currency) [S]. Presumably a premium gem/currency and ad-boost tokens, typical for the genre [E - not confirmed].

## Cost & production growth formulas
- No public formulas. Genre-typical estimate [E]: tub cost `base * 1.15^n`, tap value linear in level, with x2 milestone multipliers. Do not rely on these.

## Prestige structure
- Unknown/not documented. Possibly none or a simple reset [E].

## Unlock pacing
- Unknown. Launch metrics: 120K downloads in first week, #3 in Simulation, #26 overall free [S, self-reported], suggesting a heavy YouTube-driven burst; no data on retention.

## Offline progress
- Unknown; most tapper idle games provide capped offline earnings [E].

## Monetization effects
- Unknown details. Free mobile app, presumably ads and IAP; publisher-influencer model discussed by trade press [S, title only]. Fabito also has merchandise (Guava Toys) so the game doubled as brand marketing [S].

## What players love
- Not enough public review text found. Inferred from listings: character/brand fan service, silly bath-themed upgrades, quick mini-games [S/E].

## What players hate
- Not documented. Typical influencer-game risks: shallow depth, ad-heavy [E].

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
1. Licensed/fandom idle games can chart on brand alone but depth is what retains - so do better than a tap-and-upgrade shell.
2. Break the loop with short mini-games (Pop Bubbles, Bath Bombs) - small themed interludes suit Rider "Kamen Ride" card moments.
3. Silly themed upgrade names carry personality; give each Rider world a themed upgrade set.
4. Document public design: with this game little is public, so assume no reliable benchmark data; use other files in this folder for numbers.
5. Verify the game's developer/store pages directly before citing (this file's gaps are real).

## Verification log
- 2026-10-18, WebSearch snippets only. Confirmed: Studio 71 launch, May 2018, bubble tapping + automating bathtubs, chart ranks (self/Studio-71 reported). Not confirmed: PopReach, formulas, prestige, offline, monetization, reviews, YouTube coverage. All genre-typical numbers above stay [E].

## Update (08:5x) — gameplay snippets (search snippet only, not a fetched page)
Source: https://www.levelwinner.com/?p=15323 (guide; snippet via WebSearch, 2026-10-18) and https://www.moregameslike.com/guava-juice-tub-tapper/steam/ (listing). [S, snippet]
- Idle clicker (Android/iOS): tap, build and automate bathtubs to earn money; coins collected unlock upgrades; "bubble billionaire" goal; >100 bathtub types, >40 costumes, Pop Bubbles mini-game. [S]
- **Per-tub upgrade levels with milestone bonuses at levels 5, 10, 25, 50, 100, 200, 300, 400, 500, 700, 1000** — an AdCap-style milestone ladder; the guide advises spreading upgrades across tubs rather than maxing one, and rushing **collection automation, which unlocks at level 50**. [S, one guide; not confirmed in-game]
- No reliable information found on prestige, offline caps, formulas or monetisation numbers; the itch.io tip about "maxing tubes" may refer to another game.
Implications for the Decade game: the user's inspiration likely uses (a) many "tubs" (generators) with per-tub levels, (b) milestone bonuses spaced roughly ×2 apart (5→10→25→50→100→200→…→1000), (c) automation as a milestone reward — consistent with DESIGN_RULES R3/R10/R21; adopt the longer ladder (…300/400/500/700/1000) for late tiers so a world's top tier keeps giving goals (R25), and give "collection automation" as a milestone reward (not a purchase).
