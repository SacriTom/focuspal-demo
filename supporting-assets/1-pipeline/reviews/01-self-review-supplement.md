# IRIS Self-Review -- Research Supplement (D-021 to D-029)

**Date:** 2026-03-19
**Agent:** IRIS
**Deliverable:** pipeline/01-research-supplement.md

---

## Completeness Assessment

| # | Section | Directive | Complete | Confidence Level Stated | Sources Cited | Design Implication |
|---|---------|-----------|----------|------------------------|---------------|-------------------|
| S1 | Teen Appeal & Collection | D-021 | Yes | Yes (4 findings) | 7 sources | Yes |
| S2 | Usage Detection Accuracy | D-022 | Yes | Yes (8 sub-sections) | 15+ sources | Yes |
| S3 | Environment Degradation | D-023 | Yes | Yes (3 findings) | 3 sources | Yes |
| S4 | Adventure Mode | D-024 | Yes | Yes (4 findings) | 6 sources | Yes |
| S5 | Focus Mode Presets | D-025 | Yes | Yes (3 findings) | 6 sources | Yes |
| S6 | Sleepy Mode | D-026 | Yes | Yes (4 findings) | 7 sources | Yes |
| S7 | Chibi Interaction | D-027 | Yes | Yes (4 findings) | 8 sources | Yes |
| S8 | Heartbeat Check | D-028 | Yes | Yes (3 findings) | 2 sources | Yes |
| S9 | Multiple Chibis | D-029 | Yes | Yes (4 findings) | 5 sources | Yes |

**Verdict: 9/9 directives researched. All sections include confidence levels, sources, "What the Data Does NOT Show" subsections, and "Implication for Design" lines.**

---

## Quality Assessment

### Sources
The supplement cites 50+ distinct sources across platform documentation, peer-reviewed research, clinical guidelines, industry analysis, and product reviews. A full source index is provided in the Appendix. Source diversity is strong: no section relies on a single source type.

### Confidence Levels
Every finding uses the three-tier vocabulary (suggests/indicates/demonstrates) consistently. No finding is presented without a confidence label.

### Counter-Evidence
Counter-evidence is presented in S1 (US age verification laws), S2 (tracking alone insufficient for behaviour change), S4 (satiation risk for cosmetic rewards), and S8 (heartbeat check contradiction). Counter-evidence could be stronger in S6 (morning phone check risk) and S9 (collection-as-game-ification risk).

### Limitations
"What the Data Does NOT Show" subsections appear in all 9 sections. Key limitations flagged:
- No research tests virtual-pet-based behaviour change with accurate vs. inaccurate detection (S2)
- Optimal thresholds for environment degradation are estimates, not empirical (S3)
- The paradox of an app reducing its own usage has no long-term retention data (S7)
- Heartbeat check has no precedent in screen-time apps (S8)

---

## D-022 Depth Assessment (Most Critical Section)

This is the section the product owner cares about most. Assessment:

| Criterion | Met? | Notes |
|-----------|------|-------|
| Android UsageStatsManager technical detail | Yes | Data types, permissions, limitations documented |
| iOS Screen Time API technical detail | Yes | Three frameworks, capabilities, bugs, privacy model documented |
| GDPR assessment for opt-in usage tracking | Yes | Local-only processing assessed as manageable; DPIA flagged for Phase 2 |
| Two-tier model precedent | Yes | ScreenZen, one sec, Digital Wellbeing cited |
| Behaviour change impact of accuracy | Yes | Self-report inaccuracy research, Hawthorne effect, friction experiment cited |
| Gaming the system | Yes | Circumvention methods documented, impact on FocusPal assessed |
| Honest reassessment of original Section 7 | Yes | Self-correction explicitly stated; original brief's limitation acknowledged |
| Revised recommendation | Yes | Clear table showing original vs. revised position |
| Platform asymmetry (iOS vs. Android) flagged | Yes | Stated honestly that iOS will be less accurate |
| Opt-in rate concern | Yes | Flagged as unknown with mitigation suggestion |

**Verdict: D-022 section is thorough. It provides SAGE with sufficient technical and behavioural evidence to design the two-tier UX, and FORGE with sufficient technical detail to architect the detection system. The self-correction is honest and well-reasoned.**

**One weakness:** The section does not provide a specific Flutter/Dart code reference or package for accessing UsageStatsManager. This is FORGE's domain, but a pointer to the relevant Flutter plugin (e.g., `app_usage` or `usage_stats` packages) would have been helpful. Not blocking -- IRIS's role is research, not implementation.

---

## Cross-Directive Dependencies

The supplement includes a cross-directive dependency table, which is a quality addition not present in the original brief. This helps SAGE and FORGE understand that these directives are a system, not isolated features.

---

## Self-Evaluation

- **Quality standards met:** 9/9 sections complete with all required elements
- **Strongest element:** S2 (Usage Detection) -- the most thorough section, directly responsive to the product owner's challenge, with honest self-correction and a clear revised recommendation
- **Improved before submission:** During writing, I identified that S8 (Heartbeat Check) initially lacked a clear recommendation. Added the "minimal heartbeat approach" recommendation and Phase 1 deprioritisation rationale. Also added the cross-directive dependency table after noticing that several directives interact in ways that weren't initially obvious.
- **Remaining limitations:**
  - S8 has the weakest evidence base of any section -- "heartbeat check" is a novel concept with no direct precedent. The recommendation to deprioritise for Phase 1 is pragmatic but may not satisfy the product owner.
  - S3 threshold values are estimates, not empirical. They should be treated as starting points, not validated defaults.
  - S7 lacks long-term retention data for the "app that reduces its own usage" paradox. Finch is the best proxy, but Finch's retention data is not public.
- **Confidence level:** High -- all 9 directives are researched with sourced evidence, confidence levels, and actionable design implications. The D-022 reassessment is the strongest contribution and directly addresses the product owner's most important concern.

---

## Handoff Readiness

| Criterion | Status |
|-----------|--------|
| All directives researched | Yes (9/9) |
| Sources cited | Yes (50+ across supplement) |
| Confidence levels stated | Yes (every finding) |
| Design implications provided | Yes (every section) |
| Counter-evidence presented | Yes (key sections) |
| Limitations acknowledged | Yes (every section) |
| Cross-directive dependencies identified | Yes |
| Original brief's Section 7 honestly reassessed | Yes -- revised recommendation |

**Status: READY FOR ATLAS QA**

---

*Self-review completed by IRIS. The supplement is an addendum to the original research brief, not a replacement. It should be read alongside pipeline/01-research-brief.md.*
