---
type: concept
title: Ridondanza e Affidabilità
tags: [storage, reliability]
related: [raid, mean-time-to-data-loss, mean-time-to-repair]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
In sistemi di archiviazione di grandi dimensioni, la gestione della ridondanza è fondamentale per garantire l'affidabilità dei dati.

### Metriche Chiave
- **MTDL (Mean Time to Data Loss)**: Il tempo medio stimato prima che si verifichi una perdita di dati permanente.
- **MTTR (Mean Time to Repair)**: Il tempo necessario per sostituire un disco guasto e ricostruire i dati.

### Relazione con il RAID
- La **ridondanza** (es. mirroring) aumenta l'affidabilità proteggendo contro il guasto di un singolo disco.
- Lo **striping** aumenta le prestazioni ma non la ridondanza.
- In array di grandi dimensioni, il fallimento di un disco diventa una probabilità statistica certa; pertanto, meccanismi di replica e riparazione rapida sono obbligatori per mantenere un MTDL accettabile.
