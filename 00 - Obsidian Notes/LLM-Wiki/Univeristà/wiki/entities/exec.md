---
type: entity
title: exec()
tags: [unix, system-calls, processi, syscall, linux]
related: [fork.md, fork, wait, libc]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-5-6-AA25-26.txt"]
---
# exec()

La chiamata di sistema `exec()` sostituisce l'immagine di memoria (il corpo del programma) del processo corrente con un nuovo programma.

## Funzionamento
A differenza di `fork()`, la chiamata `exec()` non crea un nuovo processo, ma sovrascrive lo spazio di indirizzamento del processo attualmente in esecuzione con il codice del nuovo eseguibile.

## Relazione con fork()
La combinazione di `fork()` seguita da `exec()` è il metodo standard per avviare nuovi programmi in modo indipendente in ambiente POSIX.