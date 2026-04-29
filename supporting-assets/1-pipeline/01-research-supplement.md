# IRIS Research Supplement -- User Directives D-021 to D-029

**Date:** 2026-03-19
**Agent:** IRIS (Insight & Research Intelligence Specialist)
**Trigger:** Product owner reviewed original research brief and provided 9 new directives
**Status:** READY FOR ATLAS QA

---

> **Lead Finding:** The product owner's challenge on D-022 (usage detection accuracy) has merit. The original brief's app-level-only recommendation, while sound on privacy grounds, underestimated the credibility cost of inaccurate detection. A two-tier model -- app-level default with optional UsageStats/Screen Time API opt-in -- is both technically feasible and GDPR-compliant, and is now the recommended approach. This is the single most consequential revision in this supplement.

---

## S1. Teen Appeal & Collection Mechanics (D-021)

### 1.1 The Directive

Target 16+ in app store listings but design with teen appeal. Leverage Pokemon-style collection mechanics -- "bragging rights," social sharing, completionist drive.

### 1.2 Research Findings

**Finding 1: Collection mechanics are the stickiest engagement pattern for the 13-19 demographic.**

Pokemon has sustained multi-generational engagement for 30 years primarily through collection mechanics. The franchise's latest hardware product -- the "Poke-nade" virtual pet device (Takara Tomy, launching October 2025) -- features 157 collectible Pokemon with 7 designated "Partner Pokemon" offering unique voice acting and animations (Ubergizmo, 2025; Hypebeast, 2025). The device is explicitly designed around emotional bonding through touch-based interaction, where players "pet" their Pokemon and creatures respond according to duration and intensity. This is mechanically identical to FocusPal's proposed Chibi interaction model.

**Confidence level:** Demonstrates. The Pokemon franchise's commercial success ($100B+ lifetime revenue) provides overwhelming evidence that collection mechanics sustain teen engagement across decades and platforms.

**Finding 2: Neopets validates multi-creature ownership without fatal attachment dilution.**

Neopets allows up to 4 pets per account (20-21 across side accounts with Premium). Community evidence from the Neopets forums and fan communities demonstrates that players form strong emotional bonds with multiple creatures simultaneously -- one player's comment captures the pattern: "sometimes I hate myself for loving them so much!" (Neopets Times, Issue 748). The key design insight is that each creature in a collection needs a distinct personality or role to maintain individual attachment. Generic duplicates dilute bonding; distinct characters enhance it.

**Confidence level:** Suggests. Community sentiment data, not controlled research. Self-selection bias (active forum users are the most engaged). However, the 20+ year longevity of the platform with this mechanic is itself evidence.

**Finding 3: Social sharing of collections enhances engagement but carries wellbeing risks.**

Research on gamification in wellness apps identifies social recognition as a motivator that can "crowd-in" intrinsic motivations (PMC, Motivation Crowding Effects, 2024). However, this is context-dependent. In competitive contexts, social comparison can undermine wellbeing goals -- users focus on collection size rather than behaviour change. In cooperative or display-only contexts (showing off, not competing), the risk is lower.

**Confidence level:** Indicates. Multiple studies converge on the crowd-in effect, but none specifically test collection-sharing in a screen-time context.

**Finding 4: App store age ratings -- the 16+ listing is achievable and defensible.**

Apple's updated age rating system (2025) offers 4+, 9+, 13+, 16+, and 18+ tiers (Apple Developer News, 2025). Google Play uses IARC ratings. A 16+ rating is appropriate if FocusPal includes: user-generated content (Chibi names), optional social features (collection sharing), or in-app purchases. The 16+ listing establishes the intended audience for regulatory purposes without preventing teen use -- enforcement of app store age ratings is inconsistent across both Apple and Google platforms (Canadian Centre for Child Protection, 2025; 5Rights Foundation, 2025).

**Confidence level:** Demonstrates. This is regulatory fact, not inference.

**Counter-evidence:** Four US states (Texas, Utah, Louisiana, California) have passed app store age verification laws that may require more than a simple rating declaration (Privacy World, 2025). FocusPal should monitor this space but the current EU/UK regulatory environment does not require active age verification for a 16+ rated app without regulated content.

### 1.3 What the Data Does NOT Show

- Whether "bragging rights" mechanics in a wellness app specifically (vs. a game) enhance or undermine the behaviour change goal. The concern is real: if users optimise for collection completeness, they may game the system rather than genuinely reducing screen time.
- Optimal collection size for sustained engagement without overwhelm. Pokemon's 157 is far too many for Phase 1. The right number for FocusPal's scope is unknown.
- Whether the Tamagotchi/Chibi aesthetic appeals equally to male and female teens. The Pokemon data suggests broad gender appeal; the Tamagotchi data skews female historically.

**Implication for Design:** Collection mechanics are validated as a teen engagement driver. SAGE should design the collection system to reward genuine behaviour change (Chibis earned through focus milestones, not purchased or easily gamed). Social sharing should be display-only (no leaderboards, no competitive ranking) to avoid undermining wellbeing goals. Phase 1 should support the architecture for multiple Chibis (see S9) but limit the active collection to a manageable size.

---

## S2. Usage Detection Accuracy -- D-015 Reassessment (D-022)

### 2.1 The Directive

The product owner explicitly challenged the original brief's app-level-only recommendation: "2 hours on TikTok absolutely should have bearing on the Chibi mood, or the product value and credibility goes down."

### 2.2 Reassessment: The User's Challenge Has Merit

The original brief (Section 7) recommended app-level-only detection as the Phase 1 approach, with optional permission-based detection deferred to Phase 2. The reasoning was sound: privacy-by-design, zero permissions, GDPR-minimal surface.

However, the product owner identifies a genuine credibility gap. If a user spends 2 hours on TikTok and the Chibi is oblivious, the core value proposition -- "your Chibi reflects your real digital wellbeing" -- is hollow. The Chibi becomes a toy, not a behaviour change tool. This is not a minor UX issue. It is a threat to the product's reason for existing.

**Self-correction:** The original brief correctly identified this limitation ("Cannot detect which other apps the user is using... This creates potential for false positives and false negatives") but underweighted its impact on product credibility. The privacy advantage is real, but an inaccurate Chibi is worse than a private one because an inaccurate Chibi is one users stop trusting.

**Confidence level:** Indicates. No direct research tests this specific trade-off (privacy vs. accuracy in virtual-pet-based behaviour change). However, research on self-reported vs. objective screen time measurement demonstrates that self-reported screen time correlates only moderately with logged measurements (Júdice et al., *Journal of Prevention*, 2023). If FocusPal relies solely on app-level inference, it is effectively using "self-report-equivalent" accuracy for the Chibi's mood -- the very measurement approach the literature identifies as unreliable.

