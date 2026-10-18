# Player Complaints in Idle / Incremental Games: Why Players Quit

Method and honesty note. Direct page fetches (reddit.com, steam, wikipedia, dev blogs) were blocked by the sandbox proxy, so evidence comes from web-search result snippets and a few mirrors (libreddit mirror of r/incremental_games, review-aggregator sites). Reddit/App Store/Steam pages could not be opened first-hand. Where a quote appears it is as relayed in the search snippet; confirm on the live page before publishing.

- **Frequency estimates** below are *qualitative, my judgment* from the number and consistency of independent sources seen (N is small: ~25 sources). They are NOT survey statistics. Scale: VERY COMMON / COMMON / OCCASIONAL / RARE (within sources found).
- Source reliability tags: **[forum]** player posts, **[review-agg]** AI/aggregated review summaries (directional only), **[dev]** designer blog, **[acad]** peer reviewed.

---

## 0. Source inventory

| Source | Type | URL |
|---|---|---|
| r/incremental_games "What makes an idle game fun" (Aug 2024) via mirror | forum | https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhn00vj/?context=3 (also .../lhsya5e/, .../lhpz8fk/, .../lhm1s2n/) |
| r/incremental_games weekly "what are you playing" | forum | https://libreddit.neb.cx/r/incremental_games/comments/1eq66zt/what_games_are_you_playing_this_week_game |
| Hacker News thread on incremental games (via Brian Lovin mirror) | forum | https://brianlovin.com/hn/29633599 |
| AV Club "Confessions of an idle gamer" | article | https://avclub.com/confessions-of-an-idle-gamer-1832949532 |
| MetaFilter "The unclicked life is not worth living" (New Yorker discussion) | forum | https://www.metafilter.com/180147/The-unclicked-life-is-not-worth-living-So-crates |
| itch.io dev forum threads on idle design | forum | https://itch.io/post/4371860 , https://itch.io/post/15130204 , https://itch.io/post/15658446 , https://itch.io/post/8671617 |
| Steam community: Cookie Clicker offline-progress thread | forum | https://steamcommunity.com/app/1454400/discussions/0/3801649759600004600 |
| Steam review summaries (NGU Idle etc.) | review-agg | https://vaporlens.app/app/1147690/ngu_idle , https://vaporlens.app/app/3702540/between_adventures_idle , https://vaporlens.app/app/4619420/slot_grind , https://vaporlens.app/app/3959050/siegeturtle/stats/details , https://vaporlens.app/app/1535560/farmer_against_potatoes_idle |
| Mobile idle review summaries | review-agg | https://marlvel.ai/apps/idle-streamer/reviews , https://marlvel.ai/apps/idle-harbor-tycoon-sea-docks/reviews , https://marlvel.ai/apps/idle-coffee-shop-tycoon-game/reviews , https://marlvel.ai/apps/donuts-franchise-idle/reviews |
| Idle/gacha legitimacy comparison | blog | https://unstar.app/blog/is-divine-magic-goddess-legend-mushroom-watcher-realms-hero-wars-idle-heroes-gacha-games-legit-2026 |
| "I built 7 idle games in 30 days" | dev | https://dev.to/aguier/i-built-7-idle-games-in-30-days-what-i-learned-about-incremental-design-5d3f |
| Math of Idle Games I-III (Pecorella) | dev | https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii |
| How to design an idle game (Bugnet) | dev | https://bugnet.io/blog/how-to-design-an-idle-or-incremental-game |
| Playing to Wait (Alharthi et al. 2018) | acad | https://par.nsf.gov/biblio/10061230 |
| "It Started as a Joke" (Spiel et al. 2019) | acad | https://par.nsf.gov/biblio/10174274 |
| Idle Games: A Cozy Genre Turned Exploitative | acad | https://www.czasopisma.uni.lodz.pl/Replay/article/view/23588 |

---

## 1. Catalog of complaints (ranked by estimated frequency)

### C1. Grind / "too slow" / progress walls - VERY COMMON
Players hit points where the next upgrade takes hours or days, with no new decision, just waiting. Often the wall is where the exponent curve outruns production.
- NGU Idle summaries: progress "slow and grindy", "hundreds to thousands of hours", "many walls and required grinding". [review-agg] https://vaporlens.app/app/1147690/ngu_idle
- Between Adventures IDLE: leveling and skill progression "excessively slow", unbalanced numbers. [review-agg] https://vaporlens.app/app/3702540/between_adventures_idle
- Slot Grind: "devolves into a grind after a couple of hours". [review-agg] https://vaporlens.app/app/4619420/slot_grind
- Idle Streamer: "progression feel[s] frustratingly slow". [review-agg] https://marlvel.ai/apps/idle-streamer/reviews
- r/incremental_games commenter with short sessions: if progress takes very long with the game open, "I am never getting there". [forum] https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhpz8fk/?context=3 (snippet paraphrase)
- Designer view: the wall is where retention collapses unless a prestige/new system arrives; Pecorella's series covers pacing prestige cycles to avoid it. [dev] https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii
- Note: some players defend slow progression as intentional (reply in Steam Cookie Clicker thread). https://steamcommunity.com/app/1454400/discussions/0/3801649759600004600

