---
type: entity
title: listen()
tags: ["system-call", "socket", "networking", "chiamate-di-sistema"]
related: ["socket-programming", "coda-di-ascolto", "modello-client-server"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt", "SO/Trascrizioni/Lezione 29.txt"]
---
# listen()

La chiamata di sistema `listen()` mette un socket in modalità ascolto, indicando al kernel di iniziare ad accettare connessioni in entrata. Questa operazione permette al socket di ricevere richieste di connessione e non è bloccante.

### Caratteristiche principali
- **Backlog**: La chiamata accetta un parametro `backlog` che definisce la dimensione della coda delle richieste in attesa, associando il socket a tale coda.