# IRIS Self-Review: Research Brief (01-research-brief.md)

**Date:** 2026-03-19
**Agent:** IRIS (Insight & Research Intelligence Specialist)

---

## Completeness Check (12/12 Required Sections)

| # | Section | Status | Strength Assessment |
|---|---------|--------|-------------------|
| 1 | Executive Summary | Complete | **Strong.** Opens with the most surprising finding (no competitor uses emotional attachment), states the core risk clearly, ends with actionable design filter. |
| 2 | Market Landscape | Complete | **Strong.** Market size sourced, growth drivers identified, four-segment taxonomy created, "what data does NOT show" included. |
| 3 | Competitor Audit | Complete | **Strong.** 5 competitors analysed (Forest, Flora, Opal, ScreenZen, Finch) plus a 6th row for FocusPal in the comparison matrix. Strengths, weaknesses, and gaps covered for each. Exceeds the 4-6 minimum. |
| 4 | User Personas | Complete | **Adequate.** Three personas with confidence levels. Mia (student) is the strongest — well-supported by demographic data. David (professional) and Sarah (parent) are lower confidence and explicitly labelled as such. "What personas do NOT cover" section included. |
| 5 | Behavioural Psychology & Screen-Time Research | Complete | **Strong.** SDT, Fogg B=MAP, and Hook Model all applied to FocusPal specifically. Guilt-based failure mode explained with evidence. Counter-evidence and limitations stated. |
| 6 | Configurable Sensitivity Validation | Complete | **Strong.** Default values and ranges provided with evidence-based rationale. Table format is actionable for SAGE. |
| 7 | App-Level-Only Usage Detection | Complete | **Strong.** Honest assessment of what can and cannot be detected. Three-tier accuracy table (active/passive/inferred) gives FORGE clear technical guidance. Recommendation to proceed with caveats is well-supported. |
| 8 | Environment Reflects Wellbeing | Complete | **Strong.** Clear recommendation (PROCEED, simplified to 2-3 states) with evidence for and against. Ambient information research cited. |
| 9 | Premium Chibi Monetisation | Complete | **Adequate.** Market evidence provided. Pricing model comparison table included. Ethical considerations flagged. Would be stronger with specific revenue data from Finch or comparable apps, but that data is not publicly available. |
| 10 | GDPR & EU AI Act Analysis | Complete | **Strong.** Phase 1 vs Phase 2 distinction is clear. AI Act classification analysis is precise (rule-based system, not AI). Children's privacy flagged as highest-risk area with specific regulatory references. |
| 11 | Ethical & Regulatory Flags | Complete | **Strong.** Emotional manipulation line clearly drawn. Specific feature-level risks identified (dreaming, skill learning, premium framing). Dependency paradox addressed. Accessibility gap flagged. |
| 12 | Recommended Focus Areas for SAGE | Complete | **Strong.** Five priorities ranked by evidence strength with clear rationale. Actionable for downstream design work. |

**Overall completeness: 12/12 sections present. All end with "Implication for Design" lines.**

---

## Gaps Identified and Addressed

### During Writing
1. **Gap:** Initial draft of Section 7 (App-Level Detection) did not distinguish between active session accuracy and passive monitoring accuracy. **Fixed:** Added three-tier accuracy table (active/passive/inferred) to give nuanced assessment.

2. **Gap:** Section 4 (Personas) initially lacked a "what personas do NOT cover" subsection. **Fixed:** Added explicit exclusions (clinical addiction, hard-blocker seekers, 45+ age group) to prevent overextension of persona insights.

3. **Gap:** Section 8 (Environment) initially recommended deferral. On re-reading the ambient information research, the evidence supports proceeding with simplification. **Fixed:** Changed recommendation from "defer" to "proceed, simplified."

### Remaining Gaps
1. **Finch revenue data.** Finch Plus pricing is known (approximately 71 GBP/year) but revenue, user counts, and conversion rates are not publicly available. This limits the strength of the monetisation validation in Section 9.

2. **Primary research.** All data is secondary (market reports, competitor reviews, academic literature). No primary user research (interviews, surveys, usage data) was conducted. This is expected for IRIS's role but means all persona and preference claims are inferred, not observed.

