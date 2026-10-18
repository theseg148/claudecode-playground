# Source-verified formula comparison

Every row tagged [CODE] was read from the game's open-source repository this session (raw.githubusercontent.com); file paths and line numbers are in each game's `## Source-verified formulas` section in `games/<game>.md`. Round 2 (below) resolves AD IP/EP, Kittens game.js, Synergism offline cap and Cookie Clicker (public mirror). Still not found: Candy Box 2 source, see "Round 2 > Still unverified".

## 1. Cost ratio per building / purchase

| Game | Cost formula | Ratio (per purchase) | Cite |
|---|---|---|---|
| Antimatter Dimensions (AD) | `base * ratio^floor(bought/10)`, then quadratic-log scaling past 1.79e308 | Per block of 10: tier1 1e3, t2 1e4, t3 1e5, t4 1e6, t5 1e8, t6 1e10, t7 1e12, t8 1e15; bases 10, 100, 1e4, 1e6, 1e9, 1e13, 1e18, 1e24. Tickspeed: 1000 x 10^n | [CODE] antimatter-dimension.js L337-363, tickspeed.js L154 |
| AD Infinity Dim | `base * mult^n` | x1e3, 1e6, 1e8, 1e10, 1e15, 1e20, 1e25, 1e30; base 1e8..1e280 | [CODE] infinity-dimension.js L53-57 |
| AD Time Dim | `base * mult^n`, x1.5 past 1.8e308, x2.2 past 1e1300 | x3, 9, 27, 81, 24300, 72900, 218700, 656100 | [CODE] time-dimension.js L145-175 |
| Kittens Game | `val * ratio^count * (1-discount)` | field 1.12, hut 2.5, barn 1.75, most buildings 1.15, later 1.25-1.75; ratio floor via limited DR | [CODE] buildings.js L2589-2607, L358, L491 |
| A Dark Room | LINEAR: trap `10+10n`, hut `100+50n`, hard caps (traps 10, huts 20) | n/a (linear) | [CODE] room.js L13-58 |
| Trimps | `base * ratio^owned` (geometric bulk sum) | Hut 1.24, House 1.22, Mansion 1.20, Hotel 1.18, Resort 1.16, Gateway 1.14, Collector 1.12, Gym 1.185, Tribute 1.05, Warpstation 1.4 | [CODE] main.js L4824; config.js L11501-11740 |
| Synergism | `baseCost * 1.25^(growth*owned)`, extra softcaps at 1k/5k/20k/250k owned | per tier 1.25^growth: coin 1.25 / 1.5625 / 1.953 / 2.441 / 3.052; diamond & mythos 1.25 / 1.953 / 3.815 / 9.31 / 28.4; tesseract bldgs cubic `base*(n+1)^3` | [CODE] Buy.ts L14-40, L131-195, L666 |
| Evolve | `round(ratio^count * base)`, ratio floor 1.005 | basic housing 1.17 (money) / 1.23 (lumber), cottage 1.15 / 1.25, farm 1.32 / 1.36, lumber yard 1.85-1.95, smelter 1.32-1.33, mine 1.6 / 1.38, warehouse 1.26 | [CODE] functions.js L776-833; actions.js |
| Bitburner (Hacknet) | node `1000 * 1.85^(n-1)`; upgrades level 1.04, RAM 1.28, core 1.48; servers x3.2 | 1.85 / 1.04 / 1.28 / 1.48 | [CODE] Hacknet/data/Constants.ts, formulas/HacknetNodes.ts L87-92 |
| Progress Knight | XP to level L: `maxXp*(L+1)*1.01^L` | 1.01 per level (x linear) | [CODE] classes.js L10-12 |

## 2. Milestone / power multipliers

| Game | Rule | Cite |
|---|---|---|
| AD | x2 per 10 bought of a tier (`buyTenMultiplier` base 2); Dimension Boost base x2; Galaxy: tickspeed per purchase 1.1245 (0 gal), 1.11889 (1), 1.11267 (2), then `0.02*effects` per galaxy step | [CODE] antimatter-dimension.js L632-636; dimboost.js L16-29; tickspeed.js L38-52 |
| AD Infinity Dim | x50 / 30 / 10 / 5 per 10 bought (tiers 1/2/3/4..8) | [CODE] infinity-dimension.js L55, L151 |
| Kittens | Paragon: +1% production per paragon (cap 2x ratio), +10% storage per 100 paragon; +1 paragon per 1000 years | [CODE] prestige.js L553-576; calendar.js L968-972 |
| Trimps | Perk Power +5%/level, Looting +5%/level, Carpentry +10%/level compounding; equipment prestige stat x1.19, cost x1.069 | [CODE] config.js L2852-2995; main.js L5953-5970 |
| Synergism | accelerator power baseline 1.1; late buildings x1.03 per extra owned past 250k | [CODE] Synergism.js (v2.1.2) L1613; Buy.ts L180-186 |
| Bitburner | Hacknet RAM x1.035 per RAM unit; cores `(cores+5)/6`; level linear x1.5 | [CODE] HacknetNodes.ts L4-11 |
| Progress Knight | job income mult `1+log10(level+1)`; skill effect `1 + 0.01*level`; Time warping `1+log13(level+1)`; Immortality `1+log33(level+1)`; XP `1 + maxLevel/10` | [CODE] classes.js; main.js L263-290 |
| A Dark Room | none (flat per-worker +1 / -N input/output chains) | [CODE] outside.js L13-95 |

