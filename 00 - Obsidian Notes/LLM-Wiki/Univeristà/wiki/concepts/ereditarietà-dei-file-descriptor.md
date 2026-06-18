---
type: concept
title: Ereditarietà dei file descriptor
tags: [fork, file-system, multi-processing]
related: [open, lseek, offset-condiviso, file-descriptor]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 23.txt"]
---
Quando un processo viene duplicato tramite la chiamata `fork()`, i file descriptor vengono ereditati dal processo figlio. 

Poiché il figlio eredita il descrittore, entrambi i processi puntano alla stessa entry nella tabella dei file aperti di sistema. Questo comporta la condivisione dello stato del file, inclusa la posizione della "testina" di lettura/scrittura.