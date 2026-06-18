---
type: entity
title: UDP
tags: [networking, protocollo]
related: [tcp, socket]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# UDP

Il protocollo `UDP` (User Datagram Protocol) è un protocollo di trasporto non orientato alla connessione (connectionless). Invia pacchetti indipendenti (datagrammi) senza garantire l'ordine o la consegna, utilizzando chiamate come `sendto` e `recvfrom` che richiedono la specifica dell'indirizzo per ogni invio.