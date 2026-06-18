---
type: entity
title: TLB
tags: [hardware, memoria, cache]
related: [mmu, paginazione, tempo-di-accesso-effettivo-eat]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-principale-AA25-26.txt"]
---
# TLB (Translation Look-aside Buffer)

La **TLB** è una memoria associativa hardware utilizzata per accelerare la traduzione degli indirizzi logici in fisici. Funziona come una cache per le entry della tabella delle pagine.

### Caratteristiche principali:
- **Ricerca Parallela**: Permette di verificare simultaneamente se una traduzione è presente nella cache.
- **ASID (Address-space identifiers)**: Identificatori univoci che permettono alla TLB di mantenere le entry di più processi contemporaneamente, evitando il flush della cache durante ogni context switch.
- **Politiche di Rimpiazzo**: Quando la TLB è piena, vengono utilizzate strategie come LRU (Least Recently Used), Round Robin o Random per gestire le entry.
- **EAT**: La TLB è essenziale per ridurre il **Tempo di Accesso Effettivo (EAT)**, poiché evita di dover accedere alla memoria principale per ogni singola traduzione.