---
type: entity
title: waitpid()
tags: [system-call, process-management]
related: [fork, execve, exit, process-tree]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2a-AA25-26.txt"]
---
# waitpid()

La chiamata di sistema `waitpid()` permette a un processo padre di attendere la terminazione di un processo figlio specifico.

- **Descrizione**: `pid = waitpid(pid, &statloc, options)`
- **Parametri**:
    - `pid`: Identificativo del processo figlio da attendere.
    - `&statloc`: Puntatore a una struttura che conterrà le informazioni sullo stato del figlio terminato.
    - `options`: Opzioni aggiuntive per il comportamento dell'attesa.