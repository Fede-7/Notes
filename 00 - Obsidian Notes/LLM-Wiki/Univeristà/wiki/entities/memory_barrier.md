---
type: entity
title: memory_barrier
tags: [hardware, architettura, sincronizzazione]
related: [istruzioni-atomiche, lock-free]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
Una `memory_barrier` (o barriera di memoria) è un meccanismo hardware utilizzato per forzare l'ordine di esecuzione e la visibilità delle operazioni di memoria. È essenziale in architetture con modelli di memoria debolmente ordinati (weak memory models) per garantire che le modifiche effettuate da un thread siano visibili agli altri in modo coerente, prevenendo problemi di riordinamento delle istruzioni da parte della CPU o del compilatore.