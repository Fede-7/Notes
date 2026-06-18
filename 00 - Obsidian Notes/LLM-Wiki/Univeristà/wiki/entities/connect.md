---
type: entity
title: connect()
tags: [system-call, socket, networking, chiamate-di-sistema]
related: [socket-programming, three-way-handshake, modello-client-server]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt", "SO/Trascrizioni/Lezione 29.txt"]
---
# connect()

La chiamata di sistema `connect()` viene utilizzata dal client per stabilire una connessione con un server, fornendo l'indirizzo IP e la porta di destinazione. 

In caso di socket TCP, questa chiamata avvia il processo di stabilizzazione della connessione (es. il *Three-way Handshake*).