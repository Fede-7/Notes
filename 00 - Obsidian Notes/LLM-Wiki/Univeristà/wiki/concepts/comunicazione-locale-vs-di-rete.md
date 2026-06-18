---
type: concept
title: Comunicazione Locale vs di Rete
tags: [networking, IPC]
related: [af_local, socket]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# Comunicazione Locale vs di Rete

Esiste una distinzione fondamentale tra i socket utilizzati per la comunicazione tra processi sullo stesso host e quelli utilizzati per la rete:
- **Socket Locali (`AF_LOCAL`)**: Più semplici, non richiedono protocolli di routing complessi e sono ottimizzati per l'IPC locale.
- **Socket di Rete**: Richiedono l'uso di indirizzi IP e porte, gestiscono la frammentazione dei pacchetti, il routing e i protocolli di trasporto come TCP o UDP.