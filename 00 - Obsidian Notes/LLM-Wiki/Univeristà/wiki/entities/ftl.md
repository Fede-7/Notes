---
type: entity
title: FTL (Flash Translation Layer)
tags: [hardware, software, ssd, storage, flash]
related: [nand-flash, lba, bad-block-management]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt", "SO/Trascrizioni/Lezione 20.txt"]
---
# Flash Translation Layer (FTL)

Il **Flash Translation Layer (FTL)** è una struttura software/firmware interna al controller della memoria Flash (SSD) responsabile della mappatura tra le pagine logiche (visibili al sistema operativo tramite [[lba]]) e le pagine fisiche del dispositivo.

Il suo compito principale è astrarre la complessità della gestione della NAND Flash, fornendo al sistema operativo un'interfaccia di indirizzamento lineare e persistente. Per garantire il corretto funzionamento del dispositivo, l'FTL gestisce diverse operazioni critiche:

- **Mappatura degli indirizzi**: Traduzione degli indirizzi logici richiesti dal sistema operativo negli indirizzi fisici delle pagine NAND.
- **Gestione delle cancellazioni**: Distribuzione delle operazioni di cancellazione, necessarie poiché la NAND richiede la cancellazione a blocchi prima della scrittura.
- **Wear Leveling**: Gestione dell'usura dei blocchi per garantire una distribuzione uniforme delle scritture nel tempo.
- **Bad Block Management**: Mappatura e gestione dei blocchi difettosi del dispositivo.