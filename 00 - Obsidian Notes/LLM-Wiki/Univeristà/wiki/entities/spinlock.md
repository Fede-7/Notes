---
type: entity
title: spinlock
tags: [sincronizzazione, busy-waiting, multiprocessore]
related: ["mutex-lock", "livelli-di-contesa"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
Uno `spinlock` è un tipo di lock che utilizza il *busy waiting*: un thread che tenta di acquisire il lock "gira" continuamente in un ciclo finché la risorsa non diventa disponibile. È efficiente per attendere periodi molto brevi (inferiori a due *context-switch*) o in sistemi multicore dove il costo del context-switch è elevato.