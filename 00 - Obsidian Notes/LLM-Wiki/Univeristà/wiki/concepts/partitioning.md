---
type: concept
title: Partitioning
tags: [storage, file-system]
related: [volumes, logical-vs-physical-partitions]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
Il **partitioning** è la suddivisione di un disco fisico in unità logiche separate.

### Tipologie
- **Partizioni Fisiche**: Divisioni gestite direttamente dal controller del disco o dal firmware.
- **Partizioni Logiche**: Divisioni create sopra una partizione fisica (es. partizioni logiche in MBR), che permettono di organizzare lo spazio in modo più flessibile.
- **Relazione con i Volumi**: Mentre le partizioni sono divisioni dello spazio fisico, i volumi sono astrazioni logiche che possono essere contenute in una singola partizione o estendersi su più partizioni.
