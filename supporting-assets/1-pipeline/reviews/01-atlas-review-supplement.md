# ATLAS QA Re-Review -- Stage 1: IRIS Research Supplement

**Date:** 2026-03-19
**Reviewer:** ATLAS
**Deliverable:** pipeline/01-research-supplement.md
**Self-Review:** pipeline/01-self-review-supplement.md
**Context:** Product owner reviewed original brief and provided 9 new directives (D-021 to D-029)

## Decision: APPROVED

---

## Directive Coverage (9/9 check)

| # | Directive | Section | Complete | Confidence Levels | Sources | "Data Does NOT Show" | Design Implication |
|---|-----------|---------|----------|-------------------|---------|---------------------|-------------------|
| D-021 | Teen appeal & collection mechanics | S1 | Yes | Yes (4 findings) | 7 | Yes | Yes |
| D-022 | Usage detection accuracy (critical) | S2 | Yes | Yes (8 sub-sections) | 15+ | Yes | Yes |
| D-023 | Environment degradation thresholds | S3 | Yes | Yes (3 findings) | 3 | Yes | Yes |
| D-024 | Adventure mode / timer treasure hunts | S4 | Yes | Yes (4 findings) | 6 | Yes | Yes |
| D-025 | Focus mode presets | S5 | Yes | Yes (3 findings) | 6 | Yes | Yes |
| D-026 | Sleepy mode & morning mood inheritance | S6 | Yes | Yes (4 findings) | 7 | Yes | Yes |
| D-027 | Chibi interaction (loving but brief) | S7 | Yes | Yes (4 findings) | 8 | Yes | Yes |
| D-028 | Heartbeat check / intentional downtime | S8 | Yes | Yes (3 findings) | 2 | Yes | Yes |
| D-029 | Multiple Chibis with shelving | S9 | Yes | Yes (4 findings) | 5 | Yes | Yes |

**Verdict: 9/9 directives fully covered. All sections include the required elements: confidence levels, sourced evidence, "What the Data Does NOT Show" subsections, and "Implication for Design" lines.**

---

## D-022 Deep Assessment

This is the most consequential section in the supplement. The product owner explicitly challenged IRIS's original recommendation, and this section must demonstrate that IRIS took the challenge seriously, did the work, and arrived at a defensible revised position. Assessment:

### What IRIS Got Right

1. **The self-correction is genuine.** IRIS opens by acknowledging the product owner's challenge has merit, then explains why the original recommendation was insufficient -- not wrong on privacy grounds, but wrong on product credibility grounds. The framing ("an inaccurate Chibi is worse than a private one because an inaccurate Chibi is one users stop trusting") is sharp and captures the core issue.

2. **Android UsageStatsManager technical detail is thorough.** Data types, permission model (system-level, not runtime), Android version-specific limitations (Android R+ null when locked, Android Q+ manifest requirement), and GDPR assessment are all present. This gives FORGE enough to begin architecture work.

3. **iOS Screen Time API analysis is honest about asymmetry.** IRIS does not pretend iOS parity is achievable. The opaque token limitation (apps cannot see which specific apps the user is using), known bugs (riedel.wtf, 2024), and entitlement requirement are all documented. The statement "FocusPal will be a better product on Android for detection accuracy" is the kind of uncomfortable truth that builds trust.

4. **The two-tier model is well-structured.** The table (Tier 1 default/no permissions vs. Tier 2 opt-in/system-level) is clear and immediately actionable. The precedent section (ScreenZen, one sec, Digital Wellbeing) validates that the pattern exists in the market.

5. **GDPR assessment is sound.** Local-only processing with opt-in consent is correctly assessed as manageable. The system-level permission grant (user must navigate to Settings) is correctly identified as exceeding GDPR's "freely given, specific, informed and unambiguous" standard. The Phase 2 DPIA trigger (cloud sync) is correctly flagged.

6. **Behaviour change evidence is appropriately indirect.** IRIS does not overclaim. The Júdice et al. self-report inaccuracy study, the Danish friction experiment, and the Hawthorne effect research are all relevant adjacent evidence, and IRIS states honestly that no study directly tests "accurate detection + virtual pet feedback vs. inaccurate detection + virtual pet feedback."

