# ATLAS QA Re-Review -- SAGE Design Addendum (D-034 to D-037)

**Date:** 2026-03-19
**Decision:** APPROVED

---

## AD1: Real Sprites (D-034)

Strong. The 16-animation interface from Section 9.1 is fully mapped -- all 16 required animations have a concrete source animation or contextual reuse strategy. The mapping table is clear and buildable. Two observations:

- **Asset paths are explicit.** FORGE gets exact directory paths for Cat, Penguin, Panda, Home Environment, and Adventure Environment. No guessing.
- **Contextual reuse is well-handled.** Six animations (sleeping, cooking, reading, playing_music, tired, waving) use Idle/Walk base animations with speech bubble overlays. This is practical given the sprite pack contents and avoids inventing animations that don't exist in the assets.
- **Spine data noted.** The spec mentions Spine animation JSON as an option alongside PNG sequences. FORGE has a clear choice: frame-by-frame (simpler) or Spine (smoother). Either path is supported.
- **Phase 2 expansion is pre-solved.** 12 additional species already sourced. No future asset procurement needed.

**One minor note:** The "Stuned" typo (line 1501) is from the original craftpix asset naming, not a spec error. FORGE should be aware the folder name is literally "Stuned" not "Stunned."

**Verdict: PASS.**

---

## AD2: Hatching 60s (D-035)

Clean change. Max duration reduced from 60-90s to a flat 60s max. Drain rate increased from ~0.5%/s to ~1%/s to match the tighter window.

**Interaction check:** No conflict with other mechanics. Hatching is a self-contained onboarding moment -- it feeds into naming (Section 3.4) which feeds into the Tier 2 nudge (Section 3.5). The downstream flow is unaffected by a shorter hatch time.

The "calibrate after user testing" note is appropriate -- 60s is a starting point, not a hard commitment.

**Verdict: PASS.**

---

## AD3: Relaxed Minimums (D-036)

The four hard-coded minimums are reasonable:

| Parameter | Default | Minimum | Reduction allowed |
|-----------|---------|---------|-------------------|
| Time-to-annoyance | 45 min | 30 min | 33% |
| Recovery time | 3 min | 2 min | 33% |
| Ecstatic threshold | 30 min | 20 min | 33% |
| Annoyance escalation | 20 min | 10 min | 50% |

The minimums prevent users from trivialising the focus mechanic while still allowing meaningful customisation. The rationale column in the spec explains each floor clearly.

**UX for hitting the floor:** Specified -- slider stops, tooltip reads "This is the minimum for a meaningful focus experience." Non-punishing, informative. Consistent with the spec's "never guilt" principle from Section 14.

**One consideration:** The minimums only apply to Relaxed. Focus-Friendly and Super-Focused presets have tighter defaults already. If a user on Focus-Friendly wants to loosen settings, they switch to Relaxed -- which now has a floor. This is logically consistent. No gap.

**Verdict: PASS.**

---

## AD4: Adventure Daily Reset (D-037)

This is the only addendum item that modifies a prior design commitment. The original spec (Section 7.5, line 883) states explicitly: "A paused adventure never expires. It can be resumed days later. The reward is delayed, not cancelled. This is the anti-Forest principle: no tree dies, no progress is destroyed, ever."

AD4 changes this: paused adventures now reset at sleep time. Progress and potential rewards are lost.

**Does this contradict D-024 (non-punishing pause)?**

Partially, but the contradiction is managed:

1. **The pause itself remains non-punishing within the day.** Users can still peek, pause, and resume freely during waking hours. D-024's core intent -- "interrupting a session should not destroy progress" -- holds for active-day use.
2. **The daily reset is framed as the Chibi sleeping, not as failure.** Morning message: "[Chibi name] fell asleep during the adventure." This is the same sleep-time boundary used elsewhere in the spec (Sleepy mode, Section 5.6). Consistent framing.
3. **No mood penalty.** The only consequence is losing that adventure's potential reward. Mood is unaffected. This stays within the "delayed consequence, not punishment" philosophy.
4. **The anti-gaming rationale is sound.** Without the reset, 90-minute adventures become risk-free accumulation vehicles. The exploit path described in the addendum is real and would undermine the entire reward system.

**However, two lines in the original spec now need updating:**

- Section 7.5 (line 883): "A paused adventure never expires" -- now false. Must be amended or marked as superseded by AD4.
- Section 14.2 (line 1282): "Adventure paused, progress saved, resume anytime" in the punishing-vs-FocusPal comparison table -- now only true within the same day.

**Recommendation:** FORGE should treat AD4 as the authoritative version. SAGE should update Section 7.5 and Section 14.2 to reflect the daily reset before the spec is considered final -- but this is a documentation update, not a design issue. The design itself is sound.

**Verdict: PASS with documentation note.**

---

## Consistency Check

Checked the addendum against the original spec and ATLAS review:

| Check | Result |
|-------|--------|
| AD1 vs. Section 9 (Animation Interface) | Consistent. 16-animation interface preserved. Placeholder mapping superseded, not contradicted. |
| AD2 vs. Section 3.3 (Hatching) | Consistent. Only duration/drain values changed. Mechanics intact. |
| AD3 vs. Section 5.3 (Parameters) | Consistent. Adds constraints to existing parameter system. No conflicts. |
| AD4 vs. Section 7.5 (Pause) | **Partial contradiction.** Two lines in the original spec ("never expires," "resume anytime") need amendment. Design intent is coherent; documentation lags. |
| AD4 vs. Section 14.2 (Ethical table) | **Needs update.** The punishing-vs-FocusPal row about adventure pausing is no longer fully accurate. |
| AD4 vs. D-024 directive | **Acceptable evolution.** D-024's core intent (non-punishing interruption) is preserved within the daily window. The sleep-time boundary is a new constraint, not a contradiction of the underlying philosophy. |

**No structural contradictions.** One documentation gap (two lines needing amendment) is the only follow-up.

---

## Recommendations

1. **SAGE should update Section 7.5 and Section 14.2** to reflect AD4's daily reset before FORGE begins the adventure mode build. Two specific lines need revision. This prevents FORGE from implementing the old "never expires" behaviour.

2. **FORGE should note the "Stuned" folder name** in the craftpix assets (AD1). The sprite mapping refers to the Stuned animation for the "sad" state -- the typo is in the source assets, not the spec.

3. **All four addendum items include "calibrate after user testing" notes.** FORGE should implement these values as named constants or config parameters, not hard-coded literals, to support post-launch tuning.

---

## Updated Score: 5/5

The addendum items are well-specified, well-reasoned, and buildable. AD4 introduces the only tension with the original spec, and it is handled with appropriate framing (sleep-time boundary, no mood penalty, sound anti-gaming rationale). The documentation gap is minor and non-blocking for FORGE -- the addendum itself is clear about what changed.

Thread holds. The addendum strengthens the design by closing an exploit path (AD4), grounding the visuals in real assets (AD1), tightening the onboarding feel (AD2), and preventing mechanic trivialisation (AD3).

---

*Re-reviewed by ATLAS. Addendum approved. Original 5/5 score maintained.*
