---
type: entity
title: SMT-set
tags: [multiprocessor, windows, hardware]
related: [load-balancing-e-scheduling-domains]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# SMT-set

Gli [[smt-set]] (Simultaneous Multithreading sets) sono insiemi di processori logici utilizzati dal sistema operativo per organizzare lo scheduling su architetture multiprocessore. Il sistema operativo utilizza questi set per cercare di mantenere un task su un processore "ideale", ottimizzando la località dei dati e riducendo i costi di migrazione tra i core.