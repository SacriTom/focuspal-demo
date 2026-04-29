# Prototype smoke-test screenshots — pre-polish (CP-010 / CP-011)

This folder holds the labelled smoke-test screenshots from the original CP-010 (2026-04-21) and CP-011 (2026-04-26) walkthroughs against the **pre-polish** build, plus the raw 67-second walkthrough video captured at CP-018.

## Contents

| File | Stage | Description |
|---|---|---|
| `01_choose_chibi.png` | 2 | Choose-Chibi — egg wobble + selection |
| `02_hatching.png` | 3 | Hatching — hold-to-warm + crack overlays |
| `naming.png` | 4 | Naming — char-limited input + celebration entrance |
| `03_preset.png` | 5 | Preset selector + description |
| `04_tier2_nudge.png` | 6 | Tier 2 nudge screen |
| `05_home.png` | 7 | Home — Chibi + speech bubble |
| `06_focus_timer.png` | 8 | Focus pre-session — duration pills |
| `06b_timer_active.png` | 9 | Focus active — progress ring + Chibi |
| `07_stats.png` | — | Stats screen — aspirational unlock banner |
| `SS-10a_settings.png` | 10 | Settings — Focus-Friendly preset |
| `SS-10b_settings_relaxed.png` | 10 | Settings — Relaxed preset |
| `SS-10c_settings_super.png` | 10 | Settings — Super-Focus preset |
| `SS-10d_sleep_picker.png` | 10 | Sleep-window picker |
| `SS-10e_tier2_toggle_finding.png` | 10 | Bug-arc BEFORE — Tier 2 toggle lying |
| `SS-10f_tier2_intent_fixed.png` | 10 | Bug-arc AFTER — toggle fires intent |
| `SS-11_home_baseline.png` | 11 | Home baseline pre-suspend |
| `SS-11_home_resumed.png` | 11 | Home post-resume — mood transition |
| `walkthrough.mp4` | — | Raw 67 s walkthrough (no audio) — Splash → Home → Focus → Settings |
| `smoke_test_2026-04-21.md` | — | Original 12-section walkthrough journal |

## Visual divergence note (honest disclaimer)

The screenshots above were captured against the **pre-polish** build before the CP-017 / CP-018 / CP-019 polish phases. A reviewer comparing these screenshots against the live web/APK build will see visual differences in the following areas:

- **Home composition** — the screenshots show a multi-room procedural Home; the current build uses a single isometric pixel-art house backdrop (decision D-047)
- **Hatching duration** — 60 s in the screenshots, 30 s in the current build (D-035 → D-042)
- **Chibi sprite size** — 240 px in the screenshots, 380 px on Home / 320 px on Focus active in the current build
- **Focus active progress ring** — blue → amber → green gradient in the screenshots, amber/gold gradient in the current build
- **Splash screen glyph** — generic paw in the screenshots, egg sprite + tagline in the current build

The walkthrough video (`walkthrough.mp4`) was captured at CP-018, so it shows the **post-polish** state for the surfaces it covers (Splash, Choose Chibi, Hatching, Naming, Preset, Tier 2, Home, Focus pre-session, Focus active, Settings).

The bug-arc evidence pair (`SS-10e` BEFORE / `SS-10f` AFTER) is the load-bearing piece of Reflection evidence in the submission and is unaffected by visual polish.

## Why pre-polish screenshots are still the canonical evidence

The CP-010 and CP-011 walkthroughs were the disciplined, multi-section captures that exposed the Tier 2 bug arc and validated 12 functional sections live. Re-capturing 12 sections against the post-polish build was scoped out of the submission window in favour of submission compilation, citation accuracy, and the decision diagrams. The visual divergence is acknowledged in the body and via this README.
