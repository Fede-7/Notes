---
type: source
title: "Lezione 29 - Comunicazione tramite Socket e Containerizzazione"
tags: [SO1, socket, networking, docker, containerizzazione]
related: [modello-client-server, descrittori-di-socket, containerizzazione, virtualizzazione]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
authors: []
year: 2026
url: ""
venue: ""
---
# Lezione 29 - Comunicazione tramite Socket e Containerizzazione

Questa lezione approfondisce le tecniche di comunicazione tra processi (IPC) e di rete attraverso l'uso dei **socket**, analizzando sia il modello locale che quello di rete.

## Argomenti principali:
- **Socket Locali e di Rete**: Analisi della famiglia di indirizzi `AF_LOCAL` per la comunicazione interprocesso sullo stesso host e confronto con i socket di rete.
- **Modello Client-Server**: Flusso di lavoro per la creazione di server (creazione, `bind`, `listen`, `accept`) e client (`connect`).
- **Filosofia Unix**: Applicazione del principio "everything is a file" ai socket, permettendo l'uso di primitive standard come `read`, `write` e `close`.
- **Protocolli di Trasporto**: Distinzione tra `TCP` (orientato alla connessione) e `UDP` (non orientato alla connessione), con le relative chiamate di sistema (`send`/`recv` vs `sendto`/`recvfrom`).
- **Gestione dei Dati**: Tecniche per la ricezione robusta dei dati per gestire le letture parziali e la gestione dei buffer di invio.
- **Virtualizzazione vs Containerizzazione**: Confronto tra le macchine virtuali e piattaforme come `docker`, evidenziando i vantaggi di isolamento e leggerezza dei container.
- **Concorrenza nei Server**: Analisi dei modelli multi-processo (tramite `fork`) e multi-thread per la gestione delle richieste simultanee.
- **Segnali e Flag**: Uso di flag come `MSG_DONTWAIT`, `MSG_PEEK`, `MSG_WAITALL`, `MSG_NOSIGNAL` e gestione del segnale `SIGPIPE`.