# Source code

The Flutter prototype source lives in a dedicated public repo:

**https://github.com/SacriTom/focuspal-source**

This repo contains the full git history (50+ commits, 18 named tags spanning the iteration cycle), so the reviewer can browse not only the current state of the code but every step of how it got there.

## Recommended entry points

| What you're looking for | Where to look |
|---|---|
| Currently deployed build | `main` branch, tag `cp019-web-distribution-live` |
| The exact build captured on the walkthrough video | tag `cp018-recording-baseline` |
| The pre-polish baseline (before the home rooms / Tier 2 reconcile / lint sweep) | tag `cp016-fallback` |
| Browse the iteration cycle | `git tag -l --sort=creatordate` lists every step in order; commit messages explain each |
| The Flutter app itself | `app/focuspal/lib/` — 26 Dart files (10 screens, 6 widgets, 4 state providers) |
| The Kotlin native handler that drives Tier 2 Usage Access | `app/focuspal/android/app/src/main/kotlin/com/focuspal/focuspal/MainActivity.kt` |
| Build manifests | `app/focuspal/pubspec.yaml`, `app/focuspal/android/app/src/main/AndroidManifest.xml` |
| The single widget test (mood-state ordering invariant) | `app/focuspal/test/widget_test.dart` |

## Iteration tags worth knowing about

| Tag | Marks |
|---|---|
| `cp016-fallback` | Pre-polish baseline (before any post-CP-016 iteration) |
| `post-bug-sweep` | Bug-sweep round (Tier 2 reconcile, sprite precache, lint clean to 0 issues) |
| `post-rooms-a1` / `a2` / `a3` | Home rooms iteration cycle (gradient → composed walls → wall art) |
| `post-rooms-zoom` | Rejected variant (wrong direction, smaller Chibi) |
| `post-rooms-single` | Composed sprites + 240 px Chibi |
| `post-rooms-backdrop` | Final accepted layout — isometric house image as backdrop |
| `post-hatch` | Hatching alignment fix + 30 s timer (D-035 → D-042) |
| `post-onboarding` | Naming celebration entrance |
| `post-settings-stats` | Settings preset description + Stats first-journey hero |
| `post-polish-eg` | Focus timer amber ring + splash branding |
| `cp018-recording-baseline` | Exact build captured on the walkthrough video |
| `post-web-fix` | Web phone-aspect frame + Chibi persistence cache |
| `post-web-fit-or-scroll` | Intermediate web-layout variant (rolled back) |
| `post-web-force-fit` | Final accepted web layout — FittedBox uniform scale |
| `cp019-web-distribution-live` | Public distribution refreshed; current production main |

## Privacy note

The repo was kept private during the build to protect work-in-progress, then made public for the H9CEAI grading window so the reviewer can browse the history. After grading the repo will be reverted to private.
