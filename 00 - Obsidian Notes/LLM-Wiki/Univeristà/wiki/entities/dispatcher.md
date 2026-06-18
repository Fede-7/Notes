---
type: entity
title: Dispatcher
tags: [kernel, scheduling, context-switch]
related: [cpu-scheduler]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# Dispatcher

Il [[dispatcher]] è il modulo del sistema operativo che effettua il passaggio effettivo del controllo della CPU a un processo selezionato dal [[cpu-scheduler]]. 

Le sue funzioni principali includono:
- Eseguire il *context switch* (salvataggio e ripristino dello stato del processo).
- Gestire il passaggio dalla modalità kernel alla modalità utente.
- Gestire le interruzioni di sistema.

Mentre il scheduler decide "chi" deve eseguire, il dispatcher si occupa del "come" avviene il passaggio fisico.