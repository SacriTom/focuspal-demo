# FocusPal Design Specification

**Agent:** SAGE (Solution Architecture & Guided Experience Designer)
**Date:** 2026-03-19
**Status:** READY FOR SELF-REVIEW
**Input:** IRIS Research Brief + Supplement (01-research-brief.md, 01-research-supplement.md), System Design Spec, Idea Bank, User Directives D-006 through D-033

---

> **Design Principle (Read First):** Every design decision in this document traces to a numbered research finding or user directive. Where IRIS provided evidence, this spec cites it. Where evidence is absent, assumptions are flagged. The guiding question for every element: "Does this strengthen the user's bond with their Chibi?" If the answer is no or unclear, the element is cut or deferred.

---

## 1. Design Philosophy

Five principles govern every design decision. They are ordered by priority -- when principles conflict, the higher-numbered principle yields to the lower.

### P1. The Bond Is the Product

The emotional attachment between user and Chibi is not a feature -- it is the entire value proposition. Every screen, animation, and interaction exists to strengthen, protect, or reward this bond. If a feature weakens the bond (by creating guilt, anxiety, or resentment), it is removed regardless of other merits.

**Research basis:** IRIS Section 1 (competitive gap: no competitor uses emotional attachment as primary mechanism), Section 5.2 (SDT relatedness need), Section 5.4 (Hook Model investment phase), Finch validation (Section 3.5).

### P2. Reward the Positive, Never Punish the Negative

The Chibi thrives when the user puts the phone down. It does not suffer when the user picks it up -- it notices, reacts, and gently communicates. The difference is load-bearing: "Your Chibi is happy because you focused" is architecturally superior to "Your Chibi is sad because you scrolled." The emotional cost of a negative state should motivate change, not inflict guilt.

**Research basis:** IRIS Section 5.1 (guilt-based approaches fail), Section 5.2 (positive reinforcement > punishment, grounded in Self-Determination Theory and the Fogg Behavior Model), Section 11.1 (persuasion vs. manipulation line).

### P3. Autonomy Over Control

The user always has agency. Sensitivity is configurable. Adventures can be paused without penalty. Sleepy mode can be adjusted. The app never blocks, restricts, or gates access to the phone itself. "The objective is to encourage less usage, not hold the phone hostage" (product owner, Idea Bank).

**Research basis:** IRIS Section 5.2 (SDT autonomy need -- load-bearing for behaviour change), Section 6.3 (configurable thresholds serve autonomy), D-006 (configurable sensitivity).

### P4. Honesty Over Persuasion

When the app cannot determine screen time (Tier 1), it says so clearly. When features require Tier 2, it explains why without guilt. When the Chibi's mood is approximate, the system never claims precision it lacks. Transparency is the line between persuasion (permitted) and manipulation (prohibited).

**Research basis:** IRIS Section 10.2 (EU AI Act -- transparency as key differentiator), Section 11.1 (emotional manipulation risk), D-031 (Tier 1 messaging: informative, not punishing).

### P5. Simplicity as a Feature

Every interaction completes in three taps or fewer. Every screen answers one question. The Chibi communicates via emoji -- no text translation needed, universally legible. If a feature needs explaining, it needs redesigning.

**Research basis:** IRIS Section 5.3 (Fogg Ability principle -- target behaviour is inaction), Section 12 Priority 2 (mood must be "instantly legible without text"), D-012 (full-screen scene, minimal UI overlay).

---

## 2. User Journey Map

### 2.1 Journey Overview

The user journey has four phases. Each phase has a distinct emotional arc and design objective.

```
PHASE A: FIRST ENCOUNTER (0-5 min)
  Emotional arc: Curious --> Delighted --> Invested
  Objective: Create the bond

PHASE B: FIRST DAY (5 min - 24 hr)
  Emotional arc: Invested --> Experimenting --> Understanding
  Objective: Teach the feedback loop

PHASE C: FIRST WEEK (Day 1-7)
  Emotional arc: Understanding --> Habituated --> Proud
  Objective: Establish the daily loop

PHASE D: LONG-TERM (Week 2+)
  Emotional arc: Proud --> Collecting --> Committed
  Objective: Deepen through progression and collection
```

### 2.2 Phase A: First Encounter (Onboarding)

| Step | Screen | User Action | Chibi Response | Emotional Beat | Duration |
|------|--------|-------------|---------------|----------------|----------|
| 1 | Splash | Waits | App logo fades in with gentle animation | Anticipation | 2-3s |
| 2 | Choose Chibi | Taps one of 3 eggs (Cat/Penguin/Panda) | Eggs wobble gently on hover/tap | Curiosity, choice | 15-30s |
| 3 | Hatching | Holds finger on egg | Egg warms, wobbles, cracks, Chibi emerges | Wonder, investment | Max 60s (D-035) |
| 4 | Naming | Types a name, taps confirm | Chibi looks up, blinks, nods at its name | Commitment, ownership | 15-30s |
| 5 | Preset Selection | Chooses Relaxed/Focus-Friendly/Super-Focused | Chibi reacts (yawns for Relaxed, stretches for Focus-Friendly, punches air for Super-Focused) | Personalisation | 10-20s |
| 6 | Tier 2 Nudge | Reads the Chibi's request, taps to enable or skips | Chibi holds up a magnifying glass emoji, looks curious | Trust, transparency | 15-30s |
| 7 | Home | Arrives at home screen | Chibi waves, explores its new home | Arrival, belonging | -- |

**Total onboarding: 2-4 minutes.** Three meaningful actions (choose, hatch, name). One decision (preset). One optional step (Tier 2). No walls of text. No tutorials.

**Research basis:** IRIS Section 12 Priority 1 (hatching/naming is the single most important UX), Section 5.3 (Fogg: target behaviour is inaction, ability = high), D-011 (onboarding flow), D-025 (presets), D-030 (Tier 2 timing).

### 2.3 Phase B: First Day

| Moment | What Happens | Design Goal |
|--------|-------------|-------------|
| First departure | User locks phone or switches apps. After 5+ min away, Chibi starts an activity (cooking, reading). | Teach: "When I leave, good things happen." |
| First return | User opens FocusPal. Chibi looks up, waves, shows what it was doing via speech bubble. If <20 min away: Content. If >60 min: Happy. | Teach: "The longer I'm away, the happier it is." |
| First annoyance | User opens FocusPal too soon (<20 min since last check). Chibi pauses activity, looks slightly annoyed, huffs. | Teach: "Checking too often bothers it." |
| First adventure | User discovers Focus Timer tab, starts a 25-min session. Chibi gears up, sets off on adventure. | Teach: "I can actively choose to focus." |
| First night | Chibi yawns, stretches, gets into bed at configured sleep time. | Teach: "It has a life cycle. It needs rest too." |
| First morning | User opens app. Chibi wakes up, stretches. Mood reflects last night's behaviour. | Teach: "My evening choices carry forward." |

### 2.4 Phase C: First Week

| Day | Progression Element | Engagement Hook |
|-----|-------------------|----------------|
| 1 | Bond formed. Feedback loop understood. | Novelty, emotional investment |
| 2 | First cosmetic earned from adventure. Chibi wears it. | Variable reward, customisation |
| 3 | Environment brightens after sustained good behaviour. | Ambient feedback, pride |
| 4-5 | User experiments with preset switching. Finds their rhythm. | Autonomy, competence |
| 6-7 | User has accumulated several cosmetics. Notices rarity tiers. | Collection drive, completionism |

### 2.5 Phase D: Long-Term (Phase 2-3 Design)

| Timeframe | Feature | Engagement |
|-----------|---------|-----------|
| Week 2-4 | Chibi learns skills (cooking, music) -- progress bars visible | Competence (SDT), investment |
| Month 1-2 | Evolution unlocked (sustained positive behaviour) | Aspiration, long-term goal |
| Month 2+ | Multiple Chibis, shelving, collection gallery | Collection drive (D-021), social sharing |
| Month 3+ | Premium Chibis, environment customisation, cosmetic depth | Personalisation, monetisation |

---

## 3. Onboarding Flow

### 3.1 Splash Screen

```
+------------------------------------------+
|                                          |
|                                          |
|           [FocusPal Logo]                |
|                                          |
|         A gentle pulse animation         |
|                                          |
|                                          |
|              Loading...                  |
|                                          |
+------------------------------------------+
```

**Duration:** 2-3 seconds. Logo fades in with a soft scale-up animation (0.8x to 1.0x over 600ms, ease-out curve). No loading bar -- the pulse animation communicates "loading" without anxiety.

**Logic:** Check SharedPreferences for existing Chibi data. If found, route to HomeScreen. If not, route to ChooseChibiScreen.

**Interactions:** None. Passive screen.

### 3.2 Choose Chibi Screen

```
+------------------------------------------+
|                                          |
|        Choose your companion             |
|                                          |
|   +--------+  +--------+  +--------+    |
|   |  ____  |  |  ____  |  |  ____  |    |
|   | /    \ |  | /    \ |  | /    \ |    |
|   | | ** | |  | | ** | |  | | ** | |    |
|   | \____/ |  | \____/ |  | \____/ |    |
|   |  Egg 1 |  |  Egg 2 |  |  Egg 3 |    |
|   +--------+  +--------+  +--------+    |
|     Cat        Penguin      Panda        |
|                                          |
|   (Eggs wobble gently in idle state)     |
|                                          |
+------------------------------------------+
```

**Layout:** Three eggs arranged horizontally, centre-aligned. Each egg is a tappable card. Below each egg, a small species label (one word).

**Interactions:**
- **Idle:** All three eggs have a subtle wobble animation (2-3 degree rotation, 3s period, offset per egg so they do not synchronise).
- **Tap:** Selected egg wobbles more vigorously (5-degree rotation, faster period). A soft glow appears around it. Other eggs dim slightly (opacity 0.6).
- **Confirm:** After tapping an egg, a "Hatch this one?" confirmation appears as a bottom sheet with the egg centred and two buttons: "Yes!" (primary) and "Wait, let me think" (secondary, returns to selection).

**Why three eggs (not more):** D-021 specifies three free starters (Cat, Penguin, Panda). Premium types are Phase 3. Three options prevent choice paralysis while providing meaningful autonomy (IRIS Section 5.2, SDT autonomy).

**Phase 1 note:** Each starter has its own distinct sprite pack (Cat, Penguin, Panda) with unique animations, and its own egg design from the egg sprite set (48 variants available). The character-agnostic sprite system (Section 9) means adding future species requires only a new sprite folder — zero code changes.

### 3.3 Hatching Screen

```
+------------------------------------------+
|                                          |
|                                          |
|                                          |
|            [Large Egg Centre]            |
|             Wobbles on touch             |
|                                          |
|        +========================+        |
|        |  Warmth Meter (fill)   |        |
|        +========================+        |
|                                          |
|         Hold to warm your egg            |
|                                          |
+------------------------------------------+
```

**This is the most important screen in the app.** (IRIS Section 12 Priority 1.) It must feel magical, not functional.

**Layout:** Single large egg, centre screen. Warmth meter below it (horizontal progress bar). Instructional text at bottom, fading out after first touch.

