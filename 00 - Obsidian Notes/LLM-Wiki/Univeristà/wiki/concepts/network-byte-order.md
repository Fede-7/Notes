---
type: concept
title: Network Byte Order
tags: [networking, endianness, protocol]
related: [endianness, conversione-byte-order]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt"]
---
# Network Byte Order
Il **Network Byte Order** è lo standard di rappresentazione dei byte per la comunicazione di rete, che utilizza l'ordine **Big Endian**. Poiché molte architetture CPU utilizzano il formato Little Endian, è necessario eseguire una conversione dei dati (es. tramite la funzione `host-to-network-long`) prima della trasmissione e dopo la ricezione.