# FORGE Build Log — FocusPal Phase 1 Prototype

**Date:** 2026-03-19
**Agent:** FORGE (Functional Output & Rapid Game Engineering Specialist)
**Status:** READY FOR ATLAS QA
**Flutter project:** `app/focuspal/`
**Analysis:** 0 errors, 0 warnings (flutter analyze clean)

---

## Architecture Decisions

### State Management
Provider + ChangeNotifier as specified (D-014). Four state providers:
- `ChibiState` — mood, name, species, activity, interaction timer, Tier 2 status
- `FocusState` — active timer, passive tracking, session history, adventure state
- `SettingsState` — 3 named presets with configurable parameters, sleep window, Tier 2 toggle
- `EnvironmentState` — wellbeing level (bright/normal/dim), time-of-day phase, cumulative mood tracking

### Project Structure
```
lib/
├── main.dart                    # MultiProvider setup, routing
├── models/
│   ├── chibi.dart               # ChibiSpecies enum, Chibi data class
│   ├── mood.dart                # MoodState enum (6 states), transition logic
│   └── focus_session.dart       # FocusSession data class
├── screens/
│   ├── splash_screen.dart       # Logo animation, routing to onboarding or home
│   ├── choose_chibi_screen.dart # 3 eggs (Cat/Penguin/Panda), tap to select
│   ├── hatching_screen.dart     # Hold-to-warm (max 60s), egg crack, Chibi emerges
│   ├── naming_screen.dart       # Text input, Chibi celebration on submit
│   ├── preset_screen.dart       # 3 cards (Relaxed/Focus-Friendly/Super-Focused)
│   ├── tier2_nudge_screen.dart  # Chibi permission nudge, skip option
│   ├── home_screen.dart         # Full-screen scene, mood Chibi, speech bubbles, nav
│   ├── focus_timer_screen.dart  # Passive info + active adventure timer
│   ├── stats_screen.dart        # Focus history, streaks, Tier 2 locked banner
│   └── settings_screen.dart     # Presets, sliders, sleep time, Tier 2 toggle
├── widgets/
│   ├── chibi_sprite.dart        # Animated sprite renderer (character-agnostic)
│   ├── speech_bubble.dart       # Emoji thought bubble (positioned above Chibi)
│   ├── environment_scene.dart   # Full-screen background with tinting
│   ├── egg_animation.dart       # Hatching sequence with warmth meter
│   ├── mood_indicator.dart      # Top-right mood emoji with glow
│   └── warmth_meter.dart        # Hold-to-warm progress bar
├── services/
│   ├── sprite_service.dart      # Character-agnostic sprite loading
│   └── storage_service.dart     # SharedPreferences + SQLite
└── state/
    ├── chibi_state.dart         # Core Chibi logic
    ├── focus_state.dart         # Timer and session logic
    ├── settings_state.dart      # Presets and configuration
    └── environment_state.dart   # Environment wellbeing and time-of-day
```

### Character-Agnostic Sprite System
`SpriteService` maps species → animation folders. Each species implements the same animation set (Idle, Walk, Jump, etc.). Adding a new species requires:
1. Add sprite folder to `assets/sprites/`
2. Add enum value to `ChibiSpecies`
3. Register in `SpriteService` path map

Zero changes to rendering, animation, or state code. Tested with Cat, Penguin, and Panda.

### Two-Tier Detection
- Tier 1 (default): App lifecycle events via `WidgetsBindingObserver`. Detects foreground/background. Drives mood mechanics.
- Tier 2 (opt-in): Android `UsageStatsManager` via platform channel. Provides device-wide screen time. Unlocks evolution/skills/rewards.
- Tier 2 status stored in `SettingsState.isTier2Enabled`. Feature locks checked throughout the app.

## Screens Implemented

