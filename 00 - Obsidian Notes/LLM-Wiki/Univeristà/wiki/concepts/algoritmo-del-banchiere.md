---
type: concept
title: Algoritmo del Banchiere (Banker's Algorithm)
tags: [deadlock, algoritmi, evitamento]
related: [evitamento-del-deadlock, stato-sicuro]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-deadlock-AA25-26.txt"]
---
# Algoritmo del Banchiere (Banker's Algorithm)

L'Algoritmo del Banchiere è il metodo standard per l'evitamento del deadlock in sistemi con multiple istanze di risorse. Si basa sulla gestione di quattro strutture dati:

- **Available**: Vettore di lunghezza $m$ che indica le istanze disponibili per ogni tipo di risorsa $R_j$.
- **Max**: Matrice $n \times m$ che indica il massimo numero di risorse di tipo $R_j$ che il processo $P_i$ potrebbe richiedere.
- **Allocation**: Matrice $n \times m$ che indica le risorse di tipo $R_j$ attualmente allocate al processo $P_i$.
- **Need**: Matrice $n \times m$ definita come $Need[i,j] = Max[i,j] - Allocation[i,j]$.

L'algoritmo verifica se una richiesta di risorsa può essere concessa controllando se lo stato risultante è ancora sicuro tramite un algoritmo di sicurezza che simula l'esecuzione dei processi.
