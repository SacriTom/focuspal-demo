# FocusPal Research Brief

**Agent:** IRIS (Insight & Research Intelligence Specialist)
**Date:** 2026-03-19
**Status:** READY FOR SAGE
**Confidence:** High (methodology sound, sources triangulated, limitations stated)

---

> **Regulatory Flag (Read First):** FocusPal's emotion-influencing system (Chibi mood states responding to user behaviour) sits in a grey area under the EU AI Act. It is not AI-based emotion recognition (no biometric input, no inference from facial/vocal cues), so it falls outside the Article 5 prohibitions. However, if the app is accessible to children under 18 — which the Tamagotchi aesthetic strongly suggests it will be — GDPR's children's data provisions and the ICO's Age Appropriate Design Code apply. Privacy-by-design with app-level-only detection is a strong starting position, but the team must make an explicit decision about target age range and document it. See Sections 10 and 11 for full analysis.

---

## 1. Executive Summary

The screen-time reduction app market is growing at 7.2% CAGR toward a projected $4 billion by 2033 (ConsaInsights, 2024), yet the dominant apps — Forest, Flora, Opal, ScreenZen — all share a structural weakness: they treat focus as a transaction (plant a tree, block an app) rather than a relationship. No major competitor uses emotional attachment as the primary behaviour change mechanism. FocusPal's Chibi-based approach — where the user forms a bond through hatching, naming, and ongoing care — is differentiated and supported by behavioural psychology research on intrinsic motivation and the superiority of positive reinforcement over guilt-based interventions. The opportunity is real. The risk is not competition; it is whether the emotional bond is strong enough to survive the first week, and whether app-level-only usage detection provides sufficient behavioural signal to sustain the feedback loop.

**Implication for Design:** The core value proposition is emotional attachment, not productivity tracking. Every design decision should be filtered through the question: "Does this strengthen or weaken the user's bond with their Chibi?"

---

## 2. Market Landscape

### 2.1 Market Size and Growth

The global screen-time monitoring apps market is projected to reach $4 billion by 2033, with a CAGR of 7.2% from 2024 (ConsaInsights, 2024). This sits within a broader mobile app market valued at $330 billion in 2026 (Fortune Business Insights, 2025). Growth is driven by three converging forces:

1. **Rising screen time.** Global average screen time stands at 6 hours 40 minutes per day (DemandSage, 2026). Gen Z averages 6 hours 27 minutes on their phone alone. Teens aged 11-14 average approximately 9 hours per day including all screens (DemandSage, 2026). The problem is large and growing.

2. **Regulatory tailwinds.** The EU AI Act (fully applicable August 2026), GDPR children's provisions, the ICO's Age Appropriate Design Code, and the EU Digital Services Act are all pushing platforms toward digital wellbeing features. Apps that are privacy-by-design have a structural advantage.

3. **Consumer awareness.** Search interest in "digital wellbeing" and "screen time reduction" has grown steadily since 2020, with a notable spike post-pandemic as remote work and education normalised high screen-time baselines.

### 2.2 Market Segmentation

The screen-time app market segments into four categories:

| Segment | Approach | Examples | Weakness |
|---------|----------|----------|----------|
| **Blockers** | Restrict access to apps/sites | Opal, Freedom, Cold Turkey | Users feel controlled, often circumvent |
| **Friction-adders** | Add delay/awareness before opening apps | ScreenZen, one sec | Effective short-term, lacks engagement loop |
| **Gamified timers** | Reward focus time with growth metaphors | Forest, Flora | Transactional — no emotional bond |
| **Wellbeing companions** | Virtual pet/avatar tied to healthy behaviours | Finch (self-care, not screen time) | No direct competitor combines pet + screen time |

FocusPal sits in the fourth segment but is the first to combine virtual pet emotional attachment specifically with screen-time reduction. Finch (the closest analogue) targets self-care habits broadly, not screen time.

### 2.3 What the Data Does NOT Show

- No reliable data exists on long-term retention rates (>6 months) for any screen-time reduction app category. Claims of sustained behaviour change are self-reported, not independently validated.
- Market size figures for "screen time monitoring" include parental control apps, enterprise MDM tools, and consumer wellbeing apps in a single bucket. The consumer wellbeing subset is likely 15-25% of the total market (IRIS estimate; insufficient data to narrow further).
- No peer-reviewed study directly compares emotional-attachment-based interventions to gamified-timer interventions for screen time. The theoretical basis is strong but empirically untested in this specific application.

**Implication for Design:** FocusPal is entering a growing market with a genuinely novel mechanism. The competitive gap is wide, but so is the validation gap. Phase 1 should be designed to generate the behavioural data that proves or disproves the emotional attachment hypothesis.

---

## 3. Competitor Audit

### 3.1 Forest (Seekrtech)

**What it is:** Gamified Pomodoro timer. Users plant virtual trees that grow during focus sessions and die if the user leaves the app. Revenue model: paid app (iOS), freemium with ads (Android), plus in-app purchases for "Time Crystals."

**Scale:** 4 million+ paying users, ranked #1 in 136 countries at peak (Janice Lee, Medium, 2020). Recent estimates: approximately 400K monthly downloads, approximately $100K monthly revenue (SimilarWeb, 2025).

**Strengths:**
- Simple, immediately understood mechanic
- Real tree planting partnership (Trees for the Future) adds prosocial motivation
- Cross-platform including Chrome extension
- Social features (friend challenges, leaderboards)

**Weaknesses:**
- **Transactional, not relational.** Trees are interchangeable. Users don't name them, bond with them, or care about individual trees. The emotional connection is to the forest aggregate, not any single entity.
- **Punishment-oriented.** The core mechanic is loss (tree dies). This is guilt by another name. Research indicates guilt-based approaches drive short-term compliance but not sustained behaviour change (see Section 5).
- **No passive monitoring.** Only works during active timer sessions. Users must consciously initiate focus — the app has no awareness of behaviour outside sessions.
- **Aesthetic fatigue.** The tree metaphor is well-worn. Multiple clones exist (Flora, Plantie, etc.).

**Gap FocusPal fills:** Emotional bond (named creature vs. anonymous tree), passive awareness (hybrid timer), positive reinforcement (thriving creature vs. dying tree).

### 3.2 Flora

**What it is:** Forest clone with enhanced social accountability. Free to use; monetises through real tree planting donations.

