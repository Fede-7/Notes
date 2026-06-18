---
type: entity
title: CHS (Cylinder Head Sector)
tags: [hardware, memoria-di-massa]
related: [lba, mapping-indirizzi]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt"]
---
# CHS (Cylinder Head Sector)

Il **CHS** è il metodo di indirizzamento fisico legacy utilizzato per identificare la posizione di un settore su un disco rigido meccanico. Si basa su tre coordinate:
- **Cylinder**: La posizione radiale sul disco.
- **Head**: Il numero della testina che legge il dato.
- **Sector**: La posizione specifica all'interno di una traccia.

A causa dei limiti di bit per rappresentare queste coordinate, il CHS è stato superato dall'LBA nei sistemi moderni.