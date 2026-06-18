---
type: entity
title: open()
tags: [posix, system-call, file-system]
related: [read, write, close, lseek, file-descriptor, ereditarietà-dei-file-descriptor]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 23.txt"]
---
La chiamata di sistema `open()` è utilizzata per aprire o creare un file nel sistema operativo. Restituisce un `file-descriptor`, che funge da indice numerico per identificare il file aperto all'interno del processo corrente.

In contesti multi-processo, se un file viene aperto prima di una chiamata `fork()`, il processo figlio erediterà il descrittore di file, puntando alla stessa entry nella tabella dei file aperti di sistema.