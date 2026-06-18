---
type: concept
title: Working Set
tags: [memoria-virtuale, paging, windows]
related: [automatic-working-set-trimmer, demand-paging-con-clustering]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 20.txt"]
---
# Working Set
Il [[working-set]] rappresenta l'insieme di pagine di memoria che un processo sta utilizzando attivamente in un dato momento. In sistemi come Windows, la gestione del *working set* include limiti euristici e meccanismi come l'[[automatic-working-set-trimmer]] per garantire che i processi non consumino eccessivamente le risorse di memoria del sistema.