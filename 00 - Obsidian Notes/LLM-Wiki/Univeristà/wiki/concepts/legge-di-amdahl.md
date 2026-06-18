---
type: concept
title: Legge di Amdahl
tags: [prestazioni, parallelismo, algoritmi]
related: [parallelismo-di-dati, parallelismo-di-task]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# Legge di Amdahl

La **Legge di Amdahl** è una formula utilizzata per determinare il limite massimo di speed-up teorico di un'applicazione parallelizzata. Essa stabilisce che lo speed-up è limitato dalla porzione seriale del programma (la parte che non può essere parallelizzata). Se $S$ è la frazione di tempo del programma che deve essere eseguita serialmente, lo speed-up massimo è dato da $1 / (S + (1 - S) / N)$, dove $N$ è il numero di processori. Quando $N$ tende all'infinito, lo speed-up tende a $1/S$.