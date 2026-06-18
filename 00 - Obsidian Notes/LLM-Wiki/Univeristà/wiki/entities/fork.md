---
type: entity
title: fork()
tags: ["unix", "system-calls", "processi", "sistema-operativo", "syscall", "linux", "system-call", "process-management"]
related: ["exec.md", "wait.md", "init-systemd.md", "copy-on-write", "vfork", "exec", "wait", "libc", "waitpid", "execve", "exit", "process-tree"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-5-6-AA25-26.txt", "SO/Slide/SO1-Lezioni-mem-virtuale-AA25-26.txt", "SO/Slide/SO1-Lezione2a-AA25-26.txt"]
---
# fork()

La chiamata di sistema `fork()` viene utilizzata in ambiente Unix-like (come Linux) per creare un nuovo processo figlio che è una copia quasi identica del processo chiamante (il "padre").

### Descrizione e Sintassi
- **Sintassi**: `pid = fork()`
- **Relazione**: Contribuisce alla formazione del [[process-tree]].

### Meccanismo
- **Identificativi**: Il nuovo processo (il "figlio") riceve un identificativo di processo (PID) unico, mentre il processo padre riceve il PID del figlio come valore di ritorno.
- **Spazio di indirizzamento**: Il processo figlio riceve una copia dello spazio di indirizzamento del padre (con alcune eccezioni per le risorse condivise).
- **Ottimizzazione**: Nei sistemi moderni, l'efficienza di `fork()` è migliorata grazie alla tecnica del [[copy-on-write]], che permette al padre e al figlio di condividere le stesse pagine di memoria finché non avviene una modifica.

### Uso e Rischi
- **Utilizzo comune**: Viene spesso utilizzata in combinazione con `exec()` per avviare nuovi programmi.
- **Rischi**: L'uso incontrollato di `fork()` in cicli può portare a fenomeni di esaurimento delle risorse (es. fork-bomb).