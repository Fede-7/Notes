---
type: concept
title: Coda di Ascolto
tags: [networking, socket, server]
related: [server-iterativo, server-concorrente, listen]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt"]
---
# Coda di Ascolto
La **coda di ascolto** (backlog) è una struttura dati utilizzata dal kernel per memorizzare le richieste di connessione in attesa di essere accettate dal server tramite la chiamata `accept()`. Se la coda è satura, le nuove richieste di connessione potrebbero essere rifiutate.