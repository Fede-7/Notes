---
type: concept
title: Memoria Anonima
tags: ["memory", "swap", "memoria", "kernel"]
related: ["swap-space", "swap-maps", "scrittura-sincrona-vs-asincrona"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt", "SO/Trascrizioni/Lezione 25.txt"]
---
# Memoria Anonima

La **memoria anonima** è la porzione di memoria dinamica utilizzata dai processi che non è mappata direttamente su un file specifico del file system. A differenza della memoria mappata sui file, la memoria anonima richiede algoritmi di sostituzione pagina differenti.

### Caratteristiche
- **Contenuto**: Include lo stack, l'heap e altre aree di memoria non inizializzate o modificate dai processi.
- **Swapping**: Poiché non esiste un file fisico "pre-esistente" per queste pagine, il sistema operativo deve gestirle tramite lo **swap space** quando la memoria fisica è esaurita.
- **Differenza con le pagine di testo**: A differenza delle pagine di testo (che sono immutabili e possono essere ricaricate dal file eseguibile), le pagine anonime devono essere scritte nello swap per essere liberate dalla RAM.