## 3. Prestige formulas

| Game | Formula | Gate | Cite |
|---|---|---|---|
| AD | Infinity at 1.79e308 antimatter (`Decimal.NUMBER_MAX_VALUE`); IP formula not located | cap 1.79e308 | [CODE] tickspeed.js L131-135 (gate only) |
| Kittens | faith: `faithRatio += faith/1e6 * (tier+1)^2 * bonusRatio`; apocrypha bonus `getUnlimitedDR(faithRatio,0.1)*0.1` | faith accumulated before adoring | [CODE] religion.js L1549-1651 |
| Trimps | Helium perks cost `ceil(L/2 + priceBase*1.3^L)`; equipment `1.19^p` stat vs `1.069^p` cost | per zone | [CODE] main.js L3846-3880, L5953-5970 |
| Synergism | Prestige `floor((coins/1e12)^0.5)`; Transcend `floor((coins/1e100)^0.03)`; Reincarnation `floor((shards/1e300)^0.01)` | prestige at 1e16 coins or >=100 pt; transcend at 1e100 or >=0.5 | [CODE] Synergism.ts L3434-3456; Synergism.js(v2.1.2) L2321-2380 |
| Evolve | `plasmid = round(pop/divisor) + steps(knowledge, k_inc, k_mult)`; divisor 3 / 3 / 2.5 / 2.2, k_inc 1e5 / 5e4 / 4.5e4 / 4e4, k_mult 1.1 / 1.015 / 1.014 / 1.012 (MAD/bioseed/AI/big bang); cap 150 / 400 / 600 / 800 with overflow `o/(o+cap)*cap`; `phage = floor(log2(plasmid)*e*phage_mult)`; effect `ln(1+p/50)/2.888` | softcapped | [CODE] functions.js L1494-1660; resources.js L3238-3246 |
| Bitburner | Augmentation install; price x1.9 per aug bought, NeuroFlux x1.14 per level; rep donate $1e6 = 1 rep after favor 150 | rep gated | [CODE] Constants.ts L35-45 |
| Progress Knight | Rebirth 2 adds `evil += evilControl.effect * bloodMeditation.effect`; rebirth 1 keeps max levels (+10% XP/level) | age 70y (`365*70` days) | [CODE] main.js rebirthTwo, getEvilGain L318-323 |

## 4. Offline / time constants
| Game | Value | Cite |
|---|---|---|
| Bitburner | offline script income x0.75; 200 ms/cycle | [CODE] Constants.ts L18-22 |
| Kittens | 10 ticks/day, 100 days/season (400-day year) | [CODE] calendar.js L217-218 |
| A Dark Room | villager every 0.5-3 min; worker tick 10 s; fire cools 5 min | [CODE] outside.js, room.js |
| Progress Knight | baseGameSpeed 4, updateSpeed 20 | [CODE] main.js L27-31 |

## 5. Quick design reads (for the Rider idle)
1. Ratio bands: 1.12-1.15 (Kittens/Trimps late) feels slow-gentle; 1.25 (Synergism T1) normal; 1.85 (Bitburner nodes) / 2.5 (Kittens hut) used to gate how many you ever own.
2. Cheap "block" multipliers (AD x2 per 10) pair with a 10x-per-block cost step to keep breakpoints readable.
3. Prestige exponents fall per layer (Synergism 0.5 -> 0.03 -> 0.01; Evolve log scale), keeping reset gains small even when raw currency explodes.
4. Linear costs with hard caps (A Dark Room) produce a story-paced, non-exponential early game.

## Round 2

Sources: IvarK/AntimatterDimensionsSourceCode `src/game.js`, `src/core/machines.js`; bloodrizer/kittensgame root `game.js`; ozh/cookieclicker (gh-pages) `main.js`; ianfixes/universal_paperclips `main.js`/`globals.js`; Pseudo-Corp/SynergismOfficial `src/Calculate.ts`; Acamaeda/The-Modding-Tree `js/game.js`; jacorb90/Prestige-Tree `js/layers.js`. Details and excerpts in `games/*.md` (`### Round 2` / `## Source-verified formulas`). Resolves the earlier "not found" items for AD IP/EP, Kittens game.js, Synergism offline, and Cookie Clicker (a public mirror exists, so "closed source" is superseded). All [CODE].

