---
type: concept
title: Thread-Specific Data (TSD)
tags: [thread, memoria, concorrenza]
related: [thread-switching, pthread_key_t]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# Thread-Specific Data (TSD)

Il **Thread-Specific Data (TSD)** è un meccanismo che permette di associare dati privati a ogni thread, pur utilizzando variabili globali o chiavi condivise. In pratica, ogni thread ha il proprio valore unico per una determinata chiave, simile a come le variabili locali sono private a ogni invocazione della funzione, ma persistono per tutta la durata del thread.

In POSIX, questo è gestito tramite API come `pthread_key_create`, `pthread_setspecific` e `pthread_getspecific`, utilizzando il tipo di dato `pthread_key_t`.