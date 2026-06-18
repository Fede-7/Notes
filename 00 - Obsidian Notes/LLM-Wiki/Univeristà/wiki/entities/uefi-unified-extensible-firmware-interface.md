---
type: entity
title: UEFI (Unified Extensible Firmware Interface)
tags: [boot, firmware, modern]
related: [bios-basic-input-output-system, gpt-guid-partition-table, efi-system-partition]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
L'**UEFI** è il firmware moderno che sostituisce il BIOS, gestendo il boot su dischi GPT e fornendo un'interfaccia più flessibile per il caricamento del sistema operativo.

### Caratteristiche
- **ESP**: Utilizza una partizione specifica, l'**EFI System Partition (ESP)**, per memorizzare i file di avvio.
- **Boot Manager**: Permette il caricamento di più sistemi operativi tramite un menu grafico.
- **Supporto GPT**: Gestisce nativamente le tabelle di partizione GPT e capacità di disco elevate.
