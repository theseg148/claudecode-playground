# Events, choices, collections and onboarding in top idle games (no combat) -> Decade idle game

Scope: how idle games create *meaningful decisions* and *unscheduled moments* without combat, how they bolt on collection meta-systems, and how the first 10 minutes are paced. Closes with concrete proposals for Decade idle (no combat).

## 0. Evidence tags and honesty notes
- **[CODE]** read directly from open-source code in this session (file + line context given). Highest confidence for numbers.
- **[S]** published source (wiki / forum / article); I only saw search-result snippets, not full pages (the sandbox only allows WebSearch and raw.githubusercontent.com), so [S] numbers are as good as the snippet.
- **[M]** from my own memory of the game; NOT verified in this session. Treat as plausible, re-check before building on it.
- **[E]** my estimate / calculation / design proposal.
- Web search was thin: it returned mostly low-quality mirrors for Egg Inc, Realm Grinder, AdCap, Idle Miner. Where I could not confirm a number I say so instead of inventing one. Closed-source games (Realm Grinder, Egg Inc, AdCap, Idle Miner, Melvor, NGU) are therefore mostly [S]/[M].
- Cookie Clicker code: the user named the `main` branch; the ozh/cookieclicker mirror's default branch is `gh-pages`, file `main.js` (976 KB, copyright "Orteil, 2013-2026", so a current version). Minigames are `minigamePantheon.js`, `minigameGarden.js`. Base URL:
  `https://raw.githubusercontent.com/ozh/cookieclicker/gh-pages/main.js` (and `.../minigameGarden.js`, `.../minigamePantheon.js`).
- Antimatter Dimensions code: `https://raw.githubusercontent.com/IvarK/AntimatterDimensionsSourceCode/master/src/core/...`
- Kittens Game code: `https://raw.githubusercontent.com/nuclear-unicorn/kittensgame/master/js/{village,religion,buildings,science,challenges}.js`
- Local scratch copies were in the session scratchpad (not committed).

---------------------------------------------------------------------------------------------------

## 1. Meaningful decisions without combat

The common pattern: a decision is "meaningful" when (a) options are mutually exclusive or rationed, (b) each has a different *shape* (burst vs steady, active vs passive), and (c) the player can see the trade-off in numbers. The mechanisms below fall into six families.

### 1.1 Family A: Loadout slots with a rationed swap (Cookie Clicker Pantheon, dragon auras)

**Pantheon** [CODE: minigamePantheon.js]
- 11 "spirits" (gods) in the file (`desc1:` appears 11 times), 3 slots: Diamond, Ruby, Jade. The same god gives a different strength by slot: e.g. Holobore (Asceticism) = +15% / +10% / +5% base CpS in Diamond / Ruby / Jade, with the penalty "if a golden cookie is clicked this spirit is unslotted and all swaps are used up" (a direct active-vs-passive trade).
- Typical pair shape (Vomitrax/Decadence): golden-cookie effect duration +7/+5/+2% **and** buildings -7/-5/-2% CpS. Others: buildings 7/5/2% cheaper but heavenly chips 30/20/10% weaker; clicking +15/+10/+5% but buildings -3/-2/-1%; buildings +10/+6/+3% but golden/wrath cookies appear 10/6/3% less; milk +10/+5/+3% but golden cookies -15/-10/-5%; sugar lumps ripen 60/40/20 min sooner; one god (Mokalsium/Seasons) has a sinusoidal effect with cycle 3 h / 12 h / 24 h.
- Almost every effect is "+X here, -Y there", scaled by slot (about 2:1.4:1). The slot ratio (15:10:5 = 3:2:1) is the design lever: the player decides *which one thing deserves the best slot*.
- **Rationing:** `M.swaps=3`. Refill timer: 1 h if you have >=2 swaps, 4 h if 1 left, 16 h if 0 left (code: `t=1000*60*60; if(swaps==0) t=...*16; else if(swaps==1) t=...*4`). So the first swap is cheap, the last is very expensive -> players plan loadouts for the session/day rather than flip-flopping.
- Free to *place* first-time (when `slot==-1`); the cost only applies to moving.

**Dragon auras** [CODE: main.js ~15106-15260]
- Krumblor levels: 5 egg stages (cost 1M, 2M, 4M, 8M, 16M cookies - doubling), then one new aura learned per level; 21 auras listed (`Game.dragonAuras` ids 1-21). Late levels cost "bake dragon cookie: 50 of every building" and "secondary aura slot: 200 of every building" (so a second slot is a big spend, but it *replaces* nothing).
- Aura list is a menu of mutually exclusive archetypes: Breath of Milk +5% kittens, Dragon Cursor +5% click, Elder Battalion +1% per non-grandma building for grandmas, Reaper of Fields (golden cookies may trigger Dragon Harvest x15 for 60 s), Earth Shatterer (sell back 50% vs 25%), Master of the Armory (upgrades 2% cheaper), Fierce Hoarder (buildings 2% cheaper), Dragon God (+5% prestige effect), Arcane Aura (golden cookies +5% more often), Dragonflight (golden cookies may trigger x1111 for 10 s), Ancestral Metamorphosis (+10% golden gains), Unholy Dominion (+10% wrath gains), Epoch Manipulator (+5% effect duration), Mind Over Matter (+25% drops), **Radiant Appetite (all production x2)**, Dragon's Fortune (+123% CpS per golden cookie on screen), Reality Bending (10% of all other auras combined), etc.
- **Switching cost:** `Game.ObjectsById[highestBuilding].sacrifice(1)` - changing your aura sells 1 of your most expensive building ("This will affect your CpS!"; free if you own no buildings). A *small, visible, immediate* cost - the best respec-cost pattern in the sample: cheap enough to experiment, never zero.

### 1.2 Family B: Spatial puzzle with growth time (Cookie Clicker Garden)
[CODE: minigameGarden.js]
- Unlock: farm level >= 1 (farm levels cost sugar lumps). Plot grows with farm level via `M.plotLimits` (9 shapes from a tiny cross 2/2/4/4 up to a 6x6 grid).
- 34 plants (`ageTick:` x34). Each has `cost`, `ageTick` (growth per step), `mature` threshold and `children` (mutation targets). Effects are small global modifiers: baker's wheat CpS +1%; thumbcorn clicks +2%; cronerice grandma CpS +3%; gildmillet golden gains +1% / duration +0.1%; clover golden frequency +1%; golden clover golden frequency +3%; shimmerlily mixed +1% each; elderwort wrath-side; crumbspore/doughshroom explode into 1-5 min of CpS (cap 1-3% of bank); queenbeet / duketater "harvest when mature for X h of CpS (max 3-8% of bank)"; juicy queenbeet gives a sugar lump; etc. Some plants have *negative* secondary effects (e.g. -5% clicks, -10% golden frequency) -> a build choice.
- **Soils** (`M.soils`): dirt tick 5 min / effect x1; fertilizer tick 3 min, effect x0.75, weeds x1.2 (needs 50 farms); clay tick 15 min, effect x1.25 (100 farms); pebbles tick 5 min, effect x0.25 but weeds x0.1 (200 farms); wood chips same 0.25/0.1 (300 farms). So soil = fast-and-weak vs slow-and-strong - **an idle-friendly decision about visit frequency**. The Garden "tick" is minutes, not seconds.
- **Mutation** is probabilistic and adjacency-driven, e.g. 2 mature wheat neighbours -> 20% wheat, 5% thumbcorn, 0.1% bakeberry; wheat + gildmillet -> 3% clover, 0.07% golden clover; shimmerlily + whiskerbloom -> 5% chimerose. Rare mutants are "seeds" that fill a **collection** (seed log) - so Garden is simultaneously a build puzzle and a collection.
- Frozen mode (`M.freeze`) stops effects: a "pause" lever for experiments.

