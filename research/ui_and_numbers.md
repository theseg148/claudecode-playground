# UI and number handling in idle games (for the Decade idle game)

Tags: [CODE] = read this session in raw source (URL + function named); [S] = stated in a README/doc fetched this session (URL); [M] = author memory, NOT verified this session, treat as a hint; [E] = our own estimate/computation (script run this session, see section 10).
Method note: only curl to raw.githubusercontent.com worked for primary data; no WebSearch snippets were used in this file, so every non-[CODE]/[S]/[E] claim is [M].
Sources fetched:
- Cookie Clicker (mirror): https://raw.githubusercontent.com/ozh/cookieclicker/master/main.js
- Antimatter Dimensions: https://raw.githubusercontent.com/IvarK/AntimatterDimensionsSourceCode/master/src/core/format.js , .../src/core/notations.js , .../src/core/storage/serializer.js , .../src/core/storage/storage.js , .../src/core/storage/migrations.js
- break_infinity.js README: https://raw.githubusercontent.com/Patashu/break_infinity.js/master/README.md
- break_eternity.js README: https://raw.githubusercontent.com/Patashu/break_eternity.js/master/README.md

## 1. Bottom line (read this first)
1. Decade's peak magnitude is ~1e23 (goal) to ~1e30 (with headroom): a plain JS double (max 1.8e308) holds it with 278 orders of magnitude to spare [E]. **No big-number library is needed.** Needed instead: a notation formatter (section 2) and a "keep per-tick increments above the float ulp" check (section 10).
2. Use named-suffix notation up to ~1e33 then scientific as a safety net, with an options toggle (Cookie Clicker and Antimatter Dimensions both ship a switch) [CODE].
3. Cost and ride maths should be written through a tiny `N` wrapper (add/mul/pow/cmp/format) so a library can be swapped in later if world count or ride multipliers grow [E].
4. Saves: versioned, compressed or at least base64 string, with an export/import box, ending marker and migration function [CODE AD, Cookie Clicker].

## 2. Number notations

### 2.1 Cookie Clicker (the "named" family) [CODE main.js, lines ~217-300]
- `formatEveryThirdPower(notations)` returns a closure: below 1e6 the number prints in full with comma grouping; from 1e6 it divides by 1000 repeatedly (`while(Math.round(val)>=1000){val/=1000;base++}`) and appends `notations[base]`; if `base>=notations.length` it returns the literal text `'Infinity'`; the mantissa is rounded to 3 decimals (`Math.round(val*1000)/1000`).
- Two suffix tables: `formatLong=[' thousand',' million',' billion',' trillion',' quadrillion',' quintillion',' sextillion',' septillion',' octillion',' nonillion']` extended programmatically with prefix x suffix pairs (`prefixes=['','un','duo','tre','quattuor','quin','sex','septen','octo','novem']` x `suffixes=['decillion','vigintillion',...,'nonagintillion']`), and `formatShort=['k','M','B','T','Qa','Qi','Sx','Sp','Oc','No']` extended likewise (`'Un','Do','Tr'...` x `'D','V','T','Qa','Qi','Sx','Sp','O','N'`), with `formatShort[10]='Dc'`.
- A third formatter `rawFormatter` returns the number unchanged (JS then prints `1.2345e+25`); `Beautify` picks `format=Game.prefs.format?2:1`, i.e. a single preference toggles "short names" vs "raw scientific"; inputs containing `e+` with format 2 fall back to `val.toPrecision(3)`.
- Comma grouping is done with the regex `.replace(/\B(?=(\d{3})+(?!\d))/g,',')`.
- `Beautify(val, floats)` shows decimals only when `floats>0 && Math.abs(val)<1000`; it floors the integer part and handles the "9.999 rounds up to 10" case (`if (floats>0 && fixed==val+1) val++`). `BeautifyInText(str)` re-formats every number inside a tooltip string via regex `/(([\d]+[,]*)+)/g`, so text authors write plain integers and the UI formats them.
- Lesson: the named table is just an array lookup indexed by `floor(log1000(x))`; table length is the notation's ceiling (~ 1e303 here).

