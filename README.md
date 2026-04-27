# FocusPal — Demo Distribution

A Tamagotchi-style screen-time companion. A pixel Chibi hatches, gets named, and thrives when the phone is left alone — turning attention into care.

This repository exists solely to deliver the prototype to the assessor. It is **not** the source repository. Source artefacts and the agentic AI pipeline (5 agents: IRIS → SAGE → FORGE → ECHO → ATLAS) are documented in the submission PDF.

## Three ways to try it

### 1. Watch the walkthrough (universal — any device)
A 60–90 second guided demo of onboarding, the home screen, and the focus timer.

> **Link:** *(populated at submission)*

### 2. Open in your browser (iPhone, iPad, Mac, Windows, Android)
Live, interactive prototype. No install, no account.

> **Link:** https://sacritom.github.io/focuspal-demo/
>
> *Tier 2 (Android Usage Access) is disabled in the browser build — toggle it in Settings to see the consent flow, but the actual permission request only fires on Android.*

### 3. Install on Android (full-fidelity, including Tier 2)
A signed APK of the same build. Recommended for the most complete experience.

1. On an Android phone, open the [latest release](https://github.com/SacriTom/focuspal-demo/releases/latest) and tap `focuspal-v1.0.0.apk`.
2. When prompted, allow your browser to install unknown apps (one-time toggle).
3. Open the downloaded APK and tap **Install**.

The app is signed with a development certificate — Android may show a "Play Protect" notice; tap **Install anyway**. No data leaves the device.

## What to try
- Onboarding: choose Chibi → hold to hatch → name → preset → Tier 2 nudge → home
- Focus timer: start a 25-minute session, watch the Chibi react when you leave the app
- Settings: switch presets, fine-tune sliders, toggle Tier 2

## Known limitations
- Browser version: no SQLite-backed history (Stats screen will be empty); Tier 2 is stubbed
- iOS: no native build — use the browser version
- Phase 1 prototype: silent (no audio), static backgrounds, cosmetics tracked but not equipped

## Context
Built for NCI MSc H9CEAI assignment — five AI agents collaborating to design, build, and document a customer-engagement product. See submission PDF for the full agent pipeline, design rationale, and reflection.
