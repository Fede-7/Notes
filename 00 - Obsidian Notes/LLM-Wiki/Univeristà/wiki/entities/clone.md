---
type: entity
title: clone()
tags: [linux, system-call, thread]
related: [unificazione-task-thread, task_struct]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# clone()

In Linux, la chiamata di sistema **clone()** è il meccanismo fondamentale per creare nuovi task. A differenza della chiamata `fork()`, che crea un processo quasi identico, `clone()` permette di specificare quali risorse devono essere condivise tra il processo padre e il figlio tramite diverse flag (es. `CLONE_VM`, `CLONE_FS`, `CLONE_SIGHAND`).

Se tutte le flag di condivisione sono impostate, il comportamento di `clone()` è equivalente alla creazione di un thread; se nessuna è impostata, è equivalente a `fork()`. Questo approccio porta alla [[unificazione-task-thread]] nel kernel Linux.