### C2. Forced / intrusive ads - VERY COMMON (mobile)
- "Excessive forced advertisement frequency disrupts core gameplay for all users"; ads "every few seconds or after every menu interaction". [review-agg] https://marlvel.ai/apps/idle-harbor-tycoon-sea-docks/reviews
- Ads play even when player declines the reward / selects non-ad option. [review-agg] https://marlvel.ai/apps/idle-coffee-shop-tycoon-game/reviews (and others on same site)
- "Remove ads" purchases that don't remove ads. [review-agg] https://marlvel.ai/apps/donuts-franchise-idle/reviews
- Rewarded ad that crashes/reloads app without granting reward. [review-agg] marlvel.ai pages above.
- Praise-with-caveat pattern: "addictive core loop is fun, which is why they keep putting up with the ads" - i.e. ads are the leading *annoyance*, loop is the reason to stay. [review-agg] same pages.

### C3. Paywalls / pay-to-progress / deliberate stalling - COMMON (mobile & gacha-idle)
- "Progression stalls on purpose to sell you the fix." [blog] https://unstar.app/blog/is-divine-magic-goddess-legend-mushroom-watcher-realms-hero-wars-idle-heroes-gacha-games-legit-2026
- Players "stuck at the final level for months or years". [review-agg] same.
- Paywalls/full-screen promos blocking main menu. [review-agg] https://marlvel.ai/apps/water-power/reviews
- HN: resources "you can buy with real money" and daily gambling-style rewards listed as addictive design. [forum] https://brianlovin.com/hn/29633599
- Academic framing: "cozy genre turned exploitative". [acad] https://www.czasopisma.uni.lodz.pl/Replay/article/view/23588
- Expectation counter-signal: a mirrored Reddit thread noted "an expectation that an idle game must be free". [forum] (snippet; search result for the "reddit quit" query).

### C4. Not actually idle: busywork, babysitting, no automation - COMMON
- HN: "if a bot would give you a large advantage, the game is an incremental game" - i.e. designed to be left but still demands active play. [forum] https://brianlovin.com/hn/29633599
- AV Club: "a ton of busywork that's not exactly 'idle'". [article] https://avclub.com/confessions-of-an-idle-gamer-1832949532
- itch.io reviewer: "you MUST babysit the automation". [forum] https://itch.io/post/15658446 / https://itch.io/post/8671617 (snippet; confirm which).
- Dev blog claim that if it feels like "working" while the app is open, players uninstall within ~48 hours. [dev, low-quality source, treat cautiously] cited via search; see https://bugnet.io/blog/how-to-design-an-idle-or-incremental-game
- Commenter wants games supporting both passive and active play; Cookie Clicker criticised for "no agency". [forum] https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhm1s2n/?context=3 (snippet)

### C5. No meaningful choices / one dominant strategy / boring early game - COMMON among enthusiasts
- itch.io commenter: lack of meaningful choices "is the sole reason why your earlygame is boring"; late-game decisions keep it engaging. [forum] https://itch.io/post/4371860
- Another: designers "just getting lazy", dropping in "simple patterns already proven to work". [forum] https://itch.io/post/15130204 (snippet)
- Academic: idle games shift play toward planning; if the plan is solved, nothing remains. [acad] https://par.nsf.gov/biblio/10061230
- Dev guide stating meaningful choices are needed despite automation. [dev] https://bugnet.io/blog/how-to-make-a-idle-game

### C6. Prestige/reset problems (too early, too late, too frequent, no payoff) - COMMON
- HN: "lots of incrementals require way too many such resets, and the activity after a reset is frenetic"; reset = "laziness to create 'infinite' progress when it's just the same loop"; but resets "fine when sparse". [forum] https://brianlovin.com/hn/29633599
- Dev postmortem: first prestige took ~25-35 min for most players; would compress to 15-20; players who bounce before first reset never see the real game. (= too late.) [dev] https://dev.to/aguier/i-built-7-idle-games-in-30-days-what-i-learned-about-incremental-design-5d3f
- Another designer: if the player doesn't feel the difference immediately after reset, the prestige system failed. (= no payoff.) [dev] search result for "prestige too early" query; Game Developer series is the canonical reference: https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii
- Too-early prestige complaint (inferred): prompting resets before the player has built anything feels like punishment; no direct quote found. [inference]
- Wikipedia notes prestige "gives a sense of a rush of progress" (tagged citation-needed). https://en.wikipedia.org/wiki/Incremental_game

