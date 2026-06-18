---
type: source
title: "SO1 Lezioni Memoria Virtuale AA25-26"
tags: [memoria-virtuale, sistemi-operativi, paging]
related: ["memoria-virtuale", "page-replacement", "allocazione-di-memoria-kernel"]
created: 2026-06-17
updated: 2026-06-17
authors: []
year: 2025
url: ""
venue: ""
sources: ["SO/Slide/SO1-Lezioni-mem-virtuale-AA25-26.txt"]
---
# SO1 Lezioni Memoria Virtuale AA25-26

Questa fonte fornisce una trattazione approfondita dei meccanismi di gestione della memoria virtuale nei sistemi operativi moderni. I contenuti principali includono:

- **Fondamenti della Memoria Virtuale**: Concetti di separazione tra memoria logica e fisica, gestione delle tabelle delle pagine e meccanismi di *demand paging*.
- **Gestione dei Page Fault**: Analisi del ciclo di gestione delle interruzioni per le pagine non residenti, inclusi i requisiti hardware per il riavvio delle istruzioni (*instruction restart*).
- **Algoritmi di Sostituzione delle Pagine**: Studio dettagliato di algoritmi come FIFO, OPT, LRU (e le sue implementazioni tramite contatori o stack), LFU, MFU e l'algoritmo *Second-Chance* (Clock).
- **Modelli di Località e Performance**: Analisi del *Working Set Model*, della *Page Fault Frequency* (PFF) e del fenomeno del *thrashing*.
- **Allocazione della Memoria Kernel**: Descrizione del *Buddy System* e dello *Slab Allocator* (incluse le varianti SLOB, SLAB, SLUB) per la gestione della memoria fisica e degli oggetti del kernel.
- **Ottimizzazioni Hardware e OS**: Discussione sulla *TLB Reach*, sulle tabelle delle pagine invertite, sul *pinning* per l'I/O e sulle implementazioni specifiche di Linux, Windows e Solaris.