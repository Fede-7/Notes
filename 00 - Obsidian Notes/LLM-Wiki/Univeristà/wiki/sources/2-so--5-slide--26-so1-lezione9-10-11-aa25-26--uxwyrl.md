---
type: source
title: "SO1 Lezione 9-10-11 - Scheduling della CPU"
tags: [SO1, scheduling, linux, windows, real-time]
related: [cpu-scheduler, dispatcher, cfs, eevdf, rate-monotonic-scheduling-rms, earliest-deadline-first-edf]
created: 2026-06-17
updated: 2026-06-17
authors: []
year: 2025
url: ""
venue: "Corso Sistemi Operativi I"
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# SO1 Lezione 9-10-11 - Scheduling della CPU

Questa fonte fornisce un'analisi approfondita delle tecniche e degli algoritmi di scheduling della CPU, fondamentali per la gestione delle risorse in sistemi operativi moderni.

## Contenuti Principali
- **Fondamenti dello Scheduling**: Analisi del ruolo del [[cpu-scheduler]] e del [[dispatcher]], con focus sul *context switch* e sulle metriche di valutazione (throughput, turnaround time, tempo di risposta).
- **Algoritmi Classici**: Descrizione di FCFS, SJF (e la variante preemptiva SRTF), Priority Scheduling e Round Robin.
- **Strutture Avanzate**: Analisi delle Multi-level Feedback Queues (MLFQ) e degli algoritmi basati su priorità.
- **Scheduling dei Thread**: Distinzione tra modelli *user-level* e *kernel-level*, e analisi degli scope di competizione [[process-contention-scope-pcs]] e [[system-contention-scope-scs]].
- **Sistemi Multi-processore (SMP)**: Tecniche di *load balancing* (Push e Pull migration), affinità dei processori e gestione delle architetture NUMA.
- **Scheduling Real-Time**: Studio di algoritmi come [[rate-monotonic-scheduling-rms]] e [[earliest-deadline-first-edf]], oltre alle politiche POSIX (SCHED_FIFO, SCHED_RR).
- **Implementazioni Specifiche**:
    - **Linux**: Evoluzione storica degli scheduler, dal modello $O(1)$ al [[cfs]] (Completely Fair Scheduler) e al recente [[eevdf]] (Earliest Eligible Virtual Deadline First).
    - **Windows**: Sistema di classi di priorità, mappatura numerica e meccanismi di *priority boost* e *decay*.