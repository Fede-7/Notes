---
type: concept
title: Server Iterativo
tags: [networking, concurrency]
related: [server-concorrente, coda-di-ascolto]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt"]
---
# Server Iterativo
Un **server iterativo** è un modello di gestione delle connessioni in cui il server gestisce una sola comunicazione alla volta. Il processo accetta una connessione, la elabora fino alla chiusura e solo successivamente torna in stato di ascolto per accettarne una nuova.