# Progress Knight
**Sources:** (URLs, required)
- https://github.com/ihtasham42/progress-knight (original, by ihtasham42); formulas below fetched from raw `js/main.js` and `js/classes.js` on master: https://raw.githubusercontent.com/ihtasham42/progress-knight/master/js/classes.js
- https://ihtasham-42.itch.io/progress-knight (community comments about rebirth, max-level multiplier)
- https://apps.apple.com/mx/app/progress-knight-remastered/id6450839683 (Remastered: evil/angelic path choice)
- Confidence legend: [CODE] = read from source code; [COMMUNITY] = player comments; [EST] = my estimate/recollection, unverified.
## Core loop
- You are a character who ages. Each in-game day you pick ONE job (earns coins, gains job XP) and several skills (gain skill XP). 
- Days tick fast; at age ~65-70 you start to die [CODE: baseLifespan = 365*70 days].
- Death/rebirth resets almost everything but each task remembers its best level (`maxLevel`), which boosts future XP gain.
- The "world" is a career ladder: Beggar -> Farmer -> Fisherman -> ... -> Squire -> Knight -> Mage tiers. Each tier unlocks by level of previous job + skills.
- Players run a short lap (15-70 years), look at what got unlocked, and run again faster.
- Housing (Tent, House...) and items boost happiness / XP; they cost coins per day, so income vs expenses is a mini-economy.
## Resource types
- Coins (income minus daily expense from housing + items). 
- Days / Age (the real clock; lifespan is the soft timer).
- Task XP and Task Level (jobs, skills). Max level per task remembered across rebirths.
- Happiness (multiplier on all XP; from Meditation, Butler, property).
- Evil (prestige currency, "Rebirth Two"), earned from Evil Control skill x Blood Meditation.
- Later layers (versions vary) [COMMUNITY]: Essence of the Unknown, Dark Orbs/Dark Magic skills in forks; exact names differ per fork.
- Rebirth counters: `rebirthOneCount`, `rebirthTwoCount` [CODE].
## Cost & production growth formulas (public or estimated; mark which)
- XP needed for next level: `round(baseMaxXp * (level+1) * 1.01^level)` [CODE]. Linear-times-slow-exponential: levels get gentler than usual idle curves.
- Base maxXp examples [CODE]: Beggar 50; larger for later jobs (hundreds of thousands+ by endgame [EST]).
- XP gain per tick base: `10`, multiplied by xpMultipliers list [CODE].
- Max-level multiplier: `1 + maxLevel/10` per task [CODE]. A task whose best-ever level is 100 gets x11 XP next life.
- Job income level multiplier: `1 + log10(level+1)` [CODE]. Logarithmic: levels matter but with strongly diminishing returns.
- Lifespan: `365*70 * immortality * superImmortality`; Immortality = `1 + log33(level+1)` [CODE].
- Time Warping speed: `1 + log13(level+1)` [CODE].
- Bargaining/Intimidation expense reduction: `1 - log7(level+1)/10`, floor 0.1 [CODE].
- Game speed: baseGameSpeed 4, updateSpeed 20 => each tick = 0.2 day at 1x [CODE].
- Rebirth start age 14 (`days = 365*14`) [CODE].
- Unlock costs scale off item expense, e.g. Library unlock = Library expense x100, shop = Tent expense x50 [CODE].
- Logs everywhere: log-based effects make every skill "worth leveling a bit" but never dominant.
## Prestige structure
- Rebirth One (die/retire): resets levels/XP/coins; keeps maxLevel per task; increments `rebirthOneCount`. Fast, frequent, voluntary at any time (button).
- Rebirth Two ("Evil" / Rebirth of the soul): `evil += getEvilGain()`, then resets and sets every task's `maxLevel` to 0 [CODE]. This is a hard layer reset; you give up the max-level multipliers for a global evil multiplier.
- Evil gain = `evilControl.effect * bloodMeditation.effect` [CODE]; the effect formulas per skill are in task data.
- Layers: (1) one life, (2) maxLevel memory across lives, (3) evil across all memory. Each layer has a very different feel.
- Typical run counts [COMMUNITY/EST]: first Knight rank in 3-6 lives; first evil in 10-30 lives.
## Unlock pacing
- Content is a tree gated by "level X in job/skill Y". Early gates take under a minute; later gates take multiple lives [EST].
- Jobs unlock more jobs, skills unlock more skills, and each tier doubles back onto already-seen content with better multipliers.
- Max-level carry makes unlocks cheaper on subsequent lives; the player feels the same ladder shrinking.
- Evil unlocks: new tabs/skills ("Demon's wealth", evil-only jobs) that pay off later.
- The age clock forces a tradeoff each life: push a job for coins vs skill XP.
## Offline progress
- None in the original (browser tab must stay open; speed can be toggled, paused, time-warped) [CODE: `+!gameData.paused * +isAlive()`].
- Time Warping skill speeds things in-session (log13 curve), substituting for offline gains.
- Forks / Remastered mobile version may add idle gains [EST].
## Monetization effects
- Original is free, no monetization (itch.io/GitHub).
- Remastered iOS version: paid/free with possible ads/IAP [EST, unverified].
- Result: purely design-driven pacing; no timers to sell.
## What players love
- Short lives with visible improvement: "just one more life".
- Clear numerical feedback of the max-level multiplier: each life is a measurable gain.
- Tight unlock tree with real tradeoffs (what to train in a limited life).
- Log-based formulas keep effects readable and bounded.
- Dark/humorous flavor, e.g. evil path.
## What players hate
- Browser-only play; no offline; saves lost if cache cleared [COMMUNITY].
- Mid-game plateau waiting for lifespan skills before progress; repetition of identical lives.
- Opaque requirements for late unlocks (need wiki/guide).
- Forks fragmenting community, differing numbers.
## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Each Rider world could be one "life": a bounded timer after which the world resets, but a remembered best result ("max level") multiplies the next visit. Formula to copy: `mult = 1 + best/10`.
- Use log-shaped bonuses for secondary stats so no upgrade trivializes a world.
- XP cost `base*(n+1)*1.01^n` is gentle; for a no-fight game use that as the per-card/form upgrade curve so players always see progress.
- Decade's world-hopping fits "Rebirth One" (leave world, keep best) vs "Rebirth Two" (Final Form Ride: reset memory for a permanent global multiplier, i.e., Evil -> "Kamen Ride power").
- Make each world's ladder different (different job/skill tree per Rider) but reuse the same carryover rule so the player understands it.
- Add a small economy tension (coins vs upkeep) to make choices meaningful without combat.
- Offline is a gap to fix: unlike Progress Knight, grant offline progress at a reduced rate so the mobile loop works.


