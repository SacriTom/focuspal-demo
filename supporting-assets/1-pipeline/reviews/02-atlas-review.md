# ATLAS QA Review -- Stage 2: SAGE (Designer)

**Date:** 2026-03-19
**Reviewer:** ATLAS
**Deliverable:** pipeline/02-design-spec.md
**Self-Review:** pipeline/02-self-review.md

## Decision: APPROVED

---

## Completeness Assessment

### 15 Sections Check

All 15 required sections are present and substantive:

| # | Section | Present | Substantive |
|---|---------|---------|-------------|
| 1 | Design Philosophy | YES | 5 prioritised principles with research citations |
| 2 | User Journey Map | YES | 4-phase journey with emotional arcs |
| 3 | Onboarding Flow | YES | Moment-by-moment spec with wireframes |
| 4 | Screen Wireframes | YES | 4 screens (Home, Focus, Stats, Settings) with ASCII wireframes |
| 5 | Chibi Emotion State Machine | YES | 6 states + Sleepy, transition rules, parameters, Tier 1/2 logic |
| 6 | Environment State System | YES | 3 states + Storm, thresholds, visual layers |
| 7 | Adventure Mode Design | YES | Full flow, rewards, peek/pause mechanics |
| 8 | Tier 2 Permission UX | YES | Complete flow + iOS contingency + revocation handling |
| 9 | Animation & Sprite Specs | YES | Interface, placeholder mapping, particles, timing |
| 10 | Focus Timer Design | YES | Passive + active modes, Tier 1/2 variants |
| 11 | Interaction Patterns | YES | Tap responses, play session flow, positive disengagement |
| 12 | Collection System Architecture | YES | Phase 1 data model + Phase 2/3 expansion |
| 13 | Anti-Gaming Mechanics | YES | 48hr pause, single-device binding, adventure validation |
| 14 | Ethical Design Guardrails | YES | Manipulation line, non-punishing table, accessibility, data ethics |
| 15 | Phase 2 & 3 Design Notes | YES | Phase 2 designed, Phase 3 envisioned, platform parity |

**Bonus sections:** Design Traceability Matrix (29 elements traced), MoSCoW Prioritisation (10M + 7S + 6C + 10W), Success Metrics (7 Phase 1 + 5 Phase 2 targets). All three add significant value.

### 33 Decisions Coverage

SAGE's self-review correctly identifies 31/33 applicable decisions. D-014 (Provider + ChangeNotifier) and D-017 (subagents with own context windows) are correctly scoped out as architecture/pipeline decisions outside design scope.

All 31 applicable decisions are addressed with traceable section references. Spot-checked three:

- **D-026 (Sleepy mode):** Section 5.6 specifies freeze mechanic, night banking, morning mood inheritance table with four tiers. Matches the user directive exactly.
- **D-031 (Tier 1 locked features):** Section 3.6 provides the locked/unlocked feature table, messaging principles ("never guilt," "always benefit-first"), and persistent accessibility via Settings toggle. Faithful to the directive.
- **D-024 (Adventure mode):** Section 7 covers peek (no penalty), pause (never lost), cosmetic rewards with rarity tiers. The non-punishing pause is specified with exact UI including the dialogue. Matches the user directive and addresses IRIS Supplement S4.

**Verdict: COMPLETE.** No missing sections. No missing decisions.

---

## IRIS Alignment Check

This is where I applied the most scrutiny. SAGE claims every design decision traces to research. I tested this.

### Threshold Alignment

| Parameter | IRIS Supplement S5 | SAGE Section 3.5 | Match? |
|-----------|-------------------|-------------------|--------|
| Relaxed time-to-annoyance | 45 min | 45 min | YES |
| Focus-Friendly time-to-annoyance | 20 min | 20 min | YES |
| Super-Focused time-to-annoyance | 10 min | 10 min | YES |
| Recovery time (Relaxed/FF/SF) | 3/5/10 min | 3/5/10 min | YES |
| Ecstatic threshold (Relaxed/FF/SF) | 30/60/120 min | 30/60/120 min | YES |
| Annoyance escalation (Relaxed/FF/SF) | 20/10/5 min | 20/10/5 min | YES |

All six parameter values across all three presets match IRIS's recommended values exactly. No drift.

### Detection Tier Alignment

IRIS Supplement S2 recommended two-tier detection in Phase 1 (revised from Phase 2). SAGE implements this throughout the spec -- Section 5.4 provides detailed Tier 1 vs. Tier 2 mood logic, Section 8 provides the full permission UX, and Section 10 differentiates passive/active behaviour by tier. The design is faithful to the revised recommendation.

