---
type: source
title: "SO1 Lezione 4-5-6 - Gestione Processi e IPC"
tags: [SO1, processi, IPC, socket]
related: ["pcb-task-control-block.md", "ipc-interprocess-communication.md", "Socket.md"]
created: 2026-06-17
updated: 2026-06-17
authors: []
year: 2025
url: ""
venue: "Corso Sistemi Operativi I"
sources: ["SO/Slide/SO1-Lezione4-5-6-AA25-26.txt"]
---
# SO1 Lezione 4-5-6 - Gestione Processi e IPC

Questa fonte copre i fondamentali della gestione dei processi e dei meccanismi di comunicazione interprocesso (IPC).

## Contenuti Principali
- **Gestione dei Processi**: Definizione di processo, layout di memoria (Text, Data, Stack, Heap, BSS), stati del processo (new, running, waiting, ready, terminated), e la struttura del [[pcb-task-control-block.md]].
- **Schedulazione e Context Switch**: Analisi della schedulazione a breve, medio e lungo termine, e l'overhead del [[context-switch.md]].
- **Creazione e Terminazione**: Meccanismi UNIX/Linux tramite chiamate di sistema come `fork()`, `exec()`, `wait()` e `exit()`.
- **IPC (Interprocess Communication)**:
    - **Shared Memory**: Modello veloce basato su memoria condivisa e il [[problema-produttore-consumatore.md]].
    - **Message Passing**: Comunicazione tramite scambio di messaggi (diretta e indiretta), sincronizzazione bloccante/non-bloccante e buffering.
    - **Pipe**: Pipe ordinarie e [[FIFO.md]] (named pipes).
    - **Socket**: Comunicazione client-server, [[Berkeley_socket_API.md]], protocolli [[TCP.md]] e [[UDP.md]].
- **Sistemi Distribuiti**: Introduzione ai sistemi distribuiti e alle reti (LAN, WAN, MAN, PAN).