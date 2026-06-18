---
type: concept
title: Grafo di Allocazione delle Risorse (RAG)
tags: [deadlock, grafi, visualizzazione]
related: [grafo-wait-for, deadlock]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-deadlock-AA25-26.txt"]
---
# Grafo di Allocazione delle Risorse (RAG)

Il **Grafo di Allocazione delle Risorse** è una rappresentazione grafica del sistema utilizzata per identificare i deadlock.

- **Nodi**: Il grafo è partizionato in due tipi di nodi:
    - $P = \{P_1, P_2, \dots, P_n\}$: l'insieme di tutti i processi.
    - $R = \{R_1, R_2, \dots, R_m\}$: l'insieme di tutti i tipi di risorse.
- **Archi**:
    - **Request edge** ($P_i \rightarrow R_j$): indica che il processo $P_i$ sta richiedendo una risorsa di tipo $R_j$.
    - **Assignment edge** ($R_j \rightarrow P_i$): indica che un'istanza della risorsa $R_j$ è attualmente allocata al processo $P_i$.

**Fatti di base**:
- Se il grafo non contiene cicli, non c'è deadlock.
- Se il grafo contiene un ciclo e ogni tipo di risorsa ha una sola istanza, allora esiste un deadlock.
- Se esistono multiple istanze per tipo di risorsa, la presenza di un ciclo è una condizione necessaria ma non sufficiente per il deadlock.