### 2.2 Antimatter Dimensions (notation library family) [CODE]
- AD delegates to the npm package `@antimatter-dimensions/notations` (`import * as ADNotations`) [CODE notations.js]. The in-game list `Notations.all` (order = options tab order) is: scientific, engineering, letters, standard, emoji, mixedScientific, mixedEngineering, logarithm, brackets, infinity, roman, dots, zalgo, hex, imperial, clock, prime, bar, shi, blind, blobs, all [CODE notations.js].
- Joke/unreadable ones are flagged `painful(...)` (`n.isPainful = true`): standard, emoji, brackets, roman, dots, zalgo, hex, imperial, clock, prime, bar, shi, blind, blobs, all [CODE]. The UI uses this flag to warn before selecting and to keep important integers legible (see `formatInt` comment in format.js: "of the painful notations. Prevents numbers like 5004 from appearing imprecisely as '5.00 K'") [CODE format.js].
- Default/fallback is `Notation.mixedScientific` (`Notations.find` returns it when a saved name is unknown; the `current` getter returns it before the UI is initialised) [CODE].
- `format(value, places, placesUnder1000)`, `formatInt`, `formatFloat`, `formatX` ("x" multiplier), `formatPow`, `formatPercents`, `formatRarity`, `formatWithCommas`, `quantify(name, value)` (adds correct plural), `timeDisplay`, `timeDisplayShort` live in format.js [CODE]. `formatPostBreak` branches: value infinite -> `notation.infinite`; tiny decimals -> `formatVerySmallDecimal`; <1000 as plain number with `placesUnder1000` decimals; otherwise `notation.formatDecimal(decimal, places)` [CODE].
- Lesson: separate "format a big number", "format an integer count", "format a multiplier", "format time", "pluralise" as distinct helpers. One `format()` is not enough in practice.

### 2.3 Notation taxonomy (general)
| Family | Example for 6.55e22 | Readable at | Pros | Cons |
|---|---|---|---|---|
| Scientific | 6.55e22 | any magnitude | exact, uniform width, no tables | players cannot compare 6.55e22 vs 6.5e23 at a glance [M] |
| Engineering | 65.5e21 | any | exponent multiple of 3 | mantissa width changes [M] |
| Named / short | 65.5 Sx (sextillion) | to table length | familiar K M B T | tables end; abbreviations after Dc are cryptic [CODE] |
| Named / long | 65.5 sextillion | to table length | friendliest for new players | long, wraps in narrow UI [CODE] |
| Letters | 65.5 aa-style | unbounded | never runs out, compact | meaningless to newcomers [M] |
| Mixed sci. | 65.5 Sx until 1e33 then 6.55e36 | any | friendly start, safe tail | two regimes [CODE default in AD] |
| Logarithm | e22.82 | extreme | good at layer-2 sizes | hard to see +% changes [M] |
Thresholds seen in code: Cookie Clicker switches from commas to suffix at 1,000,000 [CODE]; AD's helpers switch to notation at 1000 (`formatUnder1000` below) [CODE].

### 2.4 Rules of thumb
- Always show 3 significant digits of mantissa (1.23, 12.3, 123) [CODE: Cookie Clicker rounds to 3 decimals; E for the rule].
- Never format by `toFixed` of huge integers; use exponent split.
- Format ONLY at the view layer; keep raw doubles in state.
- Let players choose notation in Options; store as a preference, not in the world record.

## 3. Big-number libraries

| Library | Range | Representation | Speed/precision claim | Source |
|---|---|---|---|---|
| native Number | 1.8e308, integers exact to 9.007e15 | IEEE double | fastest | [E] |
| decimal.js | arbitrary precision | arbitrary-precision decimal | accurate, slow | [S break_infinity README: "prioritize accuracy over speed, use decimal.js"] |
| break_infinity.js | up to ~1e9e15 ("bigger in magnitude than 1e308") | mantissa (double) + exponent (double) | "prioritize speed over accuracy" | [S README] |
| break_eternity.js | 10^^1e308 (tower height) | `sign`, `layer`, `mag` | within 2x/0.5x of break_infinity speed | [S README] |
| logarithmica_numerus_lite | positive only | single exponent | ~2x faster than break_infinity but no negatives | [S README links] |
| ExpantaNum.js / OmegaNum.js | googological sizes | array notation | low performance | [S README links] |
| double.js / Quad.cs | ~1e308 w/ 128-bit precision | double-double | accuracy+performance | [S README links] |

