---
type: concept
title: Monitoraggio Processi
tags: [linux, processi, risorse]
related: [kernel, user-mode, kernel-mode]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione6-bash-AA25-26.txt"]
---
# Monitoraggio Processi

Il monitoraggio dei processi permette di osservare l'attività del sistema, l'utilizzo delle risorse e lo stato dei programmi in esecuzione.

## Strumenti Principali
- **ps**: Mostra lo stato dei processi attivi.
    - `ps -f`: Informazioni complete (Unix style).
    - `ps -ef`: Tutti i processi (BSD style).
    - `ps aux x`: Processi senza terminale.
- **top**: Visualizzazione dinamica e interattiva dei processi e delle risorse.
- **htop**: Versione interattiva migliorata di `top`.
- **vmstat**: Fornisce statistiche sulle attività del sistema (processi, memoria, interrupt, CPU).

## Metriche di Risorse
- **PR (Priority)**: Priorità gestita dal kernel.
- **NI (Nice value)**: Valore di priorità impostato dall'utente.
- **VIRT**: Memoria virtuale totale (RAM + swap + librerie).
- **RES**: Memoria residente effettivamente occupata in RAM.
- **SHR**: Memoria condivisa con altri processi.
- **%CPU / %MEM**: Percentuali di utilizzo delle risorse.
- **STAT**: Stato del processo (R=running, S=sleeping, T=stopped, Z=zombie).

## Statistiche di Sistema (vmstat)
- **Proc**: `r` (processi attivi), `b` (processi bloccati).
- **System**: `in` (interrupt), `cs` (context switch), `us` (%user mode), `sy` (%kernel mode).
- **CPU**: `id` (%idle), `wa` (%I/O waiting), `st` (%stolen time da hypervisor).