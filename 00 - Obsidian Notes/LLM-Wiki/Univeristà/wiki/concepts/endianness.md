---
type: concept
title: Endianness
tags: [networking, architecture, data-representation]
related: [network-byte-order, conversione-byte-order]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 28.txt"]
---
# Endianness
L'**endianness** definisce l'ordine in cui i byte di un tipo di dato multi-byte vengono memorizzati in memoria:
- **Little Endian**: Il byte meno significativo viene memorizzato per primo (usato dalla maggior parte delle architetture moderne come x86-64 e ARM).
- **Big Endian**: Il byte più significativo viene memorizzato per primo.

Nella comunicazione di rete, è fondamentale gestire l'endianness per garantire che i dati siano interpretati correttamente tra macchine con architetture diverse.