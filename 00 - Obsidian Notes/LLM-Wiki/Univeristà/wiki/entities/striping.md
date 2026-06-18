---
type: entity
title: Striping
tags: [storage, performance]
related: [raid, mirroring]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
Lo **Striping** è una tecnica di distribuzione dei dati in cui i blocchi di un file vengono suddivisi e scritti su più dischi fisici contemporaneamente.

### Vantaggi e Svantaggi
- **Prestazioni**: Aumenta drasticamente il throughput e riduce il tempo di risposta per accessi grandi grazie al parallelismo di I/O.
- **Affidabilità**: Non offre alcuna ridondanza; il guasto di un singolo disco comporta la perdita dell'intero array (es. RAID 0).
