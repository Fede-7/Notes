---
type: entity
title: HDD (Hard Disk Drive)
tags: [hardware, storage, memoria-di-massa]
related: [ssd, gerarchia-di-memorie, disk-scheduling, mapping-indirizzi, seek-time, rotation-latency, transfer-time, zbr]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2a-AA25-26.txt", "SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt", "SO/Trascrizioni/Lezione 20.txt"]
---
# HDD (Hard Disk Drive)

Gli **HDD** (Hard Disk Drives) sono dispositivi di memoria secondaria meccanici basati su piatti magnetici.

### Struttura Fisica e Logica
La struttura fisica del disco è composta da piatti rotanti dotati di testine. Su questi piatti sono tracciate delle **tracce** (tracks), che sono ulteriormente suddivise in **settori**. 
- **Cilindri**: Rappresentano la sovrapposizione delle tracce su piatti diversi.

### Metriche di Performance
Le prestazioni degli HDD sono influenzate da fattori meccanici che determinano diverse latenze:
- [[seek-time]]: Il tempo necessario alla testina per spostarsi sulla traccia corretta.
- [[rotation-latency]]: Il tempo necessario affinché il settore desiderato ruoti sotto la testina.
- [[transfer-time]]: Il tempo di trasferimento effettivo dei dati (spesso espresso come *Transfer Rate* per indicare la velocità di lettura/scrittura).
- **Average Access Time**: La somma del *seek time* e della *rotational latency*.

### Ottimizzazione e Tecniche
Per ottimizzare le prestazioni e la gestione dei dati, gli HDD utilizzano:
- **[[disk-scheduling]]**: Algoritmi per gestire l'ordine di accesso ai dati.
- **[[zbr]] (Zone Bit Recording)**: Organizzazioni fisiche dei dati sui piatti per migliorare l'efficienza.

### Caratteristiche e Confronto
A causa della loro natura meccanica, gli HDD sono soggetti a usura fisica e presentano latenze che li rendono più lenti rispetto agli SSD.