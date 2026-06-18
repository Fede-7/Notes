---
type: concept
title: Dirty Bit
tags: [file-system, consistenza]
related: [journaling, dirty-bit-recovery]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 25.txt"]
---
# Dirty Bit
Il **Dirty Bit** è un flag utilizzato dal sistema operativo per segnalare che un blocco di dati o un metadato in memoria è stato modificato e non è ancora stato scritto sul disco. È fondamentale per identificare le modifiche da "materializzare" e per il recupero in caso di crash.