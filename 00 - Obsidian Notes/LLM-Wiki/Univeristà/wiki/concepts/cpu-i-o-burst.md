---
type: concept
title: CPU-I/O Burst
tags: [scheduling, performance]
related: [exponential-averaging]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# CPU-I/O Burst

Il ciclo di vita di un processo è caratterizzato da alternanze tra **CPU Burst** (periodi di calcolo intensivo in cui il processo occupa la CPU) e **I/O Burst** (periodi in cui il processo attende il completamento di operazioni di input/output). Gli algoritmi di scheduling cercano di prevedere la durata dei burst CPU per ottimizzare l'allocazione delle risorse.