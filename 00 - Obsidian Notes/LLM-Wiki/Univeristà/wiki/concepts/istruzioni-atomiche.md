---
type: concept
title: Istruzioni Atomiche
tags: [hardware, sincronizzazione]
related: ["barriere-di-memoria"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
Le [[istruzioni-atomiche]] sono operazioni hardware eseguite in modo indivisibile. Una volta iniziata, l'istruzione non può essere interrotta da altri processi o interrupt. Sono fondamentali per costruire primitive di sincronizzazione affidabili a livello di basso livello.