### 1.3 Family C: Faction / alignment picks that remake the economy (Realm Grinder)
[S: https://realm-grinder.fandom.com/wiki/Alignments ; https://www.pcgamer.com/realm-grinder-guide/ ; https://www.supercheats.com/realm-grinder/walkthrough/factions]
- Alignment (Good / Evil / Neutral) chosen by buying a Proof; factions: Fairy, Elf, Angel (good); Goblin, Undead, Demon (evil); Titan, Druid, Faceless (neutral); prestige factions Dwarf, Drow, Dragon stack with a vanilla or neutral faction; Mercenary (Afterlife expansion) combines spells/upgrades of other factions [S supercheats].
- Wiki describes Good as more active (spells, treasure clicks), Evil as more idle/passive production, Neutral as eclectic [S]. PC Gamer's beginner advice: try every faction once; Elves = steady long-term growth, Goblins = fast coin via aggressive building, Undead = offline gains + spell synergy [S].
- Each reincarnation retains some spells/bonuses [S]. The faction choice is **re-made every run**, so it is respec by design: you do not repair a bad build, you swap it next run.
- I could not confirm per-faction numbers; Realm Grinder is closed source. [M]: faction gives a % bonus to coins by building type (e.g. +X% per tier) and a unique spell; ~10 factions x 3 alignments x research tree (Research page https://realm-grinder.fandom.com/wiki/Research exists) -> hundreds of builds. Treat the "hundreds of builds" as [E].

### 1.4 Family D: Challenge runs that give permanent rewards (Antimatter Dimensions, Kittens Game)
**Antimatter Dimensions** [CODE: src/core/secret-formula/challenges/*.js]
- 12 Normal Challenges (ids 1-12), each a restriction whose **first-clear reward is an automation**: C1 = 1st-dimension autobuyer ... C8 = 8th-dim autobuyer, C9 tickspeed autobuyer, C10 Dimboost autobuyer, C11 Galaxy autobuyer, C12 Big Crunch autobuyer (reward strings "Upgradeable Nth Antimatter Dimension Autobuyer", "Tickspeed Autobuyer", "Automated Dimension Boosts / Antimatter Galaxies / Big Crunches"). Restrictions are verbs not numbers: "buying dimensions or tickspeed halts production for 3 min (recovering gradually)", "dimension boosts give no multiplier and galaxies cannot be bought", "only 6 dimensions", "each dimension produces the dimension 2 tiers below". A challenge = *the same game with one rule removed*.
- 8 Infinity Challenges: goals e.g. 1e650 (all normal-challenge restrictions at once), 1e10500, 1e5000, 1e13000, 1e16500, 2e22222... Rewards are multiplicative: IC1 = x1.3 on all Infinity Dimensions *per IC completed*; IC4 = all AD multipliers get ^1.05; IC3/IC5/IC6 etc. = multipliers tied to galaxies, tickspeed. "Dimension boost multiplier min x4" for IC7 (approx).
- 12 Eternity Challenges (EC1: Time Dimensions disabled, EC2: Infinity Dimensions disabled, EC3: ADs 5-8 don't produce, ...) with **goal + goalIncrease** per repeat (e.g. EC1 goal 1e1800, +1e200 each of 5 completions; EC2 1e975 +1e175; EC3 1e600 +1e75) - repeatable with escalating goals, so each EC has up to 5 tiers of reward.
- Design takeaways: (1) challenge = one forbidden verb; (2) reward is either *automation* (QoL) or a *multiplier you can't get otherwise*; (3) gating by Time Studies/Infinities so the player meets them in order; (4) escalating goal for repeat completion.

**Kittens Game** [CODE: challenges.js]
- 10 challenges (`name:` entries): ironWill, winterIsComing, anarchy, energy, atheism, 1000Years, blackSky, pacifism, unicornTears, postApocalypse. Examples (from the names + code): atheism disables the priest job and faith mechanics (`village.js` evaluateLocks `return !game.challenges.isActive("atheism")`); winterIsComing forces cold weather (checked in kitten growth code). Completed challenges give permanent effects. The key point for Decade: challenges are *rule removals tied to existing systems*, not new content.

### 1.5 Family E: Assigning a scarce unit pool to jobs (Kittens Game)
[CODE: village.js, `jobs:` array]
- Jobs and per-kitten yields per tick (before multipliers): woodcutter wood 0.018; farmer catnip 1; scholar science 0.035 (+0.0001 starchart after astrophysicists); hunter manpower 0.06; miner minerals 0.05; priest faith 0.0015; geologist coal 0.015 (+0.010 mining drill, +0.015 unobtainium drill, +0.0075 geodesy) and gold up to 0.0005+0.0005+0.0008; plus scientist, artisan, engineer (limit = number of factories: `getJobLimit("engineer") == bld.get("factory").val`), ambassador (limit = 1 per unlocked race, consumes culture and spice with quadratic/cubic scaling beyond 5).
- Kitten supply is the scarce thing: `maxKittens` from huts/log-houses (hut price ratio 2.5, i.e. expensive housing), growth `kittensPerTickBase`, and catnip surplus is required for growth (starvation code). You re-assign kittens at will, free, with a leader/skill system: **respec is free but pop is limited**, so decisions are *about balance at this moment*, re-balanced every few minutes as bottlenecks move.
- Unlock chain is the "science" tree: Calendar 30 science, Agriculture 100, Archery 300, Mining 500, Animal husbandry 500, Metal 900, Math 1000, Construction 1300, Civil 1500, Writing 3600, Machinery 15000, Theology 20000 + 35 manuscripts, Astronomy 28000 + 65 manuscripts, Navigation 35000 + 100 manuscripts, Physics 50000 + 35 compendia [CODE: science.js prices]. Each tech unlocks a job, building or resource - a long linear-ish tree where the player chooses *order*, paying in the scholar-produced currency.
- Religion/Faith: `faithRatio` (epiphany) grows by `faith/1e6 * ttPlus1^2 * bonusRatio`; "praise" converts faith to worship; "transcend" tiers; religion buildings (ziggurat, temple). It is a second, slow, permanent-multiplier layer [CODE religion.js lines ~1550-1660].

### 1.6 Family F: Pure allocation of a flow (NGU Idle) and skill-switching (Melvor Idle)
- **NGU Idle** [S: community threads https://steamcommunity.com/app/1147690/discussions/0/2646360821011099471 , .../2794999575673906748 , .../3111405265471869154 ]: two flows (Energy, Magic) are *allocated* to sinks (Augmentations, Time Machine, NGU upgrades, Basic Training, Wandoos, bars/power/cap). Community lore: base speed above ~50 is wasted; "power : cap : bars" ratio debated ("1:37.5k:1" vs ~1.53 power : 1 bar : 37.5k cap); experience is split energy vs magic; time machine has steep cost growth so give it ~10% of energy/magic (or all of it for the first hour). Unlock hints [S, unverified third-party]: Adventure/Inventory at boss 4, Augmentations at boss 17, Time Machine at boss 30, Blood Magic at boss 37. NGU technically has combat (Adventure), but the *idle* decisions are pure allocation and community-optimised sliders - the "spreadsheet game" the target audience enjoys. [E]: the allocation UI makes every sink a competitor for the same input, so no sink can be ignored.
- **Melvor Idle** [S: https://steamcommunity.com/app/1267910/discussions/0/3199241400250725473 ; https://earlyguides.com/melvor-idle/beginners-guide]: one active skill at a time (the choice of *what to do now*), item-level Mastery (levels 1-99), a per-skill Mastery Pool, with checkpoints at 10/25/50/95% of the pool that give skill-wide bonuses *only while the pool is kept at that level* - i.e. you *choose between spending mastery XP on items and keeping the pool full*. Beginner advice: start with Woodcutting/Firemaking, aim for the first big QoL purchase (Auto Eat, 1,000,000 GP) [S]. Township and Farming run in the background alongside the active skill [S].
- **Egg Inc research** [S/M]: two research trees: Common Research (bought with cash, reset on prestige; categories: capacity, laying rate, value, hatchery, etc.) and Epic Research (bought with Golden Eggs, permanent; e.g. Soul Food, Prophecy Bonus, Lab Upgrade) [S: https://www.touchtapplay.com/egg-inc-best-upgrades/ ; https://egg-inc.fandom.com/wiki/Prestige?oldid=9210]. Soul Eggs give a % earnings bonus (the base is 10% per Soul Egg [S], boosted by Soul Food, Prophecy Bonus gives +1% compounding on that [S]). Decision: which common tier to buy next (best marginal ROI changes every egg tier), and which epic upgrade (Golden Eggs are scarce, so epic choices feel permanent). I could not verify the number of common research tiers (I believe ~19 researches x up to 100 levels - [M], unverified).

### 1.7 Cross-cutting patterns (the actual lessons)
1. **Same slot, different value (Pantheon 15/10/5):** one object with 3 strengths forces a ranking decision, not a binary yes/no.
2. **Cheap-first, expensive-last swap budget (1 h/4 h/16 h):** teaches planning without hard-locking.
3. **Switching cost = one visible unit (dragon aura sells 1 top building):** a respec price the player can compute in their head.
4. **Plus/minus effects (almost every god and several plants):** both columns visible; avoids "obviously best".
5. **Challenge = remove one verb, reward = automation or a multiplier you can't get elsewhere (AD).**
6. **Scarce population assigned to jobs (Kittens):** rebalancing is the decision; unlock chain = order choice.
7. **Run-level faction picks (Realm Grinder):** the choice is reset-sized, so mistakes cost one run.
8. **Slow tick on a spatial puzzle (Garden 3-15 min ticks, lump 20-23 h ripeness):** gives a reason to return at defined intervals without punishing absence (plants stop being useful only after maturity decay; `lumpMatureAge=hour*20`, `lumpRipeAge=hour*23`, overripe = ripe+1 h [CODE main.js ~4634-4649]).

---------------------------------------------------------------------------------------------------

## 2. Unscheduled events and active layers

### 2.1 Cookie Clicker golden cookies - the reference implementation [CODE: main.js ~5600-6000, 6123]
**Spawn timing**
- `getMinTime = getTimeMod(m=5)`, `getMaxTime = getTimeMod(m=15)`, returned as `Math.ceil(fps*60*m)` -> base spawn interval uniform in **5-15 minutes** of game time.
- Modifiers multiply m: Lucky day x0.5; Serendipity x0.5 (so 1.25-3.75 min combined); Golden goose egg x0.95; Heavenly luck x0.95; Green yeast x0.99; Arcane Aura (dragon) x(1-0.05); Sugar blessing buff x0.9; Elder season upgrades x0.98/0.95; garden `goldenCookieFreq`; Pantheon: Industry god x1.1/1.06/1.03 (slower), Mother god x1.15/1.1/1.05 (slower), Seasons god x0.97/.98/.99 (faster). Cookie chain: m=0.05 (3 s); "Gold hoard" upgrade m=0.01 (about 0.6 s between spawns).
- **On-screen lifetime:** 13 s base; x2 with Lucky day, x2 with Serendipity (so 52 s), x1.05 Decisive fate, x1.01 for each of Lucky digit/number/payout; **x0.95 per other golden cookie currently on screen**; chain cookies: `max(2, 10/chain)` seconds. Fade curve `1-(2t-1)^4` (opacity ramps up/down smoothly) - the cookie is *offered*, not slammed.
- Wrath cookies (red) appear in the "grandmapocalypse" state; they share the machinery with different outcome lists. Also: reindeer (Christmas) `getMinTime m=3`, `getMaxTime m=6` minutes; lifetime 4 s (x2 with Weighted sleighs) [CODE ~6000-6030].

**Outcome table** (from the `list.push` code; each spawn builds a candidate list, then picks uniformly, with an 80% chance to re-roll away from the previous effect)
- Always in list: `frenzy`, `multiply cookies` ("Lucky"). Wrath adds `clot`, `ruin cookies`.
- Conditional extras: 3% (cookiesEarned >= 100,000) `chain cookie`, `cookie storm`; 10% `click frenzy` (unless Dragonflight active, 5% override); building special 25% (needs >= 10 buildings); sugar lump 0.05% (`Math.random()<0.0005`); dragon harvest / dragonflight only with the respective aura; wrath extras 30%: `blood frenzy`, `chain cookie`, `cookie storm`; 10% `cursed finger`; "blab" 0.01%.
- Effect sizes (base, before `effectDurMod`):
  - Frenzy: **x7 CpS for 77 s**.
  - Lucky ("multiply cookies"): **min(15% of bank, 15 min of CpS) + 13 cookies** (x golden-gain mult).
  - Click frenzy: **x777 click power for 13 s**.
  - Dragonflight: x1111 click for 10 s; Dragon Harvest: x15 CpS for 60 s.
  - Building special: 30 s, power = `amount/10 + 1` of one random building with >= 10 owned (a *per-build* buff, so it rewards your build identity).
  - Cookie storm: 7 s of falling mini-golden cookies ("cookie storm drop" = max(1-7 min of CpS, 1-7 cookies)).
  - Chain: payout `1/9 * 10^chain * digit`, capped at min(6 h CpS, 50% of bank), chain continues with the next cookie spawning in 3 s.
  - Wrath: ruin = -min(5% of bank, 10 min CpS) - 13; clot = x0.5 CpS 66 s; elder frenzy (blood frenzy) = x666 for 6 s; cursed finger = 10 s buff whose value is CpS*duration (net effect: CpS stops, you get the 10 s up front; exact mechanics not re-verified).
- Effect duration modifier: Get lucky x2, Lasting fortune x1.1, Lucky digit/number/payout x1.01, Epoch Manipulator aura +5%, Pantheon decadence 7/5/2%.
- **Hard cap that matters:** Lucky is capped at 15 min of CpS and ruin at 10 min, so a bank-heavy player gets *more* from keeping a bank (15% of bank) while a CpS-heavy player gets 15 min of production - a built-in "keep a buffer vs spend it" decision (the classical "Lucky bank" strategy) [CODE, strategy interpretation = E].
- The upgrade chain `goldenCookieUpgrades = ['Get lucky','Lucky day','Serendipity','Heavenly luck','Lasting fortune','Decisive fate','Lucky digit','Lucky number','Lucky payout','Golden goose egg']` converts the event system into a prestige-visible "residual luck" bonus (tooltip: +50% + 10% per such upgrade effective boost) - the event layer has its own upgrade track.

**Why it works (design reading) [E]:** 5-15 min gap = at most ~5-6 events/hour for passive players, a Pavlovian "check back" hook; 13 s window is long enough to react from another tab (sound); outcomes vary 10^3 in magnitude (x7 vs x777 vs x1111) so each event is a *lottery ticket* but the average is positive; the 80% no-repeat rule avoids frustrating streaks; the *frenzy stacking* (x7 frenzy + x777 click frenzy) gives a skill ceiling for engaged players.

### 2.2 Cookie Clicker other active layers
- **Sugar lumps** [CODE ~4595-4650]: one lump per ~20-23 h (`lumpMatureAge = 20 h`, ripe 23 h, overripe 24 h); harvest one per day, spend on building levels (unlock minigames: Garden, Pantheon, Grimoire, Market). Daily cadence, not a tap game.
- **Wrinklers**: appear as the grandmapocalypse starts, eat ~5-10% cookies, can be popped for ~1.1x return (drag-cost risk) [M].
- **Seasons** (Valentine, Easter, Halloween, Christmas, Business Day): switch costs cookies; each has its own drop upgrades and collectables - a calendar-ish unscheduled-event layer with *player-chosen timing*.
- **Grimoire** (wizard tower minigame): spells cost mana; "Force the Hand of Fate" spawns a golden cookie on demand; Spells are the "on-demand" version of the event layer [M; file minigameGrimoire.js fetched but not analysed].

### 2.3 Egg, Inc. [S/M]
- **Drones**: periodic flying drones that you tap for a reward; per wiki the reward is Golden Eggs 3/6/12 for regular and 12/48 for elite (96/192 with Drone Rewards research) and "values are significantly increased once the player has spent at least 152,000 total" [S: egg-inc.fandom.com search snippet]. Artifacts can add +100% drone frequency (Neodymium Medallion) and +100% reward (Aurelian Brooch) [S: reddit thread via redlib]. A 2019 patch made drones "worth less and less frequent" [S version history]. Exact spawn interval **not confirmed** (I believe a cadence around once every minute or two when foregrounded, [M]).
- **Boosts**: timed multipliers (e.g. Supreme Tachyon Prism 1000x IHR for 1 hour [S], Legendary Soul Beacon 500x soul eggs for 10 min [S]; Boost Beacon, Jimbo's Best Bird Feed...). They are acquired from gifts, contracts, daily gifts [S version history] and combined in "boost stacks", which creates a *planning decision*: when to pop the stack (right before prestige).
- **Contracts / co-op**: 1 shared goal across friends with a 3-day-ish timer [M]. Decision layer is coordination.
- **Tokens**: "gift" currency for boosts; one more scheduled/unscheduled layer.

### 2.4 Realm Grinder spells [S]
- Spells cost mana, run for a duration, and *multiple spells can be active at once* [S wikiwiki.jp snippet]. Examples: Call to Arms (400 mana, boosts building production for 20 s based on total building count) and Tax Collection (200 mana, collects 30 s of building + assistant production) [S: https://wikiwiki.jp/flyatama/Realm%20Grinder]. Mana regenerates slowly to max [S: supercheats mana page]. First tier of auto-cast sets one spell to fire whenever mana allows; **auto-cast halves mana regen and doesn't run offline** [S]. Gem Grinder is a neutral multi-tier spell, usually outperformed by the faction spell until max mana is boosted [S: https://realm-grinder.fandom.com/wiki/Gem_Grinder]. Good faction = more active/spell-oriented, Evil = idle [S Alignments].
- Takeaway: a **resource that refills over time (mana) with a menu of spells of different shapes**, and an *explicit offline cost for automating the active layer* (auto-cast offline off) - the clearest published example of "active layer is optional but better".

### 2.5 Idle Miner Tycoon [S/M]
- Kolibri's own stats: players get **316 boosts and 100 chests per hour** across the player base [S: https://www.kolibrigames.com/blog/what-happens-in-one-hour-of-idle-miner-tycoon/ - snippet]. Chests give worker cards (collection).
- Boosts: multiplier + duration + scope (one mine / all mines); stack multiplicatively [S bluestacks/appgamer]. Ad boost durations disagree across sources (2 h vs 4 h of x2) [S: appgamer]. Shop boosts x2 / x10 on cash and idle cash; expeditions/daily/event mines give up to x20 [S supercheats].
- Elevator/manager: managers automate each shaft; manager "perks" (e.g. movement speed boost) are manual-trigger temporary buffs to resolve a bottleneck, and must be re-activated when done [S: bluestacks]. I could not verify the "x3 super cash elevator boost" claim. The logistic bottleneck design (mine -> elevator -> warehouse, each with a throughput cap) *is* the decision: which stage is limiting [E].
- Barriers: unlocking the next shaft needs time, ad or Super Cash [S fandom].

### 2.6 AdVenture Capitalist [S/M]
- Events are scheduled-themed *alternate economies*: Mars and Moon, and recurring seasonal events (e.g. "Cashella" ran as a 2016 event and was replayed many times through 2023 [S: fandom]); event rewards need you to keep a fresh state ("take angels, have 0 upgrades, claim reward points, re-equip suits" [S: Steam thread]).
- Time Warps / Time Hops skip time to cash in angels [S Steam]; Gold gilds (Mega Tickets / Mega Bucks) boost planets; Mars has >600 unlocks and a click-on-spaceship event boost [S Steam]. Frequencies/durations not verified (I could not confirm "Time Hop" as a separate event mode; Time Warps are the item).
- Takeaway: AdCap's unscheduled layer is *calendar events that restart the economy* (scheduled), not random pops.

### 2.7 Antimatter Dimensions: no random events, active layer is timing
- Instead of random events AD rewards *when* you reset: Dimension Boost requirement is 20 of the (boosts+4)th dimension up to 8, then +15 per boost (code `amount += (targetResets-5)*(15-discount)`); Galaxy needs 80 8th dimensions +60 per galaxy (`baseCost 80`, `costMult 60`) [CODE: dimboost.js, galaxy.js]. The "active layer" is the optimal reset schedule + challenges, not pops.

### 2.8 Frequencies table (for Decade design)
| Game | Event | Gap | Window | Reward scale | Tag |
|---|---|---|---|---|---|
| Cookie Clicker | Golden cookie | 5-15 min (1.25-3.75 min fully upgraded) | 13 s (up to ~52 s) | x7 for 77 s / 15 min CpS / x777 for 13 s | CODE |
| Cookie Clicker | Reindeer (Dec) | 3-6 min | 4 s | cookies | CODE |
| Cookie Clicker | Sugar lump | 20-23 h | collect any time (overripe at 24 h) | 1 lump | CODE |
| Cookie Clicker | Pantheon swap | 1 h / 4 h / 16 h refill | - | slot change | CODE |
| Cookie Clicker | Garden tick | 3-15 min (soil) | - | plants mature in 1-10 ticks | CODE |
| Realm Grinder | Spell | mana regen bound; Call to Arms 400 mana/20 s | - | 20-30 s of production | S |
| Egg Inc | Drone | ~1 per few minutes [M] | seconds | GE 3-12 (elite 48+) | S/M |
| Idle Miner | Boost | ~300 per hour across players | hours | x2 .. x20 | S |
| AdCap | Event | days-weeks | event-long | alt economy | S |

---------------------------------------------------------------------------------------------------

## 3. Collection meta-systems

### 3.1 Achievements as multipliers
**Antimatter Dimensions** [CODE: src/core/achievements/normal-achievement.js lines ~167-172]
```
basePower = 1.25 ^ unlockedRows * 1.03 ^ effectiveCount
power = basePower ^ (effarigachievement glyph effect * Ra achievement-power unlock)
```
- Rows are 8 achievements; normal-achievements.js has 144 `id:` entries (18 rows of 8) [CODE]. If all rows are done and 144 counted: 1.25^18 * 1.03^144 = e^(4.017+4.257) ~ e^8.27 ~ **x3.9e3** (my arithmetic [E], excludes secret achievements and late-game exponent boosts).
- Interpretation [E]: ~65% of the log-multiplier comes from "individual achievements" and ~50% from "completing a row" - since the row bonus is x1.25 but one achievement is x1.03, completing 8 achievements gives 1.03^8 * 1.25 = 1.58, so *finishing rows is worth 25% of the total*, a "set bonus".
- Later layers (Reality) let you auto-unlock achievements on a timer (`timeToNextAutoAchieve`, `achievementPeriod`) - completionism becomes an idle activity.

**Cookie Clicker** [CODE: main.js 5240-5280, 3325-3416]
- Achievements do **not** multiply CpS directly. `Game.milkProgress = Game.AchievementsOwned/25` (each 25 achievements = one full "milk"). Kitten upgrades turn milk into CpS: `catMult *= (1 + milkProgress * 0.1 * milkMult)` for Kitten helpers; 0.125 workers; 0.15 engineers; 0.175 overseers; 0.2 managers; (later kittens up to 0.35?) [CODE: first five lines read]. With ~200 achievements (`new Game.Achievement(` occurs 206 times in main.js) milkProgress ~8 -> a +80% to +160% single-kitten-upgrade multiplier before milk mult (Santa 1.05, Breath of Milk 1.05, Mother god, garden "milk effects").
- So CC achievements are indirect: **milk -> kittens -> multiplier**. The "achievements make your CpS bigger" feeling is created by a purchasable upgrade chain, and *prestige* (heavenly chips: `prestige = (cookies/1e12)^(1/3)`, each chip +1% CpS (`heavenlyPower=1`)) is the main multiplier.
- Cookie Clicker's achievement *content* is also the tutorial (e.g. "Wake and bake", "Casual baking", "Clicktastic" ...) [M].

### 3.2 Card / worker collections
- **Idle Miner Tycoon**: chests -> worker cards, ~100 chests per hour across players [S Kolibri]; card sets provide bonuses [M]. 
- **Egg Inc**: artifacts (stones, ingredients, crafting) are a deep collection layer: drop-based with rarities; each gives +X% effects such as drone frequency or reward [S reddit]. 
- **Realm Grinder**: a "Gem Grinder"/trophies/relics layer [M], not verified.
- **Cookie Clicker**: seed log (garden), heavenly upgrades (~400+), cookie shop collections ("Dunk", seasonal cookie sets - each seasonal drop completes a set, which grants a permanent "season" achievement), shiny wrinklers, dragon auras [CODE/M].
- **Kittens Game**: building / science / workshop tech sets, "challenges completed", "zebra trades", and "void" items; achievements and badges [M].
- **Melvor Idle**: Mastery per item (1-99), skill capes (99 of everything), collection log of pets (one random pet per skill) [M].

### 3.3 Set bonuses
- AD rows (x1.25 per full row) are the cleanest *set bonus on achievements* [CODE].
- CC: owning N of a building gives named achievements and upgrade tiers (all at 1/5/25/50/100/150/200/250... [M]), and "upgrade tiers unlock at 1/5/25/50/100 buildings, each x2 for that building" - the same milestone ladder the project already uses (R3 in DESIGN_RULES.md).
- Takeaway for Decade: set bonus = a visible row or page of N slots; completing it gives a fixed multiplier; individual members give a small multiplier (AD 1.03 each vs 1.25 per row).

---------------------------------------------------------------------------------------------------

## 4. Onboarding: first 10 minutes (what unlocks when)

Data quality note: Cookie Clicker, Antimatter Dimensions and Kittens Game are from code [CODE]. For Egg Inc, Idle Miner, AdCap I could not get a verified timeline from the sandbox, so those are [M]/[E] and are marked "approximate".

### 4.1 Cookie Clicker [CODE main.js]
1. t=0: big cookie only. Click (1 cookie/click). Cookie counter, "Store" exists with Cursor (base 15) and Grandma (base 100) visible; others show silhouettes. Rule (line 17098): a building is revealed when `cookiesEarned >= basePrice || bought>0` - i.e. visible as soon as you have *earned* its price once.
2. ~0:15: 15 cookies -> Cursor (autoclicker 0.1 cookies/s, price grows x1.15 per copy: `priceIncrease=1.15`). First upgrade "Reinforced index finger" (x2 cursors) appears at ~1 cursor owned [M threshold].
3. ~1:30-2:00: 100 cookies earned -> Grandma (base 100, 1 cps).
4. Milestone: Farm base 1100 appears at 1100 earned (~3-5 min if clicking); Mine 12000 (~8-12 min). 
5. First golden cookie: the first spawn is drawn from the same uniform 5-15 min window (`getTimeMod(5..15)`) [CODE+E] - so one appears *by minute 5-15*, usually after the 10-minute mark. No tutorial overlay required.
6. News ticker + achievements ("Wake and bake" for 1 cookie...) give instant micro-goals; milk appears at 25 achievements.
7. Ascension is offered after 1e12 cookies for 1 chip (`prestige = (cookies/1e12)^(1/3)`), hours away; nothing in the first 10 min tells you about it. CC's first 10 min contain **no choices**, only "which building to buy".

### 4.2 Antimatter Dimensions [CODE dimboost.js, galaxy.js, normal-challenges.js]
1. t=0: antimatter counter and 1st Dimension ("buy 1st dimension" achievement), then 2nd, ..., each unlocked by buying the previous (cost multiples). Tickspeed upgrade appears early.
2. ~1-3 min: first Dimension Boost (needs 20 of the 4th dimension: `tier = targetResets+3`... first boost = 4th dimension x20) - unlocks 5th dimension and gives x2 on dims up to boost count.
3. ~5-10 min: 8 dimensions + Antimatter Galaxy (80 8th dimensions; +60 per galaxy; `baseCost 80, costMult 60`).
4. ~10-20 min: first Big Crunch at 1.8e308 (infinity). Offered tutorially via a "Big Crunch" button; first-time gives 1 Infinity Point and unlocks Infinity upgrades, Normal Challenges (first challenge C1 is "reach Infinity" itself, others locked until N infinities `lockedAt`).
5. Choices appear only after crunch (challenge order, infinity upgrades). The first 10 minutes are a "boost -> galaxy" linear ladder with the structure of 4 resets inside 10 min: (a) dimension buys, (b) boost, (c) galaxy, (d) crunch.

### 4.3 Kittens Game [CODE buildings.js, science.js, village.js]
1. t=0: only a "Gather catnip" button (each click = +1 catnip) and the log.
2. ~1 min: 10 catnip -> **Catnip field** (priceRatio 1.12, +0.125 catnip/tick base). Buildings are revealed when you hold 30% of the cost (`unlockRatio 0.3`); field has `unlockScheme: catnip threshold 56`.
3. ~2-4 min: catnip -> refine to wood (button), **Hut** (wood 5, priceRatio 2.5, `defaultUnlockable`, unlocks the "village" tab) - first kitten arrives and you assign it a job (woodcutter default; farmer unlocked after Agriculture).
4. ~4-6 min: **Library** (25 wood) -> scholar job -> science. First techs: Calendar (30 science), Agriculture (100), Archery (300), Mining (500), Animal husbandry (500); each unlocks building/job (farmer, hunter, miner...).
5. ~6-10 min: Barn, Mine (needs Mining tech), Workshop, Smelter after Metal (900); choices appear: which tech first, how to allocate kittens (woodcutters vs scholars vs farmers). The *first real decision* is job allocation under a catnip surplus constraint.
6. Seasons/weather (spring +50% catnip per a guide [S: deltiasgaming/other snippet, unverified; another forum post says summer +50%, winter -75%]) give a first hint of "events".

### 4.4 Egg, Inc. [M/S - approximate]
1. t=0: tap/hatch chickens in the first Hen House; you "run" chickens (tap to hatch, auto). Earn cash from eggs: first research ("Comfy Nests") in ~30 s.
2. 1-3 min: Common research + Hen House upgrade, new vehicle (egg transport), eggs per second visible as bars; first **drone** appears early [M] and teaches tapping (rewarded with cash/GE).
3. ~5 min: egg type upgrade (Edible -> Superfood) after reaching a threshold; the "contract" and "tokens" system comes in later; prestige is unlocked by completing the first soul-egg-rewarding mission [S: touchtapplay prestige page snippet]. Guides: wait for 50+ Soul Eggs early on or prestige when "it gets too slow" [S].
4. By 10 min you have bought research and can see the first Soul Egg mission; the first prestige typically comes in **the first hour** [M].

### 4.5 Idle Miner Tycoon [S/M - approximate]
1. t=0: "start continent", one Coal mine; tap to put the first mine shaft to work, manager hire after a little cash [S fandom snippet].
2. 1-3 min: add shafts (cost grows), elevator and warehouse upgrades appear as multiplier steps (x2 at 25/50/100 levels [M]).
3. ~5-10 min: first barrier "unlocks next shaft with time, ads or Super Cash" [S]; first boost offered by ad (x2 for a few hours depending on source: 2 h vs 4 h [S disagree]).
4. First chests (worker cards) and 316 boosts/h across player base [S] show the monetised layer by minute ~10.

### 4.6 AdVenture Capitalist [M - approximate]
1. t=0: lemonade stand, click to start a cycle; tap more cash; buy a second Lemonade; unlock Newspaper Delivery at $60 (a visible 2nd tier), then Car Wash $720 etc. Each tier costs about x10-12 of the last (R2 in DESIGN_RULES.md).
2. Managers (auto-run) are bought at about 1-3 min; each manager is a visible price unlock for a tier.
3. ~5-10 min: milestones x2 at 25/50/100... (bars show) [M]; angels not available until ~$1e15-1e16 total (approx. first hour) [M].

### 4.7 Cross-game onboarding pattern table (for the first 10 min)
| t | CC | AD | Kittens | Egg Inc | AdCap |
|---|---|---|---|---|---|
| 0:00 | click | buy dim 1 | gather catnip | tap/hatch | tap stand |
| 0:15-1:00 | cursor | dim 2 | field | research 1 | newspaper |
| 1-3 min | grandma | tickspeed, dim boost | hut + kitten | vehicle/hen house | manager |
| 3-6 min | farm | dim 5-8 | library, science | egg type | milestone |
| 6-10 min | mine, 1st golden | galaxy | techs, jobs | drones/prestige tease | angels tease |
| first real choice | >1 h | after Big Crunch (~10-20 min) | ~6-10 min (job allocation) | first research order ~1-2 min | managers vs next tier |
Summary: Kittens Game is the only one of the three code-verified games with a decision inside 10 min; AD and CC are linear until a reset or hour 1. Egg Inc is faster (research order) [M]. This supports R13 in DESIGN_RULES.md ("build fork in the first 5 min").

---------------------------------------------------------------------------------------------------

## 5. Implications for Decade idle game (no combat)

World frame (from DECADE_IDLE_DESIGN.md): Tsukasa photographs and restores worlds, 3-4-day worlds, 10-min sessions, Photo Op tap, Charge/Clock Up, Final Form Ride (layer 1), Dimension Ride (layer 2), Ride Cards, mastery tree, forms. All proposals respect "no punishment, nothing earned by decision is ever lost".

### 5.1 Unscheduled event: "Photo Window" (golden cookie analogue)
- **Spawn:** while foregrounded, uniform **90-240 s** (CC is 300-900 s but its sessions are hours; a 10-min session needs ~3-5 events). Offline: no spawns; instead bank **"Exposures"**: 1 per 30 min offline, cap 6 (so a night = 6 free windows, delivered as a "welcome-back" strip, not a pile).
- **Lifetime:** 15 s with the CC fade curve `1-(2t-1)^4`; x0.95 per extra window on screen; windows also show a pulse + sound.
- **No-repeat rule:** 80% re-roll away from the previous outcome (CC).
- **Outcomes** (weights): Windfall 35% (= min(15% of bank, 10 min of production) + 13, mirrors Lucky); Frenzy 30% (x7 production for 45 s - shorter than CC's 77 s because sessions are 10 min); Quick-shutter 15% (Photo Op power x20 for 10 s; CC click frenzy has x777/13 s but our tap is a minor source so x20); Spotlight 15% (x(owned/10+1) on one random tier you own >= 10 of, 30 s; keeps build identity); Ride Card shard 5% (1 of 5 shards = a Ride Card, ~1 card per 2 days of play).
- **Choice layer:** the window opens a 2-button card: SAFE (take the outcome as rolled) or DEVELOP (spend 1 Charge: 50% outcome x2, 50% outcome x0.5; EV 1.25). That's the "risk" option without combat or loss: worst case is half a reward.
- **Rate:** expected 2.6 windows per 10-min session x EV ~10 min production each => +40-60% effective production for an active session, +0% offline (offline gets the Exposure bank). Tune so Windows are 25-35% of active-session gain; the rest is passive (R14).
- **Upgrade track** (CC Lucky day / Serendipity pattern): 3 Studio upgrades: "Lucky Day" gap x0.5 (cost ~1 world-1 gate); "Lasting Exposure" window x2 (15 -> 30 s); "Golden Hour" effect duration x1.25. Floor gap 30 s so it never becomes spam.

### 5.2 Loadout: "Form Deck" (Pantheon analogue)
- 6 Rider Forms per world (Kabuto Rider Form, Hyper Form, ...), 3 slots (Main, Support, Finisher) with strengths 3:2:1 (e.g. +15% / +10% / +5% production for the tier the form governs).
- Every form has a plus and a minus column: e.g. Hyper Form: Charge fills 20% faster / Photo Op gives 10% less; Wizard-like Water Style: offline x1.3 / active x0.9 (note: just an example vocabulary).
- **Swap budget:** 3 Swap Tokens, refill 20 min / 90 min / 6 h (scaled so a 10-min-session player gets a free swap per session and a heavy swapper pays; CC uses 1 h/4 h/16 h for hour-long sessions).
- **Respec cost:** CC's dragon aura sells 1 top building. Decade version: changing a slot costs **1 of your top-tier unit** ("Costs 1 Shutter Drone") and is free when the slot is empty. The cost is trivial late (1 of 200) and noticeable early.
- Target: 6 forms x 3 slots = 120 ordered arrangements; the designer picks the numbers so top-3 loadouts are within 15% of each other (R-tag [E]; sim needed).

### 5.3 "Studio Garden" (Garden analogue, spatial puzzle, slow tick)
- 3x3 board unlocked at first Ride (min 8-10); grows to 4x4 at world 3 and 5x5 at world 6 (CC plotLimits ladder 2/2/4/4 -> 6x6 over 9 levels).
- Tiles = **Ride Cards** placed on adjacency grid; a card gives its bonus +50% if a matching card is orthogonally adjacent (set bonus by position).
- **Tick:** growth/charge on a 5-minute tick while open, or 1 tick per 30 min offline, max 12 banked. Soils analogue: three "Backdrops" (Studio: tick 3 min, effect x0.75; Street: tick 5 min x1; Gallery: tick 15 min, x1.25) - the visit-frequency choice.
- Mutation analogue: placing two specific cards adjacent for 3 ticks has a 10% chance per tick of producing a hidden "Fusion Card" (new album entry). 6-8 fusions per world, discoverable by experiment; hints in the album.
- Per-card effect size: +1 to +3% production per card (CC plants: +1% to +3%); full 9-card board ~+20-25% production.

### 5.4 Challenges: "Constraint Shoots" (AD / Kittens)
- Each world has **2 optional challenges** unlocked at the world's mid point (Ride #4). Each removes one verb: "No Charge" (Clock Up disabled), "Single Lens" (only 3 tiers buyable), "Slow Shutter" (buying a tier halts production for 60 s, recovering linearly - AD C2).
- Run length: 10-20 min, one session. First-clear reward is **an automation** (auto-photo, auto-buy tier N, auto-ride) or a permanent x1.15 (AD style: automation or exclusive multiplier). Repeat clear gives +5% with the goal x3 each time (EC goalIncrease), max 3 repeats.
- Unlock only after the base verb has been used 5+ times, to avoid hidden rule shocks.
- Budget: 9 worlds x 2 = 18 challenges -> total multiplier ~x1.15^18 = x12 if all multiplicative; make 10 of them automation (not multiplier) so the max stack is x1.15^8 = x3.1.

### 5.5 Job-assignment layer ("Crew", Kittens analogue)
- A pool of **crew** (Photographers, Archivists, Restorers, Couriers...). Crew count: starts 3, +1 per world milestone, to 12 by the end of world 3 and ~30 at campaign end (Kittens uses huts growing to hundreds; keep ours small for mobile).
- Jobs produce different resource types (Shots, Film, Culture, Charge) with CC-like rates (e.g. Photographer 0.5 shots/s, Archivist 0.02 Film/s, Restorer 0.01 Culture/s). Re-assign instantly, free; each job has a diminishing return per assignee (x0.95 per extra), so splitting beats stacking.
- The crew decision is the player's "build fork" in the first 5 minutes (R13): by minute 4 the player must pick which 3 jobs to run.

### 5.6 Faction-style per-world pick (Realm Grinder analogue)
- At world entry, choose 1 of 3 **Approaches** (Documentary / Portrait / Landscape): +25% to one tier family, -10% to the other, plus 1 unique Window outcome. Locked for the world (3-4 days), re-pickable at the next world. Costs nothing but is a run-level decision (RG).
- Provide a "preview" with before/after production numbers; re-pick allowed once with a Dimension Ride token.

### 5.7 Collection and achievements
- **Album = Collections:** per world, 1 Album page: 16 entries (6 Rider Cards, 4 Fusion Cards, 6 location shots). 9 worlds x 16 = 144 entries (coincides with AD's 144 achievements; also 18 rows of 8 if two pages per world).
- **Achievement multiplier (AD formula, damped):** `power = 1.05 ^ completedRows * 1.01 ^ achievementCount` where a row = 8 achievements. With 144 achievements and 18 rows: 1.05^18 * 1.01^144 = 2.41 * 4.19 = **x10.1** at 100% [E calc]. At world 3 (48 achievements, 6 rows) it's 1.34 * 1.61 = x2.2. The AD originals (1.25 and 1.03) reach x3.9e3, which our shorter game cannot absorb (R-rule on stacking). Keep the cap lower and apply the multiplier to **base Shots only** (not to Form Energy) to avoid compounding with prestige.
- **Milk-like indirect:** cap CC-style: `Album fill ratio / 25 = "Reel"` (every 25 achievements one film reel) and "Cameraman" upgrades convert reels to production (CC kittens 10%-20% per milk). Optional.
- **Rows as set bonuses:** a complete row shows a golden frame and +5% (the 1.05 above); the incomplete row displays a "n/8" bar (R4 goal-gradient).
- **Seeds/Fusion cards as discovery** (Garden-style mutation) give 40-50% of the album, so the album has a discovery arc, not only purchasing.

### 5.8 Onboarding: first 10 minutes of Decade (steps, with time targets; extends R10-R13)
| t | Unlock | Why (source) |
|---|---|---|
| 0:00 | Photo Op button (1 shot/tap), shot counter | CC click, Kittens gather |
| 0:20 | Tier 1 "Film Roll" (cost 15, growth 1.12) | CC cursor 15 |
| 0:45 | Tier 1 auto-runs; first x2 milestone bar visible ("x2 in 9") | R3/R4 |
| 1:30 | Tier 2 visible at 5 owned of T1 (R5); cost x10 | R2/R5 |
| 2:00 | **Crew tab**: pick 3 jobs (first fork) | Kittens at 6-10 min is too late; we fork at 2:00 |
| 3:00 | First **Photo Window** (forced spawn for the tutorial: the first window is guaranteed in 150-180 s, then random 90-240 s) | CC's first golden at 5-15 min is too late for our sessions |
| 4:00 | Tier 3 + first Form (free "Kabuto Rider Form" in the Main slot) | Pantheon slot teaching |
| 5:30 | Album page opens, first entry auto-awarded (endowed progress, R30) | psychology |
| 7:00 | Tier 4; first automation (auto-buy T1) | R10 first automation ~3 min is too early for the first fork; use 7:00 for the second |
| 8:00 | "Final Form Ride" preview ("+31% production for the next run", R18) | R16 first ride by ~10-15 min |
| 10:00 | Final Form Ride available; welcome-back card ("Exposures banked: n") set | R10-R11 |
- Verified comparisons: Kittens first decision at ~6-10 min; CC none until >1 h; AD after crunch (10-20 min); Decade puts first fork at 2:00, first event at 3:00, first Ride preview at 8:00 (all [E]; must be play-tested).

### 5.9 Numbers to simulate before locking (priority list)
1. Window frequency x EV so that Windows contribute 25-35% of active-session income (simulate with the existing sim/ greedy player + a reaction model: 60% hit rate).
2. Form Deck: top-3 loadouts within 15% (simple enumeration of 6P3 = 120).
3. Achievement formula cap: `1.05^rows * 1.01^count` vs world carry c (so total multiplier from collections does not exceed ~10x).
4. Challenge reward budget: automations vs multipliers (<= x3.1).
5. Garden-like board: 9 cards -> +20-25%; verify adjacency rule can't produce >+35%.

### 5.10 What NOT to copy
- CC's golden-cookie negative outcomes (wrath, ruin, clot) - Decade is "no punishment" (R14); instead the downside is opportunity (a 50% half-reward gamble).
- Realm Grinder's auto-cast-off-offline penalty: simply don't penalise offline; give a bank instead.
- Pantheon's "golden cookie click unslots the god" interaction: too hidden for a mobile idle game.
- Egg Inc's gifted boosts and tokens economy: monetisation-shaped; skip unless planned.

### 5.11 Open questions / things I could not verify
- Egg Inc drone spawn interval, common research tier count, exact first-hour timeline.
- Realm Grinder faction numbers and spell cooldowns (only Call to Arms 400 mana / 20 s and Tax Collection 200 mana / 30 s from a Japanese wiki snippet).
- AdCap event frequencies and durations; Idle Miner elevator boost durations.
- Cookie Clicker early-upgrade thresholds (cursor first upgrade) and wrinkler numbers are from memory.
- NGU unlock bosses (4/17/30/37) come from a third-party site.

## 6. Source URL index
- Cookie Clicker mirror (code): https://raw.githubusercontent.com/ozh/cookieclicker/gh-pages/main.js ; .../minigamePantheon.js ; .../minigameGarden.js ; .../minigameGrimoire.js
- Antimatter Dimensions code: https://raw.githubusercontent.com/IvarK/AntimatterDimensionsSourceCode/master/src/core/achievements/normal-achievement.js ; .../src/core/secret-formula/challenges/{normal,infinity,eternity}-challenges.js ; .../src/core/dimboost.js ; .../src/core/galaxy.js ; .../src/core/secret-formula/achievements/normal-achievements.js
- Kittens Game code: https://raw.githubusercontent.com/nuclear-unicorn/kittensgame/master/js/{village,religion,buildings,science,challenges,workshop}.js
- Realm Grinder: https://realm-grinder.fandom.com/wiki/Alignments ; https://realm-grinder.fandom.com/wiki/Gem_Grinder ; https://realm-grinder.fandom.com/wiki/Research ; https://www.pcgamer.com/realm-grinder-guide/ ; https://www.supercheats.com/realm-grinder/walkthrough/factions ; https://www.supercheats.com/realm-grinder/walkthrough/mana ; https://wikiwiki.jp/flyatama/Realm%20Grinder
- Egg Inc: https://egg-inc.fandom.com/wiki/Prestige?oldid=9210 ; https://www.touchtapplay.com/egg-inc-best-upgrades/ ; https://www.touchtapplay.com/egg-inc-how-to-prestige/ ; https://egg-inc.fandom.com/wiki/Version_History?oldid=6892 ; https://en.wikipedia.org/wiki/Egg,_Inc.
- Idle Miner: https://www.kolibrigames.com/blog/what-happens-in-one-hour-of-idle-miner-tycoon/ ; https://www.bluestacks.com/blog/game-guides/idle-miner-tycoon/idt-tips-tricks-en.html ; https://www.appgamer.com/idle-miner-tycoon/strategy-guide/what-are-boosts-for-and-how-do-i-use-them-in-idle-miner-tycoon ; https://www.supercheats.com/idle-miner-tycoon-cheats-tips-strategy/walkthrough/how-to-get-boosts
- AdCap: https://adventure-capitalist.fandom.com/wiki/Cashella ; https://steamcommunity.com/app/346900/discussions/0/1639788130266895690
- Melvor: https://steamcommunity.com/app/1267910/discussions/0/3199241400250725473 ; https://earlyguides.com/melvor-idle/beginners-guide
- NGU Idle: https://steamcommunity.com/app/1147690/discussions/0/2646360821011099471 ; .../2794999575673906748 ; .../3111405265471869154 ; https://earlyguides.com/ngu-idle/beginners-guide ; https://ngu-idle.fandom.com/wiki/New_Player_Guide_(Truth)
