---
type: concept
title: Thread Pool
tags: [thread, performance, threading-implicito]
related: [threading-implicito, thread-pool]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# Thread Pool

Un **thread pool** è una struttura di dati che mantiene un insieme di thread pre-creati che attendono di essere assegnati a dei task. Questo approccio ottimizza le prestazioni riducendo l'overhead della creazione e distruzione dei thread per ogni operazione e aiuta a limitare il numero massimo di thread attivi, prevenendo l'esaurimento delle risorse del sistema.