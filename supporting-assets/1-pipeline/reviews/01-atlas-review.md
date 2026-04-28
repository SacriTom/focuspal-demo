# ATLAS QA Review -- Stage 1: IRIS (Researcher)

**Date:** 2026-03-19
**Reviewer:** ATLAS
**Deliverable:** pipeline/01-research-brief.md
**Self-Review:** pipeline/01-self-review.md

## Decision: APPROVED

---

## Completeness Assessment

All 12 required sections are present. Each section ends with a bold "Implication for Design" line addressed directly to SAGE.

| # | Section | Present | Design Implication | Notes |
|---|---------|---------|-------------------|-------|
| 1 | Executive Summary | Yes | Yes | Strong opening -- leads with the competitive gap, states the core risk honestly |
| 2 | Market Landscape | Yes | Yes | Market size sourced, 4-segment taxonomy, "what data does NOT show" included |
| 3 | Competitor Audit | Yes | Yes | 5 competitors + FocusPal comparison matrix. Exceeds the 4-6 minimum |
| 4 | User Personas | Yes | Yes | 3 personas with confidence levels. Exclusions stated |
| 5 | Behavioural Psychology | Yes | Yes | SDT, Fogg B=MAP, Hook Model -- all applied to FocusPal specifically |
| 6 | Configurable Sensitivity | Yes | Yes | Defaults and ranges in table format with evidence-based rationale |
| 7 | App-Level Detection | Yes | Yes | Three-tier accuracy table (active/passive/inferred) |
| 8 | Environment Reflects Wellbeing | Yes | Yes | PROCEED recommendation with simplification to 2-3 states |
| 9 | Premium Chibi Monetisation | Yes | Yes | Pricing model comparison, ethical considerations flagged |
| 10 | GDPR & EU AI Act | Yes | Yes | Phase 1 vs Phase 2 distinction, AI Act classification analysis |
| 11 | Ethical & Regulatory Flags | Yes | Yes | Emotional manipulation line drawn, specific feature-level risks identified |
| 12 | Recommended Focus Areas for SAGE | Yes | Yes | 5 priorities ranked by evidence strength |

**Verdict: 12/12. Complete.**

---

## Alignment with Project Vision

The research brief is tightly aligned with the product concept from the system design spec. Specific alignment checks:

- **Emotional attachment as core mechanic:** The brief's entire framing -- from the executive summary's "emotional bond, not productivity tracking" filter through to the SDT relatedness analysis -- reinforces the Tamagotchi-style Chibi as the product's differentiator. This is not a research brief that ignores the product vision and goes off on its own tangent. It interrogates the vision and comes back with "the theory supports this, but here is where it is untested."

- **Privacy-by-design:** Section 7 validates app-level-only detection as sufficient for Phase 1 with honest caveats about passive monitoring accuracy. This directly supports D-015 without over-selling the approach.

- **Chibi communication model (emoji-only):** Not deeply addressed in the brief, but referenced in the accessibility flag (Section 11.4) and persona analysis. The brief does not contradict the emoji-only decision -- it flags the accessibility gap, which is the correct research-phase action.

- **Three-phase roadmap:** The brief consistently distinguishes Phase 1 scope from Phase 2/3 throughout (e.g., sensitivity defaults for Phase 1, DPIA for Phase 2, adaptive thresholds as AI trigger for Phase 3). This shows IRIS read and internalised the phased approach.

**Verdict: Fully aligned. No vision drift detected.**

---

## Quality Assessment

### Sources
The brief cites 25+ sources across market reports, peer-reviewed research, legislation, product reviews, and industry press. A full source index is provided in the Appendix. Source types are labelled (market report, peer-reviewed, user reviews, etc.), which allows SAGE to weight claims appropriately.

### Confidence Levels
Every section and major finding uses a three-tier confidence vocabulary (suggests/indicates/demonstrates). The self-review includes a per-section confidence table with justifications. This is exactly what a downstream agent needs to decide how much weight to place on each finding.