Details:
- break_infinity.js README: "A replacement for decimal.js for incremental games which need to deal with very large numbers (bigger in magnitude than 1e308, up to as much as 1e9e15) and want to prioritize speed over accuracy" [S]. Drop-in: "If you are already using decimal.js, just swap out for break_infinity.js" [S]. Constructor accepts Number, String or Decimal; methods are chainable and immutable [S]. It has a benchmark table "decimal.js vs break_infinity.js: Speedup" (rows per project, see README) [S]; numeric speed-up values were not copied here.
- break_eternity.js: layered representation `sign*10^10^...^mag` with `layer` count; mag renormalised when above 9e15 (log10 it and increment layer) or below ~15.954 with layer>0 [S README]. Operators `+ *` do not work; use `.add .mul .pow .cmp ...` and they return new objects [S]. Warning for converters: `log/log2/log10/ln` return Decimal, not Number [S].
- Precision trade-off (all mantissa+exponent libs): mantissa is a double, so ~15 significant digits [E]; adding 1 to 1e30 does nothing in any of them. That is acceptable for idle games and unacceptable for exact-integer needs.
- Performance: every op allocates an object and normalises (log/pow), so it is several times slower than native arithmetic in a tight tick loop [M]. A single-digit-thousand-entity UI is fine; physics-like loops are not.
- AD stores values as Decimal and passes them through `format` which calls the notation's `formatDecimal` [CODE format.js]; i.e. the formatter API is Decimal-based when a library is used.
- Cookie Clicker itself uses native Numbers and its formatter table ends around 1e303, returning the string "Infinity" past the table [CODE main.js]. The most famous clicker game therefore works without any library in its main resource.

## 4. Bulk-buy UI [mostly M; CODE where noted]
- Buy-amount selector with 1 / 10 / 100 / Max ("Max" is the idle-friendly default) [M, Cookie Clicker and AD]. A separate "buy until 10" in AD makes the x2 per-10 milestone visible [M; the x2/10 rule is in DESIGN_RULES R3 from AD code].
- The cost shown must be the TOTAL for the selected amount (geometric sum: base*r^n*(r^k-1)/(r-1)) [E]; Max uses the inverse (logarithm) rather than a loop [E].
- Show "owned (bought)" and the next milestone as `x2 in 7` (R4).
- Disabled state: grey button + show the missing amount, not just "not enough".
- Keyboard: `M` = max-all, number keys for tier N (AD has hotkeys) [M].
- Cookie Clicker tooltips on buildings show per-unit CpS and total share (percent of production) [M].
- Recommendation for Decade: 1/10/Max toggle persisted, shows total price, and a single "Buy affordable" button for the sleepy-player case.

## 5. Tooltips and transparency
- Cookie Clicker's tooltip system `Game.tooltip.draw(from, text, origin)` supports dynamic content: text may be a function re-evaluated while hovered (`typeof this.text==='function'`) [CODE main.js ~2414-2440]. Upshot: tooltips should show live numbers.
- Same file wraps text in `unescape` and attaches mouse-over/out handlers inline [CODE]; modern equivalent is a single delegated tooltip element.
- Transparency patterns (the player must be able to see the formula) [M]: (1) breakdown list "base x tier mult x ride mult x world carry = total"; (2) "next purchase gives +X/s (+Y%)"; (3) hover on the production number shows each source; (4) hidden/random effects flagged as such. Matches design-rule tone "Always show pending gain" (R18).
- On touch there is no hover: use tap-to-open info panel (mobile section).
- BeautifyInText pattern [CODE]: tooltip copy stays localisable and numbers are re-formatted by the UI.

## 6. Progress bars
- Use bars for (a) next milestone (R4), (b) world gate (R28/R30), (c) pending ride gain, (d) offline cap. Always show the number beside the bar [M].
- Compute fill on a log scale when the target is orders above the start (1e18 gate): `log10(x)/log10(goal)` [E]. Linear fill looks stuck for 99% of the time.
- Show ETA ("~3 h") using current rate; hide ETA when rate is 0.
- Avoid animating width every tick on mobile; set CSS `transform: scaleX()` and update at ~4 Hz [M].
- Endowed progress: start world 2+ bars pre-filled with a stated reason (R30).