**Interaction sequence:**
1. **Touch and hold:** User places finger on egg. Warmth meter begins filling. Egg starts glowing from the centre outward (warm orange/amber gradient expanding from touch point).
2. **Warmth builds (0-50%):** Egg wobbles gently. Subtle warm particles rise from touch point. Warmth meter fills steadily (~1.5% per second = ~33 seconds to 50%).
3. **Cracks appear (50-80%):** Small crack lines animate across the egg surface. Wobble intensifies. A faint heartbeat sound effect (optional, respecting device volume). Warmth meter fills faster (~2% per second).
4. **Hatching (80-100%):** Egg shakes vigorously. Crack lines widen. Light bursts from cracks. At 100%: egg splits apart, bright flash, particles explode outward, Chibi appears in centre with a small bounce animation.
5. **First moment:** Chibi looks around, blinks twice, looks up at the camera (user). Speech bubble: single heart emoji.

**Total duration:** Max 60 seconds of continuous hold (D-035). If user lifts finger: warmth meter pauses (does not reset). A gentle prompt appears after 2 seconds: "Your egg is getting cold..." with the warmth meter slowly draining (~1% per second). This creates gentle urgency without punishment. Exact timing is UX polishing — calibrate after user testing.

**Why this duration:** Long enough to feel like an investment (Hook Model investment phase, IRIS Section 5.4), short enough to not lose patience. The hold mechanic creates physical participation -- the user is literally warming the egg, not watching a cutscene.

**Animation specs:**
- Egg wobble: sinusoidal rotation, amplitude 2-5 degrees, period decreasing from 3s to 0.5s as warmth increases
- Glow: radial gradient, centre at touch point, radius expanding from 0% to 100% of egg size
- Cracks: pre-drawn crack overlay sprites (3 stages), crossfaded at 50%, 65%, 80% warmth
- Hatch burst: 20-30 particle sprites, radial velocity 200-400px/s, gravity pull after 300ms, fade over 1s
- Chibi entrance: scale from 0.5x to 1.1x (overshoot), settle to 1.0x. Duration: 400ms. Curve: elasticOut

### 3.4 Naming Screen

```
+------------------------------------------+
|                                          |
|          [Chibi sprite, idle]            |
|          (bouncing gently)               |
|                                          |
|        What will you call me?            |
|                                          |
|   +----------------------------------+   |
|   |  [Text input field]              |   |
|   +----------------------------------+   |
|                                          |
|        [   That's my name!   ]           |
|                                          |
+------------------------------------------+
```

**Layout:** Chibi centred in upper third, idle animation. Question text below. Text input field centred. Confirm button below input.

**Interactions:**
- **Text input:** Max 12 characters. No profanity filter in Phase 1 (local-only, no sharing). Keyboard opens automatically.
- **As user types:** Each character entered makes the Chibi's eyes follow the text (subtle head tilt tracking the text cursor position).
- **Confirm tap:** Chibi jumps once, speech bubble shows the name in a heart frame, followed by a celebratory animation (sparkle particles, 1s duration). This is the "naming ceremony" (IRIS Section 12 Priority 1: "Naming must feel like a commitment, a ceremony, not a text field").
- **Empty submit prevention:** Button is greyed out until at least 1 character is entered.

### 3.5 Preset Selection Screen

```
+------------------------------------------+
|                                          |
|     [Chibi sprite, looking curious]      |
|     Speech bubble: "How should I be?"    |
|                                          |
|   +----------------------------------+   |
|   |  Relaxed                         |   |
|   |  "I'm pretty chill about         |   |
|   |   phone time"                    |   |
|   +----------------------------------+   |
|                                          |
|   +==================================+   |
|   |  Focus-Friendly  [DEFAULT]       |   |
|   |  "A nice balance between us"     |   |
|   +==================================+   |
|                                          |
|   +----------------------------------+   |
|   |  Super-Focused                   |   |
|   |  "I take focus very seriously!"  |   |
|   +----------------------------------+   |
|                                          |
|          [    Let's go!    ]             |
|                                          |
+------------------------------------------+
```

**Layout:** Three cards stacked vertically. Each card has: preset name (bold), one-sentence description in the Chibi's voice, and a subtle indicator of strictness (e.g., 1/2/3 small focus icons).

**Default:** Focus-Friendly is pre-selected (highlighted border, slight scale-up). Anchoring bias makes the middle option feel reasonable (IRIS Supplement S5).

**Interactions:**
- **Tap a card:** Selection moves. Chibi reacts to each choice:
  - Relaxed: Chibi yawns and stretches
  - Focus-Friendly: Chibi nods and gives a thumbs-up emoji
  - Super-Focused: Chibi punches the air and looks determined
- **Confirm:** Routes to Tier 2 nudge screen.

**Preset parameters (from IRIS Supplement S5):**

| Parameter | Relaxed | Focus-Friendly | Super-Focused |
|-----------|---------|---------------|---------------|
| Time-to-annoyance | 45 min | 20 min | 10 min |
| Recovery time | 3 min | 5 min | 10 min |
| Ecstatic threshold | 30 min | 60 min | 120 min |
| Annoyance escalation | 20 min | 10 min | 5 min |

**Age range prompt:** Before presets, a lightweight age-range selector appears (D-025): "How old are you?" with ranges: 13-17, 18-25, 26+. This auto-selects a recommended preset (13-17 defaults to Relaxed, 18-25 to Focus-Friendly, 26+ to Focus-Friendly). The user can override. Age is stored locally only.

### 3.6 Tier 2 Permission Nudge

```
+------------------------------------------+
|                                          |
|     [Chibi sprite, holding a             |
|      magnifying glass]                   |
|                                          |
|     Speech bubble: magnifying glass      |
|     + phone emoji + question mark        |
|                                          |
|   +----------------------------------+   |
|   |  Right now I can only see when   |   |
|   |  you open this app.              |   |
|   |                                  |   |
|   |  If you let me see your screen   |   |
|   |  time, I can respond to your     |   |
|   |  real habits -- and you'll       |   |
|   |  unlock evolution, skills, and   |   |
|   |  progress tracking.              |   |
|   |                                  |   |
|   |  Your data stays on this phone.  |   |
|   |  I don't send it anywhere.       |   |
|   +----------------------------------+   |
|                                          |
|     [  Enable Screen Time Access  ]      |
|     (takes you to Settings)              |
|                                          |
|         Skip for now                     |
|                                          |
+------------------------------------------+
```

**This screen appears AFTER the naming ceremony (D-030).** The bond is established before asking for trust.

**Layout:** Chibi in upper third holding a magnifying glass (using the "Throwing" sprite with overlay or a speech bubble composition). Explanation card centred. Primary action button. Secondary skip link (not a button -- visually de-emphasised but fully accessible).

**Interactions:**
- **Enable:** Opens the system Settings page for Usage Access (Android) or Screen Time (iOS) via a deep link. When user returns to the app, the system checks if permission was granted. If yes: Chibi celebrates (jumping animation + confetti). If no: reverts to skip behaviour gracefully.
- **Skip:** Chibi nods understandingly (no disappointment animation -- D-031: not punishing, informative). Routes to HomeScreen. A small persistent indicator appears on the Settings tab (a subtle dot badge) so the user can always find the option.

**Messaging principles (D-031):**
- Honest: "Right now I can only see when you open this app" -- not hiding the limitation.
- Benefit-framed: "unlock evolution, skills, and progress tracking" -- what the user gains, not what they lose.
- Privacy-forward: "Your data stays on this phone" -- trust-building.
- Non-punishing: Skip is always available. No guilt language. No countdown. No "Are you sure?"

**What is locked at Tier 1 vs. unlocked at Tier 2 (D-031):**

| Feature | Tier 1 (App-Level) | Tier 2 (UsageStats) |
|---------|-------------------|-------------------|
| Chibi mood reactions | Yes (approximate -- based on app opens) | Yes (accurate -- based on total screen time) |
| Home screen + environment | Yes | Yes |
| Adventures (active focus timer) | Yes | Yes |
| Cosmetic rewards from adventures | Yes | Yes |
| Evolution system | LOCKED | Unlocked (Phase 2) |
| Skill learning | LOCKED | Unlocked (Phase 2) |
| Progress tracking / stats | Basic (sessions only) | Full (screen time trends) |
| Mood accuracy | Low-Medium | Medium-High |

**Persistent accessibility (D-031):** The Settings screen always shows a "Screen Time Access" toggle with a one-tap path to the system setting. If Tier 2 is not enabled, a gentle informational banner appears: "Enable screen time access to unlock [Chibi name]'s full potential." No nagging. No popups. Always there, never pushy.

---

## 4. Screen Wireframes

### 4.1 Home Screen

```
+------------------------------------------+
|  [Home icon]              [Mood emoji]   |
|                                          |
|                                          |
|           ENVIRONMENT SCENE              |
|     (full-screen pixel art background)   |
|                                          |
|        [Chibi sprite, animated]          |
|                                          |
|          [Speech bubble: emoji]          |
|                                          |
|                                          |
|                                          |
|                                          |
|  +------+  +------+  +------+  +------+ |
|  | Home |  | Focus|  | Stats|  | Cog  | |
|  +------+  +------+  +------+  +------+ |
+------------------------------------------+
```

**Layout (D-012: full-screen scene + emoji bubbles + time-of-day awareness):**
- **Full bleed:** Environment scene covers entire screen. No card borders, no white backgrounds. The scene IS the screen.
- **Top-left:** Location/context icon (home icon for home environment, compass for adventures). Semi-transparent background pill. Tappable -- shows environment name.
- **Top-right:** Current mood emoji indicator. Semi-transparent background circle. Subtle glow matches mood colour. Tappable -- shows mood name and a one-sentence explanation ("Happy: [Chibi name] has been enjoying the quiet").
- **Centre:** Chibi sprite, animated. Positioned on the environment's "ground plane" (bottom 40% of screen). Walks between activity stations.
- **Speech bubbles:** Float above Chibi, fade in/out over 3-4 seconds. Show what Chibi is doing (cooking emoji, book emoji, music note emoji, zzz for sleeping). Appear every 15-30 seconds during idle viewing.
- **Bottom:** Navigation bar. Semi-transparent overlay (80% opacity dark). Four tabs: Home, Focus, Stats, Settings.

**Interactions:**
- **Tap Chibi (D-027):** Chibi looks up, waves, hearts appear. A 30-60 second interaction window begins. During this window:
  - Chibi responds to taps with happy animations (jumping, spinning, heart emojis)
  - After 30 seconds: Chibi yawns gently (first tire cue)
  - After 45 seconds: Chibi waves and sits down (second tire cue)
  - After 60 seconds: Chibi settles into an activity, speech bubble says sleep/book/food emoji (wants to do its own thing)
  - Continuing to tap after tire cues: Chibi looks mildly annoyed (same as phone-pickup annoyance but milder). After 2+ minutes of continuous tapping: affects mood negatively.
- **Swipe up on Chibi:** Opens a quick-access customisation drawer (Phase 2: cosmetics, accessories). Phase 1: shows earned adventure cosmetics.
- **Tap environment background:** No response. The environment is ambient, not interactive. (Phase 3: tappable activity stations for environment customisation.)

**Time-of-day awareness (D-012):**

