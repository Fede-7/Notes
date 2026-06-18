---
type: concept
title: Three-way Handshake
tags: [tcp, networking, connection]
related: [connect]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt"]
---
# Three-way Handshake
Il **Three-way Handshake** è il processo di stabilizzazione della connessione TCP che avviene durante la chiamata di sistema `connect()`. Consiste in uno scambio di tre pacchetti tra client e server per sincronizzare i numeri di sequenza e confermare la disponibilità della connessione.