---
type: concept
title: Emulazione vs Virtualizzazione
tags: [virtualizzazione, hardware]
related: [virtualizzazione]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-AA25-26.txt"]
---
# Emulazione vs Virtualizzazione

Sebbene spesso confuse, l'emulazione e la virtualizzazione sono tecniche diverse per eseguire software su hardware non nativo o multiplo.

## Emulazione
L'emulazione riproduce un'architettura hardware diversa da quella reale.
- **Funzionamento**: Il codice viene interpretato o convertito per girare sulla CPU host.
- **Vantaggi**: Grande flessibilità (permette di eseguire programmi compilati per CPU diverse).
- **Svantaggi**: Bassa efficienza e velocità a causa dell'overhead di interpretazione.
- **Esempio**: QEMU che emula ARM su architettura x86.

## Virtualizzazione
La virtualizzazione esegue sistemi operativi della stessa architettura dell'hardware reale.
- **Funzionamento**: Non simula la CPU; i guest girano nativamente sulle istruzioni della CPU host.
- **Vantaggi**: Molto più veloce dell'emulazione.
- **Svantaggi**: Meno flessibile rispetto all'emulazione (richiede architetture compatibili).