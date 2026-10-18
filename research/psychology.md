# Psychology of Idle / Incremental Games

Research note. Evidence-quality legend used throughout:
- **[V]** = verified against a source surfaced in this research session (URL given).
- **[B]** = background knowledge from the literature that I could not re-open this session (the sandbox blocked direct page fetches, e.g. Wikipedia, so only search-result snippets were readable). Treat [B] items as "check before quoting".
- **[P]** = practitioner/blog opinion, not peer reviewed.

Search coverage caveat: web search returned many SEO-spam mirrors for generic "idle game psychology" queries. Those were discarded. Peer-reviewed claims below are tied to papers whose bibliographic details were confirmed by at least one search result.

---

## 1. What counts as an "idle game" academically

1. **Alharthi, Alsaedi, Toups Dugas, Tanenbaum, Hammer (2018), "Playing to Wait: A Taxonomy of Idle Games", CHI 2018, DOI 10.1145/3173574.3174195.** Grounded-theory analysis of 66 idle games plus 10 non-idle comparators; examined play, mechanics, rewards, interactivity, progress rate and interface. Key claim: idle games shift players from *playing* to *planning*, and use player attention and computer cycles in unusual ways. [V] https://research.monash.edu/en/publications/playing-to-wait-a-taxonomy-of-idle-games/ and https://par.nsf.gov/biblio/10061230
2. **Spiel et al. (2019), "'It Started as a Joke': On the Design of Idle Games", CHI PLAY 2019.** Interviews with six designers of popular idle games; describes active withdrawal from the game as central to idle play. [V] https://par.nsf.gov/biblio/10174274
3. **Deterding (2016), "Progress Wars: Idle Games and the Demarcation of 'Real' Games", DiGRA/FDG.** Frames idle games as boundary work: parody (Progress Quest 2002, Statbuilder 2008/9) -> boundary-blurring experiment -> boundary-extending genre. [V] https://dl.digra.org/index.php/dl/article/view/851 and slides https://www.slideshare.net/slideshow/progress-wars-idle-games-and-the-demarcation-of-real-games/64651901
4. **Deterding (2019), "Cookie Clicker: Gamification" in *How to Play Video Games* (NYU Press).** Argues incremental games use progress mechanics (inherited from CRPGs and social games like FarmVille) to make the trivial act of clicking engaging; they began as satire. [V] https://eprints.whiterose.ac.uk/id/eprint/146788 and draft PDF https://eprints.whiterose.ac.uk/146788/1/25_Deterding_draft_final_180515_SDE.pdf
5. **"Idle Games: A Cozy Genre Turned Exploitative", *Replay* (Univ. of Lodz).** Critical take on monetised idle games. [V that it exists; content not read] https://www.czasopisma.uni.lodz.pl/Replay/article/view/23588

Takeaway: the academic consensus is that the genre's satisfaction is not "skill" in the twitch sense but *progress-mechanics engagement plus planning*. This is directly relevant to why idle games satisfy without skill (section 9).

---

## 2. Compulsion loops

**Definition.** A compulsion loop is a short repeatable cycle: *anticipate -> act -> reward -> (new anticipation)*. In games design it is usually split into a core loop (seconds), a session loop (minutes) and a meta loop (days/weeks). Idle games compress all three: click/buy (seconds) -> unlock/upgrade (minutes) -> prestige/new world (hours-days).

