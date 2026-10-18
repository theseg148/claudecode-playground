# Realm Grinder
> Verification pass 2026-10-18 (WebSearch snippets only; pages not opened). [S] = confirmed in a search snippet with the URL given; [unverified] = not confirmed, treat as a design placeholder. See "Verification log" at the bottom.
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
- Building cost follows base * mult^owned. Base cost / production [S https://realm-grinder.fandom.com/wiki/Buildings]: Farm 10 / 2, Inn 125 / 6, Blacksmith 600 / 20. The 'about 1.08 to 1.15' multiplier is [unverified]; faction upgrades (Fairy, Dwarf, etc.) reduce the cost multiplier.
- Production per building is count * base_prod * upgrades, with +x% or x2 at fixed thresholds (e.g. 10, 25, 50, 100). [unverified]
- Abdication: gives gems; one PC Gamer guide says each gem raises gold production by 3% [S https://www.pcgamer.com/realm-grinder-guide/, single guide, treat as unconfirmed against the wiki]. Abdication resets buildings, upgrades and coins but keeps unlocked factions, gems, trophies, rubies and premium upgrades [S https://realm-grinder.fandom.com/wiki/Abdication]. The log-of-coins scaling is [unverified].
- Reincarnation: first possible at 1 Oc (1e27) gems, and each later one needs 1,000x more gems [S https://realm-grinder.fandom.com/wiki/Reincarnation]. Ascension replaces the Reincarnation button at R39, R99, R159 and R219 [S https://realm-grinder.fandom.com/wiki/Ascension]; the Gems page gives the first Ascension threshold as 1 Spqag (1e144) gems, which is inconsistent with the other page, so treat as [unverified]. The reincarnation bonus formula remains unknown.
- Gem production: some buildings produce a small gem trickle. [unverified]
- Spell timers: durations and cooldowns are on the wiki, specifics not checked. [unverified]

## Prestige structure
- Abdication: a quick reset to swap faction, doable in ~10-30 minutes mid-game. [unverified]
- Reincarnation: needs a high amount of coins; gives permanent boosts per faction and unlocks the extra Reincarnation upgrades.
- Ascension / Rank: the ultimate layer, with extra multiplier tiers.
- Each layer keeps gems, trophies and certain upgrades.

## Unlock pacing
- Early run: first workshop in seconds; first faction after ~10 minutes. [unverified]
- Abdication is always available, even with no benefit [S https://realm-grinder.fandom.com/wiki/Abdication]; Reincarnation needs 1e27 gems [S above]; the 'few hours / days to weeks / months' pacing is [unverified].
- Late updates add Excavations, Hybrids (mixed factions), etc., extending the arc further.

## Offline progress
- Offline: no source found for a percentage or hour cap [unverified]. Players report offline production is small versus active play, Undead are built for long absences (PC Gamer), and offline output is raised by mana regeneration upgrades (player report, '62.5% per regen' unconfirmed).
- Many players keep it running as an idle tab; mercenary and fairy spells need activation.

## Monetization effects
- The Kongregate/mobile versions have optional IAP; the Steam version is a one-time purchase. [unverified; verify per platform]
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

## Verification log

Confirmed [S]:
- Base cost/production of Farm, Inn, Blacksmith; Reincarnation first at 1e27 gems with 1,000x scaling; Ascension at R39/R99/R159/R219; what Abdication keeps and loses; Farms/Inns/Blacksmiths/Hall of Legends are universal buildings.
Partly sourced: gem bonus 3% each (one guide only).
Unconfirmed [unverified]:
- Per-building cost multipliers, upgrade thresholds, reincarnation/abdication bonus formulas, spell timers, offline cap and rate, pacing, IAP details. A commenter says the fandom wiki is partly outdated and points to musicfamily.org, which was not checked.
