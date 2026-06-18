---
type: concept
title: Rilevamento e Ripristino del Deadlock (Detection & Recovery)
tags: [deadlock, gestione]
related: [deadlock]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-deadlock-AA25-26.txt"]
---
# Rilevamento e Ripristino del Deadlock (Detection & Recovery)

In alcuni sistemi (come UNIX), il deadlock viene ignorato. In altri, il sistema permette l'ingresso in uno stato di deadlock e interviene successivamente.

### Rilevamento
- **Istanza Singola**: Si utilizza il **Grafo Wait-for**. Il sistema cerca periodicamente cicli nel grafo.
- **Multiple Istanze**: Si utilizzano strutture simili a quelle dell'Algoritmo del Banchiere per verificare se il sistema è in uno stato di deadlock.

### Ripristino
Una volta rilevato il deadlock, il sistema deve intervenire tramite:
1.  **Terminazione di Processi**: Abortare uno o più processi coinvolti. Si può abortare tutti i processi in deadlock o uno alla volta finché il ciclo non viene eliminato. La scelta della "vittima" si basa su criteri come priorità, tempo di esecuzione e risorse utilizzate.
2.  **Prelazione di Risorse**: Sottrarre risorse dai processi coinvolti. Questo richiede un meccanismo di **Rollback** per riportare il processo a uno stato sicuro precedente.
