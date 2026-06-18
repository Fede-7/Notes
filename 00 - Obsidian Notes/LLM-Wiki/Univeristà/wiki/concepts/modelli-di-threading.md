---
type: concept
title: Modelli di Threading
tags: [thread, kernel, architettura]
related: [user-thread, kernel-thread, lwp, upcalls]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# Modelli di Threading

I modelli di threading descrivono come i thread gestiti dalle librerie utente (user threads) vengono mappati sui thread gestiti dal kernel (kernel threads). I principali modelli includono:

- **Many-to-One**: Molti thread utente mappati su un unico thread kernel. Semplice, ma un blocco in un thread utente (es. I/O) blocca l'intero processo.
- **One-to-One**: Ogni thread utente ha un proprio thread kernel. Offre maggiore scalabilità e stabilità, ma può avere un overhead maggiore.
- **Many-to-Many**: Molti thread utente mappati su un pool di thread kernel. Offre un equilibrio tra i due modelli precedenti.
- **Two-level**: Una combinazione dei modelli precedenti che permette di mappare thread utente su thread kernel in modo flessibile.

In questo contesto, le **upcalls** sono meccanismi che permettono al kernel di comunicare con l'applicazione per gestire i blocchi dei thread nei modelli più complessi.