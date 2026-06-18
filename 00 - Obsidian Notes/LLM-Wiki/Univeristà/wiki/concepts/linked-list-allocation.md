---
type: concept
title: Linked List Allocation
tags: [file-system, storage]
related: [bit-vector-allocation, grouping-allocation]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 24.txt"]
---
# Linked List Allocation
Rappresentazione dei blocchi liberi come una lista concatenata. È efficiente per l'allocazione di un singolo blocco ma inefficiente per la ricerca di blocchi contigui, poiché richiede la scansione della lista in memoria secondaria.