### 2.3 Android: UsageStatsManager API -- Technical Analysis

**What it is:** `android.app.usage.UsageStatsManager` is Android's official API for accessing device-wide app usage statistics, available since Android 5.0 (API 21).

**What data it provides:**
- Per-app foreground time (how long each app was in the foreground)
- Last time each app was used
- App launch counts
- Usage events (app moved to foreground/background, with timestamps)
- Configuration changes
- Data can be queried by time interval: daily, weekly, monthly, yearly

**Permission required:** `android.permission.PACKAGE_USAGE_STATS` -- this is a **system-level permission**. It cannot be granted through a standard runtime dialog. The user must be directed to Settings > Apps > Special access > Usage access and manually toggle it on for FocusPal. This is a deliberate friction point by Google to ensure informed consent.

**Technical limitations:**
- Data is not real-time -- there is an update delay (typically seconds to minutes)
- On Android R+, returns null if the device is locked (cannot query usage while screen is off)
- On Android Q+, usage data access is further restricted; apps must declare the permission in the manifest AND the user must grant it in Settings
- The API provides aggregate statistics, not live foreground app detection -- polling is required to approximate real-time awareness

**GDPR assessment for opt-in UsageStats collection:**
- The data constitutes **personal data** under GDPR (behavioural patterns linked to a device/user)
- However, if processed **locally only** (never transmitted to servers), the GDPR surface remains minimal -- consistent with Phase 1's local-only architecture
- Opt-in consent satisfies GDPR Article 6(1)(a) (consent) and Article 7 (conditions for consent)
- The system-level permission grant provides a robust consent mechanism -- the user must take deliberate action in Settings, which exceeds the "freely given, specific, informed and unambiguous" standard
- **Key constraint:** If this data is ever synced to a cloud backend (Phase 2+), a full DPIA is required

**Confidence level:** Demonstrates. This is API documentation fact, verified against Android Developer Reference (developer.android.com).

### 2.4 iOS: Screen Time API -- Technical Analysis

**What it is:** Apple's Screen Time technology consists of three frameworks introduced at WWDC 2021:
1. **FamilyControls** -- authorisation and user/device management
2. **ManagedSettings** -- applying restrictions (shielding apps, web content filtering)
3. **DeviceActivity** -- monitoring usage and scheduling events

**What third-party apps CAN do:**
- Monitor when usage thresholds are reached (via `DeviceActivityMonitor`)
- Shield apps with overlays when limits are exceeded
- Track categories of app usage (social media, games, etc.)
- Schedule time-based restrictions

**What third-party apps CANNOT do (the critical limitation):**
- **See which specific apps the user is using.** Apple uses opaque tokens -- apps receive anonymised identifiers, not app names or bundle IDs. This is a deliberate privacy-preserving design (Apple Developer Documentation, 2025).
- Open the parent app from a shield
- Lock permissions with a passcode (unlike native Screen Time)
- Know which restriction type triggered a shield

**Known bugs and limitations (riedel.wtf, 2024):**
- Random token changes cause developers to lose context about restrictions
- Token migration problems between managed settings stores
- `FamilyActivityPicker` crashes when searching for apps
- Shield UI fails to update correctly when apps are moved between block groups
- Users can revoke Screen Time API access for any third-party app with a single toggle in Settings -- no passcode protection

**Requires Apple entitlement:** Developers must apply for the `com.apple.developer.family-controls` entitlement through Apple's developer portal before using these APIs.

**Net assessment for FocusPal on iOS:** The Screen Time API is significantly more limited than Android's UsageStatsManager. FocusPal cannot see which apps the user is using -- only whether usage thresholds for categories have been reached. The API is also buggy and Apple-controlled (entitlement approval is not guaranteed). iOS will therefore offer a less accurate detection experience than Android, which should be communicated honestly to users.

**Confidence level:** Demonstrates. Based on Apple Developer Documentation, riedel.wtf technical analysis (2024), and developer community reports.

### 2.5 The Two-Tier Detection Model

**Proposed architecture:**

| Tier | Detection Method | Permission | Accuracy | Default? |
|------|-----------------|------------|----------|----------|
| **Tier 1 (Default)** | App-level only. FocusPal monitors its own lifecycle (foreground/background), active sessions, time-of-day. | None | Low-Medium | Yes -- privacy-by-design |
| **Tier 2 (Opt-in)** | UsageStats API (Android) / Screen Time API (iOS). Device-wide usage data feeds Chibi mood. | System-level (Android) / Entitlement + user grant (iOS) | Medium-High (Android), Medium (iOS) | No -- user must explicitly opt in |

**Precedent for this pattern:**

This two-tier approach is consistent with GDPR's privacy-by-design and data minimisation principles (Article 25). The pattern of "works without permissions, works better with permissions" is used by:
- **ScreenZen** -- functions as a friction-based tool without permissions, offers enhanced tracking with usage access
- **one sec** -- core breathing intervention works without Screen Time API, but uses it for app-specific blocking when granted
- **Digital Wellbeing (Google)** -- built into Android, uses UsageStats natively but offers varying detail levels

The ICO's guidance for wellbeing app developers (2025) explicitly endorses opt-in mechanisms with clear purpose disclosure. The key requirement is that the app must function meaningfully at Tier 1 -- the permission must enhance, not gate, the core experience.

**Confidence level:** Indicates. The two-tier pattern exists in the market and aligns with regulatory guidance, but no app has implemented it specifically for a virtual-pet-based behaviour change product.

### 2.6 Does Accurate Detection Produce Better Behaviour Change?

**Finding:** The evidence is indirect but directionally strong.

Research on self-reported vs. objectively measured screen time demonstrates that people systematically underestimate their phone usage (Júdice, Sousa-Sá & Palmeira, *Journal of Prevention*, 2023, "Discrepancies between self-reported and objectively measured smartphone screen time: before and during lockdown"). If users underestimate their usage and the Chibi's mood is based on inaccurate data, the feedback loop is weakened -- the Chibi may be content while the user is actually overusing.

A 2025 field experiment by the Danish Competition and Consumer Authority found that friction-based interventions (forced pauses, time planning prompts) reduced social media usage by approximately 33% over three weeks (Cyberpsychology, Behavior, and Social Networking). Critically, these interventions required accurate detection of which app was being opened to deliver the friction at the right moment. Accurate detection enables accurate intervention.

Research on the Hawthorne effect in screen-time measurement shows that when users know their usage is being accurately tracked, this awareness itself changes behaviour (ScienceDirect, Criterion Validity, 2022). A Chibi that accurately reflects real usage creates a persistent Hawthorne effect -- the user knows the Chibi "knows," which sustains the behaviour change pressure.

**Counter-evidence:** The Journal of the Association for Consumer Research (2021) found that tracking alone (without intervention) improves awareness but does not reliably reduce usage. Accurate detection is necessary but not sufficient -- it must be paired with the emotional feedback loop (Chibi mood) to drive change.

