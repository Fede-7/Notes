---
type: entity
title: Linux
tags: ["sistema-operativo", "kernel", "os"]
related: ["bcc-toolkit", "global-page-replacement", "clock-algorithm", "active-inactive-lists"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-deadlock-AA25-26.txt", "SO/Trascrizioni/Lezione 20.txt"]
---
# Linux

**Linux** è il sistema operativo utilizzato come contesto principale per l'applicazione pratica degli strumenti di monitoraggio del deadlock, come il BCC toolkit.

## Gestione della Memoria Virtuale
Il sistema operativo Linux utilizza meccanismi di [[global-page-replacement]] per la gestione della memoria virtuale. Tra gli algoritmi principali, Linux adotta un'approssimazione del meccanismo *Least Recently Used* (LRU) nota come [[clock-algorithm]], supportata dall'uso di [[active-inactive-lists]] per monitorare l'uso delle pagine e favorire quelle più recenti.