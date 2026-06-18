---
type: entity
title: CPU Scheduler
tags: [kernel, scheduling, os]
related: [dispatcher, cfs, eevdf]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# CPU Scheduler

Il [[cpu-scheduler]] è la componente del kernel responsabile della selezione dei processi o dei thread da eseguire quando la CPU è disponibile. Il suo obiettivo principale è ottimizzare l'utilizzo della CPU e garantire un comportamento accettabile del sistema in base ai criteri di valutazione scelti (es. massimizzazione del throughput o minimizzazione del tempo di risposta).

Il scheduler opera tipicamente sulla "ready queue", decidendo quale task deve ottenere il prossimo *time slice* o quale deve essere eseguito immediatamente in caso di risorse libere.