**Confidence level:** Indicates. No study directly tests "accurate detection + virtual pet feedback vs. inaccurate detection + virtual pet feedback." The argument is constructed from adjacent evidence.

### 2.7 Gaming the System

**Finding:** Users do game screen-time apps, and this is a significant concern.

Common circumvention methods documented across iOS and Android (Cloudwards, 2025; PMC, Evaluating Effectiveness of Apps Designed to Reduce Mobile Phone Use, 2023):
- Using a second device while the primary is "resting"
- Clearing app data or reinstalling apps to reset timers
- Exploiting Do Not Disturb or airplane mode to freeze tracking
- On iOS: revoking Screen Time API access with a single toggle (riedel.wtf, 2024)
- On rooted/jailbroken devices: modifying system-level usage data

**Impact on FocusPal:** If FocusPal relies solely on app-level detection (Tier 1), gaming is trivially easy -- the user simply doesn't open FocusPal while using their phone. The Chibi stays happy because it has no signal. This does not just reduce effectiveness; it makes the product feel dishonest to the user who knows they're gaming it.

With Tier 2 (UsageStats), gaming becomes harder -- the API reports device-wide usage regardless of whether FocusPal is open. The user would need to use a second device, which is a higher friction barrier.

**Confidence level:** Indicates. Circumvention is well-documented across screen-time apps generally. The specific impact on virtual-pet-based apps is inferred.

### 2.8 Revised Recommendation

The original Section 7 conclusion is revised as follows:

| Original Recommendation | Revised Recommendation |
|------------------------|----------------------|
| App-level-only detection is validated as a reasonable Phase 1 approach. Phase 2 should evaluate optional permission-based detection. | **Two-tier detection should be implemented in Phase 1.** Tier 1 (app-level) as the default, Tier 2 (UsageStats/Screen Time API) as an opt-in upgrade presented during onboarding or settings. The architecture must support both tiers from launch. |

**Rationale for the revision:**
1. The product owner's credibility concern is valid and data-supported
2. The technical implementation is feasible on both platforms (with iOS limitations acknowledged)
3. The GDPR risk is manageable with local-only processing and opt-in consent
4. The two-tier pattern has market precedent
5. Deferring to Phase 2 risks building the entire UX around inaccurate data, requiring a costly retrofit

### 2.9 What the Data Does NOT Show

- Whether the Tier 2 opt-in rate will be high enough to matter. If 95% of users stay on Tier 1 (the Spool heuristic: fewer than 5% change defaults), the accuracy improvement is marginal at the population level. The opt-in must be compelling -- framed as "Help your Chibi understand you better" not "Grant usage access permission."
- iOS vs. Android parity is not achievable. Android's UsageStatsManager provides significantly richer data than Apple's privacy-preserving Screen Time API. FocusPal will be a better product on Android for detection accuracy. This platform asymmetry must be acknowledged in the design.
- Long-term battery and performance impact of periodic UsageStats polling. The API is read-only and lightweight, but polling frequency must be calibrated to balance accuracy with battery drain.

**Implication for Design:** SAGE should design the onboarding flow to present Tier 2 as a benefit ("Your Chibi pays attention to your whole phone, not just this app") with a clear, one-tap path to the system settings page. The UX must gracefully handle both tiers -- Chibi mood logic must work at Tier 1 (approximate) and improve at Tier 2 (accurate). FORGE must architect the mood engine to accept either data source from Day 1.

---

## S3. Environment Degradation Thresholds (D-023)

### 3.1 The Directive

Environment degradation should only occur after prolonged annoyed/sad Chibi states, not immediately. The environment should be a lagging indicator, not a real-time mirror.

### 3.2 Research Findings

**Finding 1: Threshold-based feedback outperforms immediate feedback for sustained behaviour change.**

Gamification research demonstrates that combining continuous progress indicators (gradual accumulation) with threshold-based state changes (level-ups) produces more durable engagement than either approach alone (Sam Liberty, "31 Core Gamification Techniques," Medium, 2025). The environment acting as a lagging indicator is analogous to a "level" system -- the user sees gradual mood changes in the Chibi (continuous feedback) and environment shifts only at sustained thresholds (milestone feedback). This dual-channel approach aligns with the ambient information display research cited in the original brief (Section 8).

**Confidence level:** Indicates. Gamification research supports the principle; the specific application to virtual-pet environments is inferred.

**Finding 2: Progressive degradation is less likely to trigger avoidance than immediate negative feedback.**

The original brief's Section 5 established that guilt-based approaches fail for sustained behaviour change (Self-Determination Theory, Ryan & Deci, 2000). Immediate environment degradation is a guilt trigger -- the user opens the app and immediately sees damage. A lagging threshold gives the user a window to self-correct before the environment reflects sustained poor behaviour. This is consistent with the two-stage negative feedback model already proposed (Annoyed before Sad, Section 6.2).

**Confidence level:** Indicates. The guilt-avoidance principle is well-established; the threshold-delay application is a logical extension.

**Finding 3: Recommended thresholds for environment degradation.**

No research provides specific minute-thresholds for virtual-pet environment degradation. The following are evidence-informed estimates (confidence: suggests):

| Trigger | Threshold | Rationale |
|---------|-----------|-----------|
| Degradation begins (Normal to Dim) | Chibi in Annoyed state for 30+ cumulative minutes in a 24-hour period | Short annoyance spells are normal phone use. 30 minutes of cumulative annoyance suggests a pattern, not a moment. |
| Full degradation (Dim to Storm/Rain) | Chibi in Sad state for 60+ cumulative minutes in a 24-hour period | Sustained sadness indicates the user has not responded to the Chibi's signals across multiple sessions. |
| Recovery begins (Dim to Normal) | Chibi in Content or higher for 30+ cumulative minutes | Recovery should be noticeably faster than degradation to reward positive change. Asymmetric feedback: easier to fix than to break. |
| Full recovery (Storm to Bright) | Chibi in Happy or Ecstatic for 60+ cumulative minutes | The bright state should feel earned, not automatic. |

### 3.3 What the Data Does NOT Show

- Optimal thresholds will vary by user. A power user who checks their phone 80 times/day will hit cumulative annoyance faster than a light user. Phase 1 should log environment state transitions alongside usage data to calibrate thresholds in Phase 2.
- Whether users notice gradual environment changes or only binary shifts. If the transition from Normal to Dim is too subtle, the feedback channel adds visual cost without behavioural signal.

**Implication for Design:** SAGE should implement the environment as a 24-hour rolling indicator, not a real-time mirror. The Chibi's mood is the fast feedback channel; the environment is the slow one. Degradation thresholds should be cumulative (total time in negative states over 24 hours) rather than instantaneous. Recovery should be faster than degradation -- this is the "rewarding positive behaviour over punishing negative" principle from the original brief (Section 5), applied to the environment layer.

