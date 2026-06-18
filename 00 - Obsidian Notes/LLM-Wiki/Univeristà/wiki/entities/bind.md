---
type: entity
title: bind()
tags: ["system-call", "socket", "networking", "chiamate-di-sistema"]
related: ["socket-programming", "modello-client-server"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt", "SO/Trascrizioni/Lezione 29.txt"]
---
# bind()

La chiamata di sistema `bind()` associa un socket a un indirizzo specifico (IP e porta) sulla macchina. È un passaggio fondamentale lato server per permettere ai client di connettersi a un punto d'accesso noto.

Inoltre, `bind()` può essere utilizzata per associare un socket a un percorso nel file system nel caso di Unix Domain Sockets. Per i socket locali, la chiamata `bind` crea effettivamente il file del socket sul file system.