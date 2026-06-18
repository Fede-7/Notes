---
type: concept
title: Earliest Deadline First (EDF)
tags: [real-time, scheduling]
related: [soft-vs-hard-real-time, rate-monotonic-scheduling-rms]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# Earliest Deadline First (EDF)

L'**EDF** è un algoritmo di scheduling dinamico per sistemi real-time. Assegna la priorità più alta al task la cui scadenza (deadline) è più vicina nel tempo. È teoricamente ottimo: se l'utilizzo della CPU è inferiore al 100%, EDF garantisce che tutti i task rispettino le loro deadline.