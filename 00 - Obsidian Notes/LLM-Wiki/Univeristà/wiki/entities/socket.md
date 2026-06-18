---
type: entity
title: socket()
tags: [chiamate-di-sistema, networking, kernel, network, I/O]
related: [descrittori-di-socket, comunicazione-socket]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt", "SO/Trascrizioni/Lezione 25.txt"]
---
# Socket

Il **Socket** è una primitiva di comunicazione di rete che fornisce un'interfaccia standard per le applicazioni di rete. Supporta diverse modalità di trasmissione, inclusi i flussi (stream) e i pacchetti.

## La chiamata di sistema `socket()`

La chiamata di sistema `socket()` viene utilizzata per creare un nuovo descrittore di socket. Durante la creazione, è necessario specificare:
- La **famiglia di indirizzi** (es. `AF_LOCAL` o `AF_INET`).
- Il **tipo di protocollo**.