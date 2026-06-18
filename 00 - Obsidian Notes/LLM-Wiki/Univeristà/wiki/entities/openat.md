---
type: entity
title: openat
tags: [syscall, kernel]
related: [everything-is-a-file]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 26.txt"]
---
# openat

**openat** è una chiamata di sistema specializzata per l'apertura di file, che permette di specificare un file descriptor di directory come base per il percorso del file. È la syscall utilizzata dal sistema per mappare i nomi dei dispositivi ai driver specifici.
