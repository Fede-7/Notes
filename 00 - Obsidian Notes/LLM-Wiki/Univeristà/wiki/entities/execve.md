---
type: entity
title: execve()
tags: [system-call, process-management]
related: [fork, waitpid, exit, process-tree]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2a-AA25-26.txt"]
---
# execve()

La chiamata di sistema `execve()` viene utilizzata per sostituire l'immagine core di un processo in esecuzione con un nuovo programma.

- **Descrizione**: `s = execve(name, argv, environp)`
- **Parametri**:
    - `name`: Nome del file eseguibile.
    - `argv`: Array degli argomenti del programma.
    - `environp`: Array delle variabili d'ambiente.