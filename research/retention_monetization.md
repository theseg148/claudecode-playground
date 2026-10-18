# Retention, Session Benchmarks and Monetization in Idle Games

Scope: benchmarks and monetization patterns of idle/incremental games, and what they imply for a
no-fight, upgrade-based idle game themed on Kamen Rider Decade (fan project, likely free and non-commercial).

Tag legend (every claim carries one):
- [S] = sourced from a web search snippet; URL given. Source type noted (VENDOR = company that sells ads/analytics/UA services; FAN = wiki/forum; PRESS = trade press; AI-SUM = auto-generated review summary).
- [M] = from my memory/training knowledge, not verified in this session. Treat as unverified.
- [E] = my own estimate or inference.

Research constraints: only standard WebSearch snippets were available (no page fetches), so many numbers are
second-hand. Where a source was a vendor blog it is flagged. Nothing here was verified against a primary dataset.

---------------------------------------------------------------------------------------------------

## 1. Retention and session benchmarks

### 1.1 Retention (D1 / D7 / D30)

Idle/AFK genre figures:
- Idle/AFK games: D1 35-50%, D7 20-30%, D30 10-15%. [S] Playio genre table, https://blog.playio.co/retention-by-game-genre (VENDOR blog; underlying data not named).
- Juego Studio's table repeats the same idle ranges, so it is probably the same upstream data, not independent confirmation. [S] https://www.juegostudio.com/blog/how-to-increase-user-retention-and-increase-your-games-lifetime (VENDOR, dev-services studio blog).
- Playio claims idle titles often match or beat RPG-level numbers at D7 and D30. [S] https://blog.playio.co/retention-by-game-genre (VENDOR).
- Caution: ranges that wide and that round look like top-tier or aspirational values, not medians. [E]

All-mobile-game medians (context):
- Median D1 about 22% (top 10% about 40%); median D7 about 4% (top 10% about 12%); median D30 about 0.7% (top 10% about 4%). [S] GameAnalytics 2025 data as quoted in the investgame.net PDF, https://investgame.net/wp-content/uploads/2026/01/2026-01-20-Mobile_retention_benchmarks_2026.pdf (analytics VENDOR via a re-publisher).
- The genre-table D7/D30 for idle (20-30% / 10-15%) is 5x-20x the all-game medians; that gap is implausibly large for a like-for-like measure. Likely causes: different definitions (rolling vs strict), selection of successful titles, different data panels. [E]
- Rolling retention (returned on day N or later) reads higher than strict day-N retention; check the definition before comparing. [S] same investgame.net/GameAnalytics summary above.
- iOS top-quartile D1 31-33% vs Android 25-27%. [S] same summary.
- Rule of thumb that a good casual game targets D1 40 / D7 20 / D30 10 is widely repeated. [M] (VENDOR-blog folklore; no specific source recalled.)

Interpretation for a hobby project: you will not have analytics at scale. If you want any signal, a
local "days played" counter and optional opt-in feedback are the only realistic measures. [E]

### 1.2 Sessions per day and session length