**Strengths:**
- Free tier is genuinely functional
- Social planting (shared trees die if anyone in the group checks their phone) creates strong accountability
- Unlimited real tree planting (vs. Forest's 5-tree cap)

**Weaknesses:**
- iOS only. Requires Facebook login. Both are significant friction barriers.
- Same transactional/guilt mechanic as Forest
- No passive monitoring
- No emotional differentiation from Forest

**Gap FocusPal fills:** Platform independence (Flutter = cross-platform), no social media login requirement, emotional engagement beyond social pressure.

### 3.3 Opal

**What it is:** Screen-time control app with blocking, session tracking, focus scores, and leaderboards. Premium pricing: approximately $100/year.

**Strengths:**
- Sophisticated blocking with granular controls
- Focus Score gamification adds a competence dimension
- Real-time data and usage analytics
- Professional/clean design language

**Weaknesses:**
- **Requires extensive device permissions.** Uses VPN-based blocking and accessibility services. This is the opposite of privacy-by-design.
- **Expensive.** $100/year prices out the student demographic that most needs screen-time help.
- **Restrictive, not motivational.** Users report feeling "managed" rather than empowered (Product Hunt reviews, 2026). Compliance without internalisation.
- **No emotional engagement.** Purely analytical — data and dashboards, no character, no narrative.

**Gap FocusPal fills:** Privacy-by-design (zero permissions vs. VPN/accessibility), emotional motivation (Chibi bond vs. dashboards), accessible pricing (freemium vs. $100/year).

### 3.4 ScreenZen

**What it is:** Friction-based intervention. Adds configurable delays and awareness prompts before opening distracting apps.

**Strengths:**
- Psychologically sound — based on creating "pause moments" that interrupt automatic behaviour
- Lightweight, minimal permissions
- Granular per-app configuration
- Gentle approach that respects user autonomy

**Weaknesses:**
- **No engagement loop.** Once the friction becomes habitual, users either internalise the behaviour (success, but they uninstall) or habituate to the delays (failure, they uninstall). No retention mechanism.
- **No visual feedback.** No character, no progress, no narrative. Purely utilitarian.
- **Limited to app-launch moments.** No awareness of time spent within apps, only the decision to open them.

**Gap FocusPal fills:** Sustained engagement through emotional bond (Chibi gives a reason to keep the app), visual feedback on behaviour change over time, progressive reward system.

### 3.5 Finch (Adjacent Competitor)

**What it is:** Self-care app with a virtual pet bird. Users complete wellbeing tasks (breathing exercises, journaling, habit tracking) to earn points and care for their bird. Not a screen-time app, but the closest mechanical analogue to FocusPal.

**Strengths:**
- **Proves the virtual pet + behaviour change model works.** Users report genuine behavioural change over 6+ months (Yoga Journal, 2025; Autonomous.ai review). This is the strongest external validation for FocusPal's core hypothesis.
- Hatching/naming mechanic creates emotional attachment
- Diverse wellbeing tasks prevent monotony
- Premium monetisation via Finch Plus (approximately 71 GBP/year)

**Weaknesses:**
- **Not a screen-time app.** Finch requires active engagement (completing tasks). It does not monitor or respond to screen time. A user could spend 10 hours on their phone and their Finch would be perfectly happy.
- **Complexity.** Reviews note the interface is "dense" with journeys, goals, journal tags, and energy points (Autonomous.ai review). Onboarding is a friction point.
- **Billing concerns.** Multiple App Store reviews flag unauthorised Finch Plus charges and unresponsive customer support (App Store reviews, 2025).
- **Potential for stress.** The daily task checklist can create pressure rather than reduce it — the opposite of the intended wellbeing effect (Internet Matters, 2025).

**Gap FocusPal fills:** Screen-time-specific behaviour change (Chibi responds to phone usage, not task completion), simpler interface (emoji-only communication, single home screen), passive monitoring (Chibi mood updates without requiring active task completion).

### 3.6 Competitive Landscape Matrix

| Feature | Forest | Flora | Opal | ScreenZen | Finch | **FocusPal** |
|---------|--------|-------|------|-----------|-------|-------------|
| Emotional attachment | None | None | None | None | High | **High** |
| Passive monitoring | No | No | Yes | Partial | No | **Yes** |
| Active sessions | Yes | Yes | Yes | No | Yes | **Yes** |
| Privacy-by-design | Yes | Partial (FB login) | No (VPN) | Yes | Yes | **Yes** |
| Positive reinforcement | Partial (growth) | Partial | No | No | Yes | **Yes** |
| Guilt/punishment mechanic | Yes (tree dies) | Yes | Yes (blocking) | No | No | **No** |
| Personalisation | Low | Low | Medium | Medium | High | **High** |
| Cross-platform | Yes | iOS only | iOS + Android | iOS + Android | iOS + Android | **Yes (Flutter)** |
| Free tier | Android only | Yes | Limited | Yes | Yes | **Yes** |

**Implication for Design:** FocusPal's competitive advantage is the intersection of emotional attachment + passive monitoring + privacy-by-design. No competitor occupies this intersection. Protect it. Do not drift toward becoming another timer app or another blocker.

---

## 4. User Personas

Three personas derived from screen-time usage data, competitor review patterns, and behavioural research. Confidence levels noted per persona.

### 4.1 Persona: Mia — The Overwhelmed Student

**Confidence:** Indicates (medium) — supported by screen-time demographics and Forest/Flora's primary user base being students.

| Attribute | Detail |
|-----------|--------|
| Age | 19-24 |
| Screen time | 7+ hours/day (DemandSage, 2026: 16-24 age group averages 7h 11m-7h 35m) |
| Pain point | Knows screen time is a problem, has tried Forest/blockers, keeps circumventing them |
| Motivation | Wants to study more effectively, feels guilty about phone use but guilt hasn't changed behaviour |
| Relationship with phone | Love-hate. Phone is also social lifeline, study tool, entertainment |
| Why FocusPal works for her | She bonds with creatures (grew up with virtual pets, Pokemon, Animal Crossing). Guilt makes her feel worse; a cute creature that thrives when she focuses makes her feel better. The emotional cost of making her Chibi sad is more motivating than a dead tree she never cared about. |
| Risk | May find passive monitoring too "always on" — needs clear communication that the app respects her autonomy |

### 4.2 Persona: David — The Productivity-Curious Professional

**Confidence:** Suggests (low) — inferred from Opal's user base and productivity app trends. Less direct evidence than the student persona.

| Attribute | Detail |
|-----------|--------|
| Age | 28-35 |
| Screen time | 5-6 hours/day, mostly work-adjacent (Slack, email, news) |
| Pain point | Not addicted but aware of "drift" — picks up phone during deep work, loses 20 minutes |
| Motivation | Values focus for career output, interested in "calm tech" and digital minimalism |
| Relationship with phone | Pragmatic. Phone is a tool that sometimes becomes a distraction |
| Why FocusPal works for him | The active session mode (adventure rewards) maps to his Pomodoro-style work habits. The Chibi adds a lighthearted element to an otherwise serious productivity stack. Configurable sensitivity lets him match the app to his actual work patterns. |
| Risk | May find the Tamagotchi aesthetic too childish. Tone must be "charming" not "kiddy." The premium Chibi options (dragons, unicorns) may appeal if they signal sophistication rather than cuteness. |

### 4.3 Persona: Sarah — The Concerned Parent

**Confidence:** Suggests (low) — inferred from parental control market trends and the ICO's Age Appropriate Design Code target audience. FocusPal is not positioned as a parental control app, but parents may discover it.

| Attribute | Detail |
|-----------|--------|
| Age | 35-45 |
| Screen time (child) | 5.5 hours/day for children aged 8-12 (DemandSage, 2026) |
| Pain point | Worried about child's screen time, wants a gentler approach than blockers/time limits |
| Motivation | Looking for something her child will voluntarily engage with, not resist |
| Relationship with phone | Her child's phone, not hers. She wants oversight without surveillance |
| Why FocusPal works for her | FocusPal is something her child would actually want to use. The Chibi creates intrinsic motivation — the child wants to keep the creature happy, rather than resenting a parent-imposed limit. Privacy-by-design means no tracking data she'd need to worry about. |
| Risk | **Significant regulatory implications.** If FocusPal attracts users under 13/16, GDPR Article 8 (child consent), the ICO Children's Code, and COPPA (US market) all apply. The team must decide: is FocusPal for children or not? See Section 10. |

### 4.4 What the Personas Do NOT Cover

- **Users with clinical screen addiction.** FocusPal is a wellness tool, not a therapeutic intervention. Users with diagnosed problematic internet use need clinical support, not a Chibi.
- **Users who want hard blocking.** Some users genuinely want to be locked out of apps. FocusPal does not and should not do this — it would contradict the autonomy principle that underpins the behaviour change model.
- **Users over 45.** Insufficient data to construct a credible persona. The virtual pet mechanic may or may not resonate. This segment requires primary research to validate.

**Implication for Design:** Design primarily for Mia (overwhelmed student). She is the largest addressable segment, the most underserved by current solutions, and the best match for FocusPal's core mechanic. David is a secondary audience. Sarah represents a market opportunity but triggers regulatory obligations that must be addressed before marketing to families.

---

## 5. Behavioural Psychology and Screen-Time Research

### 5.1 Why Guilt-Based Approaches Fail

The conventional wisdom in screen-time apps is that showing users how much time they waste will motivate change. The data says otherwise.

**Finding 1: Guilt drives short-term compliance, not sustained change.**
Research on parental screen guilt demonstrates that while guilt can motivate short-term screen-time reduction, excessive guilt leads to negative psychological effects including increased parental stress and decreased relationship satisfaction (Taylor & Francis, Robb & Shellenbarger, 2024). The mechanism transfers to self-directed guilt: users who feel bad about their screen time may reduce it temporarily, but the negative emotional association with the intervention leads to app abandonment. This is consistent with Self-Determination Theory's finding that extrinsic and controlled forms of motivation fail to sustain behaviour change after the intervention ends (Ryan & Deci, 2000, SDT.org).

**Confidence level:** Indicates. Multiple studies converge on this finding across different populations, though none specifically test screen-time apps as the guilt mechanism.

**Counter-evidence:** Some users do respond to "shock" data (e.g., "You spent 4 hours on TikTok today"). However, this effect habituates rapidly — the 15th notification carries less weight than the first. And for users who already feel guilty, the additional data compounds negative affect without providing a path to change.

**Finding 2: Positive reinforcement outperforms punishment for sustained behaviour change.**
Behavioural-change literature consistently identifies goal setting, positive reinforcement, and self-monitoring as the most effective techniques (Self-Determination Theory, Ryan & Deci, 2000; Fogg Behavior Model). Interventions that combine positive reinforcement with goal-setting tend to produce larger and more sustained effects than those relying on restriction or negative feedback.

**Confidence level:** Indicates. Aligned with established behaviour-change frameworks (SDT, Fogg).

**Implication for FocusPal:** The Chibi thriving (positive reinforcement) is architecturally superior to a tree dying (punishment). This is not a matter of aesthetics — it is a mechanistic difference in how the brain processes the feedback. FocusPal's design should emphasise what the user gains (happy Chibi, new activities, adventures) rather than what the user loses (annoyed Chibi).

### 5.2 Self-Determination Theory (SDT)

SDT (Deci & Ryan, 1985; 2000) identifies three innate psychological needs that, when satisfied, produce intrinsic motivation and sustained behaviour change:

| Need | Definition | FocusPal Application |
|------|-----------|---------------------|
| **Autonomy** | Feeling that actions are self-chosen, not controlled | Configurable sensitivity thresholds; user names Chibi; user initiates active sessions voluntarily |
| **Competence** | Feeling effective and capable | Chibi skill learning (Phase 2); visible progress; mood improvements as feedback on success |
| **Relatedness** | Feeling connected to others or to meaningful entities | Emotional bond with Chibi; hatching/naming ritual; Chibi as a "someone" not a "something" |

A 2024 review of behaviour change technologies identified 50 specific design suggestions mapped to SDT needs: 11 for autonomy, 22 for competence, 17 for relatedness (Interacting with Computers, Oxford Academic, 2024).

**Confidence level:** Demonstrates. SDT is one of the most extensively validated theories in motivational psychology with over 40 years of research.

**Critical insight:** FocusPal's configurable sensitivity thresholds directly serve the autonomy need. This is not a nice-to-have feature — it is load-bearing for the behaviour change mechanism. Users who feel controlled by an app will disengage (the same way they disengage from blockers they can't override). The ability to adjust thresholds converts the experience from "the app is judging me" to "I'm choosing my own challenge level."

