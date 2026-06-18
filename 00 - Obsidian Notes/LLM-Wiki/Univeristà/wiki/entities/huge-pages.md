---
type: entity
title: Huge Pages
tags: [memoria, paging, performance]
related: [paginazione, frammentazione-memoria]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-principale-AA25-26.txt"]
---
# Huge Pages

Le **Huge Pages** sono pagine di memoria di grandi dimensioni (molto più grandi dei classici 4KB) supportate da sistemi operativi come Linux e Windows. 

Vengono utilizzate per migliorare le prestazioni in applicazioni che richiedono grandi quantità di memoria continua, poiché riducono il numero di entry necessarie nella tabella delle pagine e migliorano l'efficienza della TLB.