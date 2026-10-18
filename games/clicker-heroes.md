# Clicker Heroes
**Sources:** (WebFetch was blocked by DNS in this session; formulas are recalled from the community wiki and calculators, so verify.)
- https://clickerheroes.fandom.com/wiki/Clicker_Heroes_Wiki
- https://clickerheroes.fandom.com/wiki/Ancients
- https://clickerheroes.fandom.com/wiki/Hero_Souls
- https://clickerheroes.fandom.com/wiki/Ascension
- https://www.clickerheroes.com/ (the game, by Playsaurus)
- https://store.steampowered.com/app/363970/Clicker_Heroes/ (verify app id)

## Core loop
- Click monsters to deal damage and earn gold, buy and level heroes (DPS), and push zones.
- A boss appears every 5 zones with a timer; failing kicks you back a zone.
- Gold buys hero levels; Ascension converts progress into Hero Souls, which buy Ancients.
- Transcendence (later) is a second-tier prestige.

## Resource types
- Gold; Hero Souls (HS); Ancient Souls (after Transcendence); Rubies (premium, from treasure chests); Primal bosses and relics (late); Gilds (hero gilding); Outsiders; Mana and Energy (for active skills); Faith / Hands.

## Cost & production growth formulas
- Hero cost: roughly `cost(n) = base * 1.07^n` for the level n (public community knowledge; the 1.07 constant is widely quoted). [public/recall]
- Monster HP: grows by a factor of about 1.55 per zone after zone 140 (increases piecewise earlier). [estimate]
- Early gold per monster scales with the monster's HP (about 1/15 of HP in early zones), then adds bonuses. [estimate]
- Hero Souls on ascension: `HS = floor(sum over zone-based term ...)`; the simplified recall is "you get about 1 HS for each 5 zones past 100, increased by the Primal and Ancient bonuses", so deeper = more. [estimate]
- Each Hero Soul gives +10% damage (additive to the pool), so doubling HS roughly doubles the base. [public]
- Ancients: levels cost Hero Souls on a schedule: Argaiv (damage) costs about `level` HS to go from level n to n+1 for linear Ancients; Siyalatas / Libertas use exponential cost with `~2^level` scaling. [estimate]
- Total DPS = (sum of hero DPS) * (1 + ancient multipliers) * (1 + HS * 0.1) * gilds. [public structure]
- Idle Ancients (Solomon, Libertas, Mammon, Fortuna) are tuned to balance idle vs active play. [public concept]

## Prestige structure
- Ascension: unlocks at zone 100 or so; resets gold, heroes and zone; keeps Hero Souls, Ancients and Gilds.
- Transcendence: requires an Ascension with at least a certain zone (about 100,000 Heroic souls in old versions; estimate); gives Ancient Souls and Outsiders (Xyliqil, Chor'gorloth, Phandoryss, Borb, Ponyboy, Rhageist). 
- Primal bosses and Outsiders give a third layer of long-term progression.
- Ancients can be maxed and then keep scaling through "hero souls" invest.

## Unlock pacing
- The first heroes unlock over the first ~10 minutes; buy 1 hero every few minutes.
- First Ascension at around 1 to 2 hours of play (zone 100+); typical first-day Ascensions every ~20 to 40 minutes. [estimate]
- Transcendence takes days to weeks.
- Late-game Outsiders / Ancient Souls take weeks to months.

## Offline progress
- No real offline progress in the base game; closing the tab pauses progress ("idle" requires the tab open). Offline gold is not given in the browser version; Steam added offline progress in some builds. [estimate; verify]

## Monetization effects
- Rubies purchasable (IAP) to buy skills, auto-clickers and more; Treasure chests; Buy a "Steam Pack". 
- Most rubies can be earned for free through Gilds and chests.
- Mobile version has ads for boosts.

## What players love
- Satisfying scaling and immediate "ascension" payoff.
- Strong theory-craft and ancient-build discussion.
- Huge long arc for a free browser game.

## What players hate
- Confusing Ancient system and many exponents; required spreadsheets.
- Idle vs active split causes burnout.
- Zone "walls" where progress stalls and ascending feels mandatory.
- Rubies feel overpriced.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Use a boss-every-5-zones rhythm as "world milestone" beats, but replace damage with a challenge gate (puzzle/timer, no fighting).
- Keep the 1.07 hero cost curve as a flat, easy-to-read progression rule for upgrades.
- Give two kinds of permanent upgrades (passive linear and exponential) to retain an upgrade-focused feel.
- Provide a clear "ready to ascend" indicator so players do not need spreadsheets.
- Stagger prestige layers (Ascension then Transcendence) but do not require the second until the first feels solid.
