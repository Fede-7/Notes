---
type: entity
title: TCP
tags: [networking, protocollo]
related: [udp, socket]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# TCP

Il protocollo `TCP` (Transmission Control Protocol) è un protocollo di trasporto orientato alla connessione. Garantisce l'ordine dei pacchetti e la loro integrità, utilizzando un modello a flusso (stream) dove i dati vengono inviati tramite chiamate come `send` e `recv`.