---
type: concept
title: problema-produttore-consumatore
tags: [semaforo, sincronizzazione, risorse]
related: [semaforo-contatore, semaforo-binario, sequenzializzazione]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 11.txt"]
---
# problema-produttore-consumatore

Il problema del produttore-consumatore è un classico esempio di sincronizzazione in cui più thread condividono un buffer limitato.

Per risolverlo con i semafori si utilizzano tre strumenti:
1. Un **mutex** (o semaforo binario) per garantire la mutua esclusione sull'accesso alla struttura dati.
2. Un semaforo contatore `empty` (inizializzato a $n$) per tracciare gli slot liberi.
3. Un semaforo contatore `full` (inizializzato a 0) per tracciare gli slot occupati.