| Screen | Status | Key Implementation Notes |
|--------|--------|-------------------------|
| Splash | Done | Animated logo, auto-routes based on onboarding state in SharedPreferences |
| Choose Chibi | Done | 3 egg images, wobble on tap, species selection stored |
| Hatching | Done | GestureDetector for long press, WarmthMeter widget, max 60s (D-035), EggAnimation with crack stages, Chibi Jump animation on emerge |
| Naming | Done | TextField with 12-char limit (per design spec Section 3.4), Chibi Idle animation watching, Jump celebration on submit, name persisted |
| Preset | Done | 3 selectable cards with parameter previews, hard-coded minimums on Relaxed (D-036), default Focus-Friendly |
| Tier 2 Nudge | Done | Chibi speech bubble explains request, "Enable" opens Android UsageStats settings via intent, "Skip for now" proceeds, non-punishing |
| Home | Done | EnvironmentScene background, ChibiSprite with mood animation, SpeechBubble, MoodIndicator, BottomNavigationBar (Home/Focus/Stats/Settings) |
| Focus Timer | Done | Passive mode info card, active mode with 4 duration pills (25/45/60/90 min), adventure EnvironmentScene, countdown timer, pause/resume |
| Stats | Done | Today's sessions, weekly total, current streak, Tier 2 locked features banner with one-tap enable path |
| Settings | Done | Preset radio buttons, individual sensitivity sliders with min/max bounds, bedtime/wake time pickers, Tier 2 toggle, about section |

## Animation System

- `ChibiSprite` widget uses `AnimationController` to cycle through PNG frame sequences
- Frame rate configurable per animation state (idle=8fps, walking=10fps, sleeping=3fps)
- Mood-based animation selection: `MoodState` → animation name → sprite folder → frame list
- Speech bubble overlays (emoji) tied to current activity (cooking=🍳, reading=📖, etc.)
- Transitions between mood states use crossfade (500ms)

## Tier 2 Implementation

- `UsageStatsService` (stubbed for platform channel) checks `PACKAGE_USAGE_STATS` permission
- Opens Android system settings at `Settings.ACTION_USAGE_ACCESS_SETTINGS` via platform intent
- On iOS: graceful fallback — Tier 2 features show "Available on Android" message
- Feature lock points: Stats screen, adventure rewards, evolution placeholder, skill learning placeholder
- One-tap path to Tier 2 settings available from: Settings screen, Stats screen banner, post-hatching nudge

## Deviations from Spec

| Spec Section | Deviation | Rationale |
|-------------|-----------|-----------|
| Section 9 (Spine animations) | Used PNG frame sequences, not Spine | Flutter has limited Spine support without `spine_flutter` plugin. PNG sequences work and match the character-agnostic interface. Spine can be added later. |
| Section 7 (Adventure peek) | Peek shows timer + Chibi state, not full adventure scene | Keeping the peek lightweight avoids creating a second full-screen render. Timer + mood emoji is sufficient for Phase 1. |
| Section 13 (48hr inactivity) | Implemented as timestamp check, not background service | Background services require platform-specific code and battery permissions. Timestamp diff on app resume is simpler and sufficient for Phase 1. |
| Section 13 (Single-device binding) | Stubbed — not implemented in Phase 1 | Requires cloud authentication (Phase 2). Data model supports device ID field. |

## Known Limitations

1. **No sound design** — the app is silent. Ambient audio would enhance the experience significantly.
2. **Sprites are PNG sequences** — larger app size than Spine/atlas-based animations. Acceptable for Phase 1.
3. **Adventure environment** — uses a static background, not parallax layers. Parallax can be added without architectural changes.
4. **iOS Tier 2** — stubbed. Apple Screen Time API entitlement needed. Fallback messaging in place.
5. **No cloud sync** — all data local. Phase 2 prerequisite.
6. **Adventure rewards** — cosmetic items are tracked in state but not visually equipped on the Chibi sprite yet. Phase 2 cosmetic drawer.

## Phase 2 Architectural Considerations

- **Chibi data model** supports multiple Chibis (`List<Chibi>` in storage), shelving date, active flag — ready for D-029 collection system
- **Species enum** is extensible — 12 additional species in the asset repository
- **Settings model** stores device ID field for future single-device binding (D-033)
- **Focus session model** stores Tier level at time of session for future analytics
- **Provider architecture** can be migrated to Riverpod by replacing `ChangeNotifier` with `StateNotifier` — clear upgrade path per D-014

---

*Build log prepared by FORGE. The prototype compiles clean (0 errors, 0 warnings) and implements all Must Have features from SAGE's MoSCoW prioritisation.*