---

## S4. Adventure Mode -- Timer-Based Treasure Hunts (D-024)

### 4.1 The Directive

Focus sessions trigger adventure mode where the Chibi explores and finds cosmetic treasures. Users can peek without disturbing the session. Pausing (non-punishing) vs. cancelling. Variable rewards for cosmetic items.

### 4.2 Research Findings

**Finding 1: Cosmetic rewards enhance engagement without undermining intrinsic motivation -- with a critical caveat.**

Research on gamification in health apps (PMC, Gamification for Health and Wellbeing, 2018; Smartico.ai, 2025) indicates that cosmetic rewards (visual customisation with no functional advantage) maintain engagement without the motivational crowding-out effect seen with performance-based rewards. The mechanism is hedonic motivation -- the reward feels like self-expression, not external control.

The caveat: a 2024 study on gamified loyalty programmes found that "gamified activities are particularly susceptible to satiation, especially when repeated frequently" (ScienceDirect, Non-monotonic Consumer Motivation, 2026). Cosmetic rewards must maintain novelty through variety and rarity, or they habituate into background noise.

**Confidence level:** Indicates. The cosmetic-vs-functional reward distinction is supported across multiple studies. The satiation risk is documented but the threshold for virtual-pet cosmetics is unknown.

**Finding 2: Variable reward schedules are the most effective for sustained engagement.**

B.F. Skinner's variable ratio reinforcement schedule produces the highest-frequency and most persistent behaviours (Skinner, 1957; validated extensively in game design). Unpredictable rewards trigger stronger dopamine responses than predictable ones (Rac.thairobotics.org, Psychology of Random Rewards, 2024; PSU, Slot Machine Psyche, 2025). The optimal pattern for FocusPal adventures:

| Reward Type | Frequency | Purpose |
|-------------|-----------|---------|
| Common cosmetics | Every 1-2 sessions (70-80% drop rate) | Baseline reward -- every session feels productive |
| Uncommon cosmetics | Every 3-5 sessions (15-20% drop rate) | Surprise and delight -- variable reward |
| Rare cosmetics | Every 10-20 sessions (3-5% drop rate) | Aspiration and collection drive |
| Ultra-rare cosmetics | ~1% drop rate | Social sharing fuel, completionist magnet |

**Confidence level:** Indicates. Variable ratio schedules are well-validated in behavioural psychology. The specific percentages are design estimates informed by game industry patterns (Fortnite rarity tiers, gacha game distributions), not empirically tested for a wellbeing app context.

**Finding 3: "Peek without disturbing" -- limited precedent but theoretically sound.**

No screen-time app currently implements a "peek at your creature during a focus session" mechanic. However, the concept aligns with SDT's autonomy principle -- the user can choose to check without being punished, which reduces the feeling of being controlled by the timer. The design risk is that peeking becomes habitual, undermining the focus session's purpose.

**Confidence level:** Suggests. Theoretical alignment with SDT autonomy, no empirical evidence.

**Finding 4: Non-punishing pause outperforms session-cancelled for retention.**

Research on digital self-control apps (PMC, Evaluating Effectiveness, 2023) found that rigid, punitive systems correlate with higher abandonment rates. The apps with moderate to strong evidence of effectiveness (Screen Time iOS, AntiSocial) all allow flexibility. Forest's tree-killing mechanic (session cancellation = dead tree) is effective for some users but alienates others -- it is the most polarising feature in user reviews.

The "pause but don't cancel" approach is safer for FocusPal because the emotional bond with the Chibi makes punishment more personal. Killing a tree is abstract loss. Disappointing your named Chibi is emotional loss. The emotional stakes are already high enough without adding punitive session mechanics.

**Confidence level:** Indicates. The evidence against rigid punishment is strong. The specific "pause vs. cancel" comparison is inferred from adjacent evidence.

### 4.3 What the Data Does NOT Show

- Whether cosmetic rewards in a wellbeing app (vs. a game) produce the same engagement patterns. Users may perceive cosmetic rewards as trivialising a serious goal.
- Optimal adventure duration for maximum reward satisfaction. Is a 25-minute session more rewarding than a 60-minute one, or is the relationship linear?
- Whether peeking during a focus session actually disrupts focus or satisfies curiosity harmlessly. This requires A/B testing in-app.

**Implication for Design:** SAGE should design adventures with variable cosmetic rewards following the rarity distribution above. The peek mechanic should show the Chibi's current adventure state (a snapshot, not interactive) and auto-close after 5-10 seconds to minimise focus disruption. Pausing should be non-punishing (adventure pauses, Chibi waits, resumes where it left off) but noted -- the Chibi might look mildly confused or tap its foot, providing gentle social feedback without punishment.

---

## S5. Focus Mode Presets (D-025)

### 5.1 The Directive

Three named presets: Relaxed, Focus-Friendly, Super-Focused. One-click switching. Age-appropriate defaults.

### 5.2 Research Findings

**Finding 1: Current screen time recommendations by age.**

| Source | Age Group | Recommendation |
|--------|-----------|---------------|
| WHO (2019, reaffirmed 2024) | Under 5 | No screen time under 1; max 1 hour for 2-4 |
| AAP (2024 update) | 6-12 | Max 2 hours/day non-educational |
| AAP (2024 update) | 13-17 | Max 2 hours/day entertainment; educational tracked separately |
| AACAP (2025) | 6-12 | 1 hour on school days, 3 hours on weekends |
| Royal College of Paediatrics (UK) | All ages | No specific time limits; recommends family-negotiated boundaries |

**Confidence level:** Demonstrates. These are published clinical guidelines from recognised health authorities.

**Critical observation:** The UK's Royal College of Paediatrics explicitly rejected fixed time limits in favour of contextual, family-negotiated boundaries. This aligns with SDT's autonomy principle and supports FocusPal's configurable approach over rigid enforcement. Named presets with adjustable parameters are the best synthesis: structure for users who want guidance, flexibility for those who don't.

**Finding 2: Named presets outperform raw numbers for user comprehension and adoption.**

The Jared Spool heuristic (fewer than 5% of users change defaults) indicates that most users will use whatever preset is selected at setup. Named presets with descriptive labels ("Relaxed," "Focus-Friendly," "Super-Focused") leverage anchoring and framing effects -- the user understands the intent without interpreting numerical thresholds. This is a well-established UX pattern used by macOS Focus modes, Android Do Not Disturb presets, and most VPN apps ("Quick Connect" vs. manual server selection).

**Confidence level:** Indicates. The principle is well-established in UX research. No study specifically tests named presets for screen-time sensitivity.

**Finding 3: One-click switching maintains autonomy perception.**

