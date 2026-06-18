---
type: entity
title: NAND Flash
tags: [hardware, memoria-di-massa]
related: [ssd, ftl, gestione-nand-flash]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt"]
---
# NAND Flash

La **NAND Flash** è la tecnologia di memoria non volatile utilizzata nella maggior parte degli SSD moderni. A differenza della RAM, mantiene i dati senza alimentazione.

### Caratteristiche Tecniche
- **Scrittura e Cancellazione**: La memoria NAND non può essere sovrascritta direttamente. I dati devono essere cancellati a livello di blocco prima di poter essere scritti nuovamente.
- **Garbage Collection**: Processo interno del controller per liberare blocchi contenenti pagine non valide, spostando i dati validi in nuovi blocchi.
- **Overprovisioning**: Spazio di memoria extra riservato al controller per facilitare la garbage collection e migliorare la longevità del dispositivo.
- **DWPD (Drive Writes per Day)**: Metrica che indica la durata di scrittura garantita del dispositivo.