- Natasha Dow Schull's *Addiction by Design* (Princeton UP, 2012) documents how slot-machine engineers tune games for "machine zone" continuity, i.e. minimising friction between play events. Fifteen years of fieldwork in Las Vegas. [V bibliographic] https://muse.jhu.edu/book/61897 and https://uwm.edu/digital-arts-culture/?p=300 (the title's subtitle "From Slot Machines to Candy Crush" explicitly links the casino design vocabulary to mobile games).
- Designer Lantz (Candy Box / A Dark Room lineage, quoted in a New Yorker piece surfaced via MetaFilter) says these games "tap into a very virulent, addictive quality, like slot machines" and are easy to make. [V via secondary quote] https://www.metafilter.com/180147/The-unclicked-life-is-not-worth-living-So-crates
- Ryan, Rigby & Przybylski (2006), *Motivation and Emotion*: the "pull" of games is largely explained by satisfaction of autonomy, competence and relatedness; these independently predict enjoyment and future play. [V] https://www.e-teaching.org/materialien/literatur/ryan-rigby-przybylski-2006 and https://acuresearchbank.acu.edu.au/item/8q128/the-motivational-pull-of-video-games-a-self-determination-theory-approach . Caveat in the same source: biased samples, limited genres.

**Why compulsion loops are legitimately satisfying (SDT lens).** Competence is served by constant visible growth; autonomy by choosing what to buy next; relatedness is weak in most idle games (an opportunity, see Implications).

**Ethical flag.** Compulsion-loop design shades into exploitation when paired with timers + paywalls. Press and scholarship (Schull, the Replay article above) treat this as the genre's dark side. Players notice: see player_complaints.md.

---

## 3. Variable reward schedules

- **Origin.** Skinner's operant conditioning: reinforcement schedules (fixed/variable x ratio/interval). Variable-ratio (VR) schedules - reward after an unpredictable number of responses - produce the highest, most extinction-resistant response rates, and slot machines are the textbook VR example. [V as textbook description] https://www.medschoolcoach.com/operant-conditioning-reinforcement-schedules-mcat-psychology/ (educational site; primary: Ferster & Skinner 1957, *Schedules of Reinforcement* [B]).
- **Do idle games actually use VR?** Only partly. The core incremental loop is closer to a *fixed/deterministic* schedule: a purchase is available at a calculable time. Real VR enters via: random golden cookies/events (Cookie Clicker), loot/drop rolls, gacha, critical hits, random offline events. [B/P]. A low-authority claim that "idle games employ variable reward schedules" appeared in search results but no rigorous source; do not cite it as research.
- **Predictability is itself rewarding.** Pecorella's *Math of Idle Games* series (Kongregate/GameAnalytics) treats idle games as designed around exponential cost curves with *known* next-goal timing, and prestige loops tuned so each run feels faster. [V existence/structure] https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i , https://www.gamedeveloper.com/game-platforms/the-math-of-idle-games-part-ii , https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii , talk https://www.gdcvault.com/play/1023863 . So the design blends deterministic goal-gradient pull with sprinkled VR surprises.
- **Design implication.** Use VR for *delight* (rare bonus, lucky crit), not for *progress gating*. Gating progress on randomness is the gacha/gambling mode that draws regulation and player resentment.

---

## 4. "Numbers go up"

- Lantz (via New Yorker/MetaFilter): "the human brain isn't really designed to intuitively understand things like exponential growth," and a good clicker lets the player engage directly with those numerical patterns. [V via quote] https://www.metafilter.com/180147/The-unclicked-life-is-not-worth-living-So-crates
- Pecorella: the engine of the genre is exponential cost growth vs polynomial/exponential production growth, with new generators and prestige currencies introduced at milestones so the numbers stay "meaningful". [V] https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i ; a summary of the same dynamic: https://if50.substack.com/p/2017-universal-paperclips?open=false
- Deterding argues the numeric progress is the *entire* aesthetic: it's gamification stripped to its core, which is why it works as both satire and genuine experience. [V] https://eprints.whiterose.ac.uk/id/eprint/146788
- **Player-side evidence of the limit.** A 2024 r/incremental_games thread ("What makes an idle game fun") has commenters saying numbers rising *too fast* turns them off; they want numbers to rise "because they made them rise", and dislike instant exponent notation with no sense of scale. [V via mirror] https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhn00vj/?context=3 and https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhsya5e/?context=3
- Mechanism hypotheses [B/P]: (a) Weber-Fechner: perceived change is proportional, so designers must keep *relative* growth (x1.15 per level) visible, not absolute; (b) legibility of feedback (animated counters, particle bursts) - "juice"; (c) the number is a proxy for competence.

