---
type: entity
title: close()
tags: [posix, system-call, file-system]
related: [open, read, write]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 23.txt"]
---
La chiamata di sistema `close()` chiude un file descriptor, liberando le risorse associate. Questa operazione garantisce il riversamento (flush) dei dati rimanenti dalla memoria buffer alla memoria secondaria.