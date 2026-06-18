---
type: concept
title: Bad Block Management
tags: [storage, flash, hdd]
related: [bad-block, logical-physical-mapping]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 20.txt"]
---
# Bad Block Management
Il [[bad-block-management]] è il processo con cui il controllore del disco identifica, marca e isola i blocchi fisici difettosi ([[bad-block]]) rendendoli inutilizzabili. Questo meccanismo garantisce l'affidabilità dei dati spostando le informazioni dai settori danneggiati a quelli funzionanti, mantenendo l'astrazione della [[logical-physical-mapping]].