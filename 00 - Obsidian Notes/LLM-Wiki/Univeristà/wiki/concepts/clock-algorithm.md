---
type: concept
title: Clock Algorithm
tags: [memoria-virtuale, paging, lru-approximation]
related: [global-page-replacement, active-inactive-lists]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 20.txt"]
---
# Clock Algorithm
Il [[clock-algorithm]] è un'approssimazione efficiente del meccanismo *Least Recently Used* (LRU). Utilizza un bit di accesso (*accessed bit*) e una lista ciclica di pagine: il "puntatore dell'orologio" scorre la lista e resetta il bit di accesso delle pagine incontrate; quando incontra una pagina con bit a zero, la seleziona per la sostituzione.