---
type: entity
title: SIGPipe
tags: [signal, socket, networking, segnali]
related: [socket-programming, socket]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt", "SO/Trascrizioni/Lezione 29.txt"]
---
# SIGPIPE

`SIGPIPE` è un segnale generato dal kernel quando un processo tenta di scrivere su un canale di comunicazione (come una pipe o un socket) che è stato chiuso dall'altra estremità (peer remoto).

### Comportamento e Gestione
Il comportamento predefinito di `SIGPIPE` è la terminazione del processo. Tuttavia, il segnale può essere gestito o prevenuto attraverso diversi meccanismi:

- **Maschere e Handler:** Può essere gestito tramite maschere di segnale o handler specifici.
- **Flag di Sistema:** Può essere prevenuto tramite l'uso di flag specifici, come `MSG_NOSIGNAL`.