---
type: concept
title: Volumes
tags: [storage, abstraction]
related: [partitioning]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
Un **volume** è un'astrazione logica fornita dal sistema operativo sopra le partizioni fisiche del disco.

### Caratteristiche
- **Flessibilità**: Un volume può essere contenuto in una singola partizione o accorpare più partizioni diverse.
- **Astrazione**: Permette al sistema operativo di gestire lo spazio di archiviazione in modo indipendente dalla geometria fisica del disco.
- **Esempio**: In Windows, le lettere di unità (C:, D:) rappresentano volumi che possono essere mappati su diverse partizioni o dischi fisici.