SDT research demonstrates that perceived autonomy is critical for sustained engagement (Ryan & Deci, 2000; Oxford Academic, 2024). One-click preset switching preserves autonomy by making the choice feel effortless and reversible. The user is not locked into a preset -- they can switch at any time. This reduces the "controlled" feeling that drives disengagement from rigid screen-time tools.

**Confidence level:** Demonstrates. SDT's autonomy principle is extensively validated.

**Recommended preset parameters (evidence-informed estimates):**

| Parameter | Relaxed | Focus-Friendly | Super-Focused |
|-----------|---------|---------------|---------------|
| Time-to-annoyance | 45 min | 20 min (default) | 10 min |
| Recovery time | 3 min | 5 min | 10 min |
| Ecstatic threshold | 30 min | 60 min | 120 min |
| Annoyance escalation | 20 min | 10 min | 5 min |
| Best for | Casual users, weekends, teens new to the app | Daily use, balanced approach | Study sessions, deep work, exam periods |

### 5.3 What the Data Does NOT Show

- Whether three presets is the right number. Two might be too few (no middle ground); four or more might create choice paralysis. Three aligns with the Goldilocks heuristic (low/medium/high) but is not empirically validated for this context.
- Whether users switch presets contextually (morning vs. evening, weekday vs. weekend) or set once and forget. Phase 1 should log preset changes to inform Phase 2 adaptive recommendations.

**Implication for Design:** SAGE should implement three named presets with the parameters above as starting points. The default onboarding selection should be "Focus-Friendly" (the middle option -- anchoring bias will make it feel reasonable). Preset switching should be accessible from the home screen or a single swipe -- not buried in settings. Each preset should be described in one sentence using the Chibi's voice (e.g., "Relaxed: Your Chibi is pretty chill about phone time").

---

## S6. Sleepy Mode Freeze & Morning Mood Inheritance (D-026)

### 6.1 The Directive

The Chibi goes to sleep at night (configurable). During sleep, the mood state freezes -- no degradation or improvement. The morning mood inherits from the previous evening's state, creating a "mood banking" mechanic.

### 6.2 Research Findings

**Finding 1: Nighttime phone use significantly impairs sleep quality, especially in adolescents.**

A systematic review (Wiley Online Library, Kumar, 2025) established a significant negative relationship between excessive smartphone use and sleep quality, with younger populations more susceptible. The mechanisms are threefold:

1. **Blue light suppression of melatonin** -- exposure to short-wavelength light before bedtime disrupts nocturnal melatonin secretion (Oxford Academic, Brain Communications, 2024)
2. **Time displacement** -- screen time at bedtime directly displaces sleep time
3. **Cognitive arousal** -- social media and messaging create arousal states incompatible with sleep onset (Siebers et al., SAGE Journals, 2024)

Critically, the effect is app-type-dependent: "lean-forward" apps (social media, games) before bedtime impair sleep quality significantly more than "lean-back" apps (video players) (Journal of Adolescent Health, 2024).

**Confidence level:** Demonstrates. Multiple systematic reviews and prospective cohort studies converge on this finding.

**Finding 2: The 1-hour pre-bedtime window is the evidence-based threshold.**

Research demonstrates that putting the smartphone away 1 hour before bedtime does not appear to interfere with sleep quality or sleep-dependent memory consolidation (Oxford Academic, Brain Communications, 2024). This suggests the Sleepy mode trigger should ideally activate 1 hour before the user's intended bedtime, not at bedtime itself.

**Confidence level:** Indicates. The 1-hour threshold comes from a controlled study on adolescents and young adults. The optimal window may differ for older adults.

**Finding 3: "Morning mood banking" -- no direct precedent, but the mechanic is behaviourally sound.**

No existing app implements mood inheritance across a sleep boundary in the way FocusPal proposes. However, the concept aligns with established behaviour change principles:

- **Temporal continuity:** The user's last action before bed (putting the phone down, triggering a happy Chibi) carries forward, reinforcing the behaviour-consequence link across the sleep gap.
- **Morning reinforcement:** Waking up to a happy Chibi (because the user put their phone down early the previous night) provides positive reinforcement at the start of the day -- a high-leverage moment for habit formation (Fogg, Tiny Habits).
- **Loss aversion mitigation:** The mood freeze during sleep prevents overnight degradation, which would feel unfair ("I was sleeping! How did my Chibi get sad?").

**Confidence level:** Suggests. The individual principles (temporal continuity, morning reinforcement, loss aversion) are each supported by research, but their combination in a mood-banking mechanic is novel and untested.

**Finding 4: Recommended sleep window parameters.**

| Age Group | Recommended Bedtime | Recommended Wake | Source |
|-----------|-------------------|-----------------|--------|
| Teens (13-17) | 21:00-22:00 | 06:00-07:00 | AAP, Sleep Foundation |
| Young adults (18-25) | 22:00-23:00 | 06:00-08:00 | Sleep Foundation |
| Adults (26+) | 22:00-00:00 | 06:00-08:00 | NHS, Sleep Foundation |

FocusPal's configurable Sleepy trigger (current default: 22:00, range: 20:00-00:00) is well-calibrated. Adding a configurable wake time (default: 07:00, range: 05:00-10:00) would complete the sleep window.

### 6.3 What the Data Does NOT Show

- Whether the mood-banking mechanic will incentivise users to check their phone immediately upon waking to see their Chibi's mood -- potentially increasing morning screen time. This is a design risk that should be mitigated by making the morning state visible on a lock-screen widget or notification rather than requiring an app open.
- Whether the freeze-during-sleep mechanic feels fair to users who use their phone late but sleep in (the mood is frozen at "Sad" from late-night use and greets them in the morning). The "morning recovery" mechanic needs careful design.

**Implication for Design:** SAGE should implement the Sleepy mode with a configurable sleep window (bedtime + wake time). The Chibi's sleep animation should be visually distinct and charming (not just a static screen). Morning mood inheritance should carry forward the mood at sleep onset, with a brief "waking up" animation that transitions from sleep to the inherited mood. If the inherited mood is negative (Annoyed/Sad), the Chibi should look groggy but recoverable -- not punishing. SAGE should design a morning recovery mechanic: the first 5 minutes of phone-down time after wake-up rapidly improves mood, rewarding the user for not immediately reaching for their phone.

---

## S7. Chibi Interaction -- Loving but Brief (D-027)

### 7.1 The Directive

Chibi interactions should be 30 seconds to 1 minute. Loving, rewarding, but actively encouraging the user to put the phone down. The paradox: an app that wants you to stop using it.

### 7.2 Research Findings

**Finding 1: 30-60 second micro-interactions align with observed mobile usage patterns.**

