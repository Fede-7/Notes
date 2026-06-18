---
type: concept
title: Gerarchia di Memorie
tags: [memory, hardware, architecture]
related: [caching, ssd, hdd, ram]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2a-AA25-26.txt"]
---
# Gerarchia di Memorie

Le memorie sono organizzate in gerarchie basate su un trade-off tra velocità, costo e volatilità.

| Livello | Nome | Dimensione tipica | Tecnologia | Tempo d’accesso (ns) | Ampiezza di banda (MB/s) | Gestito da | Supportato da cache |
|---------|------|-------------------|------------|-------------------------|---------------------------|-------------|---------------------|
| 1       | Registri | < 1 KB | CMOS (porte multiple) | 0,25 – 0,5 | 20.000 – 100.000 | Compilatore | - |
| 2       | Cache | < 16 MB | CMOS SRAM (on-chip/off-chip) | 0,5 – 25 | 5.000 – 10.000 | Hardware | Disco |
| 3       | Memoria Centrale | < 64 GB | CMOS DRAM | 80 – 250 | 1.000 – 5.000 | Sistema Operativo | Disco |
| 4       | SSD | < 1 TB | Memoria Flash | 25.000 – 50.000 | 500 | Sistema Operativo | Disco o nastro |
| 5       | Disco Magnetico | < 10 TB | Disco Magnetico | 5.000.000 | 20 – 150 | Sistema Operativo | Disco o nastro |