## Source-verified formulas
All excerpts [CODE] from `ihtasham42/progress-knight` (branch `master`). Base: `https://raw.githubusercontent.com/ihtasham42/progress-knight/master/` (files `js/classes.js`, `js/main.js`).

**Task XP requirement** [CODE] `js/classes.js` L10-12, L18-25, L27-29
```js
getMaxXp() { return Math.round(this.baseData.maxXp * (this.level + 1) * Math.pow(1.01, this.level)) }
getMaxLevelMultiplier() { return 1 + this.maxLevel / 10 }       // +10% XP per previous-life max level
getXpGain() { return applyMultipliers(10, this.xpMultipliers) }  // 10 xp base per second-tick
```
So XP to level L is `base * (L+1) * 1.01^L` (polynomial x mild exponential, ratio 1.01 per level).

**Job income** [CODE] `js/classes.js` L51-54: `getLevelMultiplier() = 1 + Math.log10(this.level + 1)` (log growth); `getIncome() = applyMultipliers(baseData.income, incomeMultipliers)`.
Job base table [CODE] `js/main.js` L36-57 (name: maxXp, income): Beggar 50/5, Farmer 100/9, Fisherman 200/15, Miner 400/40, Blacksmith 800/80, Merchant 1600/150, Squire 100/5, Footman 1000/50, Veteran footman 1e4/120, Knight 1e5/300, Veteran knight 1e6/1000, Elite knight 7.5e6/3000, Holy knight 4e7/15000, Legendary knight 1.5e8/50000, Student 1e5/100, Apprentice mage 1e6/1000, Mage 1e7/7500, Wizard 1e8/50000, Master wizard 1e10/250000, Chairman 1e12/1e6.

**Skill effects** [CODE] `js/classes.js` `getEffect() = 1 + baseData.effect * level` (linear +1%/level), special log effects in `js/main.js` L263-290:
```js
Bargaining/Intimidation: 1 - getBaseLog(7, level+1)/10   (floor 0.1)
Time warping:  1 + getBaseLog(13, level+1)    // gamespeed
Immortality:   1 + getBaseLog(33, level+1)    // lifespan
```
**Constants / rebirth** [CODE] `js/main.js`: `updateSpeed = 20`, `baseGameSpeed = 4`, `baseLifespan = 365 * 70` days. Homes: Homeless 0, Tent 15/1.4x, Wooden hut 100/2x, Cottage 750/3.5x, House 3000/6x, Large house 25000/12x, Small palace 300000/25x, Grand palace 5e6/60x (expense/day, happiness multiplier) [CODE] L85-92. Rebirth 2 grants `gameData.evil += getEvilGain()` where evilGain = Evil control x Blood meditation effects (L318-323).

**Design takeaways**: income within one job grows only with log10(level), so the long-term lever is *new* jobs (maxXp and income both roughly 10x per tier at the top end) and rebirth multipliers (+10% XP per prior max level).
