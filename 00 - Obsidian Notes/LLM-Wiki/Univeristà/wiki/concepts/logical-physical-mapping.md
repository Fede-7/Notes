---
type: concept
title: Logical-Physical Mapping
tags: [storage, abstraction]
related: [lba, ftl, proximity-maintenance]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 20.txt"]
---
# Logical-Physical Mapping
La [[logical-physical-mapping]] è l'astrazione che separa l'indirizzamento logico dei dati (gestito dal sistema operativo tramite [[lba]]) dalla loro posizione fisica reale sul supporto di memoria. Negli HDD, questa mappatura deve spesso rispettare la [[proximity-maintenance]] per ottimizzare le prestazioni meccaniche, mentre nelle memorie Flash tale vincolo è assente.