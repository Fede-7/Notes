---
type: entity
title: CFS (Completely Fair Scheduler)
tags: [linux, scheduling, fairness]
related: [vruntime, red-black-tree, o1-scheduling]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# CFS (Completely Fair Scheduler)

Il [[cfs]] è lo scheduler di default del kernel Linux dal 2.6.23. A differenza degli scheduler precedenti basati su code a priorità fisse, il CFS mira a garantire una "fairness" (equità) pesata sulla priorità.

Utilizza il concetto di [[vruntime]] per tracciare quanto tempo ogni task ha ricevuto rispetto alla sua priorità. I task con priorità più alta vedono il loro `vruntime` scorrere più lentamente, permettendo loro di ottenere più tempo di CPU. La struttura dati utilizzata per organizzare i task è un [[red-black-tree]].