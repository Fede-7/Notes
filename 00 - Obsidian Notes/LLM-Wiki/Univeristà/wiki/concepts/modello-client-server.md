---
type: concept
title: Modello Client-Server
tags: [architettura, networking]
related: [socket, connect, accept, bind, listen]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# Modello Client-Server

Architettura di comunicazione in cui un processo (il **server**) rimane in ascolto su una porta specifica per fornire servizi, mentre altri processi (i **client**) avviano connessioni attive verso il server per richiedere tali servizi. 

Il flusso tipico prevede:
1. Il server crea un socket e lo associa a un indirizzo tramite `bind`.
2. Il server entra in modalità ascolto tramite `listen`.
3. Il client avvia una connessione tramite `connect`.
4. Il server accetta la connessione tramite `accept`, ottenendo un nuovo descrittore per la comunicazione bidirezionale.