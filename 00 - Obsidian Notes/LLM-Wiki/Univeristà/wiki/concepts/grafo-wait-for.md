---
type: concept
title: Grafo Wait-for
tags: [deadlock, grafi]
related: [grafo-di-allocazione-delle-risorse]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-deadlock-AA25-26.txt"]
---
# Grafo Wait-for

Il **Grafo Wait-for** è una variante semplificata del Grafo di Allocazione delle Risorse utilizzata quando ogni tipo di risorsa ha una **singola istanza**.

In questo grafo:
- I nodi rappresentano solo i processi.
- Un arco diretto $P_i \rightarrow P_j$ indica che il processo $P_i$ è in attesa di una risorsa attualmente detenuta dal processo $P_j$.

Il rilevamento dei cicli in questo grafo permette di identificare immediatamente la presenza di deadlock. La complessità per rilevare un ciclo in un grafo con $n$ vertici è di $O(n^2)$.