### Environment Degradation Alignment

IRIS Supplement S3, Finding 3 recommended threshold-based degradation over immediate feedback. SAGE Section 6.2 implements 30-min cumulative thresholds for Annoyed (Normal to Dim) and 60-min for Sad (Dim to Storm), on a 24-hour rolling window. This is consistent with the research recommendation for lagging-indicator feedback.

### Ethical Guardrails Alignment

IRIS Section 11.1 drew the persuasion/manipulation line. SAGE Section 14.1 reproduces this framework as a table with five criteria (transparency, user control, reversibility, emotional framing, monetisation). Section 14.2 provides a concrete "punishing version (rejected) vs. FocusPal version" comparison for six design elements. The alignment is thorough.

### Key Research Findings Used

Spot-checked SAGE's citations against IRIS:

- "No competitor uses emotional attachment as primary mechanism" (IRIS Section 1) -- correctly cited in P1
- SDT autonomy/competence/relatedness (IRIS Section 5.2) -- correctly applied across presets, adventures, interaction design
- "<5% of users change defaults" (IRIS Section 6.4 / Supplement S5) -- correctly applied to preset defaults and collapsed fine-tune settings
- "Positive disengagement" (IRIS Supplement S7, Finding 4) -- correctly applied in Section 11.4 farewell behaviour
- Pokemon/Neopets collection research (IRIS Supplement S1) -- correctly applied in Section 12 architecture
- Joyful reunion mechanics (IRIS Supplement S9, Finding 3) -- correctly applied in Section 12.2 with duration-scaled reunions

### Research Findings NOT Used

I checked whether SAGE ignored any significant IRIS finding:

- IRIS Supplement S8 (heartbeat check) -- SAGE correctly deferred to D-032's simpler 48hr pause, marking the heartbeat as Phase 2. This is appropriate; the user directive superseded the research.
- IRIS Supplement S1 counter-evidence on social comparison risks -- SAGE addresses this in Section 12.3 (Phase 3: "No 'your Chibi wants a friend' messaging") and the MoSCoW deferring social sharing to Phase 3.
- IRIS's note about sound design -- SAGE's self-review acknowledges this as a limitation. Reasonable deferral.

**Verdict: STRONG ALIGNMENT.** SAGE built on IRIS's research faithfully. Every threshold matches. Citations are specific (section and finding numbers, not vague "as the research shows"). No invented features that lack research backing -- SAGE's self-review correctly flags the one addition (Section 9.3 colour tints) as an implementation decision, not a research-backed design choice.

---

## Buildability for FORGE

### Wireframes

All 10 screens have ASCII wireframes with layout descriptions. Each wireframe includes:
- Element positioning (top-left, centre, bottom nav)
- Interaction specifications (tap, hold, swipe, confirm)
- State variations (pre-session, active, paused, complete for Focus Timer)

The hatching screen (Section 3.3) is the most detailed -- moment-by-moment with warmth percentages, animation specs, and timing. FORGE can build this without guessing.

### Animations

Animation timing is specified throughout:
- Egg wobble: "sinusoidal rotation, amplitude 2-5 degrees, period decreasing from 3s to 0.5s"
- Chibi entrance: "scale from 0.5x to 1.1x (overshoot), settle to 1.0x. Duration: 400ms. Curve: elasticOut"
- Speech bubbles: "300ms scale from 0 to 1, easeOut (spring)" appear / "200ms fade to 0, easeIn" disappear
- Mood state change: "500ms crossfade between animation sets, easeInOut"
- Environment transitions: "30-60 seconds, linear"

Sections 9.4-9.5 provides frame rates per context, transition curves with durations, and particle system specs with counts and physics. This is actionable.

### State Transitions

The state machine (Sections 5.2-5.3) provides explicit transition rules with trigger conditions and timing for both upward and downward mood changes. The Tier 1 vs. Tier 2 logic (Section 5.4) gives FORGE concrete formulas for mood calculation.

### Data Models

Section 12.1 provides concrete data models (ChibiRecord, CosmeticItem) with field names, types, and Phase 1 defaults. FORGE can implement these directly.

### One Buildability Concern

The Tier 1 notification during active adventure ("Timer pauses. A notification shows...") in Section 10.2 may conflict with the Phase 1 "no notifications" design (self-review Gap 4). The adventure pause notification appears to be an in-app message rather than a system notification, but this could be clearer. FORGE should interpret this as an in-app screen state, not a push notification. Minor ambiguity -- not blocking.

