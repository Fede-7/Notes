---
type: concept
title: lettura-parziale
tags: [socket, networking]
related: [lettura-robusta, recv]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# lettura-parziale

La lettura parziale è un fenomeno in cui una chiamata di sistema come `recv` restituisce meno byte di quelli effettivamente richiesti dal programma. Ciò accade perché il kernel legge solo la quantità di dati attualmente disponibile nel buffer di ricezione del socket. Per gestire correttamente i messaggi completi, il programmatore deve implementare logiche di controllo dell'offset.