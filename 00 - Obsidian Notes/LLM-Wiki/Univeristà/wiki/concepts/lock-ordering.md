---
type: concept
title: Lock Ordering
tags: [deadlock, prevenzione, concorrenza]
related: [prevenzione-del-deadlock]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-deadlock-AA25-26.txt"]
---
# Lock Ordering

Il **Lock Ordering** è una tecnica di prevenzione del deadlock che rompe la condizione di *Circular Wait*. Consiste nell'imporre un ordine totale a tutti i tipi di risorse e richiedere che ogni processo le acquisisca in ordine crescente.

**Esempio Classico: Trasferimento Bancario**
Consideriamo due account, A e B, con relativi mutex. Se due transazioni simultanee tentano di trasferire denaro tra A e B in direzioni opposte, possono verificarsi deadlock.
- Transazione 1: A $\rightarrow$ B (acquisisce lock A, poi lock B)
- Transazione 2: B $\rightarrow$ A (acquisisce lock B, poi lock A)

Con il Lock Ordering, si assegna un ID univoco agli account (es. $ID(A) < ID(B)$). Entrambe le transazioni devono acquisire prima il lock dell'account con l'ID minore. Questo garantisce che non si possa mai formare un ciclo di attesa.
