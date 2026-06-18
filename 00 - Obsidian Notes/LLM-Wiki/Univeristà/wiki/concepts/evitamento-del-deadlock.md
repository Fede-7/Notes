---
type: concept
title: Evitamento del Deadlock (Deadlock Avoidance)
tags: [deadlock, algoritmi, stato-sicuro]
related: [stato-sicuro, algoritmo-del-banchiere]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-deadlock-AA25-26.txt"]
---
# Evitamento del Deadlock (Deadlock Avoidance)

A differenza della prevenzione (che è statica), l'evitamento del deadlock è una strategia dinamica. Il sistema valuta ogni richiesta di risorsa in tempo reale per assicurarsi che l'allocazione non porti il sistema in uno stato "non sicuro".

Per funzionare, l'evitamento richiede informazioni a priori: ogni processo deve dichiarare il massimo numero di risorse necessarie per tipo di risorsa. Il sistema mantiene uno **Stato Sicuro** e nega le richieste che potrebbero violarlo.
