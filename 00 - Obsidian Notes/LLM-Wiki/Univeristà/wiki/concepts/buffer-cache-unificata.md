---
type: concept
title: Buffer Cache Unificata
tags: [os, memory, performance]
related: [double-caching]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# Buffer Cache Unificata

La **Buffer Cache Unificata** è un'architettura di memoria in cui la cache del file system e la cache delle pagine del sistema di memoria virtuale sono integrate in un'unica struttura.

### Problema risolto: Double Caching
Senza unificazione, il sistema poteva soffrire di *double caching*: lo stesso dato veniva memorizzato sia nella *buffer cache* (per il file system) che nella *page cache* (per la memoria virtuale), sprecando memoria preziosa.

### Vantaggi
- **Efficienza della memoria**: Riduce la duplicazione dei dati.
- **Coerenza**: Garantisce che le modifiche ai dati siano visibili immediatamente a tutti i processi che accedono al file tramite diverse vie (es. lettura diretta o tramite mappatura di memoria).
