---
type: concept
title: Convoy Effect
tags: [scheduling, performance]
related: [fcfs]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# Convoy Effect

Il **Convoy Effect** è un fenomeno che si verifica negli algoritmi di scheduling non-preemptivi (come FCFS). Accade quando un processo lungo (CPU-bound) occupa la CPU, causando la formazione di una "coda" di processi brevi (I/O-bound) che rimangono bloccati in attesa, riducendo drasticamente il parallelismo e l'efficienza del sistema.