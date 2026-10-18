# Patterns shared by the most-beloved idle/incremental games

Scope: all 37 files in `games/`, plus `research/psychology.md`, `research/player_complaints.md`, `research/math_of_idle_games.md`, `sim/results.md`.

## Method and honesty notes
- No sales, retention or review-score data exists in this repo. "Beloved" is a judgment from the "What players love" sections, longevity, community tooling (wikis, calculators, mods) and absence of complaints about monetisation. It is not a measurement.
- **Beloved set (N = 14):** Antimatter Dimensions (AD), Cookie Clicker (CC), Universal Paperclips (UP), A Dark Room (ADR), Kittens Game (KG), Evolve, Synergism, Trimps, Melvor Idle, Progress Knight (PK), Bitburner, Realm Grinder (RG), NGU Idle, Spaceplan.
- Evidence strength per game file: strong = AD (partly `[S]`/source), Bitburner `[SRC]`, Evolve `[SRC]`, Synergism `[SRC]`, PK `[CODE]`, Melvor `[S]`, CC (`[S]` cost/prestige). Weak = ADR, KG, Trimps, Spaceplan, UP (mostly `[M]`/`[E]`/`[MEM]`), RG and NGU (mostly unverified). Counts below inherit that weakness; treat "9 of 14" as "9 of 14 as far as the files record".
- Counts are manual tallies from the files, not keyword matches. Where a game only partly fits I say so.
- Companion files: `analysis/anti_patterns.md`, `analysis/sequential_worlds.md`.

## Pattern table (counts out of the 14 beloved games)

| # | Pattern | Count |
|---|---|---|
| B1 | Non-predatory monetisation (free, open source, or one-time purchase) | 12 of 14 clean, 2 partial |
| B2 | Something new appears every few minutes, and the UI is revealed progressively | 14 of 14 |
| B3 | Each stage/layer changes the rules, not only the numbers | 14 of 14 (10 via prestige layers, 4 via phases/genres/beats) |
| B4 | Real decisions (build, route, price, allocation), not just "buy the next thing" | 13 of 14 |
| B5 | Inspectable math (open source, readable JS, or deep community wiki/calculators) | 10 of 14 |
| B6 | Prestige/gains compressed by sqrt, cbrt, log or falling exponents so numbers stay readable | 7 of 14 |
| B7 | Strong voice/theme (humour, horror, lore) that makes each unlock a story beat | 9 of 14 |
| B8 | Offline or catch-up progress exists | 9 of 14 (5 do without) |
| B9 | Optional active spikes layered on an idle base | 5 of 14 |
| B10 | Automation is itself a priced reward/milestone | 5 of 14 |
| B11 | Milestone or achievement ladders giving frequent small wins | 6 of 14 |
| B12 | Small number of visible resources early, more added later | 6 of 14 |

## B1. Non-predatory monetisation (12 of 14 clean, 2 partial)
- Clean: AD "None. Free, no ads, no premium currency" (`games/antimatter-dimensions.md`); CC Steam one-time, no IAP (`games/cookie-clicker.md`); UP free browser, "zero pay-to-win" (`games/universal-paperclips.md`); ADR free, mobile ~$0.99 no IAP (`games/a-dark-room.md`); KG free, donations (`games/kittens-game.md`); Evolve free, README rejects "features that only make the game easier" (`games/evolve.md`); Trimps free (`games/trimps.md`); Melvor one-time purchase, "no premium currency, so progress is time-based only" (`games/melvor-idle.md`); PK free (`games/progress-knight.md`); Bitburner Steam one-time, RAM limits replace paywalls (`games/bitburner.md`); NGU Steam one-time, "mostly free of pay-to-win" `[unverified]` (`games/ngu-idle.md`); Spaceplan premium one-time, no ad walls (`games/spaceplan.md`, `[MEM]`).
- Partial: Synergism PCoin upgrades buff offline cap and quark gain, which some read as pay-to-skip (`games/synergism.md`, `[SRC]` + `[MEM]`); RG has optional IAP on Kongregate/mobile, one-time on Steam (`games/realm-grinder.md`, `[unverified]`).
- Supports: `research/player_complaints.md` pattern 1 "The loop is liked; the wrapper is hated" and pattern 6 "Trust".