### R2.1 Prestige gain formulas
| Game | Formula | Cite |
|---|---|---|
| AD Infinity Points | broken: `10^(log10(maxAM)/308 - 0.75) * mult` (floor); unbroken: 1 IP | game.js L89-118 |
| AD Eternity Points | `5^(log10(IP)/308 - 0.7) * mult` (x5 per +308 OoM of IP); min IP 1.79e308 | game.js L138-163 |
| AD Reality Machines | `1000^(log10(EP)/4000 - 1) * mult`, `<10` uses linear `27/4000*logEP - 26`; hardcap 1e1000; pre-Reality log cap 8000 (75% penalty past 6000) | machines.js L1-32 |
| Kittens reset | paragon = `kittens - 70` (>70); karma kittens piecewise +1/+3/+4/+5/+10/+15 per kitten past 35/60/100/150/300/750 | game.js `getResetPrestige` |
| Cookie Clicker | `prestige = (lifetimeCookies/1e12)^(1/3)` (HCfactor 3), +1% CpS per level | main.js L4185-4192 |
| Modding Tree "normal" | `floor(((base/req)^exponent * gainMult)^gainExp)`, softcap `g^p * c^(1-p)` | game.js L10-33 |
| Modding Tree "static" | `floor(log_base(base/req/gainMult)*gainExp)^(1/exponent)`; cost of n-th = `req * base^(n^exponent/gainExp)` | game.js L24-60 |

### R2.2 Cost curves
| Game | Formula | Cite |
|---|---|---|
| Cookie Clicker | `base * 1.15^(owned-free)`; bases generated: `(n+9+[n>=5](n-5)^1.75*5)*10^n*max(1,n-14)` (2 sig. digits), CpS `n^(0.5n+2)`; Grandma 100/1 ... Portal 1e12/1e7 ... You 5.4e26/5.1e14 | main.js L7972, L8018-8031 |
| Universal Paperclips | AutoClipper `1.1^n+5`; MegaClipper `1000*1.07^n`; ads x2 per buy, effect `1.1^(lvl-1)`; wire +0.05 per buy, -0.1%/250 ticks, +-6 sine noise | main.js L1661, L1674, L2334, L3341, L12-50 |
| Prestige Tree (jacorb90) | P: req 10, exp 0.5 (normal); Boosters req 200 exp 1.25 base 5 (static); Generators req 200 exp 1.25 base 5; Time/Space (1e120+ req) exp 1.85 base 1e15; Enhance exp 0.02; Hindrance req 1e30; Quirk req 1e512 | layers.js L1-30, L281-293, L552-564, L897-918, L1302-1321 |

### R2.3 Timers, caps and offline
| Game | Value | Cite |
|---|---|---|
| Cookie Clicker golden | spawn gap 5-15 min base (x0.5 Lucky day, x0.5 Serendipity, x0.95 Golden goose egg...), lifetime 13 s | main.js L5934-6000, L5617 |
| Cookie Clicker offline | needs Twin Gates: 1 h cap (doubles per 7 demon upgrades) at 5% + 10%/angel tier (max 75%); past cap 10% rate; Perfect idling = unlimited 100% | main.js L3537-3580 |
| Cookie Clicker misc | wrinkler hard limit 14; Radiant Appetite aura x2 production; Dragon's Fortune +123% per golden | main.js L14589, L15158 |
| Synergism offline | cap 72 h + 4 h each of research 31/32, x paid buff; simulated in 200 ticks | Calculate.ts L826-840 |
| AD offline | Infinity upgrade `ipOffline`: 50% of best IP/ms; default `offlineTicks` 1e5 | game.js L935; player.js L798 |
| Modding Tree | template `offlineLimit: 1` hour | mod.js |
| UPC | ops cap = memory*1000; trust at Fibonacci*1000 clips (3000, 5000, 8000, 13000...); matter 6e27 galaxy / 3e55 universe | main.js L2436, L2606; globals.js |

### R2.4 Open-source zone/world progression
Gooboo (Tendsty/gooboo, `src/js/modules/horde.js`, `horde/upgradePrestige.js`) was found: prestige upgrade costs like `100*1.55^lvl` (butcher), `1000*(1.55+0.01*lvl)^lvl` (precision/resolve), attack/health per level x1.15. The per-zone enemy HP/gold scaling file was not located (zone data not in the paths tried). No open-source Clicker Heroes clone with the canonical `1.55^zone` HP curve was found via code search.

### R2.5 Still unverified
Cookie Clicker lifetime-to-chip in-game Heavenly upgrade prices beyond the list above, wrinkler suck rate; UPC drone/probe/combat constants (only partially read); Kittens production multipliers in `resources.js`/`village.js` (downloaded, not parsed); AD Time Study/Dilation EP formulas; Trimps/Clicker Heroes zone HP scaling in the Gooboo-like clones; Idle Game Maker not searched; the live Paperclips site may differ from the ianfixes mirror version.
