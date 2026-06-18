---
type: entity
title: Windows
tags: [os, kernel]
related: [working-set, demand-paging-con-clustering]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 20.txt"]
---
# Windows
Il sistema operativo Windows gestisce la memoria virtuale attraverso il concetto di [[working-set]], che definisce l'insieme di pagine necessarie a un processo. Il sistema utilizza il [[demand-paging-con-clustering]] per caricare pagine adiacenti alla richiesta e include meccanismi come l'[[automatic-working-set-trimmer]] per recuperare memoria dai processi che superano i limiti euristici.