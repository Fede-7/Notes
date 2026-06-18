---
type: concept
title: Offset condiviso
tags: [file-system, multi-processing]
related: [ereditarietà-dei-file-descriptor, lseek, write]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 23.txt"]
---
L'offset condiviso è la conseguenza diretta dell'ereditarietà dei file descriptor durante una `fork()`. Poiché il padre e il figlio condividono la stessa entry nella tabella di sistema, una scrittura effettuata da uno dei due processi sposta l'offset per entrambi. 

Per ottenere offset indipendenti, i processi devono eseguire una chiamata `open()` separata dopo la `fork()`, ottenendo così entry distinte nella tabella dei file aperti.