| Time Window | Environment State | Chibi Behaviour |
|-------------|------------------|-----------------|
| 06:00-08:00 | Dawn: warm orange sky, soft light | Waking up, stretching, morning idle |
| 08:00-12:00 | Morning: bright, blue sky | Active activities (cooking, reading) |
| 12:00-17:00 | Afternoon: full brightness, peak scene | Active activities, adventures |
| 17:00-20:00 | Evening: warm golden light | Winding down, relaxed activities |
| 20:00-22:00 | Dusk: purple/amber sky, indoor lights on | Calm activities, preparing for sleep |
| 22:00-06:00 | Night: dark sky, stars, warm indoor glow | Sleepy mode (see Section 5.6) |

Time windows are configurable via the sleep schedule setting (bedtime + wake time). The transition between time states uses a 30-minute crossfade.

### 4.2 Focus Timer Screen

```
+------------------------------------------+
|                                          |
|        Start an adventure!               |
|                                          |
|     [Chibi sprite, excited, with         |
|      backpack/adventure gear]            |
|                                          |
|   +----------------------------------+   |
|   |        25 min                     |   |
|   |   [Circular progress ring]        |   |
|   |        START                      |   |
|   +----------------------------------+   |
|                                          |
|   Duration:  [25]  [45]  [60]  [90]      |
|                                          |
|                                          |
|  +------+  +------+  +------+  +------+  |
|  | Home |  |*Focus|  | Stats|  | Cog  |  |
|  +------+  +------+  +------+  +------+  |
+------------------------------------------+
```

**Pre-session state (not yet started):**
- Chibi stands in adventure gear (species-specific Walk animation, but stationary). Speech bubble: compass emoji + sparkle emoji.
- Duration selector: four pill buttons (25 min, 45 min, 60 min, 90 min). Default: 25 min. Tap to select -- selected pill fills with colour.
- Large "START" button in the centre of a circular progress ring (unfilled).

**Active session state:**

```
+------------------------------------------+
|                                          |
|     [Chibi name] is exploring!           |
|                                          |
|     [Small Chibi sprite, walking         |
|      through adventure scene]            |
|                                          |
|   +----------------------------------+   |
|   |    [Progress ring: 40% filled]   |   |
|   |         18:32 remaining          |   |
|   +----------------------------------+   |
|                                          |
|        [  Pause Adventure  ]             |
|                                          |
|                                          |
|  +------+  +------+  +------+  +------+  |
|  | Home |  |*Focus|  | Stats|  | Cog  |  |
|  +------+  +------+  +------+  +------+  |
+------------------------------------------+
```

- **Progress ring:** Fills clockwise. Colour transitions from cool blue (start) to warm gold (near completion) to bright green (complete).
- **Adventure scene:** Small pixel art scene behind the progress ring showing the Chibi walking through an outdoor environment (using Outside Environment tileset). Chibi walks slowly, encounters landmarks.
- **Peek mechanic (D-024):** Opening FocusPal during an active session shows this screen. The timer continues. Viewing the adventure does NOT disturb it. No penalty for checking. The progress ring and adventure scene update in real-time.
- **Leaving FocusPal during session:** If the user switches to another app, the behaviour depends on detection tier:
  - **Tier 1:** Timer pauses. When user returns: "Want to continue your adventure? [Continue] [End here]" (D-024: non-punishing pause).
  - **Tier 2:** Timer continues in background (the app knows whether the user is on another app or phone is idle). If the user is actively using another app for >2 minutes: adventure pauses with "Your adventure is waiting when you're ready." If phone is idle (screen off): adventure continues (this is focus time).

**Session completion:**

```
+------------------------------------------+
|                                          |
|       Adventure complete!                |
|                                          |
|    [Chibi sprite, ecstatic,              |
|     jumping with treasure chest]         |
|                                          |
|     You found:                           |
|     +----------------------------+       |
|     |  [Cosmetic item image]     |       |
|     |  "Pirate Hat"              |       |
|     |  *Uncommon*                |       |
|     +----------------------------+       |
|                                          |
|        [  Back to Home  ]                |
|                                          |
|  +------+  +------+  +------+  +------+  |
|  | Home |  |*Focus|  | Stats|  | Cog  |  |
|  +------+  +------+  +------+  +------+  |
+------------------------------------------+
```

- Chibi enters Ecstatic state (celebrating animation).
- Treasure chest opens with a particle burst. Cosmetic reward revealed.
- Reward card shows item name, rarity tier (colour-coded border), and a preview of the Chibi wearing it.
- "Back to Home" returns to HomeScreen where the Chibi is now wearing the new cosmetic and in Ecstatic mood.

**Paused session (D-024):**
If user chooses to pause: adventure freezes. Next time user opens Focus Timer: "Your adventure is paused at 12:30 remaining. [Resume] [Start a new one]." Paused adventures persist until sleep time activates that day (D-037). Rewards from paused adventures are not lost during the day -- they are delayed until resumed. At sleep time, incomplete adventures reset.

### 4.3 Stats Screen

```
+------------------------------------------+
|                                          |
|       Your Journey                       |
|                                          |
|   Today's Focus                          |
|   +----------------------------------+   |
|   | Active: 1h 25m  |  Passive: 3h   |   |
|   +----------------------------------+   |
|                                          |
|   This Week              [graph area]    |
|   +----------------------------------+   |
|   | M  T  W  T  F  S  S             |   |
|   | ## ## ## ## ## .  .              |   |
|   +----------------------------------+   |
|                                          |
|   Mood Timeline                          |
|   +----------------------------------+   |
|   | Emoji row showing mood changes   |   |
|   | over the past 24 hours           |   |
|   +----------------------------------+   |
|                                          |
|   Streak: 5 days                         |
|                                          |
|  +------+  +------+  +------+  +------+  |
|  | Home |  | Focus|  |*Stats|  | Cog  |  |
|  +------+  +------+  +------+  +------+  |
+------------------------------------------+
```

**Tier 1 data:** Active session count + duration. Streak (consecutive days with at least one session). Basic mood timeline (emoji row).

**Tier 2 data (additional):** Total screen-on time vs. focus time. App category breakdown (if available on Android). Weekly trend graph. This section shows a gentle Tier 2 promotion if not enabled: "Enable screen time access to see your full picture."

**Interactions:** Scrollable. Tap on a day in the weekly graph to see that day's detail. Tap on a mood emoji in the timeline to see when/why the mood changed.

### 4.4 Settings Screen

```
+------------------------------------------+
|                                          |
|       Settings                           |
|                                          |
|   Sensitivity Preset                     |
|   [ Relaxed | *Focus-Friendly* | Super ] |
|                                          |
|   Fine-Tune (expandable)                 |
|   +----------------------------------+   |
|   | Time-to-annoyance: [20 min]  [-][+]  |
|   | Recovery time:     [5 min]   [-][+]  |
|   | Ecstatic threshold:[60 min]  [-][+]  |
|   | Annoyance speed:   [10 min]  [-][+]  |
|   +----------------------------------+   |
|                                          |
|   Sleep Schedule                         |
|   Bedtime: [22:00]  Wake: [07:00]        |
|                                          |
|   Screen Time Access                     |
|   [Toggle: OFF]  --> Tap to enable       |
|   "Unlock evolution & skill learning"    |
|                                          |
|   About FocusPal | Privacy | Help        |
|                                          |
|  +------+  +------+  +------+  +------+  |
|  | Home |  | Focus|  | Stats|  |*Cog  |  |
|  +------+  +------+  +------+  +------+  |
+------------------------------------------+
```

**Layout:** Scrollable list. Grouped by category.

**Sensitivity Preset (D-025):** Segmented control showing three presets. Tapping a preset updates all four parameters below. A custom indicator appears if the user has modified individual values after selecting a preset.

**Fine-Tune:** Collapsed by default (most users will not change these -- IRIS Section 6.4: <5% of users change defaults). Expanding reveals four sliders with +/- buttons and current value display. Each parameter shows its allowed range.

**Sleep Schedule:** Two time pickers. Default 22:00-07:00. Configurable 20:00-00:00 (bedtime) and 05:00-10:00 (wake).

**Screen Time Access (D-031):** Persistent toggle. If OFF: brief explanation text and a one-tap deep link to system settings. If ON: shows "Active" with a green checkmark. Always one tap away -- never buried.

---

## 5. Chibi Emotion State Machine

### 5.1 State Definitions

Six mood states, ordered from most positive to most negative (plus the special Sleepy state):

| State | Emoji | Visual Description | Chibi Animations | Speech Bubbles |
|-------|-------|-------------------|------------------|----------------|
| Ecstatic | Star-struck face | Golden glow, sparkle particles around Chibi | Celebrating, jumping, dancing | Star, sparkle, heart, trophy emojis |
| Happy | Smiling face | Warm glow, flowers/notes floating | Cooking, reading, playing music, walking with bounce | Food, book, music note, heart emojis |
| Content | Relieved face | Neutral, calm lighting | Idle, slow walking, looking around | Neutral face, thought bubble, leaf emojis |
| Annoyed | Huffing face | Slight dim, Chibi crosses arms | Stops activity, crosses arms, huffs, taps foot | Exclamation, huff cloud, phone emoji with X |
| Sad | Crying face | Noticeable dim, muted colours | Sits down, droopy posture, slow movements | Rain drop, broken heart, downcast emojis |
| Sleepy | Sleeping face | Night scene, warm indoor glow | Lying in bed, breathing animation, zzz particles | Moon, star, zzz emojis |

### 5.2 Transition Rules

```
                    +----------+
                    | Ecstatic |
                    +----+-----+
                         |
             (decay after 10 min or phone pickup)
                         v
                    +----------+
          +-------->|  Happy   |<--------+
          |         +----+-----+         |
          |              |               |
    (recovery:      (phone pickup   (long focus
     5+ min          or decay)       session)
     phone down)         |               |
          |              v               |
          |         +----------+         |
          +---------|  Content |         |
          |         +----+-----+         |
          |              |               |
    (recovery:      (sustained           |
     5+ min          phone use)          |
     phone down)         |               |
          |              v               |
          |         +----------+         |
          +---------|  Annoyed |---------+
          |         +----+-----+     (continued use
          |              |           after escalation
    (recovery:           |            threshold)
     10+ min             v
     phone down)    +----------+
          +---------|   Sad    |
                    +----------+

                    +----------+
                    |  Sleepy  |  (time-of-day override)
                    +----------+
```

### 5.3 Transition Parameters (Configurable via Presets)

**Upward transitions (mood improves) -- require sustained phone-down time:**

| Transition | Trigger (Focus-Friendly default) | Mechanism |
|------------|--------------------------------|-----------|
| Sad --> Annoyed | 10 min phone-down time | Gradual -- Chibi slowly uncrosses arms, stands up |
| Annoyed --> Content | 5 min phone-down time (Recovery time parameter) | Chibi relaxes, resumes idle |
| Content --> Happy | 15 min phone-down time | Chibi starts an activity (cooking, reading) |
| Happy --> Ecstatic | 60 min phone-down time (Ecstatic threshold parameter) | Requires sustained non-use OR completing an active focus session |

**Downward transitions (mood worsens) -- triggered by phone usage:**

| Transition | Trigger (Focus-Friendly default) | Mechanism |
|------------|--------------------------------|-----------|
| Ecstatic --> Happy | Any phone pickup, or natural decay after 10 min | Ecstatic is temporary and special |
| Happy --> Content | Phone open for >5 min continuous | Activity interrupted |
| Content --> Annoyed | Phone open for >20 min (Time-to-annoyance parameter) | Clear cause-and-effect: "You've been on your phone a while" |
| Annoyed --> Sad | Continued phone use for >10 min after entering Annoyed (Annoyance escalation parameter) | Two-stage warning: Annoyed is the yellow light, Sad is the red |

