---
type: concept
title: Flash-vs-HDD-Mapping
tags: [storage, hardware]
related: [proximity-maintenance, seek-time, ftl]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 20.txt"]
---
# Flash-vs-HDD-Mapping
Il [[flash-vs-hdd-mapping]] evidenzia il contrasto tra le diverse necessità di mappatura dei dati:
- **HDD**: Richiedono la [[proximity-maintenance]] poiché la vicinanza fisica dei dati riduce il [[seek-time]].
- **Flash (SSD)**: Non hanno vincoli di prossimità meccanica, permettendo al [[ftl]] una maggiore flessibilità nel mapping logico-fisico, facilitando la gestione degli errori e della distribuzione delle cancellazioni.