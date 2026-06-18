---
type: concept
title: Bit-vector Allocation
tags: [file-system, storage]
related: [linked-list-allocation, grouping-allocation]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 24.txt"]
---
# Bit-vector Allocation
Metodo di gestione dello spazio libero tramite una bitmap, dove ogni bit rappresenta un blocco del disco (1 per occupato, 0 per libero). È efficiente per la ricerca di blocchi contigui ma può diventare onerosa in termini di memoria per dischi molto grandi.