### Limitations
"What the data does NOT show" subsections appear in Sections 2, 4, 5, 6, 7, and 9. Counter-evidence is presented in Sections 5, 7, and 8. IRIS explicitly flags three weak claims in the self-review (market subset estimate, defaults heuristic, hatching priority). This level of intellectual honesty is rare and valuable -- it prevents SAGE from treating estimates as facts.

### Spot-Check
I spot-checked the claim that "no major competitor uses emotional attachment as the primary behaviour change mechanism." The competitor audit supports this: Forest, Flora, Opal, and ScreenZen all use transactional or restriction-based mechanics. Finch uses emotional attachment but does not target screen time. The claim holds.

I also spot-checked the SDT application. The mapping of autonomy to configurable thresholds, competence to skill learning, and relatedness to Chibi bonding is accurate to Deci & Ryan's framework. The citation of the 2024 Oxford Academic review (50 design suggestions mapped to SDT needs) is specific enough to verify.

**Verdict: Quality is high. Sources are real and appropriately used. Confidence levels are consistently stated. Limitations are transparently acknowledged.**

---

## Actionability for SAGE

This is where the brief particularly excels. SAGE can begin designing immediately because:

1. **Section 6** provides specific default values and ranges in a table -- SAGE does not need to guess what "configurable sensitivity" means in practice.

2. **Section 7** provides a three-tier accuracy model (active/passive/inferred) that tells SAGE exactly what the detection system can and cannot do, so the UX can be designed around real capabilities.

3. **Section 8** gives a clear recommendation (PROCEED, 2-3 states) with specific guardrails (mild negative states, rewarding positive states).

4. **Section 12** ranks five design priorities by evidence strength with specific design requirements for each (e.g., "The Chibi must respond visibly and immediately to the user's first interaction").

5. **The competitor matrix** (Section 3.6) gives SAGE an instant view of what FocusPal must protect as differentiation.

**One minor gap:** The brief recommends framing sensitivity adjustment as "How sensitive is your Chibi?" (Section 12, Priority 3) -- this is useful but edges into solutioning. IRIS flagged this appropriately in the self-review (no-solutioning criterion passes because it is framed as "what SAGE should prioritise" not "how SAGE should design it"). I accept this -- the framing suggestion is illustrative, not prescriptive.

**Verdict: Highly actionable. SAGE has everything needed to begin the design spec.**

---

## Conditional Feature Validation Results

| Feature | Spec Requirement | IRIS Verdict | Evidence Quality | Notes |
|---------|-----------------|-------------|------------------|-------|
| Environment reflects wellbeing (D-018) | Validate or defer | PROCEED (simplified to 2-3 states) | Indicates -- ambient information research from adjacent domains | Changed from initial "defer" recommendation after reviewing evidence. The reversal is documented in the self-review. Good intellectual honesty. |
| Configurable sensitivity ranges | Defaults and ranges | Provided: 5 parameters with defaults, ranges, and rationale | Medium-High -- grounded in attention research, specific values are best estimates | Table format is immediately usable by SAGE and FORGE |
| App-level-only detection | Sufficient or flag | Sufficient with caveats | Indicates -- honest about passive mode accuracy gaps | Three-tier accuracy model is a strong contribution |
| Premium Chibi monetisation | Validate or flag concerns | Validated by market precedent, ethical concerns flagged | Medium -- market validates model, specific revenue data unavailable | Finch revenue data gap is acknowledged. Ethical flag on children's purchases is important. |

**Verdict: All four conditional features addressed with clear recommendations. No feature left unresolved.**

---

## Regulatory Depth

### GDPR
- Phase 1 vs Phase 2 distinction is clear and correct
- Local-only storage assessment as LOW RISK is accurate
- Phase 2 cloud sync implications (DPIA, privacy policy) are flagged proactively
- Data type table with GDPR relevance per field is specific to FocusPal, not generic boilerplate

