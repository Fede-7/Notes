---
type: concept
title: Turnazione
tags: [sincronizzazione, algoritmi, atomicità]
related: [bounded-waiting, compare-and-swap, test-and-set]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 10.txt", "SO/Trascrizioni/Lezione 11.txt"]
---
# Turnazione

La turnazione è un protocollo di rotazione per la gestione dell'accesso alla sezione critica, basato su un sistema di turni (spesso di natura circolare). Questo meccanismo assicura che i processi in attesa ricevano l'accesso progressivamente.

## Caratteristiche principali

- **Bounded Waiting**: La turnazione garantisce che ogni processo atteso entri eventualmente nella sezione critica. Questo risolve il problema del *bounded waiting* che semplici istruzioni atomiche, come il CAS, non possono risolvere da sole.
- **Gestione della coda**: Il protocollo organizza l'accesso in modo che il "testimone" (o token) venga passato in modo ordinato tra i processi.

## Implementazione

In implementazioni a basso livello, la turnazione può essere realizzata utilizzando istruzioni atomiche per gestire il passaggio di stato tra i processi:

- **Istruzioni atomiche**: Viene spesso utilizzato `compare-and-swap` (CAS) o `test-and-set` per passare il "testimone" al prossimo processo in coda in modo sicuro e atomico.