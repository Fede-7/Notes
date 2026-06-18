---
type: entity
title: RAID (Redundant Array of Inexpensive Disks)
tags: ["storage", "hardware", "reliability", "memoria-di-massa"]
related: ["mirroring", "striping", "block-level-striping", "distributed-parity", "nested-raid", "solaris-zfs"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt", "SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt"]
---
# RAID (Redundant Array of Independent Disks)

Il **RAID** è un'architettura di configurazione che combina più unità di memoria di massa fisiche in un unico volume logico per migliorare le prestazioni, l'affidabilità o entrambi.

### Tecniche Fondamentali
Il funzionamento del RAID si basa su due concetti chiave:

- **Mirroring**: Duplicazione dei dati su più dischi. Garantisce la **ridondanza** (protezione contro il guasto dei dischi tramite duplicazione) ma non aumenta la velocità di scrittura.
- **Striping**: Distribuzione dei dati su più dischi. Aumenta il **parallelismo** e il throughput tramite la distribuzione dei dati su più unità, ma non fornisce affidabilità.

### Livelli Comuni
Esistono diversi livelli che combinano diverse tecniche di gestione dei dati per bilanciare performance e sicurezza:

- **RAID 0**: Solo striping (massima performance, nessuna ridondanza).
- **RAID 1**: Solo mirroring (alta ridondanza, bassa performance di scrittura).
- **RAID 5**: Striping con parità distribuita (bilanciamento tra performance e ridondanza).
- **RAID 6**: Striping con doppia parità distribuita (tolleranza ai guasti di due dischi).
- **RAID 1+0 (Striped Mirrors)**: Combinazione di mirroring e striping; preferibile per sistemi I/O intensi.