Research on mobile app usage demonstrates that approximately 40% of app launches last less than 15 seconds, and the average session across all app categories is under 1 minute (ResearchGate, What and How Long: Prediction of Mobile App Engagement, 2021). The proposed 30-60 second interaction window is not artificially short -- it matches how users already interact with many mobile apps. The design challenge is making those 30-60 seconds feel complete and satisfying, not truncated.

**Confidence level:** Indicates. The usage pattern data is robust, but none of it specifically measures virtual pet interaction sessions.

**Finding 2: Tamagotchi interactions were historically designed for brief, frequent check-ins.**

The original Tamagotchi (1996) required interaction approximately every 30 minutes during waking hours, with each interaction lasting 10-30 seconds (feed, clean, play a simple game). The device's constraint (tiny screen, three buttons) enforced brevity by design. Modern iterations (Tamagotchi On, Tamagotchi Paradise) offer longer optional sessions but retain the brief check-in as the core loop (Tamagotchi Wiki; Wikipedia).

Children historically took Tamagotchis to school because in the first two releases, a character could die in less than half a day without adequate care (Wikipedia). This created compulsive checking behaviour -- exactly the pattern FocusPal must avoid. The lesson: brief interactions work, but they must not create anxiety about what happens when you're away.

**Confidence level:** Indicates. Tamagotchi's design history is well-documented. The transfer to a smartphone app context is inferred.

**Finding 3: The paradox is real -- and Finch has partially solved it.**

FocusPal's central paradox -- an app that wants you to stop using it -- is shared by digital wellbeing apps broadly. Research captures this tension: "to serve the user well may mean building something they no longer need" (Scott Wallace PhD, Medium, 2024). Retention in this category is structurally different from traditional apps.

Finch's design offers the closest precedent:
- Brief daily check-in (set intentions, send Finch on an adventure)
- If users skip a day, nothing bad happens -- no punishment for absence
- Rewards earned through real-world self-care tasks, not in-app time
- The app succeeds by making users feel supported, not fixed (Autonomous.ai, 2025; Yoga Journal, 2025)

Finch demonstrates that the paradox is solvable: you maintain retention by being the thing users come back to by choice (emotional bond) not by compulsion (fear of loss).

**Confidence level:** Indicates. Finch's commercial success (4.8 stars, millions of downloads) validates the model. However, Finch does not target screen-time reduction specifically -- FocusPal's version of the paradox is sharper because the app actively works against its own usage.

**Finding 4: "Positive disengagement" design patterns.**

Research on digital self-control apps (Prosocial Design Network, 2025) identifies effective digital self-control interventions. The most successful ones share a common trait: they make the act of disengaging feel like an achievement rather than a deprivation. FocusPal's version: the Chibi waves goodbye, settles into an activity, and the user leaves knowing the Chibi is happy because they left.

Effective apps for reducing phone use showed that interventions adding friction (forced pauses, breathing prompts) at the point of app launch reduced social media usage by ~33% (Danish Competition and Consumer Authority, 2025 field experiment). FocusPal does not add friction to other apps but creates a positive pull toward disengagement -- a complementary mechanism.

**Confidence level:** Indicates. The friction-based evidence is strong. The "positive pull" mechanism is theoretically sound but empirically untested in isolation.

### 7.3 What the Data Does NOT Show

- The precise duration at which a Chibi interaction stops feeling satisfying and starts feeling truncated. 30 seconds may be too short for users who want to bond; 1 minute may feel rushed for complex interactions (dressing, adventure review). A/B testing in-app is required.
- Whether the paradox holds long-term. Finch's retention data is not public. It is unknown whether "positive disengagement" apps retain users for months or whether the novelty wears off.

**Implication for Design:** SAGE should design Chibi interactions as self-contained micro-moments: the user opens the app, sees the Chibi's state, has one meaningful interaction (pet, feed, review adventure results), and receives a gentle signal to leave (Chibi waves, settles into an activity, speech bubble says "I'm going to read now!"). The interaction should feel complete at 30 seconds and satisfying at 60 seconds. No interaction should require more than 3 taps. The Chibi should never ask the user to stay longer.

---

## S8. Intentional Downtime -- Heartbeat Check (D-028)

### 8.1 The Directive

FocusPal should verify the phone is being intentionally not used (not lost, not stolen, not forgotten). A periodic "proof of life" check to validate downtime.

### 8.2 Research Findings

**Finding 1: Technical approaches to "proof of life" detection.**

The term "heartbeat check" in this context does not mean literal heartbeat detection (biometric). It means a periodic signal that the user is intentionally not using their phone. Technical approaches:

| Approach | Mechanism | Pros | Cons |
|----------|-----------|------|------|
| **Periodic tap prompt** | Every X minutes of downtime, show a subtle notification or lock-screen prompt: "Still focusing?" User taps to confirm. | Simple, clear, no false positives | Interrupts the very focus it's measuring. Creates phone pickups. |
| **Accelerometer/gyroscope** | Detect micro-movements consistent with a phone on a person (pocket, bag) vs. stationary on a surface | Passive, no user action | Battery intensive, unreliable, privacy concern (movement tracking) |
| **Location stability** | If phone GPS hasn't moved, infer intentional rest | Passive | Requires location permission (contradicts privacy-by-design), unreliable for sedentary users |
| **Screen-off duration + unlock pattern** | If screen is off for extended periods then briefly unlocked and re-locked, infer checking behaviour | Moderate accuracy, low battery | Can't distinguish intentional rest from forgotten phone |
| **Smart heuristic** | Combine time-of-day, typical usage patterns, and recent activity to infer intentional downtime | Adaptive, no interruption | Requires historical data, Phase 2/3 complexity |

**Confidence level:** Suggests. These are technical feasibility assessments, not empirically validated approaches. No screen-time app currently implements a "proof of life" system for downtime validation.

**Finding 2: The periodic tap prompt is the most feasible but the most contradictory.**

Asking the user to confirm they're still focused requires them to pick up their phone -- the exact behaviour the app discourages. This creates a micro-interruption that could disrupt flow states (Csikszentmihalyi, 1990). However, the interruption could be designed as a brief, positive moment: a notification that shows the Chibi's current adventure state ("Your Chibi found a seashell! Still focusing?"). This converts the interruption into a variable reward check-in.

**Counter-evidence:** If the heartbeat check is too frequent, it becomes a source of phone pickups rather than a validator. If too infrequent, it fails to detect lost/forgotten phones before significant downtime credit accumulates.

**Confidence level:** Suggests. No research tests periodic confirmation prompts in a focus-session context. The interruption-as-reward concept is an inference from Hook Model theory.

**Finding 3: Edge cases are numerous and difficult to resolve.**

