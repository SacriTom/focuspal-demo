# FocusPal — Supporting Assets and Evidence

This folder is the evidence base referenced by the H9CEAI submission document. Every `Pipeline/`, `Agents/`, or `Source/` citation in the submission resolves to a file in this directory.

Top-level: this folder lives at `https://github.com/SacriTom/focuspal-demo/tree/main/supporting-assets/` for browser navigation by the reviewer. The submission PDF cites this exact path. Markdown files render natively in GitHub; source code renders with syntax highlighting.

## Folder map

```
supporting-assets/
├── README.md                                  ← this file
├── 1-pipeline/                                ← agent deliverables that fed each handoff
│   ├── 01-research-brief.md                   ← IRIS deliverable (792 lines / 9,438 words)
│   ├── 01-research-supplement.md              ← IRIS supplementary research (50-source)
│   ├── 02-design-spec.md                      ← SAGE deliverable (1,603 lines / 13,965 words)
│   ├── 03-build-log.md                        ← FORGE engineering log (the prototype itself is in 3-source-code/)
│   ├── 04-echo-launch-strategy.md             ← ECHO deliverable (477 lines / 6,706 words)
│   ├── 05-atlas-manager-report.md             ← ATLAS Stage-5 synthesis (11,417 words)
│   ├── HANDOFF_LOG.md                         ← timestamped log of every stage-to-stage handover with QA scores
│   └── reviews/
│       ├── 01-self-review.md                  ← IRIS self-review (Stage 1)
│       ├── 01-self-review-supplement.md
│       ├── 01-atlas-review.md                 ← ATLAS QA gate of IRIS
│       ├── 01-atlas-review-supplement.md
│       ├── 02-self-review.md                  ← SAGE self-review
│       ├── 02-atlas-review.md                 ← ATLAS QA gate of SAGE
│       ├── 02-atlas-review-addendum.md
│       ├── 03-self-review.md                  ← FORGE self-review
│       ├── 03-atlas-review.md                 ← ATLAS QA gate of FORGE (the gate the Tier 2 bug arc passed through)
│       ├── 04-self-review.md                  ← ECHO self-review
│       └── 04-atlas-review.md                 ← ATLAS QA gate of ECHO (includes the PT-4 persona-quote catch)
├── 2-agents/                                  ← the five system prompts, unredacted
│   ├── 01-iris-researcher.md                  ← IRIS — Researcher
│   ├── 02-sage-designer.md                    ← SAGE — Designer
│   ├── 03-forge-maker.md                      ← FORGE — Maker
│   ├── 04-echo-communicator.md                ← ECHO — Communicator
│   └── 05-atlas-manager.md                    ← ATLAS — Manager
├── 3-source-code/                             ← Flutter prototype source snapshot
│   ├── lib/                                   ← 26 Dart files (10 screens, 6 widgets, 4 state providers)
│   ├── android/app/src/main/kotlin/...        ← Kotlin native handler (Tier 2 MethodChannel)
│   ├── android/app/src/main/AndroidManifest.xml
│   ├── pubspec.yaml
│   ├── analysis_options.yaml
│   ├── test/widget_test.dart
│   └── README.md                              ← Flutter project README
└── 4-screenshots/
    ├── pipeline-process/                      ← 24 screenshots from the multi-session pipeline run
    ├── prototype-smoke-test/                  ← prototype screenshots (CP-018+ re-capture pending)
    └── decisions/                             ← (reserved for decision-log evidence)
```

## How to read the evidence in pipeline order

| Stage | Agent | System prompt | Deliverable | Self-review | ATLAS QA |
|---|---|---|---|---|---|
| 1 | IRIS (Researcher) | `2-agents/01-iris-researcher.md` | `1-pipeline/01-research-brief.md` + supplement | `1-pipeline/reviews/01-self-review.md` | `1-pipeline/reviews/01-atlas-review.md` |
| 2 | SAGE (Designer) | `2-agents/02-sage-designer.md` | `1-pipeline/02-design-spec.md` | `1-pipeline/reviews/02-self-review.md` | `1-pipeline/reviews/02-atlas-review.md` |
| 3 | FORGE (Maker) | `2-agents/03-forge-maker.md` | `1-pipeline/03-build-log.md` + the prototype itself in `3-source-code/` | `1-pipeline/reviews/03-self-review.md` | `1-pipeline/reviews/03-atlas-review.md` |
| 4 | ECHO (Communicator) | `2-agents/04-echo-communicator.md` | `1-pipeline/04-echo-launch-strategy.md` | `1-pipeline/reviews/04-self-review.md` | `1-pipeline/reviews/04-atlas-review.md` (PT-4 catch) |
| 5 | ATLAS (Manager) | `2-agents/05-atlas-manager.md` | `1-pipeline/05-atlas-manager-report.md` | (self-reviewed, see report) | (final) |

## How to run the prototype

Three free-tier access paths, all live:

| Path | URL |
|---|---|
| Browser preview (any device) | https://sacritom.github.io/focuspal-demo/ |
| Android APK release | https://github.com/SacriTom/focuspal-demo/releases/latest |
| Pipeline tracker (operator dashboard from the run) | https://sacritom.github.io/focuspal-demo/pipeline-tracker.html |
| Walkthrough video (60-90 s) | [URL populated at submission] |

## Privacy note on source code

The source-code snapshot in `3-source-code/` is taken from the private `SacriTom/focuspal-source` git repo (full history, all polish-iteration tags). The snapshot reflects tag `cp019-web-distribution-live` (current production main). If the reviewer prefers full git history, the source repo can be opened to read access on request.
