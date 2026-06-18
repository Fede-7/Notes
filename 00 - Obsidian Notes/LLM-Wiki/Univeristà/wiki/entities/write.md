---
type: entity
title: write()
tags: [posix, system-call, file-system]
related: [read, close, lseek, file-descriptor, offset-condiviso]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 23.txt"]
---
La chiamata di sistema `write()` permette di scrivere dati in un file descriptor. 

La chiamata restituisce il numero di byte effettivamente scritti, che può differire dal numero richiesto. Inoltre, ogni operazione di scrittura sposta automaticamente l'offset (la "testina") del file nella tabella dei file aperti di sistema.