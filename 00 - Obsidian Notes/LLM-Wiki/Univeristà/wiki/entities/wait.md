---
type: entity
title: wait()
tags: ["unix", "system-calls", "processi", "syscall", "sincronizzazione"]
related: ["fork.md", "SIGCHLD.md", "fork", "exec"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-5-6-AA25-26.txt"]
---
# wait()

La chiamata di sistema `wait()` è un costrutto di sincronizzazione che permette a un processo padre di attendere la terminazione di uno dei suoi processi figli.

### Scopo
- **Gestione dei processi**: Serve a prevenire la creazione di processi "zombie" e a evitare la formazione di processi orfani.
- **Recupero dello stato**: Permette al processo padre di recuperare lo stato di uscita del figlio terminato.

### Sincronizzazione
È fondamentale per la corretta gestione del ciclo di vita dei processi in programmi multi-processo.