---

## 5. Goal-gradient effect

- Hull (1932) described rats running faster nearer food [B]. **Kivetz, Urminsky & Zheng (2006), "The Goal-Gradient Hypothesis Resurrected: Purchase Acceleration, Illusionary Goal Progress, and Customer Retention", *Journal of Marketing Research* 43(1):39-58.** Findings: café "buy ten, get one free" customers bought more frequently as they neared the reward; a 12-stamp card with 2 bonus stamps was completed faster than a plain 10-stamp card; stronger acceleration predicted retention and faster re-engagement; a second study with song ratings online replicated the pattern; alternatives (habituation, expiry worries) ruled out. [V] https://business.columbia.edu/faculty/research/goal-gradient-hypothesis-resurrected-purchase-acceleration-illusionary-goal and https://business.columbia.edu/sites/default/files-efs/pubfiles/1200/goalgradient.pdf and https://www.chicagobooth.edu/review/going-goal
- **Game translation.** Progress bars toward the next unlock/upgrade/world cause acceleration of engagement as the bar fills. Idle games are essentially a nested stack of goal gradients (next generator, next milestone, next prestige). Short, visible gradients *everywhere* is the core retention trick.
- **Risk.** Acceleration near the goal implies a *drop* right after reaching it (the post-reward slump); the cure is to show the next gradient already partly filled (endowed progress, next section).

---

## 6. Endowed progress effect

- **Nunes & Drèze (2006), "The Endowed Progress Effect: How Artificial Advancement Increases Effort", *Journal of Consumer Research* 32(4):504-512.** Field experiment: 300 car-wash cards; 8-stamp card (empty) vs 10-stamp card with 2 stamps pre-applied; both need 8 purchases. After 9 months, ~34% of the pre-stamped group redeemed vs ~19% of the empty-card group. [V via secondary summaries; primary paper not re-opened] https://siliconcanals.com/t-car-wash-loyalty-cards-endowed-progress/ , https://thinkinsights.net/index.php/consulting/endowed-progress-effect , https://loyaltyrewardco.com/loyalty-psychology-series-endowed-progress-effect . One blog mislabels this as a coffee-shop study - it is a car wash.
- Moderator noted in the secondary sources: the head start must be *framed* as earned/justified (e.g. "bonus for being a customer"), not arbitrary. [V weakly] https://loyaltyrewardco.com/loyalty-psychology-series-endowed-progress-effect
- Kivetz et al. (above) independently found the same "illusory progress" speed-up with 2 bonus stamps. [V] columbia link above.
- **Game translation.** Tutorials that grant the first generator free; starting a new world with a pre-filled bar; prestige that *starts you at 10-20%* of the next goal; "welcome back" bonuses. UX piece: https://uxdesign.cc/endowed-progress-effect-give-your-users-a-head-start-97d52d8b0396 [P].

---

## 7. Zeigarnik effect (and why not to over-rely on it)

- **Original:** Bluma Zeigarnik (1927) - interrupted tasks were recalled better than completed ones; related Ovsiankina effect = tendency to *resume* interrupted tasks. [V] https://en.wikipedia.org/wiki/Zeigarnik_effect (surfaced in search; page itself not fetchable).
- **Replication problem:** Ghibellini & Meier (2025), "Interruption, recall and resumption: a meta-analysis of the Zeigarnik and Ovsiankina effects", *Humanities and Social Sciences Communications* 12 - 59 studies; **no reliable memory advantage for unfinished tasks** (secondary blog quotes recall ratio ~0.99, d ~0.15 - unverified), but a **general resumption tendency (Ovsiankina) holds**. They suggest situational factors (experimenter authority, involvement) explain early-study results. [V] https://ideas.repec.org/a/pal/palcom/v12y2025i1d10.1057_s41599-025-05000-w.html and https://www.kog.psy.unibe.ch/e48276/e1785865/s41599-025-05000-w1_ger.pdf and https://boris.unibe.ch/189777/
- **Game use.** "Quest log" folklore: Rigby & Ryan, *Glued to Games*, cited as linking it to MMO quest chains where completing one quest offers another with larger reward. [P] https://www.psychologyofgames.com/2013/03/the-zeigarnik-effect-and-quest-logs and https://www.psychologytoday.com/us/blog/mind-games/201303/the-zeigarnik-effect-and-quest-logs-8
- **Design conclusion:** cite *resumption tendency*, not "better memory". Keep a visible list of open goals (the "to-do" pull) but do not claim a strong scientific basis in docs/pitches.

