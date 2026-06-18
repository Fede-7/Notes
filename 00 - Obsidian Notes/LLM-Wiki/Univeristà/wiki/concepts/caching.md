---
type: concept
title: Caching
tags: [memory, performance]
related: [gerarchia-di-memorie, buffering-vs-spooling]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2a-AA25-26.txt"]
---
# Caching

Il principio del caching prevede la migrazione temporanea di informazioni da memorie più lente a memorie più veloci.

- **Meccanismo**: Le memorie più veloci (cache) sono considerate per prime. Se il dato è presente, viene utilizzato immediatamente; in caso contrario, viene copiato dalla memoria lenta alla cache.
- **Problematiche**:
    - Gestione della cache (politiche di sostituzione).
    - Dimensioni della cache.
    - Politiche di replicazione.