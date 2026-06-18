---
type: concept
title: multi-processo-vs-multitread
tags: [concorrenza, processi, thread]
related: [fork, thread-switching]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# multi-processo-vs-multitread

Confronto tra due modelli di concorrenza per i server:
- **Multi-processo**: Ogni richiesta viene gestita da un nuovo processo creato tramite `fork()`. Offre un isolamento della memoria totale ma ha un overhead elevato per la creazione dei processi.
- **Multi-thread**: Il server utilizza un pool di thread che condividono lo stesso spazio di memoria. È più efficiente in termini di risorse ma richiede una gestione rigorosa delle sezioni critiche per prevenire race condition.