3. **Accessibility depth.** Section 11 flags accessibility as an ethical concern but does not provide a full accessibility audit. This is appropriate for a research brief (accessibility design is SAGE's domain) but should be flagged at handoff.

---

## Unsupported Claims Flagged

All claims in the brief either cite a source or are explicitly labelled. The following are the weakest claims, flagged here for transparency:

1. **"The consumer wellbeing subset is likely 15-25% of the total market"** (Section 2.3) — labelled as "IRIS estimate; insufficient data to narrow further." This is an educated guess, not a finding.

2. **"Fewer than 5% of users change default settings"** (Section 6.4) — attributed to Jared Spool/UIE as a frequently cited heuristic. This is an industry rule of thumb, not a peer-reviewed finding with a specific N.

3. **"The hatching/naming sequence is the single most important UX"** (Section 12, Priority 1) — this is an inference from SDT, Finch validation, and the Hook Model, not a directly observed finding. Confidence level is appropriately set at "Demonstrates" for the underlying theory, but the specific claim about FocusPal is interpretive.

---

## Overall Quality Assessment

| Criterion | Rating | Notes |
|-----------|--------|-------|
| **Data-first** | Pass | Every major claim cites a source with type (market report, peer-reviewed, user review, etc.). Source index in appendix. |
| **No solutioning** | Pass | Brief diagnoses and validates. Design recommendations are framed as "what SAGE should prioritise" not "how SAGE should design it." |
| **Bias awareness** | Pass | "What the data does NOT show" subsections in Sections 2, 4, 5, 6, 7, 9. Limitations stated throughout. |
| **Actionable output** | Pass | Every section ends with a bold "Implication for Design" line. Section 12 provides ranked priorities. Section 6 provides specific threshold values. |
| **Counter-evidence** | Pass | Counter-evidence presented in Sections 5 (guilt can work short-term), 7 (app-level limitations vs. API-based), 8 (environmental feedback costs vs. benefits). |
| **Confidence levels** | Pass | All findings use suggests/indicates/demonstrates consistently. Section 4 personas explicitly graded. |

---

## Confidence Level Per Section

| Section | Confidence | Justification |
|---------|-----------|---------------|
| 1. Executive Summary | High | Synthesis of well-sourced sections |
| 2. Market Landscape | High | Multiple corroborating market sources |
| 3. Competitor Audit | High | Direct product analysis from multiple review sources |
| 4. User Personas | Medium | Inferred from secondary data, not primary research |
| 5. Behavioural Psychology | High | Peer-reviewed foundations (SDT, Fogg), meta-analytic evidence |
| 6. Configurable Sensitivity | Medium-High | Defaults grounded in attention research; specific values are best estimates |
| 7. App-Level Detection | Medium-High | Technical assessment is sound; accuracy of passive mode is uncertain |
| 8. Environment Reflects Wellbeing | Medium | Supporting research is from adjacent domains (eco-feedback, ambient displays), not direct analogues |
| 9. Premium Monetisation | Medium | Market validates model; specific revenue projections are unavailable |
| 10. GDPR & EU AI Act | High | Based on legislation text and regulatory guidance |
| 11. Ethical Flags | High | Grounded in established ethical frameworks and specific feature analysis |
| 12. SAGE Priorities | High | Direct synthesis of preceding sections with evidence-ranked ordering |

---

## Self-Evaluation Summary

```
## Self-Evaluation
- Quality standards met: 6/6 — all core criteria pass (data-first, no solutioning, bias awareness, actionable output, counter-evidence, confidence levels)
- Strongest element: Competitor audit (Section 3) — the competitive landscape matrix gives SAGE an immediate visual of where FocusPal is differentiated, and the gap analysis is specific enough to act on
- Improved before submission: Three gaps fixed during writing (detection accuracy tiers, persona exclusions, environment recommendation reversal from defer to proceed-simplified)
- Remaining limitations: All data is secondary; personas are inferred not observed; Finch revenue data unavailable; accessibility treatment is surface-level
- Confidence level: High — the brief answers all 12 required questions with sourced evidence, stated limitations, and actionable design implications. The theoretical foundation is strong. The primary uncertainty is whether emotional attachment translates to screen-time reduction in practice — but identifying that uncertainty is itself a finding.
```

---

**Status: READY FOR SAGE**

*This self-review was conducted by IRIS before handoff. All gaps identified were either addressed in-document or flagged as remaining limitations.*
