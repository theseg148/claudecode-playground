# DECADE IDLE — Design document (v1)
Applies DESIGN_RULES.md (R-numbers) to a Kamen Rider Decade idle game: Tsukasa travels the Rider worlds in sequence, photographing and "completing" each world by upgrading it. No fighting. Rider-lore hooks are author knowledge (see research/decade_worlds.md) — verify before shipping.

## 1. Fantasy & loop
Tsukasa's camera captures a world's energy ("Shots"). Shots buy upgrades; upgrades make more Shots. Nothing fights: the "monsters" are obstacles removed by upgrading (a world is *restored*, not conquered). Core loop (seconds): tap/auto-collect → buy → see multiplier bar fill. Session loop (minutes): hit milestone, unlock tier. World loop (days): clear objective, Dimension Ride to the next world. Meta loop (weeks): Ride Card collection, Decade Driver form unlocks.

## 2. Structure (R5, R8–R11, R18–R22)
- **Ladder per world:** 6 tiers, tier cost ×8–12, rate ratio ≈ cost/1.3, growth 1.12 (R1–R2); ×2 at 10/25/50/100/200 (R3).
- **Mid-world prestige "Final Form Ride":** gain = floor((lifetime/T)^0.5), +5–10 %/point, first available ≈ 25 min, then 20–45 min cycles (R12–R13). Player should hit it 8–14 times per world over its 3–5 days only if world is much longer; initial worlds use 3–6 rides.
- **World hop "Dimension Ride":** gated by an objective (R22); keeps Ride Cards, forms, automation, Decade Driver; resets generators; cleared worlds add passive income (R21).
- **Layers:** L1 Final Form Ride (per world), L2 Dimension Ride (cross-world, smaller exponent ~0.14–0.25), optional L3 "All Riders" post-game (R16).
- **Time budget:** 3–5 days per world for casual, 9 worlds ≈ 5–8 weeks (R19). Kabuto should be shorter (tutorial world, ~1 day) so the first hop lands in session 2–3.

## 3. The nine worlds (order is free; Kabuto first)
Each world = one rule (R20) + a themed upgrade family + a world-local currency from world 3.

| # | World | Rule (new verb) | Themed upgrades | Local currency |
|---|---|---|---|---|
| 1 | **Kabuto** | *Clock Up*: spend Charge to run time ×N for 10 s, Cast-Off at 25 owned doubles a tier | Zecter levels, Cast-Off armour, Hyper Clock Up speed, ZECT base, Sōji's kitchen (income ×) | none (teach basics) |
| 2 | Den-O | *Contracts*: assign Imagin to generators (time-skip +) | Rail extensions (DenLiner), Imagin contracts, Owner's tickets, time-skip | Train Tickets |
| 3 | Faiz | *Routing*: Photon lines link generators (adjacency bonus) | Photon-blood channels, phone codes, gear | Photon Stream |
| 4 | Ryuki | *Advent Cards*: collect contract-monster cards, slot 3 | Card packs by milestone, mirror-world dividers | Mirror Shards |
| 5 | Blade | *Fusion*: combine two cards into a stronger one | Rouse cards, Undead seal collection | Fusion Dust |
| 6 | Kiva | *Day/Night cycle*: night boosts rare tier, day boosts base | Castle upgrades, Arms Monsters, Wake-up | Moonlight |
| 7 | Agito | *Forms*: Ground/Flame/Storm/Trinity multipliers, switch free | Form mastery tree, G3 units | Unknown Sparks |
| 8 | Hibiki | *Training rhythm*: optional tap-timing bonuses (never required) | Oni training, Ongeki instruments | Drum Beats |
| 9 | Kuuga | *Colour switch*: Mighty/Dragon/Pegasus/Titan rotation | Arcle upgrades, Amadam | Ancient Glyphs |
Constraints: ≤3 visible currencies at once (R20); Shots + world currency + Ride Card/Driver meta.

## 4. Upgrade families (no combat)
1. **Generators** (6 tiers/world, themed names): the exponential spine (R1–R3).
2. **Milestone multipliers** (×2 bars, R3–R4).
3. **Mastery tree** (≈25 nodes per world, 3 branches, respec free; persists via best-result memory, R21): speed, multiplier, automation/offline.
4. **Automation:** auto-buy cheapest tier from first Ride shop (R17).
5. **Offline upgrades:** efficiency 50→75 %, cap 8→24 h (R23).
6. **Ride Cards:** permanent collection, passives across worlds; sold only as earned, never purchased (R26).
7. **Decade Driver forms:** cross-world unlocks (Kamen Ride cards: Kuuga form etc.), cosmetic + small multipliers.
8. **Active layer, never mandatory:** golden-cookie-style "Photo Op" (Cookie Clicker golden cookies/Realm Grinder spells as models) giving ≤1.5× progress (R24).

## 5. Transition moments
- Pre-ride: reveal next world's card at ~1/3 of the objective (R22); Tsukasa quip.
- Ride: "KAMEN RIDE … DECADE" flash, palette swap, recap card (time in world, what's kept, what resets) — prototypes/world_transition.html.
- Arrival: first purchase in the new world is affordable in < 60 s (R9); new rule introduced via a 3-step tooltip; the cleared world's passive income ticks up visibly (R21).
- Final world: ending sequence; post-game "All Riders" challenge layer (L3), Another-World replay with restrictions.

## 6. Monetisation (R26)
Cosmetic Driver skins/photo frames; optional rewarded "x2 offline claim" (never required); no sale of Ride Cards/prestige currency.

## 7. Risks
- Sim is a toy greedy model; play-test world length and rides. 
- Only ~11/37 reference games have confirmed formulas (analysis/growth_curves.md).
- Nine unique rules is large content cost: ship 3 worlds (Kabuto, Den-O, Faiz) first.
- Prototype set exists in prototypes/ (milestones, offline, prestige, unlock tree, world transition).
