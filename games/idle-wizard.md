# Idle Wizard
**Sources:** (URLs, required)
- https://idlewizard.wiki.gg/wiki/Basic_Mechanics (search snippet only; fetch failed DNS)
- https://idlewizard.wiki.gg/wiki/Exile (exile = soft reset)
- https://idlewizard.wiki.gg/wiki/Transmute (uses "All Mana This Realm")
- https://idlewizard.wiki.gg/wiki/Demiurge_Shaman_Guide (ascension forms)
- https://idlewizard.wiki.gg/wiki/Mastery
- https://idlewizard.wiki.gg/wiki/Level , /wiki/Class_Growth_Rate_Guide , /wiki/An_Introduction_to_Successful_Exiles (search snippets) [S]
- https://steamcommunity.com/app/992070/discussions/0/2794999575667851743 (dev statement on offline compensation) [S]
- https://www.bluestacks.com/apps/simulation/idle-wizard-no-iap-no-on-pc.html (third-party store text) [S]
- Legend: [PUB]/[S] stated in those search results; [EST] my recollection, unverified.
## Core loop
- Generate Mana; buy Spells (auto-casting) that produce mana, then Spell Power; tap Cast; unlock Realms/Levels.
- Wiki: the game has two prestige tiers, Exile (from the start) and Realm (from e400 mysteries onward) [S https://idlewizard.wiki.gg/wiki/Exile]. Whether a "Realm" is also a themed world with its own enemies was a guess and is UNCONFIRMED; "All Mana This Realm" is the counter used by Transmute [PUB]. Idle mode starts after the orb is unclicked for 30 s and gives a mana bonus [S wiki]; critical clicks use crit chance/profit, and Critical Rating adds log10(R)% crit chance [S].
- Use Wizard Level (XP from mana) to unlock spell tiers; Transmute converts mana to other resources [PUB].
- Exile/Ascend resets for permanent growth; Class choice (Shaman, Alchemist, etc.) changes mechanics [PUB].
## Resource types
- Mana, Spell power, Wizard Level/Experience, Gold? (Treasure), Mastery points, Ascension Experience, Paragon points [PUB nav listing].
- Class-specific resources (Shaman spirits, Alchemist potions) [EST].
- Premium currency: UNCONFIRMED; third-party store text says no IAP and no forced ads [S bluestacks].
## Cost & production growth formulas (public or estimated; mark which)
- Spell cost: exponential per level (~x1.15) [EST].
- Production per spell: linear in level x tier multiplier with milestone bonuses [EST].
- Wizard level: 1500 XP to reach level 2, each later level costs 1.09x the previous [S wiki Level page snippet]. Level cap raised by ascension [EST].
- Ascension experience gained over time based on character level (Demiurge) [PUB].
- Exile reward: Mysteries, based on the highest mana reached that Realm [S wiki]; the class timescaling guide models mysteries as the square root of mana, and exile timing as a rate decision [S https://idlewizard.wiki.gg/wiki/Class_Growth_Rate_Guide]. The "attribute points" wording earlier was a guess.
- No exact numbers published in retrievable sources.
## Prestige structure
- Exile (soft reset) grants Mysteries [S]; attribute-points wording unconfirmed [EST].
- Ascension forms (Demiurge etc.): deeper prestige with Ascension Ability Power (AAP) [PUB].
- Paragon layer: after ascension [PUB nav].
- Three-plus layers: realm -> exile -> ascension -> paragon.
- Each class has its own ascension form so repeated ascensions feel different.
## Unlock pacing
- Early: spells every few minutes; first exile within ~hours [EST].
- Realm unlocks on mana thresholds; each realm introduces new tier of spells and a twist [EST].
- Classes (T1) unlock first, then T2+ with ascension, so replays have different goals [PUB nav "T1 Classes"].
- Weeks to hit Paragon [EST].
## Offline progress
- 2020 Steam dev statement: offline compensation covers pet XP, dust gains and running trials, but spell casts were judged unrealistic to compensate because of system interactions; may be outdated [S steam thread above]. Rate and caps otherwise [EST].
- Auto-casting makes idle viable.
## Monetization effects
- Third-party store text: no IAP, no forced ads [S bluestacks]; earlier "optional IAP boosts" and "starter packs" claims unverified [EST].
## What players love
- Class variety: each class changes how the same loop plays [PUB].
- Deep wiki-able systems; frequent updates.
- Realm identity.
## What players hate
- Very complex late-game; grinding for ascension; confusion [EST].
- Some classes underpowered.
## Lessons for my game (Kamen Rider Decade idle, sequential Rider worlds, upgrade-focused, no fighting)
- Scope resource counters to the current realm ("All Mana This Realm"): each Rider world has its own counter and thresholds, resetting cleanly.
- Class = Rider form: choosing a different Rider changes the spell/upgrade mechanics so replays are new.
- Prestige ladder: world exile (cheap, frequent) -> ascension (per Rider) -> paragon (global). Keep to 3.
- Give each realm a twist (rule modification), not only bigger numbers.
- Time-based ascension XP gives rewards even for waiting.

## Verification log (refreshed 2026-10-18)
- Refreshed 2026-10-18: 3 more WebSearch queries. Replaced several guesses with wiki snippets (two prestige tiers, Mysteries, level XP 1500 x1.09, idle mode, offline dev statement). No repo (commercial).
- Not retrieved: pages themselves (only snippets), Exile formula constants, Realm unlock mechanics beyond e400 mysteries, Paragon details. Spell cost ratio 1.15 and production formulas remain [EST].
