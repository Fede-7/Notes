---
type: concept
title: Process-Contention Scope (PCS)
tags: [threads, scheduling]
related: [system-contention-scope-scs, lwp]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# Process-Contention Scope (PCS)

Il **Process-Contention Scope (PCS)** descrive un modello di scheduling in cui la competizione per la CPU avviene solo tra i thread appartenenti allo stesso processo. In questo modello, il kernel vede solo i processi, e la gestione dei thread è delegata interamente alla libreria utente.