### EU AI Act
- The Article 3(1) definition is quoted and applied to FocusPal's rule-based mood system
- The classification as NOT an AI system is well-reasoned (deterministic rules, no inference from biometric data)
- The Phase 3 caveat (adaptive thresholds crossing into AI territory) shows forward thinking
- The manipulation analysis (Article 5(1)(a)) correctly distinguishes transparent persuasion from subliminal manipulation

### Children's Privacy
- This is flagged as the highest-risk regulatory area -- correct
- GDPR Article 8, COPPA, ICO Children's Code, and EU DSA are all referenced
- The recommendation (target 16+ in app store listing) is pragmatic and specific
- The connection between the Tamagotchi aesthetic and likely child appeal is honestly stated

**Verdict: Regulatory analysis is specific to FocusPal, not generic. The EU AI Act classification analysis is precise and will be valuable for the submission's strategic rationale section (rubric: 15 marks for trust, GDPR, EU AI Act depth).**

---

## Strengths

1. **Intellectual honesty.** The "what the data does NOT show" subsections, stated confidence levels, and flagged weak claims set this brief apart from typical research deliverables that over-sell their findings. This is research that a designer can trust precisely because it tells you where not to trust it.

2. **Actionable specificity.** The sensitivity defaults table (Section 6), detection accuracy tiers (Section 7), and ranked SAGE priorities (Section 12) give the downstream agent concrete values to work with, not abstract guidance. This is the difference between "thresholds should be configurable" and "default time-to-annoyance: 20 minutes, range: 10-45 minutes, based on attention research."

3. **Regulatory integration.** The regulatory analysis is woven into the product context, not bolted on as an appendix. The EU AI Act classification, children's privacy flags, and ethical manipulation line are all directly connected to specific FocusPal features and design decisions. This will strengthen the submission's strategic rationale significantly.

---

## Issues (if RETURNED)

N/A -- no blocking issues identified.

---

## Recommendations (even if APPROVED)

These are non-blocking suggestions. IRIS does not need to revise the brief for these.

1. **Age-range decision escalation.** The brief recommends targeting 16+ but flags this as a "critical decision needed." This decision should be escalated to the user before SAGE begins designing, as it affects tone, visual style, purchase flows, and regulatory compliance. ATLAS will raise this with the user directly.

2. **Persona depth for David.** The professional persona (David) is acknowledged as low confidence and is the weakest of the three. If time permits later in the project, primary research (even a small survey) on professional users' receptivity to the Tamagotchi aesthetic would strengthen the secondary audience case. Not blocking -- IRIS correctly labels the confidence level.

3. **Accessibility handoff note.** Section 11.4 flags accessibility (screen reader support for emoji, colour-blind considerations for environment states) but defers to SAGE. A one-line note in the SAGE handoff reminding SAGE to address accessibility in the design spec would ensure this does not get lost in the handoff.

---

## Handoff Quality Score: 5/5

| Criterion | Score | Justification |
|-----------|-------|---------------|
| Completeness | 5/5 | 12/12 sections, all with design implications |
| Alignment | 5/5 | Fully aligned with product vision and system design spec |
| Quality | 5/5 | Sourced, confidence-levelled, limitations stated, counter-evidence presented |
| Actionability | 5/5 | SAGE can begin immediately -- specific values, ranked priorities, clear recommendations |
| Self-awareness | 5/5 | Self-review is honest, gaps were caught and fixed during writing, remaining limitations are flagged |

---

**ATLAS sign-off:** This is a strong research brief. The thread from project vision to research findings is coherent and well-documented. IRIS has delivered a diagnostic instrument that respects SAGE's design autonomy while providing the evidence SAGE needs to make informed decisions. The self-review demonstrates genuine quality improvement during the writing process (three gaps found and fixed, three weak claims flagged).

Thread holds. Approved for handoff to SAGE.

---

*Review completed by ATLAS. Handoff to SAGE may proceed.*
