---
type: concept
title: Push e Pull Migration
tags: [multiprocessor, load-balancing]
related: [load-balancing-e-scheduling-domains, numa]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# Push e Pull Migration

In sistemi multi-processore (SMP), il **load balancing** serve a distribuire equamente i task tra i core:
- **Push Migration**: Un processo di monitoraggio identifica un core sovraccarico e "spinge" i task verso core meno occupati.
- **Pull Migration**: Un core vuoto o sottoutilizzato "tira" (preleva) un task dalla coda di un altro core sovraccarico.