## 7. Offline progress and popups
- Cookie Clicker: offline production exists as an "angel" effect (Twin Gates of Transcendence) and as "sleep mode" when frames are skipped: the screen shows "Cookie Clicker is in sleep mode and generating offline cookies." plus a "Click here to resume" link (`l('offGameMessage')`) [CODE main.js ~2050-2052]. Changelog lines: "buffs no longer affect offline CpS", "the amount of heralds is now saved with your game, and is used to compute offline CpS the next time the game is loaded" [CODE changelog strings in main.js ~1580, 1681]. Takeaways: offline gain should be a defined formula (not the buffed live rate), and every multiplier it uses must be saved.
- Sleep-mode timeout is a user setting ("Sleep mode timeout" ON/OFF) [CODE ~6932] -> offer a toggle.
- AD runs a catch-up simulation on load: `backupOfflineSlots()` is invoked "during offline progress simulation" [CODE storage.js comments] i.e. offline is simulated in chunks, not one big multiplication, so non-linear rules stay correct.
- "Welcome back" popup contents (best practice) [M]: time away (capped), gained amount (formatted), what changed (items affordable now), one big button "Collect" and an optional "Skip to next goal" row. Show the cap rule ("capped at 8 h; Amadam Polish raises it") -> matches Decade offline-cap upgrade idea.
- Clamp absurd clocks: compare `Date.now()` with `lastSave`; ignore negative deltas; cap at max [E].
- Decade design says offline time banks into "Time Skip" charge (DECADE_IDLE_DESIGN.md R36), so the popup should read "+N charges" and the Shots gained.

## 8. Notification patterns
- Toast stack (AD: `GameUI.notify.success/info(...)`, e.g. "Game imported") [CODE storage.js]. Levels: info, success, warning, error.
- Rules [M]: max 3 visible; auto-dismiss 3-5 s; collapse duplicates ("x3"); never block input; log to a notification history; critical ones (save failed) stay until dismissed.
- Cookie Clicker `Game.Notify('Saving failed!', body)` shows an explicit failure toast when serialisation yields a too-short string (`str.length<10`) [CODE main.js ~3055].
- Badges/dots on tabs for new unlocks (R11 "new option every 2-5 min") [M].
- Respect `prefers-reduced-motion` and give a "mute notifications" option [M].

## 9. Mobile layout
[M] unless noted. 
- Single column, sticky top bar with the main resource and per-second rate, bottom tab bar (thumb reach), min tap target 44 px, buy buttons full width.
- Hover tooltips become tap-to-expand panels; avoid hover-only information.
- Long numbers: use short notation to keep width; `font-variant-numeric: tabular-nums` so digits don't jitter.
- Background throttling: browsers throttle timers in hidden tabs; use `Date.now()` delta not tick count, then feed the offline routine on `visibilitychange`. Cookie Clicker's sleep mode is the same problem seen from the other side [CODE ~2050].
- Update the DOM only for visible tab content; batch to `requestAnimationFrame` at ~10 Hz for numbers.
- Safe-area insets for notch devices: `padding: env(safe-area-inset-*)`.

## 10. Save systems

### 10.1 Cookie Clicker [CODE main.js]
- `Game.WriteSave(type)`: type 1 = export string: `escape(utf8_to_b64(str)+'!END!')`; types 2/3 = raw string; default = localStorage via `localStorageSet(Game.SaveTo, str)` [CODE ~3040-3070]. The `!END!` suffix detects truncated copy-paste.
- `utf8_to_b64` uses `Base64.encode(unescape(encodeURIComponent(str)))` with a `btoa` fallback [CODE ~653-670].
- `localStorageGet/Set` wrap access in try/catch (private mode, quota) [CODE ~134-143]. Matches our rule: wrap every storage access.
- UI: `Game.ExportSave()` opens a prompt with a read-only textarea ("This is your save code. Copy it and keep it somewhere safe!"); `Game.ImportSave()` prompts for paste with an inline error line ("Error importing save"); `ImportSaveCode` returns boolean; there is also file save/load (`e.target.result` -> ImportSaveCode) [CODE ~2821-2860].
- Save is verified after write (`if (!localStorageGet(Game.SaveTo)) ...` notify on failure) [CODE ~3070].