### C7. Offline-progress complaints - OCCASIONAL-COMMON
- Cookie Clicker Steam thread: gating offline production behind late upgrades hurts the game. [forum] https://steamcommunity.com/app/1454400/discussions/0/3801649759600004600
- Siegeturtle: "poor idle mechanics / offline progress". [review-agg] https://vaporlens.app/app/3959050/siegeturtle/stats/details
- Reddit commenter wants games to "run offline". [forum] lhm1s2n mirror link above.
- Save loss: Farmer Against Potatoes Idle autosave did not prevent progress rollback after reboot. [review-agg] https://vaporlens.app/app/1535560/farmer_against_potatoes_idle
- Guide advice: offline earnings reduced but still rewarding (so full offline = no reason to return; zero = no reason to leave). [dev] https://bugnet.io/blog/how-to-design-an-idle-or-incremental-game
- Counter complaint: "numbers when I come back are too big and I'm catching up instead of playing". [forum] https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhn00vj/?context=3

### C8. Number inflation, notation and legibility - OCCASIONAL (loud among enthusiasts)
- "Number going up too fast is the thing that turns me off most; I want the numbers to rise because I made them rise." [forum] https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhn00vj/?context=3
- Dislikes numbers that "immediately turn into exponent gibberish with no sense of scale". [forum] https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhsya5e/?context=3

### C9. UI clutter / bloat / feature sprawl - OCCASIONAL (inferred, few direct quotes)
- Taxonomy paper lists interface as a primary design dimension and notes idle games use unusual attention patterns. [acad] https://par.nsf.gov/biblio/10061230
- Unbalanced numbers + systems "bloat" are implied in NGU Idle's "hundreds of hours of content with many walls" complaints. [review-agg] https://vaporlens.app/app/1147690/ngu_idle
- Candid note: I found no direct r/incremental_games quote about UI clutter in the sources I could reach; this is a known community topic [B] but unverified here. Search the subreddit for "UI", "tab overload", "too many currencies" before relying on it.

### C10. Addictive-feeling / time-sink guilt / manipulative loops - COMMON in press, RARE as reason to quit in forums
- Press and blog "time to stop playing Cookie Clicker" pieces (mostly SEO-grade; ignore as evidence) - the better ones: AV Club https://avclub.com/confessions-of-an-idle-gamer-1832949532 ; MetaFilter quotes designer Lantz "like slot machines" https://www.metafilter.com/180147/The-unclicked-life-is-not-worth-living-So-crates
- HN: dark patterns (daily gambling-style rewards). https://brianlovin.com/hn/29633599

### C11. Bugs, crashes, lost saves, broken reward ads - OCCASIONAL
- Auto-save rollback (above); reward ads crash app (above). Technical reliability is table stakes in a game whose whole value is accumulated state.

### C12. Short-session / time-poor players vs long-form incrementals - OCCASIONAL
- Mirrored Reddit remark: long-form incrementals are harder to sustain "because they require time and not many people have the time any more". [forum] (snippet from reddit-quit search) and the short-session commenter at lhpz8fk mirror above.

---

## 2. Frequency summary table (qualitative)

| ID | Complaint | Frequency (this sample) | Mobile vs PC |
|---|---|---|---|
| C1 | Grind / walls / slow | VERY COMMON | both |
| C2 | Forced ads | VERY COMMON | mobile |
| C3 | Paywall / pay-to-progress | COMMON | mobile |
| C4 | Not idle / babysitting | COMMON | both |
| C5 | No meaningful choices | COMMON (enthusiasts) | PC/browser |
| C6 | Prestige timing/payoff/frequency | COMMON | both |
| C7 | Offline progress design | OCCASIONAL-COMMON | both |
| C8 | Number inflation/notation | OCCASIONAL | PC/browser |
| C9 | UI clutter/bloat | OCCASIONAL (weak evidence) | both |
| C10 | Manipulative/addictive guilt | COMMON in press; RARE as quit cause | both |
| C11 | Bugs/save loss | OCCASIONAL | both |
| C12 | Time-poor players | OCCASIONAL | both |

---

## 3. Cross-cutting patterns

