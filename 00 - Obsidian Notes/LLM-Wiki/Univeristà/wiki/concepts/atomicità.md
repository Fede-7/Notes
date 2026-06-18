---
type: concept
title: atomicità
tags: [sincronizzazione, hardware]
related: [compare-and-swap, test-and-set, spin-lock]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 11.txt"]
---
# atomicità

L'atomicità è la proprietà di un'operazione che viene eseguita come un'unità indivisibile. In un contesto multi-thread, un'operazione atomica garantisce che nessun altro thread possa vedere lo stato intermedio dell'operazione.

Le istruzioni atomiche fornite dall'hardware (come CAS o TAS) sono i mattoni fondamentali per costruire tutti i meccanismi di sincronizzazione software.