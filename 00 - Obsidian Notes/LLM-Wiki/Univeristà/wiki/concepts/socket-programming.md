---
type: concept
title: Socket Programming
tags: [networking, ipc, system-calls]
related: [connect, accept, bind, listen, sendto, recvfrom, berkeley-socket-distribution]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt"]
---
# Socket Programming
La **Socket Programming** è un metodo di comunicazione inter-processo (IPC) che permette a processi su macchine diverse (o sulla stessa) di dialogare tramite uno stack di comunicazione. I socket sono trattati dal kernel come file descriptor, permettendo l'uso di primitive standard come `read`, `write` e `close`.

## Componenti Chiave
- **Domini e Famiglie**: Definiti tramite costanti come `AF_UNIX` (socket locali), `AF_INET` (IPv4) e `AF_INET6` (IPv6).
- **Stili di Comunicazione**:
    - `SOCK_STREAM`: Orientato al flusso (es. TCP), garantisce l'ordine e l'integrità dei dati.
    - `SOCK_DATAGRAM`: Orientato ai pacchetti (es. UDP), invia messaggi indipendenti senza sessione persistente.
    - `SOCK_RAW`: Accesso a basso livello ai protocolli di rete.