**Key design rule:** Downward transitions are faster than upward transitions. This creates clear cause-and-effect (IRIS Section 5.1, D-006) while ensuring the user must invest time to see improvement. The asymmetry teaches: "Quick to notice, quick to forgive -- and always forgiving."

### 5.4 Tier 1 vs. Tier 2 Mood Accuracy

| Aspect | Tier 1 (App-Level) | Tier 2 (UsageStats) |
|--------|-------------------|-------------------|
| What triggers "phone use" | User opens FocusPal app | Any app is in foreground (actual screen-on time) |
| Accuracy | Low-Medium. Cannot detect usage of other apps. | Medium-High. Detects device-wide usage. |
| False positives | Chibi stays happy while user scrolls TikTok for 2 hours (because FocusPal was never opened) | Rare. Chibi accurately reflects real usage. |
| False negatives | Chibi gets annoyed when user briefly opens FocusPal to check, even if phone was idle otherwise | Rare. Context-aware. |
| Mood update frequency | On app lifecycle events only (foreground/background) | Polled every 60 seconds from UsageStats (battery-conscious) |

**Tier 1 mood logic (simplified):**
- `time_since_last_app_open > ecstatic_threshold` --> Ecstatic
- `time_since_last_app_open > 15 min` --> Happy
- `time_since_last_app_open > recovery_time` --> Content
- `app_open_duration > time_to_annoyance` --> Annoyed
- `app_open_duration > time_to_annoyance + annoyance_escalation` --> Sad
- Default (app just opened): Content

**Tier 2 mood logic (full fidelity):**
- `total_screen_off_time > ecstatic_threshold` --> Ecstatic
- `total_screen_off_time > 15 min` --> Happy
- `total_screen_off_time > recovery_time` --> Content
- `total_screen_on_time (non-FocusPal) > time_to_annoyance` --> Annoyed
- `total_screen_on_time (non-FocusPal) > time_to_annoyance + annoyance_escalation` --> Sad
- FocusPal foreground time: excluded from "screen on" calculation (using the app to check on Chibi should not count as "phone use")

### 5.5 Interaction Window (D-027)

When the user taps the Chibi on the HomeScreen, a brief interaction session begins:

| Time in Session | Chibi Behaviour | User Action |
|----------------|-----------------|-------------|
| 0-30s | Happy response: hearts, jumping, following finger | Tap, pet, play |
| 30-45s | First tire cue: gentle yawn, slower movements | User may continue or leave |
| 45-60s | Second tire cue: waves, sits down, speech bubble with book/food emoji | Clear signal to wrap up |
| 60s+ | Chibi settles into an activity, stops responding to taps | Interaction over |
| 120s+ | If user continues tapping: mild annoyance, huff animation | Affects mood slightly |

**Customisation exception:** If the user swipes up to access the cosmetic drawer (Phase 2), the interaction timer pauses. The Chibi is patient during customisation -- trying on hats, changing accessories. But after 2-3 minutes even in customisation, the Chibi will nudge toward focus: speech bubble showing a clock emoji, gentle tapping of foot.

### 5.6 Sleepy Mode (D-026)

**Activation:** At the configured bedtime (default 22:00), Chibi transitions to Sleepy state:
- Yawning animation (3 yawns over 30 seconds)
- Walks to bed area of environment
- Lies down, breathing animation, zzz particles float up
- Mood indicator changes to sleeping emoji
- Environment transitions to night scene (stars, warm interior glow)

**Freeze mechanic:** During Sleepy mode, the mood state machine is FROZEN. No mood changes occur regardless of phone usage. This prevents unfair overnight degradation (D-026: "moods and environment do NOT change during Sleepy mode").

**Night interruption banking:** If the user opens FocusPal during Sleepy mode:
- Chibi stirs, opens one eye, grumbles (but does NOT wake up fully)
- The interruption is LOGGED but does not change current mood
- Interruptions are accumulated as a "night disturbance count"

**Morning mood inheritance:** At the configured wake time (default 07:00):
- Chibi waking animation: stretches, sits up, rubs eyes, stands
- Starting mood is calculated from the pre-sleep mood adjusted by night disturbances:

| Night Disturbances | Morning Mood Adjustment |
|-------------------|------------------------|
| 0 interruptions | Start at pre-sleep mood (or one level UP if pre-sleep was Content or higher) |
| 1-2 interruptions | Start at pre-sleep mood (no change) |
| 3-5 interruptions | Start one level BELOW pre-sleep mood |
| 6+ interruptions | Start at Annoyed (floor -- never starts at Sad from sleep interruptions alone) |

**Morning recovery bonus:** The first 5 minutes of phone-down time after wake-up counts as double recovery time. This rewards the user for not immediately reaching for their phone (IRIS Supplement S6: "the first 5 minutes of phone-down time after wake-up rapidly improves mood").

### 5.7 D-022 + D-026 Interaction (ATLAS Non-Blocking Item #1)

**Question:** What happens when Tier 2 shows phone usage during the sleep window?

**Answer:** The sleep window freeze applies equally to both tiers. Tier 2 provides more accurate data about what the user does during the sleep window, but the design response is identical:

- During sleep window: mood is frozen. Tier 2 data about phone usage is accumulated as "night disturbance data" but does not trigger mood transitions.
- At wake time: the accumulated Tier 2 data from the sleep window feeds into the morning mood inheritance calculation. With Tier 2, the disturbance count is more accurate (it counts actual screen-on events, not just FocusPal opens), making the morning mood adjustment fairer.
- Rationale: the sleep window is sacred. Punishing the user for phone usage at night would undermine the Sleepy mode's core purpose (giving permission to disengage). The consequence is deferred to morning, which is honest ("your night habits affect your morning") without being real-time punishing.

---

## 6. Environment State System

### 6.1 Three Environment States

| State | Visual Description | Trigger |
|-------|-------------------|---------|
| Bright | Vibrant colours, flowers/plants visible, sparkle particles, sun rays. Chibi's home is tidy, warm, inviting. | Sustained positive mood (Happy/Ecstatic for 60+ cumulative min in 24hr) |
| Normal | Default colours, neutral atmosphere. Clean but not sparkling. Standard environment as designed. | Default state. Neither sustained negative nor sustained positive. |
| Dim | Muted/desaturated colours, slight grey overlay, no sparkles, overcast sky. Interior looks cluttered (overlaid clutter sprites). Not dark or scary -- just "tired." | Sustained negative mood (Annoyed for 30+ cumulative min in 24hr) |

**Storm state (extreme, rare):** If the Chibi reaches Sad state for 60+ cumulative minutes in a 24-hour rolling window, the environment enters a subtle rain/overcast state. Light rain particles, darker sky. This is the maximum degradation -- never destructive, never frightening. The Chibi looks cold but not harmed.

### 6.2 Degradation and Recovery Thresholds (D-023, IRIS Supplement S3)

All thresholds use a **24-hour rolling window** of cumulative mood time.

| Transition | Threshold | Notes |
|------------|-----------|-------|
| Normal --> Dim | 30+ min cumulative in Annoyed state (24hr rolling) | Brief annoyance spells are normal. 30 min cumulative suggests a pattern. |
| Dim --> Storm | 60+ min cumulative in Sad state (24hr rolling) | Only after sustained sadness. Users must really ignore the signals to reach this. |
| Dim --> Normal (recovery) | 30+ min cumulative in Content or higher (24hr rolling) | Recovery is same speed as degradation for fairness. |
| Storm --> Bright (full recovery) | 60+ min cumulative in Happy or Ecstatic | Full recovery requires earning it through sustained positive behaviour. |
| Any --> Bright | Sustained Happy/Ecstatic for 60+ cumulative min | Bright is a reward state, not the default. |

**Progressive transitions (D-023):** Environment state changes are NOT binary switches. They crossfade over 30-60 seconds. Colours desaturate/saturate gradually. Clutter sprites fade in/out. This prevents jarring visual changes and creates the "lagging indicator" feel the product owner specified.

**Preset interaction (IRIS Supplement S3):** The environment degradation thresholds do NOT change with sensitivity presets. The environment reflects cumulative behaviour over 24 hours regardless of how sensitive the Chibi's mood is. Rationale: the environment is the "honest mirror" -- it shows sustained patterns, not moment-to-moment reactions. A user on "Relaxed" preset whose Chibi is rarely annoyed will rarely see environment degradation naturally.

### 6.3 Time-of-Day Visual Layers

The environment has two independent visual layers:

1. **Time-of-day layer:** Controls sky colour, lighting direction, indoor lamp glow. Changes automatically based on real-world time. Always active.
2. **Wellbeing layer:** Controls environment condition (brightness, clutter, particles). Changes based on cumulative mood data. Semi-independent from time-of-day.

The layers combine:
- Night + Bright = peaceful starry scene with warm glow
- Night + Dim = same night scene but cooler tones, no warm glow
- Day + Bright = vibrant, flowers, sparkles
- Day + Dim = overcast, muted, cluttered

### 6.4 Implementation Notes for FORGE

The environment is a stack of sprite layers, bottom to top:
1. Sky/background (time-of-day variant)
2. Exterior elements (trees, ground -- from Home Environment tileset)
3. Interior walls/floor (walls_floor.png)
4. House details (house_details.png)
5. Wellbeing overlay (clutter sprites for Dim, sparkle particles for Bright -- fade in/out)
6. Ambient animations (cat_animation, bird_fly_animation, smoke_animation, trees_animation -- from Home Environment assets)
7. Chibi sprite layer
8. UI overlay (mood indicator, speech bubbles, navigation)

Each layer has an opacity and colour-tint property that the EnvironmentState provider controls. Transitioning between states adjusts these properties over time using an AnimationController.

---

## 7. Adventure Mode Design

### 7.1 Adventure Flow

```
SELECT DURATION --> CHIBI GEARS UP --> ADVENTURE BEGINS --> TIMER COUNTS DOWN
     |                                                           |
     |         (user can peek at any time -- D-024)              |
     |                                                           |
     +--- PAUSE (non-punishing) <--- user leaves app             |
     |         |                                                  |
     |    RESUME later                                           |
     |                                                           v
     |                                              TIMER COMPLETE
     |                                                    |
     |                                              TREASURE FOUND
     |                                                    |
     |                                              REWARD REVEAL
     |                                                    |
     +----------------------------------------> RETURN HOME (Ecstatic)
```

### 7.2 Duration Options and Reward Scaling

| Duration | Reward Pool | Rarity Boost | Best For |
|----------|------------|-------------|----------|
| 25 min | Common + Uncommon | None (base rates) | Quick study session, Pomodoro |
| 45 min | Common + Uncommon + Rare eligible | +5% Uncommon chance | Extended focus block |
| 60 min | All tiers eligible | +10% Uncommon, +2% Rare | Deep work session |
| 90 min | All tiers eligible | +15% Uncommon, +5% Rare, Ultra-rare eligible | Marathon focus |

### 7.3 Reward Rarity Distribution (IRIS Supplement S4)

