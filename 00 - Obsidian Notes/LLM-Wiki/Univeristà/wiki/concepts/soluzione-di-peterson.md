---
type: concept
title: Soluzione di Peterson
tags: ["sincronizzazione", "algoritmi-software", "algoritmi"]
related: ["mutua-esclusione", "progresso", "bounded-waiting"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
# Soluzione di Peterson

La [[soluzione-di-peterson]] è un algoritmo software classico e teorico di sincronizzazione progettato per garantire la mutua esclusione tra due processi. L'algoritmo gestisce l'accesso alla sezione critica utilizzando due tipi di variabili:
- Un **array di flag booleani** per indicare l'intenzione di entrare nella sezione critica;
- Una **variabile di precedenza** (indicata come `turn`) per gestire il turno dei processi.

### Proprietà garantite
La soluzione garantisce correttamente tutte e tre le proprietà fondamentali della sincronizzazione:
- **Mutua esclusione**: assicura che non più di un processo alla volta possa accedere alla sezione critica.
- **Progresso**: garantisce che i processi possano entrare nella sezione critica senza essere bloccati da processi che non la stanno utilizzando.
- **Bounded waiting**: garantisce che ogni processo debba attendere per un tempo limitato prima di poter accedere alla sezione critica.

### Estensioni
Sebbene sia progettato originariamente per due processi, l'algoritmo può essere esteso a $n$ processi utilizzando variabili di competizione e variabili *victim*.