1. **The loop is liked; the wrapper is hated.** Aggregated mobile reviews consistently pair "addictive core loop" praise with ad/paywall rage (marlvel.ai links above). Players quit over monetisation friction, not the genre.
2. **Walls are the real churn point; prestige is the intended escape.** Each of C1, C6 and C7 are the same problem viewed at different time scales: the player runs out of satisfying next actions. Prestige and offline progress are repair tools that fail when mistimed (dev postmortem https://dev.to/aguier/i-built-7-idle-games-in-30-days-what-i-learned-about-incremental-design-5d3f).
3. **Two opposite worries about offline progress**: too little (nothing to come back to / gated) and too much (catching up instead of playing). Tune a middle path and make the return a *decision moment*, not a number dump.
4. **Enthusiasts and casuals diverge.** Reddit enthusiasts quit over lack of choice and number legibility; mobile casuals quit over ads/paywalls/grind. A game aimed at fans of a franchise (not genre veterans) sits closer to the casual side but will attract some enthusiasts.
5. **Idle must mean idle.** Active-play mandatory loops (C4) violate genre contract; but fully passive games (Cookie Clicker criticised for "no agency") fail C5. Target: *active play accelerates, idle play never stalls.*
6. **Trust.** "Remove ads" that doesn't remove ads, rollback saves, and deliberate stalling create outright distrust; the review corpus shows these are one-star triggers.

---

## 4. Example one-liners worth designing against (quotable, paraphrased where snippet only)

- "I want the numbers to rise because I made them rise." (agency over inflation) https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhn00vj/?context=3
- "Reset mechanics = laziness to create infinite progress." https://brianlovin.com/hn/29633599
- "Progression stalls on purpose to sell you the fix." https://unstar.app/blog/is-divine-magic-goddess-legend-mushroom-watcher-realms-hero-wars-idle-heroes-gacha-games-legit-2026
- "You MUST babysit the automation." https://itch.io/post/15658446
- "No meaningful choices is the sole reason your earlygame is boring." https://itch.io/post/4371860
- "Forced ads play even when I pick the non-ad option." https://marlvel.ai/apps/idle-coffee-shop-tycoon-game/reviews

---

## 5. Gaps to close with first-hand access

- Pull top-voted threads from r/incremental_games and r/IdleGames ("hate", "quit", "dropped", "anti-features") and count themes properly.
- Sample 200 one-star App Store / Google Play reviews of Idle Miner Tycoon, AdVenture Capitalist, Cookie Clicker mobile, Egg Inc. and tag by C1-C12.
- Steam: review text of NGU Idle, Antimatter Dimensions, Realm Grinder, Cookie Clicker. Review aggregator sites in the list are AI summaries and not primary.

---

## Implications for a Kamen Rider Decade world-progression upgrade idle game

Design against the catalog above:

1. **Walls (C1):** Pace so no wait exceeds ~the session length without a *new* thing: each wall is paired with a side option (a "Side Rider" card, an alternate-world detour). Put the first "world gate" within ~10-15 minutes (dev postmortem says 25-35 min first prestige was too late: https://dev.to/aguier/i-built-7-idle-games-in-30-days-what-i-learned-about-incremental-design-5d3f).
2. **Ads/paywalls (C2/C3):** Ship ad-free or strictly opt-in rewarded ads (never when declining), no purchase that gates progress. If IAP, sell cosmetics (Rider suits, henshin sounds) and a one-time "remove ads" that actually works. Fandom tolerates cosmetics; it will not forgive forced ads on a licensed property.
3. **Idle really idle (C4):** Auto-henshin/auto-card-ride unlocks early; active play = "Attack Ride" burst that speeds things up but is never required.
4. **Meaningful choices (C5):** Each world offers a branching choice of which Rider's power set to field (Kuuga vs. Kabuto style tradeoffs: breadth vs. burst) and card-combo synergies from the Decade form-ride roster. Early game needs at least one real fork in the first 5 minutes.
5. **World transitions as prestige (C6):** First ride into a new world visibly boosts speed ("Final Kamen Ride" = permanent multiplier, with a before/after production comparison shown on the screen). Keep resets sparse (a handful of worlds per week of play, not per hour). Never reset the card collection.
6. **Offline (C7):** Offline gains at ~50-70% rate, capped at a fixed window, with a "welcome back" report that offers 1-2 decisions (spend tickets to claim a card, choose next world) so the return feels like play, not catch-up. Never gate basic offline behind late upgrades.
7. **Numbers (C8):** Use named ranks and capped notation; keep per-world numbers resettable in scale so players never face e47.
8. **UI (C9):** One screen per world, a max of ~3 currencies visible, progressive disclosure of systems; Rider-card "binder" as the single hub.
9. **Trust (C10/C11):** Cloud + local dual save, versioned backups, no dark-pattern daily streak penalties.
10. **Audience fit (C12):** Support 2-minute sessions: every return surfaces one clear next action.
