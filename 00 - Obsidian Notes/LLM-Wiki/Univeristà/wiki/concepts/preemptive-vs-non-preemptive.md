---
type: concept
title: Preemptive vs. Non-preemptive
tags: [scheduling, os]
related: [convoy-effect]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# Preemptive vs. Non-preemptive

- **Scheduling Non-preemptivo**: Un processo mantiene il controllo della CPU finché non termina volontariamente o non entra in uno stato di blocco (es. I/O).
- **Scheduling Preemptivo**: Il sistema operativo può interrompere un processo in esecuzione per assegnare la CPU a un altro processo (es. tramite timer hardware o interruzioni). I sistemi moderni sono quasi esclusivamente preemptivi per garantire l'interattività.