---

## 8. Loss aversion (and the idle-game paradox)

- **Kahneman & Tversky (1979), prospect theory, *Econometrica*; Tversky & Kahneman (1992) CPT** - losses loom larger than gains, canonical coefficient ~2 (2.25 median in 1992) [B; unverified this session].
- **Critique:** Gal & Rucker (2018), "The Loss of Loss Aversion: Will It Loom Larger Than Its Gain?", *J. Consumer Psychology*: evidence does not support a general claim that losses are more impactful than gains; critics say this attacks a strong straw-man and that weaker forms survive. [V] https://economics.uq.edu.au/node/5353 , https://www.jasoncollins.blog/posts/the-case-against-loss-aversion , https://ritholtz.com/2018/08/losing-loss-aversion , https://atticusli.com/replication-crisis/loss-aversion/
- **Idle game relevance.** (a) *Sunk cost / reset dread*: players resist prestige because they feel they lose progress; HN commenters complain about resets being "laziness to create 'infinite' progress" yet others find sparse resets fine. [V] https://brianlovin.com/hn/29633599 (via search snippet). (b) *Streaks and decay mechanics* (daily login loss) exploit loss aversion but are widely resented as dark patterns. (c) Clash-style "your resources can be raided" is loss-driven; idle games rarely use it - and mostly shouldn't.
- Design rule: frame prestige as **gain** ("+240% production, keep your cards") not **loss** ("reset your world").

---

## 9. Why idle games satisfy *without skill*

Synthesising the above:

1. **Competence without risk.** SDT says competence need satisfaction predicts enjoyment (Ryan et al. 2006, link in sec. 2); idle games supply perceived competence via visible growth while removing failure states. Cheap, guaranteed competence.
2. **Planning replaces execution.** Alharthi et al.: players move from playing to planning (CHI 2018 link). The "skill" is optimisation/forecasting - spreadsheet-brain - available to anyone willing to think, not requiring reflexes.
3. **Exponential legibility.** Lantz: engaging directly with exponential patterns (MetaFilter link).
4. **Dense nested goal gradients + endowed progress** (secs 5-6) => constant micro-wins.
5. **Low activation energy and interruptibility.** Designers describe "active withdrawal" as central (Spiel et al. 2019). You can leave and come back to a gain (offline progress) rather than a loss.
6. **Deterministic control with sprinkled randomness** (sec. 3).
7. **Satire of progress itself.** Deterding: they began as parodies of RPG/social-game progress mechanics, yet the mechanics still work on the player - an honest demonstration that progress mechanics alone are motivating. https://eprints.whiterose.ac.uk/146788/1/25_Deterding_draft_final_180515_SDE.pdf

Counter-evidence: the same lack of skill creates boredom: "no meaningful choices is the sole reason your earlygame is boring" (itch.io dev forum commenter) [V via snippet] https://itch.io/post/4371860 ; developer guide arguing idle games still need meaningful choices https://bugnet.io/blog/how-to-make-a-idle-game [P].

---

## 10. Other relevant ideas (brief)

