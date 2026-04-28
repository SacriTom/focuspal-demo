# Prototype smoke-test screenshots — re-capture pending

This folder will hold the labelled screenshots from a re-run of the smoke test against the **CP-018+ post-polish build** (current source tag: `cp019-web-distribution-live`, demo release: `v1.1.1`).

## Why a re-capture is needed

The original smoke test ran on 2026-04-21 (CP-010) and 2026-04-26 (CP-011) and produced 17 labelled PNGs against the pre-polish build. That build had:
- A multi-room procedural Home composition (later replaced by the isometric pixel-art house backdrop, decision D-047)
- A 60-second hatching cap (later halved to 30 s, decision D-035 → D-042)
- A 240 px Chibi sprite (later sized up to 380 px on Home, 320 px on Focus active)
- A blue → amber → green progress ring on Focus active (later changed to amber/gold gradient)
- A generic paw glyph on the splash screen (later swapped for an egg sprite + tagline)

A reviewer comparing the screenshots in this folder against the live web/APK build would see visual divergence. The re-capture brings the evidence into alignment with what's deployed.

## Re-capture plan

12 sections to re-run on `Medium_Phone_API_36.1` Android emulator from a fresh `pm clear` install:

1. Splash → Choose-Chibi routing
2. Choose-Chibi (egg wobble + selection)
3. Hatching (30 s hold-to-warm + crack overlays)
4. Naming (12-char limit + scale-bounce celebration entrance)
5. Preset selector + description animation
6. Tier 2 nudge screen
7. Home (single isometric backdrop + 380 px Chibi)
8. Focus pre-session + passive-baseline strip + duration pills
9. Focus active session (amber/gold ring + 320 px Chibi)
10. Settings (preset description + Tier 2 toggle row)
11. Mood transitions (lifecycle pause/resume)
12. Persistence (kill + relaunch)

Plus the bug-arc evidence pair from CP-011 (`SS-10e` BEFORE / `SS-10f` AFTER), which can be re-captured against the **post-bug-sweep** state by running the live Tier 2 toggle test once.

## Where the existing CP-010/CP-011 screenshots are

`docs/evidence/screenshots/` in the source repo (`SacriTom/focuspal-source`) — preserved as historical evidence of the bug-arc and the CP-011 smoke test, but not the current visual state.