- Idle gamers average about 5.3 sessions/day vs 4.6 for hyper-casual; average session about 8 minutes. [S] GameAnalytics, summarized at https://gameworldobserver.com/2020/12/22/gameanalytics-names-benchmark-engagement-metrics-idle-games (analytics VENDOR data, trade-press summary, 2020 dataset).
- Top 10% idle titles: 5.82 sessions/day, 7 min average session. Top 25%: 5.03 sessions/day, 6 min. [S] same GameAnalytics summary (https://wnhub.io/news/marketing/item-3203 carries the same story).
- Note the oddity: top performers have SHORTER sessions than the average (7 vs 8 min). The sources do not explain it. Plausible reading: the best idle games are checked often and briefly. [E]
- Implication: the dominant pattern is roughly 5 short check-ins per day, about 30-40 minutes total daily play. [E derived from S figures: 5.3 x 8 = about 42 min]
- One summary states a "stickiness" of 18% vs 10.5% for idle vs hyper-casual; sources conflict on stickiness and session-length ratios. [S] gameworldobserver / wnhub summaries above; treat as low-confidence.
- Idle Miner Tycoon and Egg Inc are designed around "check in, collect, spend, leave" loops; offline accumulation is the reason players return. [M]
- AFK Arena's daily quests are timed to push a second session per day; idle chest accumulation acts as an appointment mechanic. [S] https://www.gamedeveloper.com/design/flexible-time-session-design-in-afk-arena and https://www.deconstructoroffun.com/blog/2019/6/6/afk-arena-puts-lilith-into-the-billionaire-club (the latter is an industry-analysis blog by a consultancy that sells services, so semi-VENDOR).

### 1.3 Monetization metrics: ARPDAU, LTV

- Idle ARPDAU is reported as about 9x hyper-casual ARPDAU (ratio only, no dollar amount). [S] GameAnalytics via https://gameworldobserver.com/2020/12/22/gameanalytics-names-benchmark-engagement-metrics-idle-games (VENDOR data).
- Absolute ARPDAU/LTV: the searches returned no reliable dollar figures. From memory, hybrid-casual ARPDAU is commonly quoted in the range of a few cents to tens of cents, and idle RPGs higher. [M] unverified; for orientation only, do not cite.
- Typical ad-heavy idle game: ad revenue is the majority of income for the casual end (Idle Miner Tycoon-style), while idle-RPGs (AFK Arena class) are IAP/gacha dominated. [M]
- Users open on average 9.7 rewarded video ads per session in one ironSource-cited figure (undated, VENDOR). [S] summarized in the GameAnalytics/is.com search results (https://is.com/?p=58444). Sounds high; likely "per engaged user" or per day. [E]
- Pangle (ad network) claims its rewarded-video solution lifted Idle Miner Tycoon CPM by 12.65% and ARPDAU by 12.52%. [S] https://www.pangleglobal.com/resource/27816 (VENDOR case study; this is a claim about an ad network's own product).
- Scale reference: AFK Journey (AFK Arena successor) reported at about $110M revenue. [S] https://maf.ad/en/blog/afk-journey-analysis/ (VENDOR; UA agency blog).
- AFK Arena revenue/billion-dollar-club framing. [S] title of https://www.deconstructoroffun.com/blog/2019/6/6/afk-arena-puts-lilith-into-the-billionaire-club (snippet shows title only; number not read in this session).

### 1.4 Player attitudes to rewarded ads (survey evidence, all from ad vendors)

- Unity survey (2015, published 2016, 2000+ respondents): 71% preferred watching video ads as a way to "pay"; 62% engage with video ads for rewards regularly; 18% always, 44% sometimes, 16% rarely, 22% never. [S] https://gamesbeat.com/unity-the-majority-of-mobile-gamers-are-open-to-engaging-with-incentivized-video-ads/ and https://unity.com/en/news/new-industry-study-reveals-more-half-game-developers-identify-video-ads (VENDOR: Unity sells ads; dated).
- Tapjoy (2017, n=2,615 US): 79% prefer opt-in rewarded to pre-roll video; 75% "very likely" to watch a rewarded ad. [S] https://www.pocketgamer.biz/tapjoy-modern-mobile-gamer-report/ (VENDOR: Tapjoy sells rewarded ads; likely biased).
- Tapjoy 2022: rewarded video still top ad type, preferred by 53%. [S] same pocketgamer.biz result.
- Takeaway: the pro-ad numbers are all from ad sellers; they support "opt-in beats forced" but not the magnitude. [E]

---------------------------------------------------------------------------------------------------

## 2. Monetization models of top idle games

### 2.1 Idle Miner Tycoon (Kolibri Games)

- Rewarded video placements: (a) double the cash earned while away, offered on return; (b) a "Boost" button that doubles income for a time and stacks. [S] https://www.pangleglobal.com/resource/27816 (VENDOR case study).
- Premium currency: Super Cash, mostly bought with real money, some free via play; used for boosts and instant cash. [S] https://www.bluestacks.com/de/blog/game-guides/idle-miner-tycoon/idt-currency-guide-de.html (guide site, FAN-grade).
- Price anchoring example: a 12-hour x2 boost for about 144 Super Cash (about 0.85 EUR) vs a 1-hour x2 boost for one ad. [S] guide/blog result in the Idle Miner Tycoon search (lower reliability, not independently confirmed).
- Boosters, time-skip-style instant cash packs, and mine "managers" bought with currency are core. [M]
- Prestige-like "Super Cash from boosts" tie. [S] same Bluestacks guide.
- Player friction: reviews of similar ad-heavy idle apps complain of excessive pop-up frequency. [S] https://marlvel.ai/apps/idle-miner-tycoon-gold-digger (AI-SUM of reviews; directional only).
- Studio background: Kolibri was founded 2017 in a student flat, per the Pangle case study. [S] https://www.pangleglobal.com/resource/27816.

### 2.2 AdVenture Capitalist (Hyper Hippo)

- Two-tier premium currency: Gold (bought, some free) and MegaBucks (earned via events, ads, milestones, or bought). [S] https://en.wikipedia.org/wiki/AdVenture_Capitalist and https://adventure-capitalist.fandom.com/wiki/Mega_Tickets (Wikipedia + FAN wiki).
- Gold buys: angel investors without resetting, an instant "day of idle income", time warps. [S] https://apps.apple.com/us/app/-/id927006017 (official store listing) and the Wikipedia page above.
- Mega Tickets permanently boosted one business x7.77 (cost 20 Gold or 10 MegaBucks); a later update reportedly retired tickets and converted them to MegaBucks. [S] fandom wiki and App Store listing (they conflict on version; old numbers may be stale).
- Time warps: players discuss them as a time-saver that is a waste unless used well; some players cheat by moving the phone clock forward. [S] https://steamcommunity.com/app/346900/discussions/0/1639788130266895690 (FAN forum snippet). This shows that time-skips are cheap for players to defeat locally.
- Steam version also exists and is a paid/IAP hybrid. [M]

### 2.3 Egg, Inc. (Auxbrain)

- Premium currency: Golden Eggs, earnable in play or purchasable; they survive prestige. [S] https://en.wikipedia.org/wiki/Egg,_Inc. (Wikipedia).
- Rewarded videos plus a random "drone" that crosses the screen and drops cash or Golden Eggs when tapped. [S] Wikipedia above; a review says it "makes heavy use of rewarded video ads" but "players don't necessarily need to watch ads to get far", per https://childrenandmedia.org.au/app-reviews/apps/egg-inc (independent reviewer, not a vendor).
- Piggy Bank accumulates Golden Eggs as you progress and is bought out with real money; an "Ultra" bonus (25% Standard / 40% Pro) increases piggy fills. [S] https://egg-inc.fandom.com/wiki/Piggy_Bank (FAN wiki). This implies a paid tier, details unverified.
- Epic research (permanent boosts to Soul Egg bonus) is bought with Golden Eggs. [S] Wikipedia above. Note this means long-term prestige power can be bought, which is the usual flashpoint. [E]
- Egg Inc is widely praised as a gold standard for the genre by industry press. [S] https://www.pocketgamer.biz/egg-inc-idle-games-gold-standard/ (PRESS; title seen, body not read).
- Contracts / co-op events as a daily-return and social hook. [M]
- Revenue figures: not found. A London Design Festival page with "revenue" numbers labels them hypothetical, so discard. [S] result noted in the Egg Inc search.

### 2.4 Cookie Clicker (Steam)

- Paid once at $4.99 (some sources say $5 / 4.99 EUR); released 1 Sep 2021, eight years after the web game. [S] https://www.pcgamesn.com/cookie-clicker/steam , https://destructoid.com/?p=278544 , https://www.steamspy.com/app/1454400 (PRESS / stats site).
- Steam version removes web ads, adds 500+ achievements, cloud saves, Workshop mod support, new C418 soundtrack. [S] PCGamesN and Destructoid above.
- Orteil said the web version keeps getting updates first; both are meant to get the same development. [S] Destructoid above.
- No microtransactions seen in any result. [S] absence in the above; confirm on the Steam store page. [M] I also recall no IAP.
- The web version historically ran on ads and Patreon. [M]
- This is the clearest model for a one-time-purchase/zero-IAP idle game and it is among the most successful in the genre. [E]

### 2.5 Realm Grinder (Divine Games / Kongregate)

- Premium upgrades "Gifts" sold for Kreds (Kongregate currency) or Rubies; tiers 50 / 100 / 200 Kreds, mapped to $4.99 / $9.99 / $19.99 on Steam. Gifts are permanent and survive soft and hard resets. [S] https://realm-grinder.fandom.com/wiki/Shop (FAN wiki).
- Rubies: earned through monthly "Gift of the Faithful" login rewards; spent on, for example, an 8-Ruby time-skip boost. [S] same wiki.
- iOS listing says free-to-play with optional purchases. [S] https://apps.apple.com/app/id1110149506.
- Design approach: deep prestige/faction system, heavy buy-once permanent perks, no forced ads. [M]
- Community friction over paid permanent perks in a competitive-ish community. [M] unverified.

### 2.6 AFK Arena (Lilith Games)

- Idle RPG; monetization = character collection (gacha), idle rewards, a variety of store offers. [S] https://www.blog.udonis.co/mobile-marketing/mobile-games/afk-arena-analysis (UA/agency VENDOR blog; snippet-only).
- Idle chest as appointment mechanic; daily quests prompt a second session. [S] Deconstructor of Fun and Game Developer links in 1.2.
- Event/feature launches drove revenue steps (e.g. +23.7% WoW for Voyage of Wonders, iOS US 2019; +30% from Medal Rewards, 2021). [S] https://www.liquidandgrit.com/?p=9769 and https://liquidandgrit.com/?p=12296 (analyst reports, paywalled/partial).
- Over 100M downloads claimed. [S] Lilith press release at https://gamespress.westeu-v2.propressroom.com/ (publisher PR).
- VIP tiers and exact pricing: not found. [M] VIP levels and monthly pass style are standard in this class.
- This is combat-centric gacha, a different monetization class from the clicker/tycoon group above. [E]

### 2.7 Cross-cutting patterns

Summary of mechanisms across the six games:

| Mechanism | Idle Miner | AdCap | Egg Inc | Cookie Clicker Steam | Realm Grinder | AFK Arena |
|---|---|---|---|---|---|---|
| Rewarded ads | yes (x2 offline, boost) [S] | yes (MegaBucks) [S] | yes + drones [S] | none [S] | not primary [M] | some [M] |
| Premium currency | Super Cash [S] | Gold, MegaBucks [S] | Golden Eggs [S] | none [S] | Kreds, Rubies [S] | gems/diamonds [M] |
| Time-skip | cash packs [M] | time warps [S] | via GE [M] | none | Ruby boost [S] | quick-claim [M] |
| Permanent bought perks | partial [M] | tickets [S] | epic research [S] | none | Gifts [S] | gacha [S] |
| Upfront price | free | free | free | $4.99 [S] | free | free |

### 2.8 What players tolerate vs hate

Tolerated / liked:
- Opt-in rewarded ads where the reward is clearly valuable (x2 earnings, boosts). [S] https://marlvel.ai/apps/idle-streamer/reviews and sibling pages (AI-SUM of store reviews: players appreciate optional ads for boosts).
- A one-time purchase to remove ads is the most-requested item in several reviewed idle apps. [S] marlvel.ai review summaries above (AI-SUM, directional).
- Working offline progress is praised; missing or slow offline progress is a common complaint. [S] same.
- Games where you can "get far without ads". [S] https://childrenandmedia.org.au/app-reviews/apps/egg-inc.
- Premium currency that is also earnable in play. [S] Wikipedia Egg Inc.

Hated:
- Forced interstitials every few minutes, long (up to 2 min) ads, ads after basic actions such as opening inventory, ads still triggered after declining a boost. [S] https://marlvel.ai/apps/cash-inc-fame-fortune-game/reviews , /idle-apocalypse/reviews , /taps-to-riches/reviews (AI-SUM; directional, not counts).
- Aggressive monetization combined with slow late-game progression felt as pay-to-win. [S] marlvel.ai summary above.
- Cloud-save failures and total progress loss after reinstall. [S] marlvel.ai summaries, and fan-forum folklore. [M]
- Paid permanent power in prestige economies. [M]; [E] flashpoint.
- Caveat: AI-generated review summaries are the only "voice of player" evidence collected; I could not fetch Reddit or forum threads. Existing repo file research/player_complaints.md may hold stronger evidence. [E]

---------------------------------------------------------------------------------------------------

## 3. Ethics and regulation (brief)

Loot boxes / randomized purchases:
- Apple App Store requires odds disclosure for randomized paid items before purchase; Google Play adopted a similar rule in 2019. [S] https://www.pocketgamer.biz/app-store-now-requires-developers-to-list-loot-box-odds and https://www.pocketgamer.biz/google-play-developers-must-now-disclose-loot-box-odds (PRESS).
- Belgium's Gaming Commission classed loot boxes as gambling and called for a ban; Nintendo reportedly pulled Fire Emblem Heroes and Pocket Camp there. [S] fortune.com / thegamer.com results from the loot box query (PRESS, circa 2018-2019).
- Netherlands: Kansspelautoriteit took a hard line in 2018 and a court later partly reversed (Electronic Arts case, 2022). [M] unverified here; the search did not confirm.
- UK: Gambling Commission stance; the government's 2022 review favored industry self-regulation rather than legislation. [M] unverified.
- Relevance: an idle game with gacha pulls is regulated; a game with deterministic upgrades is not. [E]

Kids and consumer protection:
- FTC v Epic (Fortnite), Dec 2022: $275M COPPA penalty plus $245M refunds over dark-pattern purchases. [S] https://www.deseret.com/u-s-world/2022/12/19/23516939/fortnite-privacy-case-ftc-fine/ and the Fenwick analysis https://fenwick.com/insights/publications/ftcs-aggressive-enforcement-of-childrens-privacy-and-dark-patterns-a-cautionary-tale-and-simple-steps-companies-can-take-to-reduce-risk (law firm commentary).
- FTC complaint against HoYoverse alleged confusing virtual currency and deceptive odds. [S] same Fenwick/FTC results.
- COPPA: verifiable parental consent before collecting personal data from under-13s. [S] FTC results (https://www.ftc.gov/node/80135).
- CARU guidelines revised for in-app ads and purchase options aimed at children. [S] https://bbbprograms.org/media/insights/blog/in-app-and-in-game-ads-compliance-2022 (self-regulatory body).
- Advocates (Fairplay) asked the FTC to restrict microtransactions and virtual currency in kids' apps. [S] https://fairplayforkids.org/?p=27097.
- Nothing specific on rewarded ads in kids' games was found. [S] absence of results.
- Ethical framing: Kamen Rider's audience skews young; any monetization would sit near child-directed territory. A free, ad-free, no-account game avoids nearly all of this. [E]

Rights-holder risk (relevant to a fan project):
- Nintendo's mass DMCA on Game Jolt covered 562 fan games; some reporting says site ad revenue was cited. Sega is described as supportive of fan projects. [S] https://www.nintendolife.com/news/2021/01/nintendo_issues_mass_dmca_takedown_379_fan-made_games_forcibly_removed , https://techraptor.net/content/nintendo-game-jolt-dmca , https://gamesbeat.com/?p=127347.
- No result covered Toei/Kamen Rider fan-game policy specifically. [S] absence. Toei and Ishimori Productions are known as protective of the franchise. [M] unverified.
- Monetizing Toei IP is the single biggest legal risk in this project. [E]

---------------------------------------------------------------------------------------------------

## 4. Implications for a no-fight Kamen Rider Decade idle upgrade game

Assumptions: fan project, free, non-commercial, likely a static web page or small app, solo or small team,
no analytics backend. [E]

### 4.1 Monetization stance

1. Ship with zero monetization: no ads, no premium currency, no IAP, no donation button inside the game. Reasons: IP exposure (Nintendo/Game Jolt example shows ad revenue being cited) [S/E], kids-law exposure avoided [E], and Cookie Clicker Steam proves a clean, no-IAP model can anchor a genre leader [S]. 
2. If any support channel is wanted, keep it off the game page (e.g. a link on the author's profile) and do not sell Rider content, Decade-themed items, or any boosts. [E] Not legal advice. [E]
3. If the project is ever made commercial, it needs a license or full re-skin to original IP. [E]

### 4.2 Use the monetization mechanics as design inspiration without the money

The genre's monetization hooks map to free design features, which makes the game feel "complete" to idle-game fans:
- "Watch an ad for x2" -> a free earnable "Rider Card" or "Ride Booster" boost on cooldown (e.g. x2 for 10 minutes, once per real hour), obtained by a simple tap-and-hold action. [E]
- Offline x2 on return -> free "welcome back" bonus window (Idle Miner pattern [S]) with no ad. [E]
- Premium currency -> a single soft "Kamen Ride" token earned via play, not purchasable; Egg Inc shows premium currency can be earnable and survive prestige [S].
- Time-skip -> a rare earned item that fast-forwards N hours; AdCap time warps and Realm Grinder Ruby boost show demand [S]. Since local time-skipping by changing the clock is common [S], treat the clock as untrusted and cap offline gains, or just accept it in a single-player game. [E]
- Prestige/permanent perks -> keep them earned, never bought, avoiding the Realm Grinder / Egg Inc epic research controversy [M/E].

### 4.3 Retention and session design (from 1.x)

- Target pattern of about 5 short sessions/day at 6-8 minutes [S/E]: design each session around one decision cluster (spend currency, pick a form/ride, claim a reward) that finishes in under 5 minutes. [E]
- Appointment mechanics: a Decade-themed "dimension travel" daily rotation (a different Rider world each day, per research/decade_worlds.md) gives a return reason without punishing absence (AFK Arena chest + daily quests pattern [S]). [E]
- Avoid hard streak penalties: no losing progress for missed days. Kids and casual fans will miss days. [E]
- Offline progress must work and be generous; it is both the top praised feature and top complaint when absent [S].
- Reliable saving: export/import save string plus local autosave; cloud-save loss is a recurring complaint [S]. For a static fan site, a copy-paste save code is the cheapest fix. [E]
- Without an accounts backend, retention can only be measured by the author via opt-in feedback; set qualitative goals (e.g. "a fan can finish the first dimension in one 8-minute session") rather than D1/D7/D30 targets. [E]

### 4.4 Theme-specific suggestions that serve engagement without fights

- Collection loops fit Decade's Kamen Ride cards (the form roster as the "generators"): each Rider form is an upgrade tier; unlocking is deterministic, no gacha, which sidesteps loot-box rules entirely. [S for regulation / E for design]
- Deterministic unlock order with visible costs, so there is no "odds" disclosure issue. [S for rules] / [E]
- Light random events (e.g. a drone-like "Dimensional Rift" appearing on screen, reward for tapping) mimic Egg Inc's drones [S] while remaining free and non-gambling. [E]
- Keep numbers exciting but readable: prestige around the first 2-3 hours so a first-time player experiences a reset quickly (common idle practice). [M]

### 4.5 Risks and open questions

- Benchmarks are mostly vendor-sourced, old (2020 GameAnalytics session data) and not for hobby/web games; do not use them as pass/fail targets. [E]
- Not verified: Egg Inc revenue/Ultra details, AFK Arena VIP and revenue, Netherlands/UK current law, Toei fan-policy. Each needs a primary-source check before being relied on. [E]
- Voice-of-player evidence here is AI-summarized store reviews; check research/player_complaints.md for stronger material. [E]
- A secondary "ad-free by design" story is itself a differentiator: ad removal is the top request across reviewed idle apps [S]. [E]

---------------------------------------------------------------------------------------------------

## 5. Source index (URLs seen in search results)

Retention / sessions:
- https://blog.playio.co/retention-by-game-genre (VENDOR)
- https://www.juegostudio.com/blog/how-to-increase-user-retention-and-increase-your-games-lifetime (VENDOR)
- https://investgame.net/wp-content/uploads/2026/01/2026-01-20-Mobile_retention_benchmarks_2026.pdf (GameAnalytics data, republished)
- https://gameworldobserver.com/2020/12/22/gameanalytics-names-benchmark-engagement-metrics-idle-games (PRESS on VENDOR data)
- https://wnhub.io/news/marketing/item-3203 (PRESS)
- https://www.gameanalytics.com/blog/how-to-keep-players-engaged-and-coming-back-to-your-idle-game (VENDOR)
- https://www.gamedeveloper.com/design/flexible-time-session-design-in-afk-arena
- https://www.deconstructoroffun.com/blog/2019/6/6/afk-arena-puts-lilith-into-the-billionaire-club

Monetization:
- https://www.pangleglobal.com/resource/27816 (VENDOR)
- https://www.bluestacks.com/de/blog/game-guides/idle-miner-tycoon/idt-currency-guide-de.html
- https://en.wikipedia.org/wiki/AdVenture_Capitalist
- https://adventure-capitalist.fandom.com/wiki/Mega_Tickets
- https://steamcommunity.com/app/346900/discussions/0/1639788130266895690
- https://en.wikipedia.org/wiki/Egg,_Inc.
- https://childrenandmedia.org.au/app-reviews/apps/egg-inc
- https://egg-inc.fandom.com/wiki/Piggy_Bank
- https://www.pocketgamer.biz/egg-inc-idle-games-gold-standard/
- https://www.pcgamesn.com/cookie-clicker/steam
- https://destructoid.com/?p=278544
- https://www.steamspy.com/app/1454400
- https://realm-grinder.fandom.com/wiki/Shop
- https://www.blog.udonis.co/mobile-marketing/mobile-games/afk-arena-analysis (VENDOR)
- https://maf.ad/en/blog/afk-journey-analysis/ (VENDOR)
- https://www.liquidandgrit.com/?p=9769 , https://liquidandgrit.com/?p=12296
- https://gamesbeat.com/unity-the-majority-of-mobile-gamers-are-open-to-engaging-with-incentivized-video-ads/ (VENDOR survey)
- https://www.pocketgamer.biz/tapjoy-modern-mobile-gamer-report/ (VENDOR survey)
- https://marlvel.ai/apps/idle-streamer/reviews and sibling pages (AI-SUM)

Regulation / ethics:
- https://www.pocketgamer.biz/app-store-now-requires-developers-to-list-loot-box-odds
- https://www.pocketgamer.biz/google-play-developers-must-now-disclose-loot-box-odds
- https://www.deseret.com/u-s-world/2022/12/19/23516939/fortnite-privacy-case-ftc-fine/
- https://fenwick.com/insights/publications/ftcs-aggressive-enforcement-of-childrens-privacy-and-dark-patterns-a-cautionary-tale-and-simple-steps-companies-can-take-to-reduce-risk
- https://bbbprograms.org/media/insights/blog/in-app-and-in-game-ads-compliance-2022
- https://fairplayforkids.org/?p=27097
- https://www.nintendolife.com/news/2021/01/nintendo_issues_mass_dmca_takedown_379_fan-made_games_forcibly_removed
- https://techraptor.net/content/nintendo-game-jolt-dmca
