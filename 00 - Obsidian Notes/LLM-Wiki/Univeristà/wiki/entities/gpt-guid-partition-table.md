---
type: entity
title: GPT (GUID Partition Table)
tags: [boot, modern, hardware]
related: [master-boot-record-mbr, uefi-unified-extensible-firmware-interface, lba-logical-block-address]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
La **GPT (GUID Partition Table)** è lo standard moderno per la tabella delle partizioni, progettato per sostituire l'MBR.

### Caratteristiche
- **Indirizzamento a 64 bit**: Utilizza il sistema `lba-logical-block-address` per superare i limiti di capacità dell'MBR, supportando dischi di dimensioni enormi.
- **Identificatori Univoci**: Utilizza i `uuid` per identificare le partizioni in modo univoco.
- **Struttura**: Include header al blocco 1 e tabelle delle partizioni distribuite tra i blocchi 2 e 33, aumentando la robustezza rispetto all'MBR.
