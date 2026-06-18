---
type: concept
title: Mirroring
tags: [raid, ridondanza]
related: [striping, raid]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt"]
---
# Mirroring

Il **mirroring** è una tecnica di ridondanza dei dati in cui ogni blocco di dati viene scritto simultaneamente su due o più unità fisiche indipendenti.

- **Vantaggi**: Alta affidabilità; se un disco fallisce, i dati sono ancora disponibili sull'altro.
- **Svantaggi**: Costo elevato (si occupa il doppio dello spazio fisico); non migliora la velocità di scrittura (poiché il sistema deve attendere la conferma da entrambi i dischi).