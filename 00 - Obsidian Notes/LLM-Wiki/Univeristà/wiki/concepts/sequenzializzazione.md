---
type: concept
title: sequenzializzazione
tags: [semaforo, sincronizzazione]
related: [semaforo, wait, signal]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 11.txt"]
---
# sequenzializzazione

La sequenzializzazione è l'uso dei semafori per ordinare l'esecuzione di thread indipendenti. 

Ad esempio, un thread P2 può essere fatto attendere finché un thread P1 non raggiunge un determinato punto di esecuzione, garantendo che le operazioni avvengano in un ordine specifico richiesto dalla logica del programma.