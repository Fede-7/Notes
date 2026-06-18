---
type: concept
title: Processor Affinity
tags: [multiprocessor, scheduling]
related: [push-e-pull-migration, numa]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# Processor Affinity

L'**affinità del processore** è la preferenza o il vincolo che un thread deve rimanere eseguito su un determinato processore fisico o logico.
- **Soft Affinity**: Il sistema operativo cerca di mantenere il thread sullo stesso core per sfruttare la località della cache, ma può spostarlo se necessario.
- **Hard Affinity**: Il thread è vincolato a un set specifico di core e non può essere spostato altrove.