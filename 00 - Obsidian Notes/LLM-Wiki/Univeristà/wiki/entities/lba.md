---
type: entity
title: LBA (Logical Block Address)
tags: ["hardware", "memoria-di-massa", "storage", "abstraction"]
related: ["chs", "mapping-indirizzi", "ftl", "logical-physical-mapping"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt", "SO/Trascrizioni/Lezione 20.txt"]
---
# Logical Block Address (LBA)

L'[[lba]] è un metodo di indirizzamento dei blocchi di dati che fornisce un'astrazione lineare dei settori del disco. Invece di utilizzare coordinate fisiche complesse, il sistema operativo vede il disco come una sequenza continua di blocchi numerati.

L'LBA permette al sistema operativo di identificare i blocchi di dati in modo astratto dalla geometria fisica del dispositivo di memoria di massa, consentendo di interagire con il controller del disco senza dover conoscere la posizione fisica dei dati.

L'uso di LBA semplifica drasticamente lo sviluppo dei file system e dei driver, poiché nasconde la geometria fisica del dispositivo sottostante.