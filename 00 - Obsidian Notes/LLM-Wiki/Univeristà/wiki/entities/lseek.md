---
type: entity
title: lseek()
tags: [posix, system-call, file-system]
related: [open, read, write, close, file-hole]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 23.txt"]
---
La chiamata di sistema `lseek()` viene utilizzata per manipolare l'offset di lettura/scrittura all'interno di un file. 

È fondamentale per eseguire operazioni di "rewind" (ritorno all'inizio) in scenari di comunicazione tra processi che condividono lo stesso file descriptor, permettendo a un processo di tornare a leggere dati precedentemente scritti da un altro.