- **Autotelic / flow** (Csikszentmihalyi) and **curiosity/novelty** (Berlyne) - [B], not verified in this session; flow needs challenge-skill balance, which idle games sidestep by letting the *player choose how engaged to be*.
- **Sunk cost** is frequently asserted in popular articles about Cookie Clicker "addiction" but those pages were low-quality SEO mirrors and were not used as evidence.
- **Cozy-turned-exploitative.** The Replay article title itself captures the main ethical trajectory. https://www.czasopisma.uni.lodz.pl/Replay/article/view/23588

---

## Summary table: effect -> evidence strength -> usage

| Effect | Evidence strength | How to use |
|---|---|---|
| Goal gradient | Strong (field + online, Kivetz 2006) | Many short visible bars; show distance to next unlock |
| Endowed progress | Moderate-strong (field, Nunes & Drèze 2006; Kivetz) | Pre-fill new worlds/forms; justify the head start |
| Variable reward | Strong in animals/gambling; partial fit to idle | Rare delight events, never gate core progress |
| Zeigarnik (memory) | Weak/non-replicating (2025 meta-analysis) | Don't rely on it; use Ovsiankina resumption instead |
| Loss aversion | Contested magnitude (Gal & Rucker 2018) | Frame as gains; avoid punishing decay |
| SDT competence/autonomy | Strong, but biased samples | Offer meaningful choices (autonomy) + visible growth |

---

## Implications for a Kamen Rider Decade world-progression upgrade idle game

Decade's premise (a Rider who passes through parallel Rider worlds, collecting their powers via Kamen Ride cards, ending in the Final Form Ride / Dimension Kick) is a near-perfect carrier for the psychology above. Concrete proposals:

1. **World = prestige layer, framed as gain.** Do not make "reset" the verb. Make it "ride into the next world": you *keep* Rider cards and a compact "Decade Driver" meta-multiplier (avoids loss-aversion backlash; Gal & Rucker caveat means we shouldn't lean on loss framing anyway). Sparse resets are tolerated (HN thread, https://brianlovin.com/hn/29633599).
2. **Endowed progress at each world entry.** On arrival, the world's first Rider card is already "half-charged" (e.g. 20% of its gauge), justified diegetically ("Tsukasa's camera remembers this world"). Nunes & Drèze / Kivetz show 2 free stamps of 10 => ~34% vs ~19% completion.
3. **Goal gradients everywhere.** Each Rider's Final Form Ride/Attack Ride card gets a visible gauge; a master "Dimension Kick" charge bar shows distance to world boss. Expect acceleration as bars fill (Kivetz).
4. **Collection quest log = Ovsiankina not Zeigarnik.** Show 9-Rider-world completion tiles, partially filled, so the player is pulled to resume; don't market it as "memory science".
5. **Variable reward for delight only.** Random "Kamen Ride" surprise summons (a bonus Rider appears for 30s) as golden-cookie analogue; never gate world progress on RNG.
6. **Make the planning meaningful.** Alharthi's planning-over-playing finding means the skill is choosing *which Rider synergies* (e.g. Kiva bat-swarm vs. Den-O time-skip) to slot; ensure >=2 viable builds so choice is real (itch.io critique https://itch.io/post/4371860).
7. **Control number inflation.** Reddit commenters dislike numbers that jump too fast and exponent gibberish (https://libreddit.neb.cx/r/incremental_games/comments/1epowcl/what_makes_an_idle_game_fun/lhn00vj/?context=3): use named tiers (Rank D -> S) and show multipliers as "x1.5" rather than "1.2e47" until late.
8. **Competence + autonomy first, relatedness as opportunity.** Ryan et al. 2006: lean on card-collection autonomy; consider light social (shared "Rider Rally" weekly goals) later.
9. **Ethics guardrail.** Avoid daily-streak loss mechanics and forced ads; the genre is under critique as exploitative (https://www.czasopisma.uni.lodz.pl/Replay/article/view/23588). Authentic Decade tone (a "destroyer" who is secretly a connector of worlds) supports a generous, non-predatory design.