| Edge Case | Problem | Potential Handling |
|-----------|---------|-------------------|
| Airplane mode | Phone unreachable, no data connectivity | Treat as valid downtime -- airplane mode is often intentional focus behaviour |
| Do Not Disturb | Notifications suppressed, user may not see prompt | Use high-priority notification channel (Android) or time-sensitive notification (iOS) |
| Phone charging overnight | Phone stationary for 6-8 hours | Sleepy mode (D-026) handles this -- no heartbeat needed during sleep window |
| Phone lost/stolen | Downtime credit for non-intentional absence | Accept this as an edge case with minimal impact. The user will notice their phone is missing and the downtime credit is harmless. |
| Phone in bag during commute | Phone not in use but user not "focusing" | This is legitimate downtime -- the user is not on their phone. Credit should apply. |

### 8.3 What the Data Does NOT Show

- Whether users perceive the heartbeat check as caring ("the app is checking on me") or invasive ("the app doesn't trust me"). This is a framing and UX challenge, not a data question.
- Battery impact of any passive detection approach. Accelerometer/gyroscope polling is known to be battery-intensive. The tap-prompt approach has negligible battery impact but high UX cost.
- Whether the problem this solves (false downtime credit) is significant enough to warrant the complexity. If the Chibi gives credit for a forgotten phone, the user knows it was unearned -- and the gaming-the-system research (S2.7) suggests that unearned credit undermines the user's trust in the system.

### 8.4 Recommendation

For Phase 1, implement a **minimal heartbeat approach:**
- During active focus sessions (adventure mode), no heartbeat needed -- the user explicitly started the session.
- During passive downtime (phone not in use, no session active), the Chibi accrues downtime credit.
- No periodic prompts in Phase 1. The complexity and UX risk outweigh the benefit for the edge case of a lost/forgotten phone.
- If Tier 2 detection (D-022) is active, UsageStats data already provides a reliable signal for whether the phone is being used.

Phase 2 consideration: a smart heuristic based on accumulated usage patterns could infer intentional vs. incidental downtime without interrupting the user.

**Implication for Design:** SAGE should deprioritise the heartbeat check for Phase 1. The active session mechanic (D-024) already handles the highest-value focus scenarios. Passive downtime credit is an acceptable approximation for Phase 1. If the product owner requires heartbeat validation, the least-invasive approach is a single, optional mid-session check-in during adventures (not passive downtime) that doubles as a peek/reward moment.

---

## S9. Multiple Chibis with Shelving (D-029)

### 9.1 The Directive

Users can collect multiple Chibis. Inactive Chibis are "shelved" (stored). Reunions should be joyful. Architecture should support this from Phase 1 even if full implementation is Phase 2.

### 9.2 Research Findings

**Finding 1: Successful collection systems use distinct character identities to maintain parallel bonds.**

Pokemon's collection system succeeds because each creature has a distinct type, appearance, moveset, and personality. Neopets allows up to 4 active pets per account, with each pet having its own species, colour, stats, and customisation (Wikipedia; Jellyneo Petpet Guide). The key insight from both systems: generic duplicates dilute attachment, while distinct characters sustain parallel bonds.

For FocusPal, this means each Chibi species (Cat, Penguin, Panda, Dragon, Unicorn) must feel meaningfully different -- not just visually but behaviourally. Does the Cat Chibi react differently to phone pickups than the Penguin? Does the Dragon have a different adventure style? Without behavioural differentiation, multiple Chibis become a cosmetic collection rather than an emotional one.

**Confidence level:** Indicates. The principle is demonstrated by Pokemon and Neopets at scale. The transfer to a screen-time app's smaller collection is inferred.

**Finding 2: Emotional attachment transfer is a real risk but manageable.**

Research on virtual pet attachment (ISPR, 2010; ResearchGate, Exploring Affection-Oriented Virtual Pet Game Design, 2017) demonstrates that users form genuine emotional bonds with virtual creatures, and these bonds are reinforced by investment (time, naming, customisation). Introducing a new Chibi creates a potential attachment conflict -- the user's attention and investment shift to the new creature, potentially weakening the bond with the original.

**Mitigation strategies observed in successful systems:**
- **Pokemon:** The "starter Pokemon" retains special status regardless of collection size. Players report the strongest bond with their first Pokemon decades later.
- **Neopets:** Active/inactive pet distinction allows users to rotate attention without permanently losing any creature.
- **Tamagotchi Uni:** "Tama Planet" stores previous Tamagotchis who can be visited.

The consistent pattern: the first creature retains a privileged status, and shelved creatures remain accessible and visually present (not deleted or hidden).

**Confidence level:** Indicates. Multiple virtual pet platforms demonstrate this pattern. The emotional dynamics are consistent with psychological research on primacy effects and attachment theory.

**Finding 3: "Joyful reunion" mechanics -- limited precedent but high emotional potential.**

No existing app implements a specific "reunion" mechanic where a shelved creature celebrates being reactivated. However, the concept aligns with separation-reunion dynamics in attachment theory (Bowlby, 1969). In real relationships, reunions after separation are emotionally heightened -- the joy of reconnection is proportional to the separation duration.

Design opportunity: when a user reactivates a shelved Chibi, the creature could display a "missed you!" animation with progressively more enthusiastic reactions based on shelving duration. A Chibi shelved for a day gets a wave; a Chibi shelved for a month gets an ecstatic running-toward-you animation with confetti.

**Confidence level:** Suggests. Attachment theory supports the emotional logic. The specific mechanic is a design hypothesis, not an evidence-backed recommendation.

**Finding 4: Phase planning recommendation.**

| Aspect | Phase 1 | Phase 2 |
|--------|---------|---------|
| Data architecture | Support multiple Chibi records in local storage | Cloud sync for cross-device collections |
| UI | Single active Chibi only; selection during onboarding | Collection screen, shelving/reactivation, reunion animations |
| Mood engine | Designed for one Chibi; data model extensible | Per-Chibi mood tracking, shelved Chibis in frozen state |
| Premium store | Stub UI for future premium Chibis | Active purchasing, new species releases |

**Confidence level:** Indicates. This phasing aligns with the incremental delivery model in the original brief and minimises Phase 1 complexity while preventing architectural debt.

### 9.3 What the Data Does NOT Show

- Whether FocusPal users will want multiple active Chibis simultaneously or prefer the single-active-Chibi model. Pokemon allows a party of 6; Tamagotchi has traditionally focused on one creature at a time. The single-active model is simpler and preserves emotional intensity. Multiple active Chibis split the user's attention and complicate the mood engine.
- The revenue impact of collection mechanics. If users can earn premium Chibis through extended gameplay (focus milestones), the monetisation model shifts from purchase-driven to engagement-driven. Both are viable but have different economics.
- Whether the "joyful reunion" mechanic creates a perverse incentive to shelve Chibis specifically to experience the reunion animation.

