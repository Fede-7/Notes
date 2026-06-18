---
type: concept
title: wait
tags: [semaforo, sincronizzazione]
related: [signal, semaforo]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 11.txt"]
---
# wait

L'operazione `wait` (storicamente indicata con la lettera **P**) è un'operazione atomica utilizzata nei semafori.

Essa decrementa il valore del semaforo $S$. Se il valore risultante è minore o uguale a zero, il processo viene messo in stato di attesa e inserito in una coda di attesa specifica.