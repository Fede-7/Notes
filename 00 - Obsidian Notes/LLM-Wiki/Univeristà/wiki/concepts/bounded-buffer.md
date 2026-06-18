---
type: concept
title: Bounded Buffer
tags: [sincronizzazione, produttore-consumatore]
related: ["problema-del-produttore-consumatore"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
Il [[bounded-buffer]] è un classico problema di sincronizzazione (produttore-consumatore) in cui un produttore aggiunge elementi a un buffer di dimensione limitata e un consumatore li rimuove. Il sistema deve garantire che il produttore non sovrascriva dati e che il consumatore non legga dati non ancora prodotti.