| Tier | Drop Rate (25 min) | Visual Indicator | Examples |
|------|-------------------|------------------|----------|
| Common | 70-80% | White/grey border | Basic hats, simple glasses, scarves |
| Uncommon | 15-20% | Green border | Patterned hats, coloured glasses, umbrellas |
| Rare | 3-5% (only 45 min+) | Blue border, sparkle | Themed sets (pirate hat, wizard hat), special accessories |
| Ultra-rare | ~1% (only 90 min) | Gold border, glow | Animated accessories (glowing crown, floating halo), unique items |

**Variable reward psychology (IRIS Supplement S4, Finding 2):** The rarity tiers create variable ratio reinforcement (Skinner, 1957). Every session yields something (Common floor prevents empty sessions), but the possibility of a Rare or Ultra-rare creates anticipation. The reward is revealed only after completion -- not previewed during the adventure.

### 7.4 Peek Mechanic (D-024)

When the user opens FocusPal during an active adventure:
- The Focus Timer screen shows the adventure in progress
- Chibi is animated walking through the adventure scene
- Progress ring shows time elapsed and remaining
- **No penalty.** The peek does not pause, cancel, or affect the adventure
- The peek auto-closes if the user navigates away (the adventure continues)
- Maximum peek duration: unlimited. The user can watch the entire adventure if they choose. The key design insight: watching the Chibi explore IS engagement with the app that does not involve other screen-time activities. It is benign.

### 7.5 Pause Mechanic (D-024)

If the user needs to leave mid-adventure (Tier 1 behaviour, or explicit pause):

```
+------------------------------------------+
|                                          |
|     [Chibi sprite, looking back          |
|      over shoulder]                      |
|                                          |
|     Pause your adventure?                |
|                                          |
|     Your treasure will wait for you.     |
|     You can come back anytime.           |
|                                          |
|     [  Keep going  ]  [  Pause  ]        |
|                                          |
+------------------------------------------+
```

- **Pause:** Adventure timer stops. State is saved. Chibi in adventure scene sits down and waits (idle animation). When user returns: "Ready to continue? [Resume] [Start fresh]"
- **Keep going:** Dismiss the dialog, adventure continues.
- **Never punished (D-024, D-037):** A paused adventure can be resumed any time during the same day. At sleep time activation, incomplete adventures reset -- framed as "your Chibi fell asleep mid-adventure" (relatable, not punishing). No mood penalty. The anti-Forest principle holds within the daily window: no guilt, only a fresh start tomorrow.

### 7.6 Cosmetic Reward UI

After adventure completion:
1. **Treasure chest animation:** Chest appears centre screen. Chibi runs to it excitedly.
2. **Open sequence:** User taps chest (or it opens automatically after 2s). Lid flips open, light burst, item rises from chest with rarity-appropriate particle effects.
3. **Reveal card:** Item displayed on a card with:
   - Item image (cosmetic rendered on the Chibi)
   - Item name
   - Rarity tier label + colour-coded border
   - "NEW" badge if first time found
4. **Dismiss:** Tap anywhere or "Wear it!" button --> returns to Home with Chibi wearing the item.
5. **Collection storage:** All earned cosmetics stored in a local database, accessible from the customisation drawer (swipe up on Chibi).

---

## 8. Tier 2 Permission UX

### 8.1 Complete Permission Flow

```
ONBOARDING: Hatch --> Name --> Presets --> TIER 2 NUDGE --> Home
                                              |
                                         [Enable]    [Skip]
                                              |            |
                                    System Settings    Home (Tier 1)
                                              |
                                         [User grants]  [User doesn't]
                                              |               |
                                    Home (Tier 2, celebrate)  Home (Tier 1)
```

### 8.2 Post-Onboarding Reminders

The Tier 2 prompt appears ONCE during onboarding (D-030). After that, the app does NOT nag. Instead:

1. **Settings screen:** Persistent toggle with one-tap path to system settings. Always visible, never hidden.
2. **Stats screen:** If Tier 1, a gentle informational banner: "Your stats show app sessions only. Enable screen time access for your full picture."
3. **Locked features (Phase 2):** When evolution or skill learning would trigger but Tier 2 is not enabled: "To unlock [feature], [Chibi name] needs to understand your screen time. [Enable] [Not now]." This appears in-context at the moment the user would benefit -- not as a random popup.

### 8.3 iOS Entitlement Contingency (ATLAS Non-Blocking Item #2)

**Risk:** Apple may deny the `com.apple.developer.family-controls` entitlement needed for the Screen Time API.

**Contingency design:**
- If entitlement is denied, iOS users operate at Tier 1 only.
- The Tier 2 nudge screen is suppressed on iOS builds without the entitlement.
- iOS users receive a modified Stats screen that explains: "On iPhone, [Chibi name] watches this app. For the most accurate experience, try FocusPal on Android."
- No features are permanently locked on iOS -- evolution and skill learning unlock based on active focus session completion (alternative progression path using verified in-app timer data, not device-wide usage).
- This is a known platform asymmetry acknowledged in IRIS Supplement S2.4.

### 8.4 Tier 2 Permission Revocation

If a user grants UsageStats/Screen Time permission and later revokes it via system Settings:
- App detects the revocation on next foreground event (permission check).
- Falls back to Tier 1 silently. No error screen, no popup.
- Next app open: a gentle, dismissible banner on the HomeScreen: "Screen time access was turned off. [Chibi name] is using app-level tracking now. [Re-enable] [Dismiss]."
- Locked features (evolution, skills) re-lock. Progress is preserved but paused -- no loss.
- The Settings screen toggle updates to reflect the current state.

### 8.5 Messaging Principles

All Tier 2 messaging follows these rules:
- **Never guilt:** "You haven't enabled..." is banned. Use "When you're ready..." instead.
- **Always benefit-first:** Lead with what the user gains, not what they're missing.
- **Always private:** Every mention of screen time access includes "stays on this phone" or "never leaves your device."
- **Always skippable:** Every prompt has a clear, guilt-free dismiss option.
- **The Chibi delivers:** Permission prompts come from the Chibi (via speech bubbles and screen context), not from system dialogs or corporate-sounding notifications.

---

## 9. Animation & Sprite Specs

### 9.1 Character-Agnostic Animation Interface

Every Chibi type (Cat, Penguin, Panda — and future species like Bear, Bunny, Doggo, etc.) implements the same `ChibiAnimationSet` interface. FORGE builds the renderer once; swapping sprite folders produces a new character with zero code changes. 15 species are available in `Sprites/Chibi Repository/`.

```
ChibiAnimationSet {
  idle: SpriteSequence           // Default standing/breathing
  idle_blink: SpriteSequence     // Idle with periodic blinking
  walking: SpriteSequence        // Moving around environment
  running: SpriteSequence        // Faster movement (adventure)
  sleeping: SpriteSequence       // Lying down, breathing, zzz
  celebrating: SpriteSequence    // Jumping, dancing (Ecstatic)
  annoyed: SpriteSequence        // Crossed arms, huffing
  sad: SpriteSequence            // Sitting, droopy posture
  cooking: SpriteSequence        // Preparing food (Happy activity)
  reading: SpriteSequence        // Reading a book (Happy activity)
  playing_music: SpriteSequence  // Playing instrument (Happy activity)
  hatching: SpriteSequence       // Emerging from egg
  waking_up: SpriteSequence      // Morning stretch sequence
  yawning: SpriteSequence        // Tired cue
  waving: SpriteSequence         // Greeting / farewell
  heart_react: SpriteSequence    // Response to user interaction
}

SpriteSequence {
  frames: List<String>           // Ordered file paths
  frame_rate: int                // Frames per second
  loop: bool                     // Whether to loop or play once
  transition_curve: Curve        // easeIn, easeOut, linear
}
```

### 9.2 Real Chibi Sprite Mapping (D-034)

Each starter species has its own sprite pack from craftpix.net with distinct animations. No placeholder or colour tinting needed — each species looks and animates differently.

**Available animations per species (Cat, Penguin, Panda):**
Each species folder contains animations: Idle (20 frames), Walk, Jump, Roll, Fly, Hit, Dead, Stuned, Throwing

**Mapping to required ChibiAnimationSet interface:**

| Required Animation | Sprite Animation | FPS | Loop | Notes |
|-------------------|-----------------|-----|------|-------|
| idle | Idle | 8 | Yes | Direct map (20 frames — rich, smooth idle) |
| walking | Walk | 10 | Yes | Direct map |
| sleeping | Idle (slowed) | 3 | Yes | Use Idle at reduced FPS. Overlay: zzz particles. |
| celebrating | Jump + Roll | 10 | Yes (3x then stop) | Combine for celebration sequence. Overlay: sparkle particles. |
| annoyed | Hit | 6 | No (hold last frame) | Recoil animation reads as annoyed |
| sad | Stuned | 4 | No (hold last frame) | Stunned animation reads as dejected |
| cooking | Walk (stationary) | 8 | Yes | Overlay: cooking pot speech bubble 🍳 |
| reading | Idle | 6 | Yes | Overlay: book speech bubble 📖 |
| playing_music | Idle | 6 | Yes | Overlay: music note speech bubble 🎵 |
| hatching | Jump | 10 | No (play once) | Chibi springs out of egg crack sequence |
| waking_up | Jump | 6 | No (play once) | Quick stretch/stand-up |
| yawning | Idle (slowed) | 4 | No (play once) | Slow idle reads as yawn. Overlay: 🥱 speech bubble |
| waving | Throwing (first half) | 8 | No (play once) | Arm raise reads as wave. Overlay: 👋 speech bubble |
| heart_react | Jump | 10 | No (play once) | Excited jump. Overlay: heart particles |
| adventuring | Walk or Fly | 10 | Yes | Context-dependent — Walk for ground, Fly for air adventures |
| cleaning | Walk (around scene) | 8 | Yes | Chibi moves through environment tidying up |

**Spine animation support:** All three species include Spine skeletal animation data (`Spine/` and `Json Atlas/` folders). FORGE may use Spine for smoother animations if preferred over frame-by-frame PNG sequences. Both approaches work with the character-agnostic interface.

**Sprite asset paths:**
- Cat: `Sprites/Chibi Repository/Cat/craftpix-net-532103-cute-cats-game-character-sprites/Png/Character01/`
- Penguin: `Sprites/Chibi Repository/Penguin/craftpix-net-145571-cartoon-penguins-game-character-sprites-pack/Png/Character01/`
- Panda: `Sprites/Chibi Repository/Panda/craftpix-net-634797-cute-panda-game-person-sprites/Png/Character01/`

**Character variants:** Each species has 15 character variants (Character01 through Character15 — different colours/styles). Phase 1 uses Character01 for each. Variants can serve as cosmetic unlocks or premium options in Phase 2+.

### 9.3 Egg Sprites

48 dragon egg vector icons available at `Sprites/Eggs/craftpix-net-509791-dragon-egg-loot-vector-icons/PNG/without_shadow/`.

| Species | Egg Assignment | Notes |
|---------|---------------|-------|
| Cat | Egg 1 (warm-coloured egg) | FORGE selects a visually fitting egg from the 48 variants |
| Penguin | Egg 2 (cool-coloured egg) | Each egg should feel distinct and match the species personality |
| Panda | Egg 3 (neutral/earth-toned egg) | Remaining eggs available for Phase 2+ species |

