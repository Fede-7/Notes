---
type: source
title: "Lezione 12-13: Sincronizzazione e Liveness"
tags: [sincronizzazione, sistemi-operativi, deadlock, liveness]
related: [sincronizzazione, sezione-critica, mutua-esclusione, inversione-di-priorità]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
authors: []
year: 2025
url: ""
venue: ""
---
Questa fonte copre i meccanismi fondamentali di sincronizzazione tra processi e thread. I temi principali includono:
- **Problema della Sezione Critica**: Requisiti di mutua esclusione, progresso e *bounded waiting*.
- **Soluzioni Software e Hardware**: Algoritmo di Peterson, istruzioni atomiche come `test_and_set` e `compare_and_swap` (CAS), e l'uso di barriere di memoria.
- **Primitive di Sincronizzazione**: Mutex, semafori (contatori e binari) e monitor (variabili di condizione).
- **Liveness e Performance**: Analisi dell'inversione di priorità (caso studio Mars Pathfinder) e valutazione delle performance basata sui livelli di contesa (approcci ottimistici vs pessimistici).