---
type: entity
title: LWP (Lightweight Process)
tags: ["threads", "linux", "many-to-many", "thread", "kernel", "architettura"]
related: ["process-contention-scope-pcs", "system-contention-scope-scs", "modelli-di-threading", "upcalls"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt", "SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# Lightweight Process (LWP)

Un **Lightweight Process** (LWP) è una struttura dati intermedia utilizzata dai sistemi operativi per gestire i thread. Mentre un processo rappresenta un'unità di isolamento delle risorse, un LWP rappresenta un'unità di esecuzione che condivide lo spazio di indirizzamento e le risorse del processo padre, ma mantiene uno stato di esecuzione proprio (come il registro delle istruzioni e lo stack).

## Ruolo e Funzionamento
I LWP sono fondamentali per mappare i thread di alto livello (user-level threads) ai thread di basso livello gestiti dal kernel. Questa architettura è essenziale per implementare modelli di threading complessi, in particolare il modello *many-to-many*, dove più thread utente possono essere mappati su un pool di LWP.

L'utilizzo degli LWP permette al kernel di gestire la schedulazione dei thread in modo efficiente, senza dover creare un processo completo per ogni singola unità di esecuzione. Questo approccio garantisce una gestione più flessibile della concorrenza e del multitasking all'interno del sistema.