**Implication for Design:** SAGE should design Phase 1 with a single active Chibi and a data model that supports future collection. The onboarding Chibi selection (3 free starters) is the Phase 1 collection moment. FORGE should architect the Chibi data model to store multiple records from Day 1 -- species, name, mood history, earned cosmetics, shelving date. Full collection UX (shelving screen, reunion animations, collection gallery) is Phase 2 scope. The first Chibi should retain "starter" status with a visual badge or distinction in the collection screen.

---

## Cross-Directive Dependencies

Several directives interact and should be designed as a system, not in isolation:

| Interaction | Directives | Design Implication |
|-------------|-----------|-------------------|
| Detection accuracy affects adventure rewards | D-022 + D-024 | Tier 2 detection validates that the user genuinely focused during adventure mode, making rewards feel earned |
| Presets affect environment thresholds | D-025 + D-023 | "Relaxed" preset should have higher environment degradation thresholds; "Super-Focused" should degrade faster |
| Sleep mode interacts with heartbeat check | D-026 + D-028 | No heartbeat needed during sleep window -- the modes are mutually exclusive |
| Collection mechanics tie to adventure rewards | D-029 + D-024 | Rare adventure cosmetics could be Chibi-specific, incentivising trying different Chibis |
| Teen appeal drives collection depth | D-021 + D-029 | Teens will want larger collections and social sharing; the architecture must support this from Phase 1 |
| Brief interactions must accommodate peek mechanic | D-027 + D-024 | The 30-60 second window includes the peek-during-adventure use case |

---

## Appendix: Source Index

| Source | Type | Used In |
|--------|------|---------|
| Ubergizmo, Pokemon Poke-nade Virtual Pet (2025) | Industry press | S1 |
| Hypebeast, Takara Tomy Poke-nade (2025) | Industry press | S1 |
| Neopets Times, Issue 748, Pet Organisation | Community data | S1 |
| PMC, Motivation Crowding Effects in Gamified Fitness Apps (2024) | Peer-reviewed | S1 |
| Apple Developer News, Updated Age Ratings (2025) | Platform documentation | S1 |
| Canadian Centre for Child Protection, App Age Ratings Report (2025) | Research report | S1 |
| 5Rights Foundation, Misleading App Age Ratings (2025) | Research report | S1 |
| Privacy World, App Store Age Verification Laws (2025) | Legal analysis | S1 |
| Android Developer Reference, UsageStatsManager API | Platform documentation | S2 |
| CIIT Training, Android UsageStatsManager Guide (2024) | Technical guide | S2 |
| Apple Developer Documentation, Screen Time Frameworks (2025) | Platform documentation | S2 |
| riedel.wtf, State of the Screen Time API (2024) | Technical analysis | S2 |
| Júdice et al., Discrepancies Between Self-reported and Objectively Measured Smartphone Screen Time: Before and During Lockdown (*Journal of Prevention*, 44, 2023) | Peer-reviewed | S2 |
| Danish Competition and Consumer Authority, Digital Strategies for Screen Time Reduction (Cyberpsychology, Behavior, and Social Networking, 2025) | Peer-reviewed / government study | S2, S7 |
| PMC, Evaluating Effectiveness of Apps Designed to Reduce Mobile Phone Use (2023) | Peer-reviewed | S2, S4 |
| Cloudwards, How to Bypass Screen Time (2025) | Technical guide | S2 |
| Journal of the Association for Consumer Research, Screen-Time App Tracking (2021) | Peer-reviewed | S2 |
| ScienceDirect, Criterion Validity of Research-Based Screen Time Tracking (2022) | Peer-reviewed | S2 |
| Secureprivacy.ai, Privacy by Design GDPR Guide (2025) | Regulatory guide | S2 |
| ICO, Guidance for Wellbeing App Developers (2025) | Regulatory guidance | S2 |
| Sam Liberty, 31 Core Gamification Techniques (Medium, 2025) | Industry analysis | S3 |
| PMC, Gamification for Health and Wellbeing Systematic Review (2018) | Peer-reviewed | S4 |
| ScienceDirect, Non-monotonic Consumer Motivation in Gamified Programmes (2026) | Peer-reviewed | S4 |
| Rac.thairobotics.org, Psychology of Random Rewards in Modern Games (2024) | Industry analysis | S4 |
| PSU, Slot Machine Psyche: Variable Ratio Reinforcement (2025) | Industry analysis | S4 |
| Starglow Media, Recommended Screen Time by Age (2025) | Health guidance compilation | S5 |
| TinyPal, Screen Time Recommendations by Age Chart (2026) | Health guidance compilation | S5 |
| AAP, Screen Time for Teenagers (2024) | Clinical guideline | S5, S6 |
| AACAP, Children and Screen Time (2025) | Clinical guideline | S5 |
| Kumar, Exploring the Link Between Smartphone Use and Sleep Quality (Wiley, 2025) | Peer-reviewed / systematic review | S6 |
| Oxford Academic, Brain Communications, Evening Smartphone Use and Sleep (2024) | Peer-reviewed | S6 |
| Siebers et al., Adolescents' Digital Nightlife (SAGE Journals, 2024) | Peer-reviewed | S6 |
| Journal of Adolescent Health, Bedtime Screen Use and Sleep Outcomes (2024) | Peer-reviewed | S6 |
| JMIR, Smartphone Usage Patterns and Sleep Behavior (2025) | Peer-reviewed | S6 |
| National Sleep Foundation, Impact of Screen Use on Sleep Health (2024) | Consensus statement | S6 |
| ResearchGate, Prediction of Mobile App Engagement (2021) | Peer-reviewed | S7 |
| Wikipedia, Tamagotchi History | Reference | S7 |
| Scott Wallace PhD, Best Mental Health Apps Lose Users (Medium, 2024) | Industry analysis | S7 |
| Autonomous.ai, Finch Self-Care App Review (2025) | Product review | S7 |
| Yoga Journal, Finch Review (2025) | Product review | S7 |
| Prosocial Design Network, Digital Self-Control Apps (2025) | Research compilation | S7 |
| Finchcare.com, Finch App | Product reference | S7 |
| ISPR, Our Undeniable Bond with Virtual Pets (2010) | Academic commentary | S9 |
| ResearchGate, Affection-Oriented Virtual Pet Game Design (2017) | Peer-reviewed | S9 |
| Bowlby, Attachment Theory (1969) | Peer-reviewed (seminal) | S9 |

---

*Research supplement prepared by IRIS. This is an addendum to the original research brief (pipeline/01-research-brief.md), not a replacement. All findings carry stated confidence levels. The most significant revision is S2 (Usage Detection Accuracy), where the product owner's challenge prompted a reassessment that changed the recommendation from "app-level-only for Phase 1" to "two-tier detection in Phase 1." This revision is data-supported and the original brief's limitation is honestly acknowledged.*

---

**Status: READY FOR ATLAS QA**
