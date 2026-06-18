---
type: entity
title: Master Boot Record (MBR)
tags: [boot, legacy, hardware]
related: [gpt-guid-partition-table, bios-basic-input-output-system, bootloader]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
---
Il **Master Boot Record (MBR)** è una struttura di 512 byte situata all'inizio del disco rigido, utilizzata dai sistemi legacy per il processo di avvio.

### Componenti
- **Bootcode**: Contiene il codice iniziale (circa 446 byte) necessario per localizzare e caricare il `bootloader`.
- **Tabella delle Partizioni**: Una struttura di 64 byte che definisce le partizioni del disco.
- **Limiti**: L'architettura MBR è limitata a un massimo di 4 partizioni primarie e a un indirizzamento a 32 bit, che limita la capacità del disco a 2.2 TB.
