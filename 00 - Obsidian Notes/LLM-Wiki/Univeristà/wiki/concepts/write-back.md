---
type: concept
title: Write-back
tags: [file-system, caching]
related: [prepaging]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 24.txt"]
---
# Write-back
Schema di scrittura in cui i dati vengono inizialmente scritti in cache e trasferiti asincronamente sul disco in un secondo momento. Questo approccio ottimizza le prestazioni ma introduce rischi di perdita dati in caso di crash improvviso.