The egg is displayed on the Hatching screen (Section 3.3). The user holds to warm it, cracks appear as overlays, and the species-specific Chibi emerges using the Jump animation.

### 9.4 Phase 2+ Species Expansion

12 additional species already available in `Sprites/Chibi Repository/` — no additional asset purchases needed:
Bear, Beaver, Bunny, Capybara, Chick, Doggo, Duckling, Koala, Mushroom, Pig, Raccoon, Red Panda

Each has the same folder structure (15 variants, 9 animations, Spine data). Adding a new species requires only:
1. Copy sprite folder into the app's asset directory
2. Register the species in the Chibi data model
3. Assign an egg from the remaining 45 egg variants
4. No code changes to the renderer or animation system

### 9.4 Frame Rates and Timing

| Context | Base FPS | Notes |
|---------|---------|-------|
| Idle animations | 6-8 | Slow, calm, breathing feel |
| Active animations (walking, cooking) | 8-10 | Moderate energy |
| Energetic animations (running, celebrating) | 10-12 | High energy, lively |
| Sleepy animations | 3-4 | Very slow, peaceful |
| Transition animations (mood change) | 10 | Smooth transitions |

### 9.4 Transition Curves

| Transition Type | Curve | Duration |
|----------------|-------|----------|
| Mood state change | easeInOut | 500ms crossfade between animation sets |
| Speech bubble appear | easeOut (spring) | 300ms scale from 0 to 1 |
| Speech bubble disappear | easeIn | 200ms fade to 0 |
| Environment state change | linear | 30-60 seconds (very slow crossfade) |
| Time-of-day transition | linear | 30 minutes (imperceptible per-frame change) |
| Chibi movement (walking to position) | easeInOut | Variable based on distance |

### 9.5 Required Particle Systems

| Particle | Usage | Specs |
|---------|-------|-------|
| Hearts | User interaction, Happy state | 3-5 particles, float upward, fade over 1s |
| Sparkles | Ecstatic state, Bright environment | 5-8 particles, random positions, twinkle (opacity oscillation) |
| ZZZ | Sleeping | 1 particle at a time, float upward, loop |
| Huff cloud | Annoyed state | 2-3 small clouds, puff outward, fade over 0.5s |
| Rain drops | Storm environment state | 20-30 particles, fall from top, semi-transparent |
| Confetti | Celebration (hatching, Tier 2 enable, adventure complete) | 15-20 particles, burst from centre, gravity fall, multi-coloured |
| Warm glow | Hatching egg | Radial gradient, centre at touch point, orange/amber |

---

## 10. Focus Timer Design

### 10.1 Passive Mode (Always-On)

**How it works:** The app runs a background service (or periodic work manager task) that tracks the Chibi's mood based on usage patterns. No user action is required.

**Tier 1 passive logic:**
- App lifecycle events (onResume, onPause) are the primary signal.
- When the app goes to background (onPause): a timestamp is saved.
- When the app returns to foreground (onResume): elapsed time since last onPause determines mood direction.
- If the app is never opened, no mood change occurs (Tier 1 limitation).

**Tier 2 passive logic:**
- A periodic WorkManager task (every 60 seconds when the app is in background) queries UsageStatsManager for device-wide foreground app time.
- Total screen-on time (excluding FocusPal) feeds the mood state machine.
- This runs silently. No notifications. No UI unless the user opens the app.

**Passive mode drives the cozy home activities:**
- Phone idle for 5+ min: Chibi starts pottering (walking around, looking at things)
- Phone idle for 15+ min: Chibi starts an activity (cooking, reading, music)
- Phone idle for 30+ min: Activity is "in full swing" (bigger speech bubbles, more animated)
- Phone idle for 60+ min: Chibi reaches Ecstatic (celebrating, sparkles)

### 10.2 Active Mode (User-Initiated Adventures)

**How it works:** User explicitly starts a focus session from the Focus Timer tab (Section 4.2). This triggers adventure mode.

**Timer behaviour:**
- Countdown timer runs in the foreground if the app is open.
- If the app is backgrounded:
  - Tier 1: Timer pauses. A notification shows: "[Chibi name] is waiting for you to continue the adventure."
  - Tier 2: Timer continues IF the phone screen is off (phone in pocket/on desk = genuine focus). Timer pauses if another app is in foreground for >2 min.
- Timer completion triggers the treasure reveal sequence.

**Preset switching during sessions:** Not allowed. The preset affects passive mood mechanics but does not change active session durations. This prevents gaming (switching to Relaxed mid-session).

### 10.3 Session UI States

| State | Timer Display | Chibi | Actions Available |
|-------|--------------|-------|-------------------|
| Pre-session | Duration selector + Start button | Excited, adventuring gear | Select duration, Start |
| Active (app open) | Countdown + progress ring | Walking through adventure scene | Peek (view progress), Pause |
| Active (app background, Tier 2) | Notification: "Adventure in progress" | Continues walking (not visible) | Peek (open app) |
| Paused | "Paused at XX:XX" | Sitting, waiting | Resume, Abandon |
| Complete | "Adventure complete!" | Ecstatic, treasure chest | Reveal reward, Return home |

---

## 11. Interaction Patterns

### 11.1 Core Tap Responses

| User Action | Chibi Response | Timing | Mood Effect |
|-------------|---------------|--------|-------------|
| Single tap on Chibi | Looks up, blinks, small bounce | Immediate | None |
| Double tap on Chibi | Jumps, hearts appear | Immediate | Starts interaction window (D-027) |
| Hold on Chibi | Chibi purrs (vibration feedback), leans into touch | 500ms to trigger | Interaction window |
| Tap during sleep | Stirs, opens one eye, grumbles | 1s delay | Logs night interruption |
| Tap during adventure (Home screen) | Cannot -- Chibi is away on adventure | N/A | N/A |
| Tap on speech bubble | Bubble pops with a small particle effect | Immediate | None |

### 11.2 Play Session Flow (D-027)

1. **Enter:** User double-taps or holds Chibi. Interaction window begins (30-60s).
2. **Play:** Chibi follows finger position (subtle tracking, not exact). Taps trigger happy reactions (jumping, spinning, hearts). Each tap response is slightly different (variable reward micro-pattern).
3. **Tire cue 1 (30s):** Chibi yawns. Still responsive but slower. Speech bubble: sleepy face.
4. **Tire cue 2 (45s):** Chibi waves. Sits down. Speech bubble: book/food emoji (wants to do its own thing).
5. **Settle (60s):** Chibi starts an activity. Stops responding to taps. Wave animation if tapped (acknowledges user but does not engage).
6. **Overstay (120s+):** Gentle annoyance if user keeps tapping. Huff animation. This is the "phone use" signal applied to in-app behaviour -- even interacting with the Chibi too long is noticed.

### 11.3 Customisation Time (Phase 2)

When the user accesses the cosmetic drawer:
- Interaction timer pauses (customisation is allowed to take longer -- D-027)
- Chibi poses for cosmetic try-on (stands still, turns when item is applied)
- After 2-3 minutes: Chibi taps foot, speech bubble with clock emoji
- After 5 minutes: Chibi sits down and starts an activity (gentle dismissal)

### 11.4 Transition to Focus

When the user puts the phone down (app goes to background):
- If during interaction window: Chibi waves goodbye, then starts an activity
- If during customisation: Chibi puts on the last selected item, waves, starts activity
- The farewell is always positive. Chibi never looks sad when the user leaves -- it looks happy to start its own activities. This is the "positive disengagement" pattern (IRIS Supplement S7, Finding 4).

---

## 12. Collection System Architecture

### 12.1 Phase 1: Single Chibi, Extensible Model

**What ships in Phase 1:**
- One active Chibi. Selected during onboarding from 3 starters (Cat, Penguin, Panda — each with distinct sprites).
- Cosmetic rewards earned from adventures, stored in local database.
- Cosmetic drawer accessible from HomeScreen (swipe up on Chibi).
- Data model supports multiple Chibis from Day 1 (architecture ready, UI not).

**Phase 1 data model:**

```
ChibiRecord {
  id: String (UUID)
  species: String ("cat", "penguin", "panda")
  name: String
  created_at: DateTime
  is_active: bool (always true in Phase 1)
  is_starter: bool
  mood_state: String (current mood)
  mood_history: List<MoodEntry> (timestamped mood changes)
  cosmetics_owned: List<String> (cosmetic IDs)
  cosmetics_equipped: List<String> (currently worn items)
  evolution_stage: int (always 0 in Phase 1)
  skills: Map<String, int> (empty in Phase 1)
  total_focus_time: int (cumulative minutes)
  adventures_completed: int
  shelved_at: DateTime? (null in Phase 1)
}

CosmeticItem {
  id: String
  name: String
  rarity: String ("common", "uncommon", "rare", "ultra-rare")
  category: String ("hat", "glasses", "accessory")
  sprite_path: String
  earned_at: DateTime
  earned_from: String ("adventure_25", "adventure_45", etc.)
}
```

### 12.2 Phase 2: Multi-Chibi Collection

**Shelving UX:**
- Collection screen accessible from a new tab or HomeScreen menu
- Active Chibi prominently displayed. Shelved Chibis shown in a row below.
- Tap a shelved Chibi --> "Reunite with [name]? [Yes!] [Not now]"
- Reunion animation: shelved Chibi runs toward camera, jumps, hearts explode, speech bubble with excited emojis
- Shelving the current Chibi: "Let [name] rest? They'll be right here when you come back." Chibi waves, walks to a cozy shelf spot, curls up (not sad -- content, resting).

**Joyful reunion scaling (IRIS Supplement S9, Finding 3):**

| Shelving Duration | Reunion Animation |
|------------------|-------------------|
| <1 day | Simple wave and smile |
| 1-7 days | Running toward user, jumping |
| 1-4 weeks | Ecstatic running, confetti, extended celebration |
| 1+ month | Full celebration sequence, unique "I missed you!" speech bubble with multiple heart emojis |

**Starter badge:** The first Chibi hatched is permanently marked with a star badge in the collection screen (IRIS Supplement S9, Finding 2: "the first creature retains a privileged status").

### 12.3 Phase 3: Premium Expansion

- Premium Chibi types (Dragon, Unicorn) available for one-time purchase
- Each premium type has unique idle animations and activity variants (not just a reskin)
- Environment themes tied to species (bamboo forest for Panda, ice cave for Penguin)
- No "your Chibi wants a friend" messaging for premium promotion (IRIS Section 11.1: emotional manipulation for monetisation is prohibited)
- Premium promotion is display-only: a "Chibi Shop" section in the collection screen showing locked premium types with their unique features listed

---

## 13. Anti-Gaming Mechanics

### 13.1 48-Hour Inactivity Pause (D-028/D-032)

**Trigger:** If the phone shows zero app interaction with FocusPal AND (if Tier 2) zero screen unlocks for 48 consecutive hours.

**Effect:** Chibi evolution and skill progress are silently paused. No notification is sent. No UI change is visible until the user returns.

**When user returns after 48hr+ absence:**
- Chibi wakes up (if Sleepy) or looks up (if any other state)
- Speech bubble: question mark emoji, then wave
- Mood resets to Content (neutral -- no punishment for being away, no reward for unintentional absence)
- A subtle message in the Stats screen: "Welcome back! Your progress resumes now."
- Evolution and skill progress resume immediately