**Verdict: BUILDABLE.** FORGE has enough detail to implement Phase 1 without clarifying questions on any critical element.

---

## Tier 2 UX Assessment

### Permission Flow

The flow is clear and well-sequenced:
1. Bond first (hatch, name) -- D-030 honoured
2. Nudge after naming -- Chibi delivers the ask, not a system dialog
3. Enable leads to system Settings via deep link
4. Skip is always available, visually de-emphasised but accessible
5. No "Are you sure?" on skip -- D-031 honoured

### Locked Features

The locked/unlocked table (Section 3.6) is clear:
- Tier 1 gets: mood reactions (approximate), home screen, adventures, cosmetics
- Tier 2 unlocks: evolution (Phase 2), skill learning (Phase 2), full stats
- Framing: "the app literally cannot provide this without the data" -- honest, not punishing

### Always-Accessible Path

Three access points verified:
1. Settings screen: persistent toggle with one-tap deep link
2. Stats screen: gentle banner ("Enable screen time access for your full picture")
3. Feature lock points (Phase 2): in-context prompt when user would benefit

### iOS Contingency

Section 8.3 provides a complete fallback: suppress Tier 2 nudge on iOS without entitlement, offer alternative progression path via in-app timer data, and communicate the limitation honestly. This addresses ATLAS Non-Blocking Item #2.

### Permission Revocation

Section 8.4 (added during self-review) handles the edge case: silent fallback to Tier 1, gentle re-enable banner, progress preserved but paused. No punishment.

**Verdict: PASS.** The Tier 2 UX is clear, non-punishing, and always accessible. D-030 and D-031 are implemented correctly.

---

## State Machine Validation

### Transition Completeness

Checked all possible state pairs:

- **Ecstatic to Sad in one step:** NOT POSSIBLE. Must decay through Happy, Content, Annoyed. Correct.
- **Sad to Ecstatic in one step:** ONLY via completing an active focus session (Ecstatic is a legitimate reward state). Otherwise must recover through Annoyed, Content, Happy. Correct.
- **Sleepy concurrent with other states:** NOT POSSIBLE. Sleepy is a time-of-day override that freezes the mood machine. Correct.
- **Mood change during Sleepy:** NOT POSSIBLE. Freeze mechanic prevents this. Night interruptions are banked, not applied. Correct.

### Edge Cases

- **Exact boundary between time-of-day and mood:** Section 5.6 specifies Sleepy activates at configured bedtime, mood freezes. 30-minute crossfade for visual transition. Covered.
- **Preset change mid-session:** Section 10.2 explicitly prevents this. Covered.
- **Tier 2 enabled then revoked:** Section 8.4 handles this (added during self-review). Covered.
- **48hr inactivity return:** Section 13.1 specifies mood resets to Content, progress resumes. Covered.

### Morning Inheritance

The morning mood table (Section 5.6) provides four tiers based on night disturbance count (0, 1-2, 3-5, 6+). The floor is Annoyed (never starts at Sad from sleep interruptions alone). The morning recovery bonus (double recovery for first 5 minutes) is specified. This is a complete mechanism.

### One Edge Case Not Explicitly Addressed

