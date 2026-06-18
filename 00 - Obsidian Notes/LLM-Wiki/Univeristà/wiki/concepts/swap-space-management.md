---
type: concept
title: Swap Space Management
tags: [memoria-virtuale, memoria-di-massa]
related: [boot-process]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt"]
---
# Swap Space Management

Lo **swap space** è un'area del disco utilizzata dal sistema operativo per estendere la memoria virtuale quando la memoria fisica (RAM) è satura.

### Gestione dello Swap
- **Memoria Anonima**: Lo swap è utilizzato principalmente per memorizzare dati non associati a file, come lo stack e l'heap dei processi.
- **Mappe di Swap**: Il kernel utilizza strutture dati per tracciare quali pagine di memoria sono state spostate sullo swap e a quale processo appartengono.
- **File di Swap vs Partizioni**: Lo swap può essere gestito tramite una partizione dedicata del disco o tramite un file speciale nel file system.