**What this prevents:**
- Lost/stolen phone accumulating fake progress
- Forgotten Chibi in a drawer earning undeserved rewards
- "Set it and forget it" gaming (leave phone unused to farm Ecstatic time)

**What this does NOT do:**
- It does NOT send notifications ("We miss you!")
- It does NOT degrade the environment or mood
- It does NOT reset any progress already earned
- It does NOT trigger any guilt or urgency mechanics

**Phase designation (ATLAS Non-Blocking Item #3):** The heartbeat check from D-028 is Phase 2 scope. The 48hr pause from D-032 is the Phase 1 implementation of anti-gaming. FORGE should implement D-032 in Phase 1.

### 13.2 Single-Device Binding (D-033)

**Phase 1:** Not enforced (no cloud sync, no accounts). The Chibi lives on one device by virtue of local-only storage.

**Phase 2 (when cloud sync is added):**
- Chibi account linked to Google Account or Apple ID
- One active device per account
- If the user signs in on a new device: "Move [Chibi name] to this device? They can only live on one device at a time." The old device becomes deactivated.
- This prevents gaming via multiple phones (one "resting" while the other is used)

### 13.3 Adventure Validation

- Adventures require the user to START the session (tap the Start button). Cannot be automated.
- Tier 2: adventures only count if screen-off time matches the timer duration (phone was genuinely idle during the adventure, not just FocusPal backgrounded while scrolling).
- Tier 1: adventures pause when the app is backgrounded (cannot game by switching apps).

---

## 14. Ethical Design Guardrails

### 14.1 The Manipulation Line

Every design pattern in FocusPal is evaluated against this framework (IRIS Section 11.1):

| Criterion | Persuasion (Acceptable) | Manipulation (Not Acceptable) |
|-----------|------------------------|------------------------------|
| Transparency | User understands why Chibi is in this mood | User feels bad but doesn't know why |
| User control | User can adjust sensitivity, skip prompts, disable features | User is locked into settings, cannot opt out |
| Reversibility | Every state can be recovered from | Permanent loss, irreversible damage |
| Emotional framing | "Your Chibi is happy because you focused" | "Your Chibi is suffering because you failed" |
| Monetisation | "This Chibi type has unique animations" | "Your Chibi is lonely -- buy them a friend" |

### 14.2 Non-Punishing Philosophy (Applied)

| Design Element | Punishing Version (REJECTED) | FocusPal Version |
|---------------|------------------------------|------------------|
| Adventure interruption | Session cancelled, progress lost (Forest's dead tree) | Adventure paused, progress saved, resume anytime (D-024) |
| Skill learning interruption | Progress bar resets | Progress bar pauses (Phase 2) |
| Dream interruption | Dream pops, never returns (Idea Bank suggestion) | Dream pauses, can be resumed (IRIS Section 11.1 recommendation) |
| Night phone use | Immediate mood degradation | Banked, applied as morning mood adjustment (D-026) |
| 48hr absence | Environment destroyed, Chibi sick | Silent pause, neutral restart (D-032) |
| Shelving a Chibi | Chibi cries, guilt trip | Chibi rests contentedly, joyful reunion later (D-029) |

### 14.3 Accessibility Considerations

| Area | Current Design | Accessibility Note |
|------|---------------|-------------------|
| Emoji communication | Chibi speaks via emoji only | Screen readers need alt-text for all emoji. Phase 2: add accessibility labels. Phase 1: ensure all emoji are standard Unicode with platform-level accessibility. |
| Environment states | Bright/Normal/Dim visual differences | Use brightness AND contrast changes, not colour alone (colour-blind users). Dim state uses desaturation + reduced brightness, not colour shift. |
| Hatching hold gesture | Hold finger to warm egg | Alternative: provide a "tap repeatedly" option for users who cannot sustain a hold. Progress fills per tap instead of per second. |
| Mood indicator | Small emoji in top-right | Tappable to show text explanation. Ensure touch target is at least 48x48dp (Android accessibility guidelines). |
| Speech bubbles | Small floating elements | Ensure minimum font size, high-contrast background. |
| Timer | Visual progress ring | Add a text time readout alongside the ring. Announce time remaining for screen readers. |

### 14.4 Data Ethics (Phase 1)

- All data local. Nothing leaves the device.
- Tier 2 usage data (UsageStats) processed locally only. Never synced, even in Phase 2.
- No analytics, no crash reporting, no third-party SDKs in Phase 1.
- If analytics are added in Phase 2: anonymised, aggregated, opt-in only. Never individual usage patterns.

---

## 15. Phase 2 & 3 Design Notes

### 15.1 Phase 2: Designed, Not Built

| Feature | Design Status | Key Design Decisions |
|---------|--------------|---------------------|
| Evolution system | Concept: Chibi evolves visually after sustained positive behaviour milestones. Requires Tier 2 (accurate data). 3 evolution stages per species. | Evolution is visible transformation (size, detail, accessories), not replacement. The user's Chibi grows -- it does not become a different creature. |
| Skill learning | Concept: Chibi learns skills (cooking, music, art) with visible progress bars. Each skill requires uninterrupted focus blocks. | Progress bars pause on interruption, never reset (Section 14.2). Each skill has 3 mastery levels. Mastered skills become part of the Chibi's idle activity rotation. |
| Collection screen | Full shelving/reunion UX. Collection gallery showing all owned Chibis with stats. | See Section 12.2. |
| Cloud sync | Anonymous auth via Google/Apple. Chibi state synced. Usage data stays local. | Requires DPIA before development. Sync conflict resolution: latest-write-wins for state, merge for cosmetics. |
| Premium Chibi store | Storefront with premium species. One-time purchase per Chibi (1.99-3.99). | No emotional manipulation in store design. No "limited time" pressure. No "your Chibi wants..." messaging. |
| Environment customisation | Place furniture, activity stations. Chibi uses placed items. | Builder mode accessible from HomeScreen long-press. Grid-based placement. Items earned through milestones + purchased. |
| Riverpod migration | Replace Provider + ChangeNotifier with Riverpod | Pure technical migration. No UX change. Better testability. |

### 15.2 Phase 3: Envisioned, Not Designed

| Feature | Concept |
|---------|---------|
| Mini-games | Rock-paper-scissors, tic-tac-toe with Chibi. Brief (30s-1min) interactions. Purchasable game packs. |
| Social sharing | Display-only collection sharing (screenshot/link). No leaderboards. No competitive features (IRIS Supplement S1: social comparison undermines wellbeing goals). |
| Wellness score | Composite score based on focus trends. Shareable. Framed as celebration, not surveillance. |
| Adaptive thresholds | System learns user's patterns and suggests optimal presets. Crosses into AI territory -- requires EU AI Act transparency review (IRIS Section 10.2). |
| Multiple active Chibis | 2+ Chibis active simultaneously. Requires significant mood engine rework. |

### 15.3 Platform Parity Notes

| Feature | Android | iOS | Notes |
|---------|---------|-----|-------|
| Tier 2 detection | UsageStatsManager -- full app-level data | Screen Time API -- category-level data, opaque tokens | iOS will always be less accurate. Design for this asymmetry. |
| Permission UX | Settings > Apps > Special access > Usage access | Settings > Screen Time > [FocusPal toggle] | Both require navigation to system Settings. Deep links available on both platforms. |
| Background work | WorkManager (reliable) | BGTaskScheduler (less reliable, iOS throttles aggressively) | Passive mood updates may be less frequent on iOS. |
| Notifications | Full control | Requires notification permission prompt (iOS 16+) | Phase 1: no notifications. Phase 2: minimal, opt-in. |

---

## Design Traceability Matrix

Every major design decision traces to a research finding or user directive:

| Design Element | Decision Reference | Research Basis |
|---------------|-------------------|---------------|
| Onboarding as emotional ceremony | D-011, IRIS S12 P1 | SDT relatedness, Hook Model investment |
| Three free starters | D-021 | IRIS S9.2 Finding 4, Goldilocks heuristic |
| Hold-to-warm hatching | D-011 | Physical participation creates investment (Hook Model) |
| Naming ceremony | D-011, IRIS S12 P1 | SDT relatedness, Finch validation |
| Two-tier detection | D-022, D-031 | IRIS Supplement S2 (revised recommendation) |
| Tier 2 nudge after bonding | D-030 | Bond-first, trust-second sequence |
| Tier 1 mood-only restriction | D-031 | Honest: app literally cannot track without data |
| Six mood states | D-006, System Design S5 | Clear cause-and-effect, configurable sensitivity |
| Configurable sensitivity presets | D-025, IRIS S6 | SDT autonomy, <5% change defaults heuristic |
| Sleepy mode freeze | D-026 | IRIS Supplement S6, loss aversion mitigation |
| Morning mood inheritance | D-026 | Temporal continuity, morning reinforcement (Fogg) |
| 30-60s interaction window | D-027 | IRIS Supplement S7, mobile session length research |
| Tire cues (yawning, waving off) | D-027 | Positive framing of usage limit |
| Environment 3-state system | D-018, D-023 | Ambient information research, guilt-avoidance |
| Lagging environment degradation | D-023 | IRIS Supplement S3, threshold > immediate feedback |
| Adventure mode treasure hunts | D-024 | Hook Model variable reward, SDT autonomy (peek) |
| Non-punishing pause | D-024 | IRIS Supplement S4, anti-Forest philosophy |
| Cosmetic rarity tiers | D-024, IRIS S4 | Variable ratio reinforcement (Skinner) |
| 48hr inactivity pause | D-032 | Anti-gaming without UX contradiction |
| Single-device binding | D-033 | Anti-gaming, Phase 2 scope |
| Full-screen scene home | D-012 | Ambient display research (Stanford) |
| Emoji-only communication | System Design S4 | Universal legibility, simplicity |
| Collection architecture | D-021, D-029 | Pokemon/Neopets validation, primacy effect |
| Joyful reunion mechanic | D-029 | Attachment theory (Bowlby), IRIS S9 |
| No guilt in monetisation | IRIS S11.1, S9.4 | ICO Children's Code, ethical design |
| Privacy-by-design default | D-022, IRIS S7 | GDPR Art. 25, competitive advantage |
| Positive disengagement | D-027, IRIS S7 | Finch validation, prosocial design research |
| Age-range presets | D-025 | Clinical guidelines (AAP, AACAP, WHO) |
| Character-agnostic sprites | D-008 | System Design S9, zero-code character swaps |

---

## MoSCoW Prioritisation (Phase 1)

### Must Have (Ship is broken without these)

| # | Feature | Justification |
|---|---------|---------------|
| M1 | Onboarding flow (choose, hatch, name) | Core bond formation. Without this, there is no product. |
| M2 | Home screen with Chibi, mood, speech bubbles | The primary experience screen. |
| M3 | 6-state mood system with configurable sensitivity | Core feedback loop. |
| M4 | Passive mood tracking (Tier 1 at minimum) | The Chibi must respond to behaviour. |
| M5 | Active focus timer with countdown | Primary behaviour change lever. |
| M6 | Time-of-day awareness (Sleepy mode) | Completes the life cycle. |
| M7 | Preset selection (3 presets) | Onboarding step, autonomy. |
| M8 | Settings screen with threshold adjustment | User control. |
| M9 | Character-agnostic sprite system | Architecture requirement for future species. |
| M10 | Local data persistence (SharedPreferences + SQLite) | Data must survive app restart. |

### Should Have (Significant value, ship without if needed)

| # | Feature | Justification |
|---|---------|---------------|
| S1 | Tier 2 detection (UsageStats API) | D-022 rates this as critical for credibility. Should-have because Tier 1 is functional alone. |
| S2 | Environment states (Bright/Normal/Dim) | Ambient feedback. High impact, moderate complexity. |
| S3 | Adventure cosmetic rewards | Variable reward loop. High retention value. |
| S4 | Tier 2 nudge screen (onboarding) | Permission flow. Can function without it (Settings toggle suffices). |
| S5 | Sleepy mode freeze + morning inheritance | D-026. Adds fairness. Can default to continuous mood if cut. |
| S6 | Stats screen (basic) | Usage visibility. Validates behaviour change. |
| S7 | 48hr inactivity pause | D-032 anti-gaming. Edge case but important. |

### Could Have (Nice-to-have, defer without guilt)

| # | Feature | Justification |
|---|---------|---------------|
| C1 | Cosmetic drawer (equip items) | Personalisation. Can defer if adventure rewards are earned but not equippable yet. |
| C2 | Interaction window with tire cues | D-027. Enhances bond but Home screen works without it (Chibi reacts to taps without the full 60s window). |
| C3 | Age-range question in onboarding | D-025. Presets work without it (user manually selects). |
| C4 | Adventure peek mechanic | D-024. Timer works without peek (user just waits). |
| C5 | Storm environment state | Only affects extreme cases. Normal/Dim is sufficient for Phase 1. |
| C6 | Morning recovery bonus | D-026 refinement. Nice but not essential. |

### Won't Have (Phase 1 -- explicitly deferred)

| # | Feature | Phase |
|---|---------|-------|
| W1 | Evolution system | Phase 2 |
| W2 | Skill learning | Phase 2 |
| W3 | Multiple Chibis / shelving UI | Phase 2 |
| W4 | Cloud sync | Phase 2 |
| W5 | Premium Chibi store | Phase 3 |
| W6 | Mini-games | Phase 3 |
| W7 | Social sharing | Phase 3 |
| W8 | Environment customisation (builder) | Phase 3 |
| W9 | Adaptive thresholds (AI) | Phase 3 |
| W10 | Notifications | Phase 2 |

---

## Success Metrics

### Phase 1 (Prototype) Targets

| Metric | Target | Measurement Method | Why This Matters |
|--------|--------|-------------------|-----------------|
| Onboarding completion rate | >90% of users who start onboarding complete it (reach HomeScreen) | Count: SplashScreen --> HomeScreen vs. SplashScreen --> abandon | If onboarding fails, the bond never forms |
| First-day return rate | >60% of users who complete onboarding open the app again within 24 hours | Timestamp comparison: onboarding completion vs. next app open | The bond must survive the first day |
| Average session duration | 30-90 seconds (matching D-027 interaction window) | App lifecycle timestamps | Too short = no engagement. Too long = the app is contributing to screen time, not reducing it. |
| Active focus sessions per user per week | >3 | Session count in local DB | Users must use the primary behaviour change feature |
| Mood state distribution | Content or higher >60% of waking hours | Mood state timeline from local DB | If users are mostly Annoyed/Sad, the defaults are too strict or the app creates more stress than it resolves |
| Tier 2 opt-in rate | >20% of users (stretch: >40%) | Permission state check | Validates whether the nudge design is compelling enough |
| Preset change rate | <20% (validates defaults are good) | Settings change log | If >20% change presets, defaults need recalibration |

### Phase 2 Targets (Projected)

| Metric | Target |
|--------|--------|
| 7-day retention | >40% |
| 30-day retention | >20% |
| Evolution unlock rate | >30% of Tier 2 users |
| Collection engagement | >2 Chibis per active user |
| Premium conversion | >3% of active users purchase a premium Chibi |

---

---

## Addendum: Product Owner Design Refinements (2026-03-19, D-034 to D-037)

The following refinements were provided by the product owner after the initial design spec was approved. They update specific sections of this spec.

### AD0. UI Assets, Adventure Backgrounds, and Icons Added (2026-03-19)

The product owner added Menu/Game UI asset packs and adventure environment backgrounds. These provide ready-made UI components FORGE can use instead of building from scratch.

**Menu and Game Assets** (`Sprites/Menu and Game Assets/`):

| Pack | Key UI Elements for FocusPal | Best Use |
|------|------------------------------|----------|
| **Animals Game Assets** | Buttons (play, quit, spin, settings, shop, profile, scores), coin icons, checkmarks, progress boxes, confetti, pause icon, star ratings, shop UI (price boxes, boosters), popup frames (completed, failed, goal) | Home screen buttons, settings icons, adventure reward popups, stats screen elements |
| **Bubble Shooter Game Assets** | Coloured buttons (blue, green, red), play buttons (big/small), continue/cancel/replay buttons, star ratings (grey/yellow), coins counter, lives counter, profile button, shop button, level completed popup | Focus timer start/pause buttons, preset selection pills, adventure completion UI, reward stars |
| **Candies Game Assets** | Game clock icon, booster icons, map icons, profile/shop/scores icons, help bubble, play button, character expressions | Timer display, adventure map concept, help/onboarding tooltips |
| **Cooking Match Game Assets** | Clock icon, booster icons, map/profile/shop/scores/wheel icons, play button, character expressions (boy/girl variants) | Timer icons, navigation icons, shop UI concepts |

**How these fit the design spec:**
- **Buttons:** Replace the spec's text-based button descriptions with actual styled game buttons (rounded, coloured, with icons)
- **Preset selection pills (D-025):** The coloured pill buttons from Bubble Shooter (blue/green/red) map directly to Relaxed/Focus-Friendly/Super-Focused presets
- **Adventure duration pills (Section 7):** Same button style for 25/45/60/90 min selection
- **Timer display:** Clock icons from Candies/Cooking packs for the focus timer screen
- **Reward popups:** Level-completed/confetti assets for adventure reward reveal
- **Settings/Profile icons:** Ready-made icons for bottom navigation and settings screen
- **Star ratings:** Grey/yellow stars from Bubble Shooter for adventure completion rating or streak display
- **Coin icons:** Reusable as a "focus points" or reward currency visual if needed

**Adventure Environment** (`Sprites/Adventure Environment/`):
4 cartoon forest backgrounds with **parallax layers** (Sky, Ground, Middle_Decor, BG_Decor, Foreground). These provide:
- Rich, layered adventure scenes for focus timer active mode
- 4 different forest variants for adventure variety (variable reward — different scene each time)
- Parallax-ready layers for subtle animation (clouds drifting, foreground sway)
- Replaces the previously referenced `Outside Environment - Summer` tileset as the primary adventure backdrop

**FORGE should:**
- Browse all 4 packs and cherry-pick UI elements that fit FocusPal's visual style
- Use button/icon PNGs directly as Flutter `Image.asset` widgets
- Use the cartoon forest backgrounds as adventure mode scenes
- Maintain visual consistency — pick elements from 1-2 packs maximum to avoid style clashes
- Vector source files (AI/EPS) are available if resizing or recolouring is needed

---

### AD1. Real Chibi Sprites (D-034) — APPLIED

**Status:** Sections 9.2, 9.3, and all Skeleton placeholder references in the main spec have been updated inline. Real Cat, Penguin, and Panda sprites with distinct animations are now the Phase 1 sprites. Egg sprites (48 variants) are available for the hatching screen. See updated Sections 9.2, 9.3, and 9.4 for full details. Cosmetic items (hats, glasses) from the sprite packs are available for adventure rewards (D-024).

### AD2. Hatching Duration: Max 60 Seconds (D-035)

**Updates Section 3.3 (Hatching Screen) and Section 2.2 (Phase A table).**

- Total warmth progression: **max 60 seconds** (was 60-90s)
- Progress bar fills at ~1.67% per second of continuous hold
- Drain rate if finger lifted: ~1% per second (was 0.5%)
- All other hatching mechanics remain unchanged (wobble, crack stages, Chibi emergence)
- Product owner note: "UX polishing — calibrate to what feels best after user testing"

**Egg sprites available:** 48 dragon egg vector icons at `Sprites/Eggs/craftpix-net-509791-dragon-egg-loot-vector-icons/PNG/without_shadow/`. FORGE should assign 3 distinct egg designs to the 3 starter species (e.g., egg 1 = Cat, egg 2 = Penguin, egg 3 = Panda). Remaining eggs available for premium/Phase 2 species.

### AD3. Relaxed Preset: Hard-Coded Minimums (D-036)

**Updates Section 5.3 (Configurable Parameters) and Section 4.4 (Preset Selection Screen).**

The Relaxed preset parameters cannot be reduced below hard-coded minimums. Without these, users can effectively disable the focus mechanic.

| Parameter | Relaxed Value | Hard-Coded Minimum | Rationale |
|-----------|--------------|-------------------|-----------|
| Time-to-annoyance | 45 min | 30 min | Below 30 min, even casual phone use triggers annoyance — no focus benefit |
| Recovery time | 3 min | 2 min | Below 2 min, recovery is instant and consequence-free |
| Ecstatic threshold | 30 min | 20 min | Below 20 min, ecstatic state is trivially achievable |
| Annoyance escalation | 20 min | 10 min | Below 10 min, escalation from annoyed → sad takes too long to feel meaningful |

Product owner note: "Calibrate after user testing and feedback." These are starting minimums.

**UX impact:** When user tries to adjust a slider below the minimum, the slider stops and a tooltip appears: "This is the minimum for a meaningful focus experience." No guilt, just honest explanation.

### AD4. Adventure Daily Reset at Sleep Time (D-037)

**Updates Section 7 (Adventure Mode) — specifically the pause/resume mechanic.**

**Previous design:** Paused adventures never expire. Can be resumed days later.

**Updated design:**
- Adventure timers reset when **sleep time activates** each day (the daily boundary)
- Users can un-pause and continue their adventure any time during the day before sleep time
- At sleep time activation: any incomplete/paused adventure resets. Progress and potential rewards for that adventure are lost.
- Next day: user starts a fresh adventure

**Rationale:** Without daily reset, users exploit the system:
1. Start only 90-minute adventures (highest rarity tier)
2. Never complete them intentionally — just accumulate paused ultra-rare-eligible sessions
3. No urgency to focus during the day
4. Adventures become meaningless — no intentional focus time required

**With daily reset:**
- Users must choose adventure duration wisely (can I complete 90 min today, or should I pick 25 min?)
- Completing an adventure before sleep is rewarding and intentional
- Short adventures (25 min) become valuable — they're completable in a busy day
- The reward system maps to real daily focus behaviour, not accumulated pauses

**UX for adventure expiry:**
- At sleep time: if an adventure is in progress, the Chibi goes to sleep mid-adventure. Morning message: "[Chibi name] fell asleep during the adventure. Ready for a new one today?"
- Framing: the Chibi needed sleep (relatable), not "you failed to complete it" (guilt)
- No penalty beyond the lost adventure rewards — mood is not affected

Product owner note: "Calibrate after user testing."

---

**Status: READY FOR ATLAS QA RE-REVIEW**

*Design specification prepared by SAGE. Addendum added by orchestrator with product owner refinements D-034 to D-037. All refinements are calibration-ready — exact values will be tuned after user testing.*