### 10.2 Antimatter Dimensions [CODE serializer.js, storage.js]
- Pipeline (`steps`): UTF-8 encode -> `pako.deflate` -> bytes to char string -> `btoa` -> strip `=`, escape `0 + /` as `0a 0b 0c` (so double-click selects the whole string) -> append `EndOfSavefile` -> prefix `AntimatterDimensionsSavefileFormat` + 3-letter version `AAB` [CODE].
- Version letters "should ideally go AAA, AAB, AAC ... so that we can do inequality tests on it"; steps have `condition: version => version >= "AAB"` for backward-compatible decoding [CODE].
- Self-identifying prefix prevents importing another game's/mod's save; the comment tells modders to change it [CODE].
- JSON converter maps `Infinity` -> "Infinity" and Set -> array [CODE]; NaN entries "will still be strings" on import and are validated (`import` checks "a string roughly stating what's wrong with the save") [CODE storage.js ~200-230].
- Backups: `AutoBackupSlots`, `backupDataKey(saveSlot, backupSlot)`, `saveToBackup`, time-based backup timers, and offline backups [CODE storage.js]. Multiple save slots (`currentSlot`).
- Migrations: `migrations.js` has `patches` keyed by version number that mutate `player` step by step (e.g. `infinitiedConversion`, `etercreqConversion`) [CODE]. Run all patches whose version is greater than the save's version.
- Import UX: success toast "Game imported"; import also from file (`importAsFile`) [CODE].
- Cloud save: AD supports Google-account cloud save via the same serialised string [M]; not verified in code read here.

### 10.3 Recommended for Decade [E]
`{v:1, t:lastSave, worlds:[...], ...}` -> JSON -> (optional `CompressionStream('deflate')`, widely available) -> base64url -> `DECADE1:` prefix + `:END`; migration table keyed by `v`; autosave every 15-30 s + on `visibilitychange`; keep 2 rolling backups; export/import textarea plus file download; validate NaN/Infinity on load; wrap storage in try/catch; show "last saved" in Options.

## 11. Accessibility
[M] unless noted.
- Do not rely on colour alone (affordable vs not: add icon/text).
- Keyboard: every action reachable by Tab/Enter; visible focus ring; shortcuts documented and remappable.
- Live regions: avoid `aria-live` on per-second counters (screen reader spam); announce milestones and offline popups only. Use `role="status"` for toasts.
- Provide the "readable numbers" option: AD marks unreadable notations `isPainful` and keeps counts in plain integers [CODE]; Decade should default to named/short and offer plain scientific.
- Reduced motion, adjustable text size, high-contrast theme, no flashing; pausable animations (Cookie Clicker has a "Fancy graphics"/"Particles" toggles in options [M]).
- Time pressure: nothing should require sub-second reaction (also R14).
- Dark/light scheme via `prefers-color-scheme`.

## 12. How large do Decade's numbers get? [E]
Computation (node, this session):
- Gate goal per world: `goal(w) = 1e18 * s^w`. For w=8 (ninth world): s=4 -> 6.5536e22; s=3 -> 6.561e21 (DECADE_IDLE_DESIGN.md section 4 uses 1e18*s^w).
- Cost per unit: `base * r^n`, r=1.15: n=200 -> 1.4e12; n=1000 -> 5.0e60; n=4000 -> 6.2e242; overflow of a double at n ~ 5,100 (log(1.8e308)/log(1.15)) [E]. A player owning 1000 of one tier is far beyond plan (milestones at 10/25/50/100/200 per R3).
- Milestone multiplier: x2 per 10 owned: 400 owned -> 2^40 = 1.1e12 [E].
- Tier base cost x10 per tier, 8 tiers -> 1e8 spread [E].
- Final Form Ride: Seals = floor(sqrt(run_lifetime/T_w)) at 5 %/pt (R15). With T_w sized so a world needs ~100 points, ride multiplier ~ 1+0.05*100 = 6; DESIGN_RULES range 2e2-6e3 final multiplier [sweep]. The computed worst case with the toy T=1e6 gives 2.5e8 points -> 1.3e7 multiplier, which shows T_w MUST scale with the world cost (as R15 says) [E].
- Dimension Ride carry: c = s/1.1 = 3.64 per world; product over 8 hops = 3.06e4 [E].
- Production side: rate needed to hit goal in 3 days (2.6e5 s) at 6.55e22 is ~2.5e17/s average; peak maybe 10x that = 2.5e18/s [E].
- Practical peak "Shots" value in play: 6.5e22 (gate) x overshoot (players can run past gate ~100x) = ~1e25; with a safety margin to the stated ~1e30 [E]. Double max 1.8e308 leaves 10^278 headroom [E].
- Precision: ulp at 6.5e22 = 8.4e6 (2^23) [E, computed]. Therefore per-tick increments must exceed ~1e7 to register; at 2.5e17/s with a 100 ms tick the increment is 2.5e16, 3e9x larger than the ulp. OK. Lifetime counters near 1e23 will drop any single add below 8e6 (e.g. a 10-Shot click when late) - harmless but a "click adds nothing" bug is theoretically visible: keep clicks scaled (click value tied to production) or show them as zero.
- Exact integers: only exact below 9.007e15 (`Number.MAX_SAFE_INTEGER`), so never use Shots as an array index, key or equality target above that; compare with `>=` only.
- Per-world reset keeps magnitude lower in early worlds, so world 1 never exceeds ~1e19.

