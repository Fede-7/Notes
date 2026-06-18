---
type: concept
title: Cancellazione Thread
tags: [thread, concorrenza]
related: [cancellation-point]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# Cancellazione Thread

La **cancellazione di un thread** è il processo di terminazione forzata o volontaria di un'unità di esecuzione. Esistono due approcci principali:
- **Asincrona**: Il thread viene interrotto immediatamente in qualsiasi punto. È difficile da gestire in sicurezza perché può lasciare risorse in uno stato inconsistente.
- **Differita**: Il thread viene interrotto solo quando raggiunge un punto specifico nel codice, chiamato [[cancellation-point]], dove è sicuro eseguire la terminazione (es. chiamate di I/O, sleep, o sincronizzazioni esplicite).