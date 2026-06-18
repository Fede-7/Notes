---
type: entity
title: accept()
tags: [system-call, socket, networking, chiamate-di-sistema]
related: [socket-programming, server-concorrente, modello-client-server, descrittori-di-socket]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt", "SO/Trascrizioni/Lezione 29.txt"]
---
# accept()

La chiamata di sistema `accept()` è utilizzata dai server per accettare una nuova connessione in attesa nella coda di ascolto. È una funzione bloccante che sospende l'esecuzione finché non arriva una nuova connessione.

Una volta ricevuta la richiesta, `accept()` crea e restituisce un *nuovo* descrittore di file (FD) o descrittore di socket dedicato esclusivamente alla comunicazione con quel client specifico. Questo meccanismo permette al socket originale di rimanere libero e disponibile per continuare ad ascoltare altre richieste in entrata.