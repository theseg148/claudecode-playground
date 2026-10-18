# Tap Titans 2
**Sources:** (URLs, required)
- https://www.bluestacks.com/blog/game-guides/tap-titans-2/tt2-tips-tricks-en.html (prestige at stage 60, higher stage = more rewards, clan benefits)
- https://www.bluestacks.com/blog/game-guides/tap-titans-2/tt2-leveling-guide-en.html
- https://www.levelwinner.com/tap-titans-2-strategy-guide-how-to-prestige/
- https://pol1.lr.ggtyler.dev/r/TapTitans2/wiki/newplayerguide (reddit mirror)
- https://redlib.ssps.io/r/TapTitans/comments/2s4uhq/relic_stage_bonus_chart (TT1 relic per stage chart, 2015)
- Legend: [PUB] from those; [EST] estimate/recollection.
## Core loop
- Tap to damage the current Titan, auto-attack from Sword Master + Heroes you level with gold; kill to advance stage by stage.
- Every stage ends with a boss (timer); fail and you retreat.
- Prestige (Master Reset) once you hit stage 60+ [PUB]; get Relics proportional to depth; buy Artifacts and Skill Tree upgrades.
- Realms of play: Clan Quests (clan boss), Tournaments, Raids, Ship/Trophies [EST].
## Resource types
- Gold (per run), Relics (prestige currency) [PUB], Skill Points, Artifacts, Equipment, Pets, Hero weapons, Clan Credits, Diamonds (premium), Fairy gold/ Mana [EST], Tournament tokens.
- Artifacts raise damage, gold, mana regen [PUB].
- Skill tree: four trees (Knight, Warlord, Sorcerer, Rogue); a skill point per new 50 stages passed at each reset [S https://giantbomb.com/wiki/Games/Tap_Titans_2, bluestacks guides]. Artifacts (about 97 total per one guide) and Pets/Skill Trees persist through prestige [S]. Equipment has five slots (weapon, helmet, armor etc.) [S giantbomb]. Clans give an All Damage bonus and Advanced Start [S reddit newplayerguide].
## Cost & production growth formulas (public or estimated; mark which)
- Relics: TT1 chart: ~1 relic per 10 stages after stage 80, with 3-12 bonus relics [PUB, old, reddit]. TT2 formula grows faster: relics ~ depends on stage^something and artifact multipliers [EST].
- Hero/Sword Master upgrade cost: ~x1.07-1.1 per level geometric [EST].
- Boss HP: exponential per stage with x(1.2+) step per stage, extra for bosses [EST].
- Artifact cost: relics, with exponent growth per level; many artifacts have max levels or diminishing returns [EST].
- "Advanced Start": clan/skill allows beginning prestige run at higher stage [PUB]. Practically formula `start_stage = floor(best_stage * f)`, f ~0.1-0.4 [EST].
- Stage-based advice: don't prestige until past ~level 600 per one guide [PUB single guide].
## Prestige structure
- Master Reset at stage 60+; payout rises with stage [PUB].
- Resets gold, hero levels, equipment? (keeps gear), stage returns to Advanced Start [EST].
- Layers: Prestige -> Titan Lord clan quest -> "Skill Tree (Prestige Upgrades)" -> Equipment/Pet evolution (semi-permanent).
- Event Prestige types ("Event Prestige" with Event currency) [EST].
- Prestige timing is a per-player optimization: "prestige when marginal relic gain per hour drops" [EST].
## Unlock pacing
- Stage 60 unlock first prestige in ~1h [EST].
- New heroes unlock by gold thresholds (a hero every few stages up to ~30+ heroes) [EST].
- Pet, Equipment, Clan, Tournament unlock at specific stage levels (e.g., stage 150 clan?) [EST].
- New "Realms"/Biomes visual changes every set number of stages; bosses have thematic names.
## Offline progress
- Store text only says the game can be played offline (without internet); offline EARNINGS and caps are not confirmed [S App Store]. Tournaments/Clan bosses are timers [EST].
- Fairy / Auto-prestige perk (VIP) [EST].
- Offline gold relative to active is small [EST].
## Monetization effects
- Diamonds sold in bundles (e.g. 180 for 300 yen up to 14,000 for $99.99) and a Season Pass; global tournaments with prizes [S https://apps.apple.com/app/tap-titans-2/id1120294802]. What diamonds buy, ad doubling and fairies are [EST].
- Heavy spenders reach deeper stages; clan competition drives pay [EST].
## What players love
- Satisfying dopamine, many parallel systems (pets, equipment, artifacts), social clans [PUB].
- Prestige gains visible.
## What players hate
- Overload of systems; confusing currencies [EST].
- Pay pressure for competitive clans [EST].
- Slow mid-game stalls.
## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Prestige gate at an easy early point (stage 60 ~1 hour) teaches loop early.
- "Advanced Start" carryover is the key: start new runs at a fraction of best; use it for each world so repeating doesn't repeat early content.
- Provide a single marginal-gain readout for prestige timing.
- Many systems is a trap; ship with 3-4 (cards, forms, items, world bonus).
- Stage bosses on a timer can become "build deadlines" (no combat required): timed assembly challenges.
- Clan analogue: shared community goals, optional.

## Verification log (refreshed 2026-10-18)
- Refreshed 2026-10-18: 2 more WebSearch queries. Added skill trees, artifact persistence, equipment, clan bonus and App Store monetization facts [S]. No fandom wiki text retrieved; no code (commercial).
- Still [EST]: relic formula for TT2, cost ratios, hero count, unlock stages for clans/pets, offline cap, VIP auto-prestige. The 2015 relic chart is TT1 only. Conflict: one guide says prestige after level 600, store/guides say stage 60 unlocks it.