### 5.3 The Fogg Behavior Model (B=MAP)

BJ Fogg's model (Stanford Behavior Design Lab) states that behaviour occurs when three elements converge simultaneously:

- **Motivation (M):** The user wants to reduce screen time
- **Ability (A):** The target behaviour is easy enough to perform
- **Prompt (P):** Something triggers the behaviour at the right moment

**Application to FocusPal:**

| Element | How FocusPal Delivers |
|---------|----------------------|
| Motivation | Emotional bond with Chibi. User wants the Chibi to be happy. This is intrinsic motivation, the most durable type. |
| Ability | Putting the phone down is extremely simple (Ability = high). The target behaviour is inaction, not action. This is an unusual advantage — most behaviour change apps ask users to do something hard. FocusPal asks them to do nothing. |
| Prompt | Passive monitoring detects phone pickup. Chibi mood change serves as a just-in-time prompt. The user sees an annoyed Chibi and is motivated to put the phone down. |

**Confidence level:** Indicates. The model is well-validated but the specific application (inaction as target behaviour) is novel and untested.

### 5.4 The Hook Model (Nir Eyal)

Eyal's Hook Model describes the habit loop that makes products "sticky":

1. **Trigger:** Internal (guilt about screen time, desire to check on Chibi) or external (notification, lock screen)
2. **Action:** Open FocusPal, see Chibi's current state
3. **Variable Reward:** Chibi is doing something unexpected — learning guitar, cooking sushi, reading a tiny book. The variability is critical; predictable rewards lose power (Rewards of the Self: mastery/care-giving satisfaction)
4. **Investment:** User has named the Chibi, watched it learn skills, accumulated progress. Switching cost increases over time.

**Key insight:** The skill-learning system (Phase 2) serves double duty. It is both a competence reward (SDT) and a variable reward (Hook Model). The user doesn't know what the Chibi will learn next, creating anticipation. This suggests skill learning should be prioritised in Phase 2.

**Confidence level:** Indicates. The Hook Model is a commercial framework, not peer-reviewed science. However, its principles align with operant conditioning research (variable ratio reinforcement schedules produce the most persistent behaviours).

### 5.5 What the Research Does NOT Show

