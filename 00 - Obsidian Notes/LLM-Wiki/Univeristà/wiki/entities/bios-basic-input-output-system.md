---
type: entity
title: BIOS (Basic Input/Output System)
tags: [boot, firmware, legacy]
related: [uefi-unified-extensible-firmware-interface, master-boot-record-mbr]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
Il **BIOS** è il firmware legacy responsabile dell'inizializzazione dell'hardware e del caricamento del sistema operativo.

### Funzionamento
- **POST**: Esegue il *Power-On Self-Test* per verificare l'integrità dei componenti hardware.
- **Boot**: Carica il codice contenuto nell'MBR per avviare il processo di boot.
- **Sostituzione**: È stato progressivamente sostituito dall'architettura UEFI per supportare dischi più grandi e funzionalità avanzate.
