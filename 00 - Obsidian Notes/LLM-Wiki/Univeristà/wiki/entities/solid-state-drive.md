---
type: entity
title: Solid State Drive (SSD)
tags: [hardware, storage]
related: [hard-disk-drive, disk-scheduling]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
Il **Solid State Drive (SSD)** è un dispositivo di memoria secondaria elettronico che utilizza memorie flash per l'archiviazione dei dati.

### Caratteristiche Tecniche
- **Assenza di parti mobili**: A differenza degli HDD, gli SSD non hanno testine o piatti rotanti, eliminando il problema del *seek time* meccanico.
- **Scheduling**: Poiché l'accesso è quasi istantaneo e non influenzato dalla posizione fisica dei dati, gli algoritmi di `disk-scheduling` complessi non sono necessari; spesso viene utilizzato un semplice ordine di arrivo.
- **Prestazioni**: Offrono velocità di I/O superiori e una maggiore resistenza agli urti rispetto agli HDD.