- No study has tested whether emotional attachment to a virtual creature reduces screen time specifically. The theoretical basis is strong (SDT + Fogg + Finch's validated pet model) but the specific hypothesis is unproven.
- The optimal "dose" of negative feedback (Chibi annoyance) before users disengage rather than change behaviour is unknown. Too little and there's no signal; too much and users avoid the app.
- Whether adults form emotional attachments to virtual pets with the same intensity as children/teens is unclear. The Finch evidence suggests yes, but Finch users self-select for the mechanic.

**Implication for Design:** FocusPal's behaviour change model is theoretically well-grounded but empirically untested in this specific configuration. Phase 1 should instrument mood state transitions and session data to validate the core hypothesis: does Chibi emotional state actually correlate with reduced screen time?

---

## 6. Configurable Sensitivity Validation

### 6.1 Why Configurable Sensitivity Matters

Decision D-006 specifies "clear cause-and-effect emotional response with configurable sensitivity." This section validates whether configurable thresholds are appropriate and recommends default values and ranges.

### 6.2 Recommended Defaults and Ranges

The 6-state emotion machine (Ecstatic > Happy > Content > Annoyed > Sad > Sleepy) needs threshold parameters for mood state transitions. Based on behavioural research on feedback timing and Fogg's Ability principle:

| Parameter | Default | Adjustable Range | Rationale |
|-----------|---------|-----------------|-----------|
| **Time-to-annoyance** (continuous use before Chibi becomes annoyed) | 20 minutes | 10-45 minutes | 20 min aligns with Pomodoro research on optimal focus intervals. Below 10 min creates frustration; above 45 min loses signal strength. |
| **Recovery time** (phone-down time before Chibi mood improves one level) | 5 minutes | 2-15 minutes | Short enough to feel achievable (Fogg: high Ability), long enough to constitute meaningful disengagement. |
| **Ecstatic threshold** (sustained non-use duration for highest mood) | 60 minutes | 30-120 minutes | Rewards extended focus sessions without making the top state unreachable. |
| **Annoyance escalation rate** (how quickly Chibi moves from Annoyed to Sad) | 10 minutes of continued use after Annoyed state | 5-20 minutes | Gives users warning time. Two-stage negative feedback (Annoyed, then Sad) is gentler than immediate punishment. |
| **Sleepy trigger** (time-of-day based, e.g., after 10pm) | 22:00 local time | 20:00-00:00 | Aligns with sleep hygiene research. Chibi "going to sleep" normalises putting the phone down at night. |

### 6.3 Evidence Base

- **Pomodoro research:** The Pomodoro Technique's 25-minute intervals are widely used but the original research base is thin. More robust evidence from attention research suggests sustained attention degrades after 20-25 minutes for most adults (Mackworth, 1948; re-validated in digital contexts by Mark et al., 2016). A 20-minute default is conservative and appropriate.
- **Recovery time:** Cognitive restoration research (Attention Restoration Theory, Kaplan, 1995) indicates that even brief nature exposure (5 minutes) can restore directed attention capacity. A 5-minute default recovery aligns with this.
- **Configurable range rationale:** SDT's autonomy need requires that users can adjust thresholds. Fixed thresholds would feel controlling. The ranges are bounded to prevent users from trivialising the system (e.g., setting annoyance at 3 hours, effectively disabling feedback) while preserving meaningful choice.

### 6.4 What the Data Does NOT Show

- Optimal thresholds for teenagers vs. adults are likely different. Teens have shorter sustained attention spans but higher emotional reactivity to virtual pet distress. Phase 1 should log threshold adjustments alongside mood data to identify age-related patterns.
- Whether users actually adjust thresholds or leave them at defaults is unknown. In software generally, fewer than 5% of users change default settings (Jared Spool, UIE, frequently cited heuristic). The defaults must be good enough for the 95%.

**Implication for Design:** Ship with the defaults above. Make threshold adjustment accessible but not prominent — a settings screen, not the home screen. Log all threshold changes for Phase 2 analysis. The defaults should err on the side of gentleness (slower escalation) to avoid early-stage app abandonment.

---

## 7. App-Level-Only Usage Detection

### 7.1 The Decision

Decision D-015 specifies app-level usage detection only, with privacy-by-design and zero device permissions. This section validates whether this is sufficient for behaviour change.

### 7.2 What App-Level Detection Can and Cannot Do

**What it CAN detect (no permissions required):**
- Whether the FocusPal app is in the foreground or background
- How long since the app was last opened
- Time-of-day context (for sleep/wake Chibi behaviour)
- Duration of active focus sessions (user-initiated)
- App lifecycle events (app opened, app closed, app backgrounded)

**What it CANNOT detect (would require permissions):**
- Which other apps the user is using
- Total screen-on time across the device
- Notification frequency
- Specific usage patterns (social media vs. productivity)
- Screen unlock count

### 7.3 Assessment: Sufficient with Caveats

**The case FOR app-level-only:**
- Privacy-by-design is a genuine competitive advantage. Opal requires VPN configuration. Forest requires accessibility service permissions on some devices. FocusPal requiring zero permissions is a trust signal.
- The EU AI Act and GDPR trajectory is toward less data collection, not more. Building with minimal data is future-proof.
- ScreenZen demonstrates that effective behaviour change is possible with minimal data — friction at the point of app launch doesn't require knowing what the user does elsewhere.
- The Chibi's emotional state is a proxy for behaviour, not a surveillance tool. This framing is critical for user trust.

**The case AGAINST (limitations):**
- Without knowing total screen time, FocusPal cannot show the user how their behaviour is changing in absolute terms. The Chibi mood is qualitative feedback, not quantitative data.
- The passive monitoring component (hybrid timer) can only detect when the user is NOT in FocusPal. It infers "phone usage" from "not in FocusPal" but cannot distinguish between "using TikTok for 2 hours" and "phone is on the table screen-off." This creates potential for false positives (Chibi gets annoyed when user hasn't actually been using their phone) and false negatives (user uses phone heavily but FocusPal app lifecycle events don't capture it).
- Competitors who access Screen Time API (iOS) or UsageStats API (Android) can provide richer, more accurate behavioural data.

### 7.4 Mitigation Strategy

The hybrid timer design (D-013) partially addresses these limitations:

| Mode | Detection Method | Accuracy |
|------|-----------------|----------|
| **Active session** | User explicitly starts/stops a focus session. Chibi goes on adventure. | High — clear signal, user-initiated |
| **Passive background** | App monitors its own foreground/background state via Flutter lifecycle. | Medium — can detect app switches but not what user switches to |
| **Inferred rest** | If app hasn't received any lifecycle event for X minutes, infer phone is idle. | Low — inference, not observation. Phone could be in use with FocusPal in background. |

**Confidence level:** Indicates. App-level detection is sufficient for a meaningful behaviour change feedback loop, but the passive component will have accuracy gaps. These gaps are acceptable for Phase 1 if the user understands the system is approximate, not precise.

### 7.5 What the Data Does NOT Show

- Whether users trust approximate feedback as much as precise feedback is unknown. A Chibi that gets annoyed "unfairly" (user wasn't actually on their phone) could erode trust in the system.
- The iOS Screen Time API has "major issues" even for apps that do request permission (riedel.wtf, 2024), suggesting that precise detection is harder than it appears. App-level-only may sacrifice less accuracy than assumed.

**Implication for Design:** App-level-only detection is validated as a reasonable Phase 1 approach. The active session mode is high-accuracy and should be the primary behaviour change lever. Passive monitoring should be clearly communicated as approximate ("Your Chibi notices when you're away") and never claim precision it doesn't have. Phase 2 should evaluate whether optional permission-based detection (via Screen Time API / UsageStats API) is worth offering as an opt-in upgrade.

---

## 8. Environment Reflects Wellbeing (D-018 Validation)

### 8.1 The Question

Decision D-018 conditionally approved the concept that the Chibi's environment (home scene) reflects its emotional state — e.g., clean and bright when happy, cluttered and dim when sad. This section validates whether this aligns with behaviour change research.

### 8.2 Evidence For

**Ambient information displays work.** Stanford's research on ambient display interventions (WholsZuki project) demonstrated that visualising behaviour change on phone lock screens leverages the 150+ daily phone checks as nudging opportunities. Users don't need to consciously engage with the display — the ambient information influences behaviour subconsciously. Environmental changes in FocusPal serve the same function: the user opens the app and immediately perceives wellbeing state without reading numbers or text.

**Eco-feedback research validates the approach.** A study on real-time feedback in sustainability contexts found that ambient visual feedback (e.g., changing colours to represent energy use) reduced target behaviours by 22% — substantially greater than information-only interventions (ScienceDirect, Froehlich et al., 2010). The mechanism is rapid visual processing: users don't need to interpret data, they see the state.

**Consistent with the Chibi's emotional system.** The environment is a secondary channel reinforcing the primary channel (Chibi mood). Redundant encoding (same message through multiple channels) is a well-established principle in information design and increases the probability of the message being received.

### 8.3 Evidence Against / Risks

- **Implementation cost.** Environmental changes require additional art assets and state logic for Phase 1. If the environment has 3+ states and the Chibi has 6 mood states, the combinatorial space grows.
- **Potential for negative affect.** A visually "sad" environment (dark, cluttered) could make the app unpleasant to open, creating avoidance rather than motivation. This is the same guilt-based failure mode discussed in Section 5.
- **Diminishing marginal value.** The Chibi's mood (expressed through emotion states and emoji speech bubbles) already communicates wellbeing. The environment is redundant. Redundancy aids comprehension but costs development time.

### 8.4 Recommendation: PROCEED, but Simplified

Environmental feedback is supported by ambient information research. However, for Phase 1:

- **Simplify to 2-3 states** (not 6 matching mood states): Bright/Normal/Dim. More nuance can be added in later phases.
- **Keep negative states mild.** "Dim" not "destroyed." The environment should signal a dip, not create distress.
- **Ensure the positive state is rewarding.** A bright, clean environment with sunlight, flowers, or seasonal touches makes the app pleasant to open when the user is doing well — positive reinforcement.

**Confidence level:** Indicates. The evidence supports environmental feedback as a behaviour change mechanism. The specific implementation (2-3 states, mild negative) is a design recommendation based on the guilt-avoidance research in Section 5.

**Implication for Design:** Proceed with environmental feedback in Phase 1, simplified to 2-3 visual states. The bright/positive state should be noticeably rewarding. The dim/negative state should be noticeable but not unpleasant. SAGE should design the states; FORGE should implement them as a simple conditional on the dominant mood.

---

## 9. Premium Chibi Monetisation

### 9.1 The Model

FocusPal proposes a freemium model: three free starter Chibis (Cat, Penguin, Panda) with premium Chibis (baby dragons, unicorns, etc.) available for purchase.

### 9.2 Market Evidence

**The virtual pet games market is large and growing.** Estimated at approximately $2 billion in 2025 with a projected CAGR of approximately 15% through 2033 (Market Report Analytics, 2025). The freemium model dominates, with in-app purchases for cosmetics, virtual currency, and creature variants as the primary revenue driver.

**Tamagotchi's resurgence validates creature-based monetisation.** Global Tamagotchi sales have doubled in recent years, and a London flagship store opened in 2024 (Electronic Specifier, 2024; The Toy Book, January 2025). My Tamagotchi Forever uses freemium mechanics successfully.

**Finch validates the model in the wellbeing space.** Finch Plus costs approximately 71 GBP/year and monetises through premium features, cosmetics, and expanded content. Users pay for emotional value (dressing their bird, new habitats), not utility.

**Forest validates willingness to pay in the focus space.** 4 million+ paying users (iOS one-time purchase) plus in-app Time Crystal purchases (Medium, Janice Lee, 2020).

### 9.3 Pricing Considerations

| Model | Pros | Cons |
|-------|------|------|
| **One-time purchase per Chibi** (e.g., 1.99-3.99) | Simple, low friction, feels fair | Lower LTV, revenue ceiling |
| **Subscription** (monthly/yearly) | Higher LTV, funds ongoing development | Subscription fatigue, especially for a "fun" app |
| **Season/bundle packs** | Middle ground, feels like value | Requires ongoing content creation |

**Recommendation:** Start with one-time purchases per premium Chibi. The emotional investment model means users buy a Chibi they want to bond with — this is a one-time emotional decision, not a recurring utility. Subscription can be explored in Phase 3 if the content pipeline (new Chibis, environments, accessories) justifies ongoing payments.

### 9.4 Ethical Consideration

If FocusPal attracts minors (see Section 10), in-app purchases targeting children face regulatory scrutiny under the ICO Children's Code (Standard 12: "Nudge techniques should not be used to encourage children to provide unnecessary personal data, weaken or turn off their privacy settings" — and by extension, should not be designed to pressure children into purchases). The purchasing flow must not use dark patterns, countdown timers, or "your Chibi wants this" emotional manipulation.

### 9.5 What the Data Does NOT Show

- Willingness to pay for premium creatures in a screen-time app (vs. a game) is untested. Users may view a wellness tool differently from an entertainment product.
- The optimal number of free starters is unknown. Three is reasonable (enough choice to feel autonomous, few enough that premium options are attractive) but has not been A/B tested.
- Whether cosmetic customisation (dressing/themes, Phase 3) generates more revenue than creature variants is unknown. Finch's revenue breakdown is not public.

**Implication for Design:** The freemium model with premium Chibis is validated by market precedent. Phase 1 should implement the three free starters and the selection UX. The premium Chibi store can be stubbed (UI present, payment not connected) to validate interest before Phase 2 investment. SAGE should design the selection screen to feel generous (three great free options) rather than restrictive (three basic options gating the good stuff).

---

## 10. GDPR and EU AI Act Analysis

### 10.1 GDPR Assessment

**FocusPal's data profile (Phase 1 — local storage only):**

| Data Type | Stored | Location | GDPR Relevance |
|-----------|--------|----------|---------------|
| Chibi name | Yes | Local device | Personal data if name is real; likely not if fantasy name |
| Chibi mood state history | Yes | Local device | Not personal data (it describes the creature, not the user) |
| Focus session timestamps | Yes | Local device | Potentially personal data (behavioural pattern) |
| App usage duration | Yes | Local device | Potentially personal data (behavioural pattern) |
| User preferences (thresholds) | Yes | Local device | Not personal data |
| Account credentials | No (Phase 1) | N/A | No GDPR issue in Phase 1 |

**Phase 1 GDPR assessment: LOW RISK.** All data is stored locally on the user's device. No data is transmitted to servers. No accounts are created. Under GDPR, local-only processing by an app that does not transmit data to a controller or processor has minimal GDPR surface. The user is effectively the controller of their own data.

**Phase 2 GDPR implications (cloud sync via Google/Apple Sign-In):**
- The moment data leaves the device, GDPR applies fully.
- Anonymous cloud sync (D-016) reduces but does not eliminate GDPR obligations. Google/Apple Sign-In provides an identifier; usage data linked to that identifier is personal data.
- A Data Protection Impact Assessment (DPIA) should be completed before Phase 2 development begins.
- Privacy policy and data processing documentation must be in place before Phase 2 launch.

### 10.2 EU AI Act Assessment

**Classification question: Is FocusPal an AI system under the EU AI Act?**

The EU AI Act defines an AI system as "a machine-based system designed to operate with varying levels of autonomy... that may exhibit adaptiveness... and that infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions" (Article 3(1)).

FocusPal's mood state machine is a **rule-based system**, not an AI system. It does not infer emotions from biometric data. It does not learn or adapt. It applies deterministic rules: IF (phone used > threshold) THEN (mood = Annoyed). This is closer to a thermostat than to an AI.

**Assessment: FocusPal Phase 1 is NOT an AI system under the EU AI Act and the prohibited practices in Article 5 do not apply.**

However, two caveats:

1. **If Phase 3 introduces adaptive/learning thresholds** (e.g., the system learns the user's patterns and adjusts sensitivity automatically), this crosses into AI territory and may require transparency obligations under the EU AI Act.

2. **Manipulation concern:** Article 5(1)(a) prohibits AI systems that use "subliminal techniques beyond a person's consciousness" or "purposefully manipulative or deceptive techniques" to "materially distort the behavior of a person." FocusPal's Chibi mood system is designed to influence behaviour, but it does so transparently (the user sees the mood, understands why it changed, and can adjust thresholds). Transparency is the key differentiator. As long as the cause-and-effect relationship is clear and user-controllable, this is persuasion (permitted) not manipulation (prohibited).

### 10.3 Children's Privacy

**This is the highest-risk regulatory area for FocusPal.**

If users under 16 (GDPR) or under 13 (COPPA, US) use FocusPal:

| Requirement | Source | FocusPal Impact |
|-------------|--------|-----------------|
| Parental consent for data processing | GDPR Art. 8 | Applies to Phase 2+ (cloud sync). Not Phase 1 (local only). |
| Age verification | EU DSA guidelines (2025) | Required if the app processes children's data. Phase 1 local-only may be exempt. |
| High privacy by default | ICO Children's Code | FocusPal's zero-permission, local-only design already meets this standard. |
| No nudge techniques for data/purchases | ICO Children's Code Standard 12 | Premium Chibi purchases must not use emotional manipulation targeting children. |
| Best interests assessment | ICO Children's Code Standard 1 | If the app is "likely to be accessed by children," a best interests assessment is required regardless of the intended audience. |

**Critical decision needed:** Is FocusPal intended for users under 16? The Tamagotchi aesthetic, cute creatures, and emoji-only communication all suggest a younger audience. If the answer is "yes" or "probably," the team must comply with the ICO Children's Code and equivalent regulations from launch — not retrospectively.

**Recommendation:** Define the target age as 16+ in the app store listing and terms of use. This does not prevent younger users from using the app (especially Phase 1 with no account creation), but it establishes the intended audience and reduces regulatory exposure. If the team wants to explicitly target under-16s, a full Children's Code compliance review is needed before launch.

**Implication for Design:** Phase 1's local-only, zero-permission architecture is privacy-by-design in the strongest sense. This is a competitive advantage and a regulatory advantage. Do not compromise it. Phase 2 cloud sync must be planned with a DPIA. Premium purchases must not use emotional manipulation (no "Your Chibi is sad because you haven't bought them a hat"). The team must make an explicit age-range decision and document it.

---

## 11. Ethical and Regulatory Flags

### 11.1 Emotional Manipulation Risk

FocusPal deliberately creates emotional attachment to influence behaviour. This is the product's strength and its ethical vulnerability.

**The line between persuasion and manipulation:**
- **Persuasion (acceptable):** Transparent mechanism, user understands cause-and-effect, user controls sensitivity, user can disengage at any time.
- **Manipulation (unacceptable):** Hidden mechanism, user doesn't understand why they feel guilty, no user control, designed to create dependency.

FocusPal's current design is on the persuasion side. The cause-and-effect is visible (emoji speech bubbles), the user controls thresholds, and there is no lock-in mechanism. But the team should actively monitor for drift toward manipulation, especially as features accumulate in Phases 2 and 3.

**Specific risks to watch:**
- **Dreaming feature (Idea Bank):** If interrupting a dream "pops the bubble" and the user feels guilty, this is a guilt-based punishment mechanic. Design it so the dream pauses (can be resumed) rather than is destroyed.
- **Skill learning interruption:** If interrupting a Chibi learning an instrument resets the progress bar, this is loss aversion, not positive reinforcement. Design it so progress pauses, not resets.
- **Premium Chibi emotional framing:** "Your Chibi wants a friend" (showing a premium creature alongside the free one) is emotional manipulation for monetisation. Do not do this.

### 11.2 Dependency and Wellbeing

**Paradox:** FocusPal aims to reduce phone dependency by creating dependency on a phone app. If the emotional bond is too strong, users may check FocusPal compulsively to see how their Chibi is doing — increasing screen time rather than reducing it.

**Mitigation:**
- The Chibi should be most rewarding when NOT checked frequently. Ecstatic state after 60 minutes of non-use is the key mechanic — it rewards absence.
- Limit notification frequency. FocusPal should not become another source of phone pickups.
- The Sleepy state (nighttime) gives the user explicit permission to disengage.

### 11.3 Data Ethics

- **Phase 1:** No data leaves the device. Ethical risk is minimal.
- **Phase 2+:** Cloud sync creates data. Even anonymised usage data can be de-anonymised with sufficient auxiliary data. The team should commit to never selling or sharing usage data with third parties, and document this commitment in a privacy policy.

### 11.4 Accessibility

- Emoji-only communication excludes screen reader users. Phase 2+ should add accessibility labels to all emoji and visual states.
- Colour-based environmental feedback (bright vs. dim) may not be perceivable by colour-blind users. Use brightness/contrast, not colour alone.

**Implication for Design:** The ethical line is clear: FocusPal should make users feel good about putting their phone down, not bad about picking it up. Every feature should be tested against this principle. When in doubt, reward the positive behaviour rather than punish the negative one.

---

## 12. Recommended Focus Areas for SAGE

Based on this research, SAGE should prioritise the following areas in the design specification. Ranked by evidence strength and impact on the core value proposition:

### Priority 1: Onboarding Emotional Bond (CRITICAL)

**Evidence strength:** Demonstrates (SDT relatedness need, Finch validation, Hook Model investment phase).

The hatching/naming sequence is the single most important UX in the entire app. If the user does not form an emotional bond during onboarding, no subsequent feature matters. The incubation ritual (hold-to-warm) must feel magical, not functional. The naming prompt must feel significant, not bureaucratic. The Chibi's first reaction to its name must be emotionally rewarding.

Research-backed design requirements:
- The Chibi must respond visibly and immediately to the user's first interaction (hatching touch)
- Naming must feel like a commitment (a "ceremony" not a "text field")
- The first 5 minutes must establish the cause-and-effect relationship: "When I leave, it's happy. When I interrupt, it notices."

### Priority 2: Mood State Communication (CRITICAL)

**Evidence strength:** Indicates (ambient information research, Fogg Behavior Model prompts).

The Chibi's mood must be instantly legible without text. Emoji speech bubbles are the right choice, but the specific emoji vocabulary needs careful design. Each of the 6 states should have:
- A distinct Chibi animation/pose (primary channel)
- A distinct emoji speech bubble (secondary channel)
- A distinct environmental tone (tertiary channel, per Section 8)

The user should never need to guess what state the Chibi is in or why.

### Priority 3: Configurable Sensitivity UX (HIGH)

**Evidence strength:** Demonstrates (SDT autonomy need, guilt-avoidance research).

The defaults must be good (see Section 6 thresholds). The adjustment UX must feel like empowerment, not like cheating. Frame it as "How sensitive is your Chibi?" not "How strict do you want the app to be?"

### Priority 4: Active Session (Adventure) Experience (HIGH)

**Evidence strength:** Indicates (Fogg Ability principle, Hook Model variable reward).

Active sessions are the highest-accuracy detection mode and should be the primary behaviour change lever. The adventure experience (Chibi goes on a journey while user focuses) creates variable rewards (what will the Chibi discover?) and investment (accumulated adventure memories). SAGE should design adventures that are visually rewarding to review after a focus session.

### Priority 5: Environmental Feedback Design (MEDIUM)

**Evidence strength:** Indicates (ambient information research). See Section 8 for detailed recommendation.

Design 2-3 environmental states (bright, normal, dim). Keep negative states mild. Make the positive state genuinely pleasant to look at.

---

## Appendix: Source Index

| Source | Type | Used In |
|--------|------|---------|
| ConsaInsights, Screen Time Monitoring Apps Market (2024) | Market report | Section 2 |
| DemandSage, Average Screen Time Statistics (2026) | Statistical compilation | Sections 2, 4 |
| Fortune Business Insights, Mobile Application Market (2025) | Market report | Section 2 |
| SimilarWeb, Forest App Statistics (2025) | App analytics | Section 3 |
| Janice Lee, "How Forest app ranked #1" (Medium, 2020) | Case study | Section 3 |
| Product Hunt, Opal Reviews (2026) | User reviews | Section 3 |
| riedel.wtf, "State of the Screen Time API" (2024) | Technical analysis | Section 7 |
| Autonomous.ai, Finch Self-Care App Review (2025) | Product review | Sections 3, 5 |
| Yoga Journal, Finch Review (2025) | Product review | Section 3 |
| Internet Matters, Finch Review (2025) | Product review | Section 3 |
| Ryan & Deci, Self-Determination Theory (2000) | Peer-reviewed (seminal) | Section 5 |
| Oxford Academic / IwC, SDT in Behaviour Change Technologies (2024) | Peer-reviewed | Section 5 |
| Taylor & Francis, Parental Screen Guilt (2024) | Peer-reviewed | Section 5 |
| BJ Fogg, Behavior Model / Tiny Habits (Stanford) | Academic framework | Section 5 |
| Nir Eyal, Hooked: Habit-Forming Products (2014) | Commercial framework | Section 5 |
| Mark et al., Attention Span in Digital Context (2016) | Peer-reviewed | Section 6 |
| Kaplan, Attention Restoration Theory (1995) | Peer-reviewed | Section 6 |
| Market Report Analytics, Virtual Pet Games Market (2025) | Market report | Section 9 |
| Electronic Specifier / The Toy Book, Tamagotchi Resurgence (2024-2025) | Industry press | Section 9 |
| EU AI Act, Articles 3 and 5 (2024) | Legislation | Section 10 |
| GDPR, Article 8 (2018) | Legislation | Section 10 |
| ICO, Age Appropriate Design Code (2021, updated 2025) | Regulatory guidance | Section 10 |
| Stanford Behavior Design Lab, Ambient Displays (2024) | Academic research | Section 8 |
| Froehlich et al., Eco-Feedback Design (ScienceDirect, 2010) | Peer-reviewed | Section 8 |

---

*Research brief prepared by IRIS. All findings carry stated confidence levels. Claims without cited sources are explicitly labelled as inference or hypothesis. This document is a diagnostic instrument — it diagnoses the opportunity and the risks. It does not prescribe solutions. Solutions are SAGE's domain.*

---

## Addendum: User Directives Post-IRIS Review (2026-03-19)

The following directives were provided by the product owner after reviewing IRIS's research brief. These supplement and in some cases override IRIS's recommendations. SAGE must incorporate all of these into the design specification. Decisions are logged as D-021 through D-029.

### A1. Age Rating & Teen Appeal (D-021)

**Decision:** App store listing targets 16+, but the product must appeal to teens. The Pokemon collection mentality is the model — loved by young and old. Rare, evolved, well-dressed Chibis with special environments should carry bragging rights and pride of ownership.

**Impact on IRIS Section 10:** Children's privacy is managed via 16+ listing, but SAGE should design the collection/evolution/customisation UX to resonate with teen aesthetics without triggering under-13 regulatory obligations.

### A2. Usage Detection: Accuracy is Critical (D-022 — Revisits D-015)

**User directive:** "2 hours on TikTok absolutely should have bearing on the Chibi mood, or the product value and credibility goes down." The system cannot be gamed or worked around. Achievements, behaviour changes, and bonding feel hollow if not tangible.

**Impact on IRIS Section 7:** IRIS recommended app-level-only as sufficient. The user challenges this — accuracy matters more than broad encouragement. SAGE and FORGE must investigate offering **optional UsageStats API permission** as an opt-in upgrade that provides real device-wide screen time data, while maintaining app-level-only as the privacy-by-design default. Two-tier detection:
- **Tier 1 (default):** App-level only, privacy-by-design, zero permissions — as IRIS recommended
- **Tier 2 (opt-in):** UsageStats API permission grants real screen-time data, more accurate Chibi mood responses

This preserves privacy-by-design as the default while addressing the accuracy concern for users who want the full experience.

### A3. Environment Degradation Thresholds (D-023)

**User directive:** Environment only degrades after **prolonged** time in annoyed or sad states (the two worst tiers). A brief annoyance should not dirty the kitchen. A 9-hour screen-time binge should be visible.

Mechanics:
- Environment degrades only after significant sustained time in annoyed AND/OR sad states
- Chibi immediately starts cleaning when phone is put down
- ~1 hour uninterrupted → environment progressively fixed (not restart — picks up where it left off)
- Environment can worsen again if unhealthy habit continues
- Fixing is progressive, not binary

**Impact on IRIS Section 8:** Refines the "2-3 states" recommendation. The degradation threshold prevents the guilt-based failure mode IRIS identified.

### A4. Adventure Mode: Detailed Mechanics (D-024)

**User directive:** Adventures are timer-based treasure hunts with cosmetic rewards.

- User sets timer (countdown to finding treasure chest)
- Rewards depend on adventure length (cosmetics: hats, glasses, umbrellas for the Chibi)
- **Checking the adventure/clock does NOT disturb it** — user can peek
- Unlocking phone for another activity triggers: "Are you sure you want to pause the adventure here?"
- Adventures stopped early are **never punished** — reward is delayed, not lost
- User can complete the adventure another time
- Philosophy: never guilt, only self-induced delay of reward

**Impact on IRIS Section 5 (Hook Model):** Adventure rewards serve as variable rewards (what will the treasure be?). The "peek without disturbing" mechanic respects autonomy (SDT). The non-punishing pause aligns with the guilt-avoidance research.

### A5. Focus Mode Presets (D-025)

**User directive:** Ask age range during onboarding. Offer focus mode presets:
- **Relaxed** — gentler thresholds
- **Focus-Friendly** — balanced defaults
- **Super-Focused** — stricter thresholds

Base ranges on research per age group. Give user easy one-click option to switch between presets.

**Impact on IRIS Section 6:** Extends the configurable sensitivity system. Instead of raw threshold numbers, present as named presets with age-appropriate defaults. User can still fine-tune, but presets give a simpler entry point.

### A6. Sleepy Mode: Freeze + Morning Inheritance (D-026)

**User directive:** Moods and environment do NOT change during Sleepy mode. Night interruptions only affect the next day's starting mood:
- Many interruptions during night → day starts at a worse mood tier (bad night's sleep)
- No interruptions → day starts at best mood tier
- Only affects starting position — recovery rate is the same as normal

**Impact on IRIS Section 6 (Sleepy trigger):** The Sleepy state becomes a freeze/accumulation state, not an active mood. Night behaviour is banked and applied as a morning starting position.

### A7. Chibi-Human Interaction: Loving but Brief (D-027)

**User directive:** Chibis love interacting with their human — instant happy feedback (purring, hearts). But they tire quickly:
- 30 seconds to 1 minute of active play before Chibi gets tired
- Gentle visual cues: yawning, waving off
- Continuing to interrupt after cues → starts affecting mood
- More time allowed for customisation (environment, dressing)
- But Chibi will eventually nudge toward focus activities even during customisation
- Balance: meaningful engagement + emotional bonding + reducing screen time

**Impact on IRIS Section 5 (SDT):** The brief interaction satisfies the relatedness need without undermining the product's core purpose. The "tired Chibi" mechanic is positive framing (the Chibi needs rest) not negative (you're using too much screen time).

### A8. Intentional Downtime Only (D-028)

**User directive:** Phone must be on and used (e.g., screen unlocked once) for focus progress to continue. Prevents:
- Lost/stolen phone accumulating fake progress
- Forgotten Chibi earning undeserved rewards
- Gaming the system by simply not using the phone for days

**Status:** Further research/recommendations needed on implementation mechanics. SAGE should design the UX; FORGE needs to investigate technical feasibility (heartbeat check intervals, battery impact).

### A9. Multiple Chibis with Shelving (D-029)

**User directive:** Players can hatch new Chibis for more choice and collection. Mechanics:
- Only one Chibi active at a time
- Active Chibi is shelved when starting a new one (journey progress paused, not lost)
- Shelving must NOT feel punishing
- Reactivating a shelved Chibi = joyful reunion (Chibi is happy to see you again)
- Never a guilt trip for shelving
- Enables collection aspect (ties into D-021 teen appeal and bragging rights)

**Impact:** Adds to Phase 2/3 scope. Phase 1 prototype may stub this (single Chibi only) but the architecture should be designed to support it.

---

### A10. Tier 2 Permission Timing — After Hatching Ceremony (D-030)

**User directive:** The Tier 2 permission request must happen AFTER the hatching and naming ceremony, not during onboarding. The emotional bond must be established first. The Chibi itself delivers the gentle nudge as part of the UX flow.

Requirements:
- Easy to understand: what is being asked, how to complete it (one-tap to setting), and why
- Confirm data stays local — "not collected, only used to run app accurately"
- Don't need to know which specific apps the user is using — only that the screen is actively engaged
- Exception consideration: school/educational screen time for teens (they may not have control over necessary screen time)
- Minimum GDPR exposure — only enough to make the app work effectively

### A11. Tier 1 = Mood Only; Rewards/Progression Locked Until Tier 2 (D-031)

**User directive:** The app works on Tier 1 (mood mechanics function), but evolution, skill learning, and progress tracking require Tier 2. This creates a clear, non-punishing incentive to enable Tier 2.

Requirements:
- Clear messaging explains WHY: "Can't determine screen time without the setting"
- Players always aware of what blocks progression
- One-tap path to the Tier 2 setting always available (not buried in menus)
- Not punishing — informative. The Chibi can't evolve or learn new skills without accurate data.
- Framing: the feature is locked because the app literally cannot provide it without the data, not as a paywall or restriction

**Impact on IRIS S2 (D-022):** This is a significant UX decision that addresses IRIS's concern about opt-in rates. By locking progression behind Tier 2, users have a strong, clear incentive to enable it. This is not a dark pattern — it is honest: the app genuinely cannot track progress without the data.

### A12. Heartbeat: 48hr Inactivity Pause, No Notifications (D-032)

**User directive:** Replaces the heartbeat check concept from D-028. If the phone shows zero unlocks or app usage for 48 hours (unusual for a modern phone user), simply pause Chibi evolution and skill progress until active usage returns, then resume.

Requirements:
- No "proof of life" notifications
- No periodic prompts
- Simple inactivity detection only
- 48 hours is the threshold (covers weekends, holidays, phone repairs)

**Impact on IRIS S8 (D-028):** This is simpler and more elegant than IRIS's recommended approaches. No UX contradiction (no prompts that create phone pickups). The 48hr threshold handles the lost/forgotten phone edge case without disrupting normal use.

### A13. Single-Device Binding via Platform Account (D-033)

**User directive:** The Chibi account should be connected to only one active signed-in device (Google Account or Apple ID). This prevents gaming via multiple phones. Feasibility to be validated by FORGE.

**Impact:** Addresses the multi-device gaming concern raised in D-028's original context. Combined with the 48hr pause (D-032), this provides two anti-gaming mechanisms without any UX friction for honest users.

---

*Addendum added by orchestrator after user review of IRIS research brief. These directives carry equal or higher weight than IRIS's original recommendations where they conflict. All decisions logged in EVIDENCE_TRACKER.md as D-021 through D-033.*
