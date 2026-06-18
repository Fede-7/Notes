---
type: concept
title: Soft vs. Hard Real-time
tags: [real-time, scheduling]
related: [rate-monotonic-scheduling-rms, earliest-deadline-first-edf]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# Soft vs. Hard Real-time

- **Soft Real-time**: Sistemi in cui è desiderabile che i task vengano completati entro una certa scadenza, ma il mancato rispetto della deadline non causa un fallimento catastrofico (es. streaming video).
- **Hard Real-time**: Sistemi in cui il mancato rispetto di una deadline è considerato un fallimento totale del sistema, spesso con conseguenze critiche (es. sistemi di controllo aerospaziali, freni ABS).