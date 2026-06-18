---
type: concept
title: Hybrid Indexed Allocation
tags: [file-system, storage]
related: [multi-level-indexing, mixed-indexing]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 24.txt"]
---
# Hybrid Indexed Allocation
Modello di allocazione (tipico dei sistemi Unix) che combina puntatori diretti (per file piccoli) e puntatori indiretti (per file di dimensioni crescenti) all'interno dello stesso blocco indice per ottimizzare l'overhead.