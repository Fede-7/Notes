---
type: source
title: "Lezione 20: Sostituzione delle Pagine e Memoria di Massa"
tags: [so1, memoria-virtuale, memoria-di-massa]
related: [global-page-replacement, clock-algorithm, disk-scheduling, hdd, ssd]
created: 2026-06-17
updated: 2026-06-17
authors: []
year: 2026
url: ""
venue: ""
sources: ["SO/Trascrizioni/Lezione 20.txt"]
---
Questa trascrizione della Lezione 20 del corso di Sistemi Operativi I tratta due macro-aree fondamentali: la gestione della memoria virtuale attraverso i meccanismi di sostituzione delle pagine e le basi della memoria di massa.

La prima parte della lezione analizza come i sistemi operativi gestiscono la scarsità di memoria fisica utilizzando algoritmi di *page replacement* (come il meccanismo *Clock* in Linux, il *Working Set* in Windows e il sistema a "due lancette" in Solaris).

La seconda parte si concentra sull'hardware di storage, confrontando le caratteristiche meccaniche degli HDD (Hard Disk Drive) con quelle elettroniche delle memorie Flash (SSD). Vengono discussi i fattori di latenza (seek time, rotation latency, transfer time), le tecniche di schedulazione del disco (SSTF, SCAN, C-SCAN, LOOK, CLUK) e i meccanismi di gestione degli errori e del mapping logico-fisico (LBA, FTL, bad blocks).