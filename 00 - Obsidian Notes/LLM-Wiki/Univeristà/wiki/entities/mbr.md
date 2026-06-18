---
type: entity
title: MBR (Master Boot Record)
tags: [hardware, boot-process, firmware, storage]
related: [uefi, gpt, bootstrapping]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt", "SO/Trascrizioni/Lezione 24.txt"]
---
# MBR (Master Boot Record)

L'**MBR** (Master Boot Record) è la struttura di boot legacy di 512 byte situata all'inizio del disco, utilizzata per il boot nei sistemi più vecchi.

## Caratteristiche e Limitazioni
A causa dell'indirizzamento a 32 bit, l'MBR è limitato a dischi di dimensioni massime di 2.2 TB. Oggi è stato ampiamente superato dalla **GPT** in termini di capacità e flessibilità.