7. **Gaming the system analysis adds genuine value.** The observation that Tier 1 is trivially gameable (just don't open FocusPal) while Tier 2 raises the friction barrier is a practical insight that strengthens the case for the two-tier model.

### Where D-022 Could Be Stronger (Non-blocking)

1. **Opt-in rate uncertainty is flagged but under-researched.** IRIS cites the Spool heuristic (<5% change defaults) and correctly flags that if 95% stay on Tier 1, the accuracy improvement is marginal at population level. However, no research is cited on opt-in rates for similar permissions in comparable apps. ScreenZen and one sec presumably have data on this, but it may not be public. This is a known unknown rather than a gap -- IRIS flags it, which is the right move.

2. **The iOS entitlement approval risk is mentioned but not weighted.** Apple's entitlement review process is opaque, and rejection would mean no Tier 2 on iOS at all. This is a binary risk that could affect the platform strategy. IRIS mentions the requirement but does not assess the probability of approval or the contingency if denied.

3. **The self-review correctly notes the absence of Flutter/Dart package pointers.** This is FORGE's domain, not IRIS's, so it is not a gap in the research. Noted for completeness.

### Spot-Check

I verified the claim about Android's UsageStatsManager requiring a system-level permission (not a runtime dialog). This is consistent with Android's documentation -- `PACKAGE_USAGE_STATS` is indeed a special permission that requires user action in Settings. The claim holds.

I also verified the iOS Screen Time API limitation regarding opaque tokens. Apple's DeviceActivity framework documentation confirms that apps receive anonymised identifiers, not bundle IDs or app names. This is a fundamental architectural constraint, not a bug. The claim holds.

**D-022 Verdict: Thorough, honest, and actionable. The revised recommendation (two-tier detection in Phase 1) is well-supported by technical feasibility analysis, GDPR assessment, market precedent, and behaviour change evidence. The self-correction is genuine and the original brief's limitation is explicitly acknowledged. This section directly addresses the product owner's most important concern.**

---

## Quality Assessment

### Sources
The supplement cites 50+ distinct sources across:
- Platform documentation (Android Developer Reference, Apple Developer Documentation)
- Peer-reviewed research (Júdice et al., Kumar systematic review, Oxford Academic)
- Clinical guidelines (WHO, AAP, AACAP, Royal College of Paediatrics)
- Industry press and product reviews (Ubergizmo, Hypebeast, riedel.wtf)
- Seminal academic works (Skinner, Bowlby, Csikszentmihalyi)

Source diversity is strong. No section relies on a single source type. The Appendix source index is a quality addition that makes verification straightforward.

### Confidence Levels
The three-tier vocabulary (suggests/indicates/demonstrates) is used consistently across all 9 sections. Confidence is stated at the finding level, not just the section level, which allows SAGE to weight individual claims appropriately. I checked for overconfidence -- the "demonstrates" label is reserved for regulatory facts and API documentation, while behavioural inferences are appropriately labelled "indicates" or "suggests." This calibration is correct.

### Counter-Evidence
Counter-evidence is present in S1 (US age verification laws), S2 (tracking alone insufficient), S4 (cosmetic reward satiation risk), and S8 (heartbeat check contradiction). The self-review correctly notes that counter-evidence could be stronger in S6 (morning phone check risk) and S9 (collection-as-gamification risk). These are minor gaps that do not undermine the recommendations.

### Limitations
"What the Data Does NOT Show" subsections appear in all 9 sections. Key limitations are honest and non-trivial:
- No research tests virtual-pet-based behaviour change with accurate vs. inaccurate detection (S2)
- Environment degradation thresholds are estimates, not empirical (S3)
- The paradox of an app reducing its own usage has no long-term retention data (S7)
- Heartbeat check has no precedent in screen-time apps (S8)

These limitations are the kind that build downstream trust -- SAGE and FORGE know exactly where they are building on evidence and where they are building on informed hypotheses.

---

## Cross-Directive Dependencies

The cross-directive dependency table is a quality addition that was not present in the original brief. Six interactions are identified:

1. D-022 + D-024: Detection accuracy validates adventure rewards
2. D-025 + D-023: Presets affect environment degradation thresholds
3. D-026 + D-028: Sleep mode and heartbeat check are mutually exclusive
4. D-029 + D-024: Chibi-specific adventure cosmetics incentivise trying different Chibis
5. D-021 + D-029: Teen appeal drives collection depth
6. D-027 + D-024: Brief interaction window includes the peek mechanic

**Assessment:** All six interactions are logically sound and actionable. The D-025 + D-023 interaction (presets affecting environment thresholds) is particularly important -- without this link, SAGE might design presets and environment degradation as independent systems when they must be coupled.

One interaction I would have liked to see: D-022 + D-026 (does Tier 2 detection change how sleep mode should work -- e.g., if UsageStats shows the phone was used at 2 AM, should the Chibi's frozen sleep state reflect this in the morning?). This is a design question rather than a research gap, so it is not blocking, but SAGE should be aware of it.

---

## Self-Correction Honesty

This is where IRIS earns significant trust. The self-correction on D-022 is not defensive or qualified -- it is direct:

- "The original brief correctly identified this limitation... but underweighted its impact on product credibility."
- "The privacy advantage is real, but an inaccurate Chibi is worse than a private one."
- The original vs. revised recommendation table makes the change explicit and traceable.

IRIS does not pretend the original recommendation was wrong in principle -- it was sound on privacy grounds. But it was incomplete because it did not adequately weight the credibility cost. This is exactly the right tone for a self-correction: the original position is explained, the new evidence is presented, and the revised conclusion follows logically.

The self-review also demonstrates genuine self-improvement during writing: S8's recommendation was strengthened, and the cross-directive dependency table was added after IRIS noticed systemic interactions. These are not cosmetic revisions -- they add real value.

**Verdict: Self-correction is honest, well-reasoned, and traceable. This is the standard for how agents should handle product owner feedback.**

---

## Actionability for SAGE

Can SAGE begin designing with the original brief plus this supplement? Yes. Specifically:

1. **S2 provides a clear two-tier detection architecture** that SAGE can design the onboarding UX around (opt-in framing, graceful degradation between tiers).
2. **S3 provides specific environment degradation thresholds** in a table format with trigger conditions and rationale.
3. **S4 provides a rarity distribution table** for adventure rewards that SAGE can use directly for the cosmetic reward system.
4. **S5 provides preset parameters** in a table (Relaxed/Focus-Friendly/Super-Focused) with specific values for each sensitivity parameter.
5. **S6 provides sleep window parameters by age group** and a clear recommendation for the morning recovery mechanic.
6. **S7 provides the 30-60 second interaction constraint** with specific design guidance (3-tap maximum, Chibi never asks user to stay).
7. **S8 provides a pragmatic Phase 1 recommendation** (deprioritise heartbeat check) with a clear fallback if the product owner insists.
8. **S9 provides a Phase 1 vs. Phase 2 architecture table** that tells SAGE what to design now and what to stub for later.
9. **The cross-directive dependency table** ensures SAGE designs these features as a system, not in isolation.

**Verdict: Highly actionable. SAGE has everything needed to incorporate these 9 directives into the design spec. No section leaves SAGE guessing about what to do.**

---

## Strengths

1. **D-022 is the right section done the right way.** The product owner's most important concern received the deepest treatment (8 sub-sections, 15+ sources, platform-specific technical analysis, GDPR assessment, market precedent, behaviour change evidence, and an honest self-correction). IRIS correctly identified this as the supplement's centre of gravity and allocated proportionate depth.

2. **Evidence-informed estimates are clearly labelled.** The environment degradation thresholds (S3), preset parameters (S5), and reward rarity distributions (S4) are all marked as estimates, not empirical findings. This prevents SAGE from treating design hypotheses as validated facts. The confidence vocabulary is doing real work here, not just decorating the text.

3. **The supplement functions as a true addendum.** It does not repeat or contradict the original brief. It extends the research into 9 new areas and revises exactly one original recommendation (Section 7) with a clear change table. The relationship between the two documents is well-defined.

---

## Issues (if RETURNED)

N/A -- no blocking issues identified.

---

## Recommendations (even if APPROVED)

These are non-blocking. IRIS does not need to revise the supplement for these.

1. **D-022 + D-026 interaction.** SAGE should consider what happens when Tier 2 detection reveals phone usage during the sleep window. If UsageStats shows 30 minutes of TikTok at 1 AM but the Chibi's mood was frozen at "Happy" from bedtime, there is a design tension. This is a design question for SAGE, not a research gap for IRIS, but it should be flagged in the handoff.

2. **iOS entitlement approval risk.** The Apple entitlement requirement for the Screen Time API is a binary gate. If Apple denies the entitlement, FocusPal has no Tier 2 on iOS. SAGE and FORGE should be aware that the iOS Tier 2 design may need a contingency (e.g., fallback to category-level detection via the limited APIs available without the entitlement). Not blocking -- this is an implementation risk, not a research gap.

3. **S8 product owner alignment.** IRIS recommends deprioritising the heartbeat check for Phase 1. This is pragmatically sound (weak evidence base, high UX risk, contradictory to the app's core purpose). However, the product owner specifically requested this feature. ATLAS recommends that SAGE acknowledge the heartbeat check in the design spec with a clear "Phase 2 -- pending user research" designation rather than silently dropping it, to ensure the product owner's directive is visibly addressed.

---

## Updated Handoff Quality Score: 5/5

| Criterion | Score | Justification |
|-----------|-------|---------------|
| Completeness | 5/5 | 9/9 directives with all required elements (confidence, sources, limitations, design implications) |
| Responsiveness to PO | 5/5 | D-022 directly and thoroughly addresses the product owner's primary challenge; all 9 directives researched to actionable depth |
| Quality | 5/5 | 50+ sources, consistent confidence calibration, counter-evidence present, limitations honestly stated |
| Actionability | 5/5 | Tables, parameters, thresholds, and phase-planning recommendations give SAGE and FORGE concrete values to work with |
| Self-correction | 5/5 | The D-022 reassessment is honest, data-supported, and clearly traces the change from original to revised recommendation |

---

**ATLAS sign-off:** The supplement is strong work under pressure. The product owner challenged a core recommendation, and IRIS responded with depth, honesty, and a revised position that is better than the original. The self-correction on D-022 is the most valuable contribution -- it transforms a privacy-first-but-inaccurate approach into a privacy-by-default-but-upgradeable one. Every directive is researched to actionable depth with appropriate confidence labelling.

Let's trace the thread: Original brief -> Product owner directives -> Research supplement. The thread holds. The supplement extends the original brief without contradicting it, revises exactly one recommendation with full traceability, and gives SAGE everything needed to incorporate 9 new features into the design spec.

Thread holds. Approved for handoff to SAGE.

---

*Re-review completed by ATLAS. SAGE may proceed with the original research brief (pipeline/01-research-brief.md) and this supplement (pipeline/01-research-supplement.md) as the combined research foundation.*
