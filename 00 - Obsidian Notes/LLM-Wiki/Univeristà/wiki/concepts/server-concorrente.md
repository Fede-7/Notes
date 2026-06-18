---
type: concept
title: Server Concorrente
tags: [networking, concurrency, threads]
related: [server-iterativo, coda-di-ascolto]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt"]
---
# Server Concorrente
Un **server concorrente** è un modello in cui il server lancia un nuovo thread (o processo) per ogni connessione accettata. Questo permette di gestire più comunicazioni simultanee, poiché il thread principale rimane libero di accettare nuove richieste dalla coda di ascolto mentre i thread figli gestiscono le sessioni attive.