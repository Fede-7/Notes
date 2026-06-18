---
type: entity
title: compare_and_swap
tags: [hardware, istruzioni-atomiche, lock-free]
related: [istruzioni-atomiche, barriere-di-memoria, lock-free]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
`compare_and_swap` (spesso abbreviato come CAS) è un'istruzione hardware atomica che confronta il valore attuale di una variabile con un valore atteso. Se i due valori corrispondono, la variabile viene aggiornata con un nuovo valore. È la base per molte strutture dati e algoritmi di sincronizzazione *lock-free*.