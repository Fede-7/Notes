---
type: concept
title: Corsa Critica
tags: [sincronizzazione, concorrenza]
related: [sezione-critica, mutua-esclusione]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
Una [[corsa-critica]] (race condition) si verifica quando l'ordine di esecuzione di operazioni non atomiche su dati condivisi produce risultati inconsistenti o imprevedibili. Questo accade perché l'esito finale dipende dal tempismo relativo dell'interfogliamento tra i processi.