## B2. A new thing every few minutes, revealed progressively (14 of 14)
- ADR: each button appears only when relevant; each new tab is a story beat (`games/a-dark-room.md`). Village stage names (Lonely Hut -> Raucous Village) tie to counts.
- UP: "Every few minutes a new mechanic; no filler waiting" (`games/universal-paperclips.md`).
- Spaceplan: "Every 3-10 minutes a new item/dialogue appears" (`games/spaceplan.md`, `[EST]`).
- CC: later buildings revealed at about 1/3 to 1/2 of price so the next tier is always visible (`games/cookie-clicker.md`).
- AD: each layer "re-teaches the same loop with new rules"; 150+ achievements (`games/antimatter-dimensions.md`).
- Synergism: each layer unlocks a new building set and minigame (`games/synergism.md`).
- KG, NGU, Evolve, Bitburner, Trimps, RG, PK, Melvor: heavy unlock ladders (NGU "a fixed number of features each day"; Bitburner subsystems unlock via Source Files; Trimps new permanent layers at zone thresholds; PK unlock tree "level X in job Y"; Melvor items every few levels). See each file's "Unlock pacing".
- Psychology: dense goal gradients plus endowed progress (`research/psychology.md` sections 5-6).
- Sim support: the best configs gave 32 goals in 3 h, median gap 46 s, max gap 344 s (`sim/results.md`, sweep).

## B3. Each stage changes the rules (14 of 14)
- Via prestige layers (10): AD (Infinity/Eternity/Reality, Celestials with their own rules), Evolve (each reset type has its own constants table and mechanic), Synergism (5 layers, each a new subsystem), Trimps (Heirlooms, Nature, Universe 2), RG (factions, abdication, reincarnation), Bitburner (BitNodes change `currentNodeMults`), KG (karma/paragon/time layers, challenges), NGU (rebirth, titans, challenges), PK (rebirth one/two), CC (heavenly tree plus Garden/Grimoire/Stock mini-games).
- Via phases/genres/beats (4): UP (clips -> drones -> probes), ADR (village economy -> map -> shooter), Spaceplan (new currency per story beat), Melvor (expansions add skills/worlds).
- Players' words: AD "Every layer reinvents the game"; Evolve "Reset layers each introduce a mechanic (not just a bigger number)".
- Detail in `analysis/sequential_worlds.md`.

## B4. Real decisions (13 of 14)
- RG faction choice; Evolve race and government; Bitburner writing the scripts; KG job assignment; NGU energy/magic allocation; Trimps perk purchases; PK "what to train in a limited life"; AD challenges and time studies; Synergism ants/runes/corruptions; CC golden-cookie combos; Melvor skill/mastery choices; UP price slider and Yomi tournaments; ADR supply-chain jobs (hunter -> charcutier).
- Exception: Spaceplan (writing is the product; "shallow for experienced fans", `games/spaceplan.md`).
- Maps to `research/player_complaints.md` C5 ("no meaningful choices is the sole reason your earlygame is boring") and SDT autonomy (`research/psychology.md` section 2).

## B5. Inspectable math (10 of 14)
- Source or code available: AD (GitHub), Bitburner, Evolve, KG, Synergism, Trimps (plus AutoTrimps/Perky), PK, CC (`main.js`), UP (unobfuscated JS), ADR (open source, MPL-2.0).
- Even without code, RG and NGU have heavy wiki/spreadsheet culture. The counter-case: the community built spreadsheets because the game would not explain itself (see anti-patterns A3).

## B6. Compressed gains keep numbers readable (7 of 14)
- AD IP = `10^(log10(AM)/308 - 0.75)`, EP uses base 5 (`games/antimatter-dimensions.md`, `research/math_of_idle_games.md` 3.4).
- CC `cbrt(C/1e12)`, +1% CPS per level `[S]`.
- Synergism exponents fall per layer: 0.5 -> 0.03 -> 0.01 `[SRC]`.
- Evolve: log curves plus plasmid soft cap `cap + overflow/(overflow+cap)*cap` `[SRC]`.
- PK: income `1 + log10(level+1)`, lifespan and speed on log33/log13 `[CODE]`.
- KG: paragon with `getLimitedDR` diminishing returns `[SOURCE CODE]`.
- RG: sqrt formula (`research/math_of_idle_games.md` 3.1).
- Player evidence: "I want the numbers to rise because I made them rise" (`research/player_complaints.md` C8).

## B7. Strong voice and theme (9 of 14)
- ADR atmosphere and late twist; UP "ever-escalating scope... ending with a real 'oh no'"; Spaceplan sarcastic computer voice; CC jokes on every upgrade; PK dark humour and evil path; KG text charm; Evolve "from primordial ooze to spacefaring empire"; AD celestial narrative; Trimps flavour. Sources: each game's "What players love".
- Psych support: Deterding says progress mechanics work even as satire (`research/psychology.md` section 1).

## B8. Offline progress (9 of 14; 5 without)
- With: AD (chunked simulation), CC (Twin Gates 5% for 1 h, up to 91% with all upgrades `[S]`), KG (capped catch-up), Melvor (24 h cap `[S]`), Bitburner (0.75 multiplier `[SRC]`), Synergism (3 days base, 200-tick simulation `[SRC]`), Trimps, NGU, RG (small).
- Without or banked: ADR (state frozen), UP (page must stay open), PK (tab open; Time Warping skill instead), Evolve (banked "time skip"), Spaceplan (modest, `[MEM]`).
- Reading: offline is not a requirement for being loved, but all five no-offline games are either finite (ADR, UP, Spaceplan) or session-based by design (PK, Evolve). Open-ended games have it (`sim/results.md`: eff 0 -> 0.25 makes a 3x10 min/day player about 9x faster).

