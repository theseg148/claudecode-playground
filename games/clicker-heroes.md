# Clicker Heroes
> Verification pass 2026-10-18 (WebSearch snippets only; pages not opened). [S] = confirmed in a search snippet with the URL given; [unverified] = not confirmed, treat as a design placeholder. See "Verification log" at the bottom.
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
- Hero cost [S https://clickerheroes.fandom.com/wiki/Heroes]: floor(floor(BaseCost * 1.07^CurrentLevel) * CostReduction); each level raises the next cost by 6.975% (cost doubles about every 10 levels); base costs: Cid 5, Treebeast 50; Ace Scouts use 22% per level. Dogcog's cost reduction decays toward a 99.99999999% reduction.
- Monster HP [S https://clickerheroes.fandom.com/wiki/Formulas, https://clickerheroes.fandom.com/wiki/Zones]: piecewise; zones 1-140 use a separate expression, then HP is multiplied by 1.145 per zone (boss zones included) until zone 500. The earlier 'about 1.55 per zone after 140' was wrong. Boss HP = 10 + 0.2*floor(Z/500) monster-equivalents and monsters per zone = 10 + 0.1*floor(Z/500). Boss every 5 zones. A patch note reworked scaling after zone 200k (~8.8x HP per 5 zones).
- Early gold per monster scales with monster HP (about 1/15 early); the wiki says gold rises to keep pace with hero cost, formula on a separate page not retrieved. [unverified]
- Hero Souls on ascension: one guide says 1 Hero Soul per 2,000 total hero levels across unlocked heroes [S https://blog.clickerheroes.com/clicker-heroes-hero-souls-complete-guide-to-power-up/, single source]; Quick Ascension pays by highest zone for 50 rubies (formula not seen). The earlier '1 HS per 5 zones past 100' is [unverified] and likely wrong.
- Each Hero Soul gives +10% to all damage (DPS and click) [S several sources incl. the official blog]; one source adds a gold-drop bonus of 2% per soul capped at 50% [unverified].
- Ancients: Solomon costs n^1.5 Hero Souls for level n (removed in patch 1.0e10, replaced by Ponyboy) [S https://clickerheroes.fandom.com/wiki/Solomon,_Ancient_of_Wisdom]. Argaiv/Siyalatas/Libertas formulas not found [unverified]. Ancient Souls on transcension = floor(5*log10(total Hero Souls sacrificed)) per the official blog, but its own examples contradict it [unverified].
- Total DPS = (sum of hero DPS) * ancient multipliers * (1 + HS * 0.1) * gilds. [public structure; HS multiplier part confirmed above]
- Idle Ancients (Solomon, Libertas, Mammon, Fortuna) are tuned to balance idle vs active play. [public concept]

## Prestige structure
- Ascension: unlocks at zone 100 or so; resets gold, heroes and zone; keeps Hero Souls, Ancients and Gilds.
- Transcendence: requires an Ascension with at least a certain zone (about 100,000 Heroic souls in old versions; estimate); gives Ancient Souls and Outsiders (Xyliqil, Chor'gorloth, Phandoryss, Borb, Ponyboy, Rhageist). 
- Primal bosses and Outsiders give a third layer of long-term progression.
- Ancients can be maxed and then keep scaling through "hero souls" invest.

## Unlock pacing
- The first heroes unlock over the first ~10 minutes; buy 1 hero every few minutes.
- First Ascension: one guide suggests zone 130 as the best first ascension [S gamerofpassion.com guide, single source]; the 1-2 hour estimate is [unverified].
- Transcendence takes days to weeks.
- Late-game Outsiders / Ancient Souls take weeks to months.

## Offline progress
- Offline progress exists: the official blog says on exit the game records DPS and simulates combat/gold while away [S https://blog.clickerheroes.com/offline-progression-in-clicker-heroes/]. Forum reports of it stalling are anecdotal. Clicker Heroes 2 differs (no idle when closed at launch). The earlier 'no offline progress' claim was wrong. Caps are [unverified].

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

## Verification log

Confirmed [S]:
- 1.07 hero cost base with floor formula, 6.975% per level, Cid 5 / Treebeast 50 base costs; monster HP x1.145 per zone from 141 to 500 (replaces wrong 1.55); boss HP and monster-count formulas; +10% damage per Hero Soul; Solomon n^1.5; offline progression exists.
Unconfirmed [unverified]:
- Gold formula, ascension Hero Soul formula (a '1 per 2,000 hero levels' claim from one guide only), other Ancients' costs, timing estimates, offline caps.
