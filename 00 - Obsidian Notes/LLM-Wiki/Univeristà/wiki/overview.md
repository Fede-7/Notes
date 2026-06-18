---
type: overview
title: Project Overview
tags: [SO1, Sistemi Operativi]
related: []
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 0.txt", "SO/Slide/Nuova cartella/SO1-Presentazione-AA25-26.txt", "SO/Trascrizioni/Lezione 11.txt", "SO/Trascrizioni/Lezione 14.txt", "SO/Trascrizioni/Lezione 16.txt", "SO/Slide/SO1-Lezione-deadlock-AA25-26.txt", "SO/Slide/SO1-Lezione1-AA25-26.txt", "SO/Slide/SO1-Presentazione-AA25-26.txt", "SO/Trascrizioni/Lezione 10.txt", "SO/Trascrizioni/Lezione 25.txt", "SO/Trascrizioni/Lezione 20.txt"]
---
# Overview

Questo wiki documenta lo studio del corso di Sistemi Operativi I (SO1), tenuto da Alberto Finzi. L'obiettivo è comprendere i concetti fondamentali dei sistemi operativi, come la gestione dei processi, la memoria virtuale e il deadlock, utilizzando testi accademici standard (Silberschatz et al., Tanenbaum & Bos) e materiali forniti dal corso stesso.

Il wiki copre la teoria dei deadlock, inclusa la caratterizzazione tramite le Condizioni di Coffman, le rappresentazioni grafiche (RAG e Wait-for Graph), e le diverse strategie di gestione: prevenzione (es. Lock Ordering), evitamento (es. Algoritmo del Banchiere e Stato Sicuro) e rilevamento/ripristino. 

Inoltre, il wiki include le basi storiche e architettoniche dei sistemi operativi:
- **Evoluzione Storica**: Dalle valvole e sistemi batch (IBM 7094) alla multiprogrammazione, fino ai moderni sistemi mobili.
- **Concetti Architetturali**: Il Sistema Operativo come allocatore di risorse e "Macchina Estesa", la gestione delle interruzioni (Interrupt Driven, Interrupt Vector), e le tecniche di I/O come Buffering e Spooling.
- **Architettura dei File System**: Studio della stratificazione (Logical File System, File Organization Module, Basic File System, I/O Control), meccanismi di consistenza (Journaling, Copy-on-Write) e gestione dei file nel kernel (FCB, tabelle dei file aperti).
- **Protezione e Modalità**: Il funzionamento della Dual Mode (User vs Kernel Mode) e l'uso delle System Call per l'accesso alle risorse.
- **Sottosistema I/O e Driver**: Classificazione dei dispositivi (blocco, carattere, rete), funzionamento dei driver in Ring 0, e meccanismi hardware come DMA e MMU, e l'uso di `ioctl`.
- **Strumenti Pratici**: L'uso di standard POSIX, mutex e strumenti di monitoraggio come il BCC toolkit su sistemi Linux.
- **Gestione della Memoria Virtuale**: Analisi dei meccanismi di [[global-page-replacement]], algoritmi di sostituzione come [[clock-algorithm]] (Linux), [[working-set]] (Windows) e il sistema a "due lancette" ([[second-chance-solaris]]) in Solaris.
- **Memoria di Massa**: Studio delle tecnologie HDD (Hard Disk Drive) e SSD (Solid State Drive), inclusi i fattori di latenza (seek time, rotation latency, transfer time), le tecniche di [[disk-scheduling]] (SSTF, SCAN, C-SCAN, LOOK, CLUK), e i concetti di [[lba]], [[ftl]] e gestione dei bad blocks.

**Nuovi contenuti aggiunti**:
- **Struttura del Corso**: Definizione del programma di massima suddiviso in 5 macro-aree (Introduzione, Processi, Memoria, Sistemi I/O, Dati permanenti).
- **Requisiti di Ambiente**: Specifiche sull'ambiente POSIX e sull'uso di strumenti come WSL e VMware per la compatibilità tra piattaforme.
- **Riferimenti Bibliografici**: Inclusione dei testi di Silberschatz, Galvin e Gagne e Tanenbaum e Bos come pilastri teorici del corso.
- **Sincronizzazione e Schedulazione**: Analisi delle metodologie di valutazione della schedulazione (deterministica, modelli di coda, real-time) e dei meccanismi di sincronizzazione dei thread (sezione critica, problema produttore-consumatore, istruzioni atomiche come *compare-and-swap*).
- **Sincronizzazione Avanzata e Priorità**: Studio delle istruzioni atomiche `test-and-set`, dei `spin-lock` e del *busy waiting*, dei semafori di Dijkstra (binari e contatori), dei monitor e delle variabili di condizione. Analisi dei problemi di *priority inversion* e della soluzione tramite *priority inheritance*, oltre alle proprietà di *liveness* (*bounded waiting* e *starvation*).
- **Architettura File System e I/O**: Analisi della stratificazione dei sistemi di file, tecniche di journaling per la consistenza dei dati, gestione dei file nel kernel (FCB, tabelle dei file aperti) e studio dei driver di dispositivo (Ring 0, DMA, MMU, ioctl).
- **Interfacce e Terminali**: Studio di TTY, pseudo-terminali (PTY), line discipline e primitive di comunicazione di rete (Socket).
- **Logistica dell'Esame**: Focus sulla teoria e su compiti di programmazione pratica ("to-do").