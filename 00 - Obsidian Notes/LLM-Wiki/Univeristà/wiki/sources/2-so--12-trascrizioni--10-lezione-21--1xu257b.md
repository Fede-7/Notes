---
type: source
title: "Lezione 21 - Gestione Memoria Secondaria e Architetture RAID"
tags: [SO1, file-system, hardware, boot-process]
related: [hard-disk-drive, solid-state-drive, master-boot-record-mbr, gpt-guid-partition-table, bios-basic-input-output-system, uefi-unified-extensible-firmware-interface, bootloader, raid, mirroring, striping, disk-scheduling, partitioning, volumes, boot-process-phases, boot-process-uefi, memoria-anonima, ridondanza-e-affidabilita, block-level-striping, distributed-parity, nested-raid]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt"]
authors: []
year: 2026
url: ""
venue: ""
---
Questa trascrizione della Lezione 21 del corso SO1 tratta della gestione della memoria secondaria e delle architetture di storage. I temi principali includono:

1. **Hardware di Memoria Secondaria**: Differenze tra HDD (meccanici) e SSD (elettronici), con particolare attenzione agli algoritmi di `disk-scheduling` necessari per minimizzare il *seek time* negli HDD.
2. **Astrazioni Logiche**: La gerarchia di astrazione che va dalle partizioni fisiche ai volumi logici, fino ai file system.
3. **Processo di Avvio (Boot)**: L'evoluzione storica dai sistemi legacy (BIOS/MBR) alle architetture moderne (UEFI/GPT), inclusa la sequenza di caricamento dal firmware al kernel.
4. **Gestione dello Swap**: Analisi della memoria anonima e delle strategie di swapping su partizioni raw rispetto ai file di swap.
5. **Architetture RAID**: Studio delle tecniche di `mirroring` e `striping` per bilanciare prestazioni e affidabilità, analizzando i vari livelli RAID (0-6) e le configurazioni *nested* (es. RAID 1+0).