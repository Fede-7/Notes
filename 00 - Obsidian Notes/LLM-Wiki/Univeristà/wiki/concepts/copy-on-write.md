---
type: concept
title: Copy-on-Write
tags: [file-system, consistency]
related: [journaling]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# Copy-on-Write (CoW)

Il **Copy-on-Write (CoW)** è una tecnica di gestione dei dati e di consistenza in cui i dati non vengono sovrascritti direttamente.

### Meccanismo
- Quando una modifica viene richiesta su un blocco di dati, il sistema non sovrascrive il blocco originale.
- Invece, crea una copia del blocco in una nuova posizione fisica.
- La modifica viene applicata sulla copia.
- I metadati vengono aggiornati per puntare alla nuova posizione.

### Vantaggi
- **Consistenza**: Poiché i dati originali rimangono intatti finché la nuova scrittura non è completata, il file system è intrinsecamente più resistente ai crash.
- **Snapshot**: Facilita la creazione di snapshot istantanee del file system.
