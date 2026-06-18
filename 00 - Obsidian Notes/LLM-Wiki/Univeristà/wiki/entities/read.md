---
type: entity
title: read()
tags: [posix, system-call, file-system]
related: [write, close, lseek, pipe, file-descriptor]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 23.txt"]
---
La chiamata di sistema `read()` viene utilizzata per leggere dati da un file descriptor. 

A differenza delle `pipe`, la lettura su un file non blocca il processo se il file è vuoto o se è stata raggiunta la fine (EOF); in questi casi, la chiamata restituisce semplicemente un valore vuoto o indica la fine del flusso.