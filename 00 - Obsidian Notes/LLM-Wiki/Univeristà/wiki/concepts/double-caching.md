---
type: concept
title: Double Caching
tags: [file-system, memoria-virtuale]
related: [buffer-cache-unificata]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 24.txt"]
---
# Double Caching
Il **double caching** è un problema di ridondanza in cui i dati di un file vengono mantenuti contemporaneamente sia nella `buffer-cache` del file system che nella `page-cache` del sistema di memoria virtuale. Questo fenomeno viene risolto tramite l'integrazione delle due cache in una struttura unificata.