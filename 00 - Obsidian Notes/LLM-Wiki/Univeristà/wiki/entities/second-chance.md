---
type: entity
title: Second-Chance
tags: [algoritmi, memoria-virtuale]
related: [lru, bit-di-riferimento]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-virtuale-AA25-26.txt"]
---
# Second-Chance

L'algoritmo **Second-Chance** (spesso implementato come algoritmo *Clock*) è un'approssimazione efficiente di LRU. Utilizza una coda circolare e il [[bit-di-riferimento]] per dare una "seconda possibilità" alle pagine recentemente accedite prima di essere rimpiazzate.