## B9. Optional active spikes (5 of 14)
- CC golden cookies (Frenzy x7), RG spells, UP price slider and projects, NGU Adventure mode, Synergism automation toggles/challenges. Active play accelerates; the base keeps running. Matches `research/player_complaints.md` cross-cutting pattern 5 ("active play accelerates, idle play never stalls").

## B10. Automation as a reward (5 of 14)
- UP WireBuyer costs 7,000 ops (`games/universal-paperclips.md`, `[S]`); AD Break Infinity requires a 0.1 s Big Crunch autobuyer `[S]`; Synergism auto-prestige credited offline as `timeAway / fastestPrestige` `[SRC]`; Bitburner (automation is the game); Trimps (the community built AutoTrimps, which doubles as a complaint).

## B11. Milestone and achievement ladders (6 of 14)
- AD 150+ achievements with row rewards; CC achievements and milk; Synergism "hundreds of achievements"; Evolve achievement level raises the plasmid cap `[SRC]`; UP Trust milestones on Fibonacci-spaced clip counts `[S]`; ADR village stage names by count.

## B12. Few visible resources early (6 of 14)
- Spaceplan 2-4 visible resources (`[EST]`); UP money plus ops; ADR wood first; AD one currency, eight dimensions; CC cookies; PK coins only. Counter-case: KG, NGU, Synergism show many resources and are the most-cited for complexity.

## Cost-curve facts shared by the beloved set
- Core production-building ratios sit in 1.07-1.15 (CC 1.15 `[S]`, KG 1.12-1.15 `[M]`, RG likely 1.08-1.15 `[unverified]`), with outliers by design: Synergism 1.25, PK `1.01^level` polynomial, ADR linear (`a + b*n`, pacing from events), Melvor XP doubling every ~7 levels `[S]`.
- Sim result: the *shape* (cost ratio between tiers slightly above rate ratio, ~1.2-1.5, plus x2 milestones) matters more than the growth constant (`sim/results.md`).

## Implications for Kamen Rider Decade world-progression idle game
1. **Be the "wrapper-clean" game (B1).** 12 of 14 beloved games have no predatory monetisation. A licensed Rider game should be one-time purchase or free with cosmetic-only sales (suit skins, henshin sounds); `research/player_complaints.md` implication 2 says fandom will not forgive forced ads on a licensed property.
2. **Reveal, don't dump (B2, B12).** Start with one number and one button (Kabuto's Clock Up or a photograph), and show at most 2-4 resources at a time. Each new Rider world = one new tab/currency, never several (NGU, Synergism, KG are the cautionary cases).
3. **Every world must change a rule (B3).** Use `research/decade_worlds.md` hooks: Kabuto speed/cast-off, Den-O time-skip, Ryuki card collection, Faiz routing, Blade fusion, Kiva day/night, Agito form tiers, Hibiki rhythm, Kuuga colour forms. That is the cheapest way to hit 14 of 14.
4. **Ship real choices (B4).** Give each world a fork in the first 5 minutes (which Rider power set to slot) and at least two viable builds. Avoid combat; choices are card loadouts, routing and allocation.
5. **Compress prestige (B6).** World-ride gain should use sqrt/cbrt or a falling exponent per layer, with a visible "pending gain" readout; the sim's best band is first gate ~25 min, then 20-45 min cycles (`sim/results.md`). Keep per-point bonus 5-10% so final multipliers stay 2e2-6e3x.
6. **Give the game a voice (B7).** Tsukasa's quips as narrator reacting to each unlock; this costs little and is shared by 9 of 14.
7. **Offline at ~50% with an 8 h cap (B8)** is supported by the sim (offline efficiency is the dominant lever) and by Bitburner's 0.75; make the return a decision moment (`research/player_complaints.md` pattern 3).
8. **Active spikes optional (B9):** an "Attack Ride" burst (x3 for 30 s, 5 min cooldown) like CC golden cookies or RG spells, never required.
9. **Automation as milestone (B10):** unlock auto-henshin/auto-card-ride as a priced purchase per world.
10. **Ladder of small wins (B11):** card binder and per-world achievements with small multipliers so each session ends with something earned.
11. **Evidence caveat:** the strongest beloved-game evidence is for AD, Evolve, Synergism, Bitburner, PK. Treat ADR, Spaceplan, KG, Trimps patterns as design inspiration, not measured facts.
