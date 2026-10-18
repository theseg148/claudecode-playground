# Realm Grinder
**Sources:** (WebFetch was blocked by DNS in this session; everything here is from recall of the wiki and forums. Realm Grinder has little officially published math, so the many numbers below are estimates.)
- https://realm-grinder.fandom.com/wiki/Realm_Grinder_Wiki
- https://realm-grinder.fandom.com/wiki/Factions
- https://realm-grinder.fandom.com/wiki/Abdication
- https://realm-grinder.fandom.com/wiki/Reincarnation
- https://www.kongregate.com/games/divinegames/realm-grinder
- https://store.steampowered.com/app/1117730/Realm_Grinder/ (Steam release; verify the app id before citing)

## Core loop
- Click to earn coins, then buy buildings (Workshops, Hovels ... up to the 15 or so tiers, estimate).
- Cast spells for temporary boosts, buy upgrades with coins and later gems.
- Choose a faction (Fairy, Elf, Angel, Goblin, Undead, Demon, Titan, Druid, Faceless, Dwarf, Drow, Mercenary, etc.), each giving different multipliers and spells.
- Abdicate (a soft reset that lets you switch faction) to grow the long-term multipliers.
- Reincarnate (a deeper prestige) and then Ascend for the highest layers.

## Resource types
- Coins; Gems (earned from Abdication and a daily dungeon-like event and from gem-producing buildings); Spell mana; Faction Coins (one per faction, tracked for Reincarnation); Trophies from events; Research from the Research tree; Excavations / Ruby tiers added later; Prestige/rank "Mana".
- Production is modified by faction, Spells, upgrades, Research, and Mercenary ("Hire and Fire") effects.

## Cost & production growth formulas
- Building cost follows `base * mult^owned`, and the community calls the multiplier "about 1.08 to 1.15" depending on the building. [estimate]
- Production per building is `count * base_prod * upgrades`, and upgrades give +x% or x2 at fixed thresholds (e.g. 10, 25, 50, 100 owned). [estimate]
- Abdication gives a bonus that scales approximately with the log of coins earned in that run, and the number of gems you hold. [estimate]
- Reincarnation: bonus = `1 + (faction_coins / threshold)^0.? ` is not public in a precise form; players use calculators. [estimate; do not rely on]
- Gem production: some buildings produce a small gem trickle, which is why gems are a "slow" currency. [estimate]
- Spell timers: spell duration and cooldowns are constants in the wiki, e.g. Fairy's "Lucky Draw" and Elf's "Mana Surge". [public, specifics need verifying]

## Prestige structure
- Abdication: a quick reset to swap faction and re-earn the faction multiplier faster, can be done within ~10-30 minutes in mid-game. [estimate]
- Reincarnation: needs a high amount of coins; gives permanent boosts per faction and unlocks the extra Reincarnation upgrades.
- Ascension / Rank: the ultimate layer, with extra multiplier tiers.
- Each layer keeps gems, trophies and certain upgrades.

## Unlock pacing
- Early run: first workshop in seconds; unlocking the first faction after ~10 minutes. [estimate]
- Abdication appears after a few hours; Reincarnation after days to weeks; Ascension after months. [estimates]
- Late updates add Excavations, Hybrids (mixed factions), etc., extending the arc further.

## Offline progress
- Realm Grinder awards offline coins at a fraction of the active rate (commonly said 50% or "spell time" disabled), with a cap on the length of time. [estimate]
- Many players keep it running as an idle tab; mercenary and fairy spells need activation.

## Monetization effects
- The Kongregate/mobile versions have optional IAP (gem packs, ad-skipping), and the Steam version is a one-time purchase. [estimate; verify per platform]
- Gems are mostly free-to-earn, though premium purchases speed up some tasks.

## What players love
- Huge faction variety and build theory-crafting (many ways to play).
- Active spell timing as a skill layer in an idle game.
- Great community content: spreadsheets, calculators.

## What players hate
- Opaque math; new players cannot tell what upgrades do.
- Reincarnation/Ascension steps feel grindy and long.
- UI and balance updates that favor existing players.

## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Factions map to Rider forms or worlds: a choose-one trait per run adds replay value without combat.
- A cheap soft reset (Abdication) to swap forms makes "Decade" shifting between worlds a native mechanic.
- Include a spell-like timed ability (Kamen Ride card) to give a small active layer.
- Display formulas and breakdowns in-game to avoid the opacity complaint.
- Layer prestige (soft reset and then deep reset) so players always have a near-term and a far-term goal.
- Keep the grind to unlock new layers bounded and show progress to the next unlock.
