---
type: entity
title: EEVDF (Earliest Eligible Virtual Deadline First)
tags: [linux, scheduling, real-time]
related: [virtual-deadline-vd, eligibility-e-lag, cfs]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# EEVDF (Earliest Eligible Virtual Deadline First)

L'[[eevdf]] è il nuovo scheduler introdotto in Linux 6.6. È progettato per combinare i vantaggi della fairness del CFS con le garanzie di deadline dei sistemi real-time. 

Il meccanismo si basa su due concetti chiave:
- **Eligibility**: Determina se un task ha diritto a ricevere tempo di CPU in base alla sua priorità e al tempo già ricevuto.
- **Virtual Deadline (VD)**: Calcola una scadenza virtuale per i task eligibili, selezionando quello con la scadenza più vicina per l'esecuzione.