What happens if the user changes their sleep schedule while the Chibi is already in Sleepy mode? For example, moving bedtime from 22:00 to 23:00 at 22:30. The spec does not address whether the Chibi should wake up (new bedtime hasn't arrived yet) or stay asleep (it was already asleep). This is a minor edge case that FORGE can handle with a reasonable default (stay in Sleepy until new wake time), but it could be documented.

**Verdict: PASS.** State machine is well-defined. One minor undocumented edge case (sleep schedule change during Sleepy mode) -- not blocking.

---

## Ethical Guardrails

### Manipulation Drift Check

Reviewed each design pattern against IRIS Section 11.1's persuasion/manipulation line:

| Pattern | Risk | Assessment |
|---------|------|-----------|
| Chibi mood as feedback | Could create guilt | MITIGATED: framed as cause-and-effect, recovery faster than degradation, Sleepy freeze prevents overnight guilt |
| Adventure pause | Could punish interruption (Forest model) | MITIGATED: pause not cancel, reward delayed not lost, "Your treasure will wait for you" |
| Tier 2 nudge | Could pressure for permissions | MITIGATED: skip always available, no "Are you sure?", benefit-first messaging, Chibi delivers (not system dialog) |
| Locked features (D-031) | Could feel like a paywall | MITIGATED: framed as honest technical limitation ("app literally cannot provide this without the data"), not as restriction |
| Interaction window tire cues | Could frustrate users | MITIGATED: gentle yawn/wave, Chibi settles into own activity (positive framing), 120s+ annoyance is mild |
| Collection/cosmetics | Could drive compulsive engagement | MITIGATED: no "daily login" rewards, no FOMO mechanics, no limited-time items, rewards earned through genuine focus |
| Shelving mechanic | Could create guilt | MITIGATED: shelving framed as "rest," reunion is joyful, Chibi waves contentedly |

### Monetisation Ethics

Section 12.3 (Phase 3) explicitly prohibits emotional manipulation in premium promotion: no "your Chibi wants a friend," no "limited time," no countdown. Premium is display-only in a shop section. Consistent with IRIS Section 11.1.

**Verdict: PASS.** No design pattern drifts toward manipulation. The persuasion/manipulation line is maintained throughout.

---

## Cross-Agent Alignment

### ATLAS Non-Blocking Items Resolution

| # | Item | Status | Section | Assessment |
|---|------|--------|---------|-----------|
| 1 | D-022 + D-026: Tier 2 during sleep window | RESOLVED | S5.7 | Sleep freeze applies equally to both tiers. Tier 2 data accumulated as night disturbances, applied at morning. Clear and consistent. |
| 2 | iOS entitlement contingency | RESOLVED | S8.3 | Complete fallback: suppress nudge, alternative progression via in-app timer data, honest communication. |
| 3 | D-028/D-032 heartbeat as Phase 2 | RESOLVED | S13.1 | Heartbeat explicitly marked Phase 2. 48hr pause (D-032) is the Phase 1 implementation. Clear delineation. |

**Verdict: All three items resolved.** SAGE addressed each with specific, implementable solutions.

---

## Strengths

1. **Onboarding flow (Section 3).** This is exceptional work. Moment-by-moment specification with emotional beats, animation timing to the millisecond, and interaction logic that FORGE can build without a single clarifying question. The hatching screen alone is more detailed than most complete app specs.

2. **Research traceability.** Every major design decision cites a specific IRIS section and finding number. The Design Traceability Matrix (29 elements) and the inline citations throughout the spec make it possible to trace any element back to its research basis. This is exactly what the rubric means by "cumulative outputs."

3. **Tier 2 UX architecture.** The two-tier detection design is handled with unusual sophistication -- the permission flow, the locked/unlocked table, the messaging principles, the iOS contingency, and the revocation handling form a complete system. SAGE turned a technically complex problem (optional permissions that affect the entire app) into a coherent UX that feels natural and non-punishing.

---

## Issues

None blocking. Approved without return.

---

## Recommendations (Non-Blocking)

1. **Fix duplicate subsection numbering.** Section 9.4 appears twice ("Frame Rates and Timing" and "Transition Curves"). The second should be 9.5, and current 9.5 should become 9.6. Cosmetic but could confuse FORGE when referencing sections.

2. **Clarify adventure pause notification vs. no-notifications policy.** Section 10.2 mentions a notification during Tier 1 adventure pause. Self-review Gap 4 says Phase 1 has "no notifications." Recommend SAGE or FORGE treat this as an in-app screen state (shown when user returns to FocusPal), not a system push notification, and document this explicitly.

3. **Document sleep schedule change during Sleepy mode.** Minor edge case: user adjusts bedtime/wake time while Chibi is already asleep. Recommend a simple rule: "If bedtime is moved later than current time while Chibi is Sleepy, Chibi wakes up. If wake time is changed, Chibi wakes at the new wake time." FORGE can implement a sensible default even without this spec, but documenting it prevents ambiguity.

4. **Stats screen animation depth.** SAGE's self-review correctly notes the Stats screen has the least design depth. For Phase 1 this is acceptable (it is a data display screen), but FORGE should not invest zero effort here -- even a simple fade-in on data cards would prevent the screen from feeling flat compared to the richly animated home screen.

---

## Handoff Quality Score: 5/5

The design spec is complete, research-aligned, buildable, ethically sound, and internally consistent. The self-review caught and fixed the two most significant gaps (Tier 2 revocation, Phase 1 species differentiation) before submission. All three ATLAS non-blocking items are resolved. The traceability matrix and MoSCoW prioritisation give FORGE a clear build roadmap.

**Thread holds from Research to Design.** Every core claim traces. SAGE used the research; SAGE did not ignore it.

---

*Reviewed by ATLAS. Approved for handoff to FORGE.*
