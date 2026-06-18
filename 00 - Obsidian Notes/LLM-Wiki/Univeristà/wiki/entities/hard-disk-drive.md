---
type: entity
title: Hard Disk Drive (HDD)
tags: [hardware, storage]
related: [solid-state-drive, disk-scheduling]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
Il **Hard Disk Drive (HDD)** è un dispositivo di memoria secondaria di tipo meccanico. La sua architettura si basa su piatti rotanti e testine mobili, il che introduce vincoli fisici significativi sulle prestazioni di I/O.

### Caratteristiche Tecniche
- **Seek Time**: Il tempo necessario alla testina per spostarsi sulla traccia corretta. È il principale collo di bottiglia nelle operazioni di lettura/scrittura.
- **Scheduling**: A causa dei vincoli meccanici, il sistema operativo deve utilizzare algoritmi di `disk-scheduling` (come SSTF, SCAN, C-SCAN, C-LOOK) per ordinare le richieste e minimizzare i movimenti della testina.
- **Formattazione**: Sottoposto a *low-level formatting* (tracce, settori) e *high-level formatting* (blocchi logici).
