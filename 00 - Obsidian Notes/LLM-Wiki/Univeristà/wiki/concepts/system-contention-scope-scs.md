---
type: concept
title: System-Contention Scope (SCS)
tags: [threads, scheduling, linux, windows]
related: [process-contention-scope-pcs, lwp]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# System-Contention Scope (SCS)

Il **System-Contention Scope (SCS)** descrive un modello in cui la competizione per la CPU avviene tra tutti i thread di tutti i processi del sistema. In questo modello, il kernel è consapevole di ogni singolo thread e lo schedula indipendentemente. È il modello adottato dai sistemi operativi moderni come Linux e Windows.