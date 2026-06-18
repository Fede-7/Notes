---
type: source
title: "SO1 Lezione 7-8 - Thread e Concorrenza"
tags: [SO1, sistemi-operativi, thread, concorrenza]
related: [modelli-di-threading, thread-specific-data, unificazione-task-thread, clone, thread-pool]
created: 2026-06-17
updated: 2026-06-17
authors: []
year: 2025
url: ""
venue: "Corso Sistemi Operativi I"
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# SO1 Lezione 7-8 - Thread e Concorrenza

Questa fonte copre i concetti fondamentali della gestione dei thread e della concorrenza nei sistemi operativi moderni. I punti chiave includono:

- **Fondamenti dei Thread**: Analisi della differenza tra concorrenza (progresso simultaneo) e parallelismo (esecuzione simultanea), e le motivazioni dell'uso dei thread (leggerezza, condivisione risorse).
- **Analisi delle Prestazioni**: Introduzione della [[legge-di-amdahl]] per determinare i limiti dello speed-up in sistemi multicore.
- **Modelli di Threading**: Studio delle mappature tra thread utente e kernel, inclusi i modelli Many-to-One, One-to-One, Many-to-Many e Two-level, con particolare attenzione ai [[LWP]] e alle [[upcalls]].
- **Threading Implicito**: Tecniche come i [[thread-pool]], OpenMP e Grand Central Dispatch.
- **Gestione dei Segnali**: Analisi del [[signal-handling]] in ambiente Unix, distinguendo tra segnali standard e real-time.
- **Meccanismi Avanzati**: Studio della [[cancellazione-thread]], dei [[thread-specific-data]] (TSD) e delle implementazioni specifiche nei kernel di Linux (tramite la chiamata di sistema [[clone()]]) e Windows (strutture [[ETHREAD]], [[KTHREAD]], [[TEB]]).