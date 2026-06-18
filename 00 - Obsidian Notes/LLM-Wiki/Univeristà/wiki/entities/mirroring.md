---
type: entity
title: Mirroring
tags: [storage, reliability]
related: [raid, striping]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
Il **Mirroring** è una tecnica di ridondanza in cui i dati vengono duplicati identicamente su due o più dischi fisici.

### Vantaggi e Svantaggi
- **Affidabilità**: Se un disco guasta, i dati sono ancora disponibili sull'altro (es. RAID 1).
- **Prestazioni**: Può velocizzare le letture (lettura parallela dai duplicati), ma le prestazioni di scrittura sono limitate dalla velocità del disco più lento.
- **Capacità**: Dimezza la capacità utile totale del sistema (es. due dischi da 1TB forniscono solo 1TB di spazio utile).
