---
type: concept
title: Paginazione
tags: [memoria, architettura]
related: [mmu, tlb, frammentazione-memoria, tabella-delle-pagine-invertite]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-principale-AA25-26.txt"]
---
# Paginazione

La **paginazione** è una tecnica di gestione della memoria che permette l'allocazione non contigua della memoria fisica, eliminando la frammentazione esterna.

- **Frame**: Blocchi di dimensione fissa della memoria fisica.
- **Pagina**: Blocchi di dimensione fissa della memoria logica.

Il sistema operativo utilizza una **tabella delle pagine** per mappare ogni pagina logica a un frame fisico. Esistono diverse varianti:
- **Paginazione Gerarchica**: Suddivisione della tabella in più livelli per risparmiare memoria.
- **Hashed Page Tables**: Utilizzate per spazi di indirizzamento molto ampi (>32 bit).
- **Tabella delle Pagine Invertite**: Una tabella per ogni pagina fisica reale, utile per risparmiare memoria ma più complessa per la condivisione.