## 13. Recommendation table for the Decade idle game
| Topic | Recommendation | Why | Evidence |
|---|---|---|---|
| Number type for Shots | Native `Number` (double) | peak ~6.5e22..1e30 << 1.8e308 | [E] sec. 12 |
| Big-number library | NOT needed now. Keep `N.add/mul/pow/cmp/fmt` wrapper; swap to break_infinity.js only if the peak design exceeds ~1e300 or if post-game "All Riders" layer (log-scaled) goes beyond | cost/speed; libs cost allocation and bundle size | [S] break_infinity README; [CODE] Cookie Clicker uses doubles |
| If a library is ever added | break_infinity.js (range 1e9e15, speed), not break_eternity (tower height unnecessary) and not decimal.js (slow) | [S] READMEs | [S] |
| Notation default | Named short (K M B T Qa Qi Sx Sp Oc No Dc) up to 1e33, then scientific; show 3 significant digits | friendly, matches CC and AD "mixed" default | [CODE] |
| Notation options | Short names / Scientific / Engineering; nothing joke-y | accessibility; AD flags painful ones | [CODE] |
| Formatting helpers | `fmt`, `fmtInt`, `fmtX`, `fmtPct`, `fmtTime`, `plural` (separate) | AD format.js shape | [CODE] |
| Exact-integer rule | Only exact < 9.007e15; use `>=` comparisons; never use big values as keys | doubles | [E] |
| Tick maths | Increment = rate*dt; check increment >= value*1e-15 | float ulp | [E] |
| Cost maths | Closed-form geometric sum and log inverse for Max buy; not loops | speed, correctness | [E] |
| Bulk buy | 1/10/Max toggle, total price shown, next-milestone text | R3/R4 | [M] [CODE AD] |
| Tooltips | Live (function-valued) tooltips with breakdown list; tap-panel on touch | CC dynamic tooltip | [CODE] |
| Progress bars | Log-scale fill for gate (1e18..), ETA, always numeric label | linear stalls | [E] |
| Offline | Simulate in chunks, cap by Amadam Polish upgrade, popup with time/gain/charges, clamp clock | CC offline, AD sim | [CODE] [M] |
| Notifications | Toast stack max 3, dedupe, history, persistent failure toasts | CC `Game.Notify` | [CODE] |
| Mobile | Single column, bottom tabs, 44px targets, tabular-nums, Date.now() delta | background throttling | [M] |
| Save format | `DECADE1:` + base64(deflate(JSON)) + `:END`, version char, migrations keyed by version, 2 rolling backups, file export | CC `!END!`; AD prefix/version/EndOfSavefile/pako | [CODE] |
| Save safety | try/catch around storage, verify-after-write, toast on failure | CC | [CODE] |
| Cloud | Skip for v1 (export string is enough) | cost | [M] |
| Accessibility | Keyboard everywhere, no colour-only cues, reduced motion, no aria-live on counters | | [M] |

## 14. Open items to verify (not done this session)
- Real speed-up numbers from the break_infinity README benchmark table (README row exists; values not read).
- AD offline-progress chunking details in `src/core/player.js` / `GameCache` (only storage comments read).
- Mobile and accessibility claims are [M]; confirm with WebSearch when available.
