---
type: source
title: "Lezione 28: Socket Programming e Containerizzazione"
tags: [socket, networking, docker, containerizzazione]
related: [socket-programming, containerizzazione, endianness, network-byte-order]
created: 2026-06-17
updated: 2026-06-17
authors: []
year: 2026
url: ""
venue: ""
sources: ["SO/Trascrizioni/Lezione 28.txt"]
---
# Lezione 28: Socket Programming e Containerizzazione

Questa lezione approfondisce i meccanismi di comunicazione tra processi tramite **Socket Programming**, coprendo sia le comunicazioni locali (Unix Domain Sockets) che quelle di rete (Internet Sockets). Vengono analizzati i modelli di gestione delle connessioni (iterativo vs concorrente), le sfide della rappresentazione dei dati in rete (endianness) e le basi della containerizzazione tramite **Docker**.

## Argomenti principali
- **Socket Programming**: Analisi dei socket come file descriptor e delle operazioni fondamentali (`socket`, `bind`, `listen`, `accept`, `connect`).
- **Comunicazione Locale vs Rete**: Differenze tra `AF_UNIX` e `AF_INET`/`AF_INET6`.
- **Modelli di Server**: Confronto tra server iterativi e server concorrenti, inclusa la gestione della coda di ascolto (backlog).
- **Endianness e Network Byte Order**: Necessità di conversione dei dati (es. `host-to-network-long`) per garantire la portabilità tra architetture diverse.
- **Stream vs Datagramma**: Differenze tra comunicazioni orientate al flusso (TCP) e a pacchetto (UDP), inclusi i problemi di troncamento dei messaggi.
- **Containerizzazione**: Introduzione a Docker e all'isolamento degli ambienti tramite namespace del kernel.