---
type: source
title: "Lezione 3: Servizi del Sistema Operativo e Chiamate di Sistema"
tags: [so, lezione3, servizi, syscall]
related: [servizi-sistema-operativo, system-call, passaggio-parametri, trap, gerarchia-astrazione]
created: 2026-06-17
updated: 2026-06-17
authors: []
year: 2025
url: ""
venue: "Corso Sistemi Operativi I"
sources: ["SO/Slide/SO1-Lezione3-AA25-26.txt"]
---
# Lezione 3: Servizi del Sistema Operativo e Chiamate di Sistema

Questa lezione esplora le funzioni fondamentali fornite dai sistemi operativi (SO) ai programmi e agli utenti, nonché il meccanismo tecnico attraverso il quale queste funzioni vengono accessate.

## Servizi del Sistema Operativo
Il SO funge da ambiente di esecuzione fornendo diversi servizi chiave:
- **Interfaccia Utente (UI)**: CLI, GUI, Touch-screen, Comandi Vocali.
- **Esecuzione di Programmi**: Caricamento, esecuzione e terminazione.
- **Operazioni I/O**: Astrazione della complessità dell'hardware.
- **Gestione File-system**: Lettura, scrittura, creazione, eliminazione e permessi.
- **Comunicazione**: Scambio di informazioni tra processi (locali o di rete).
- **Rilevamento di Errori**: Gestione di errori hardware, CPU e software.
- **Allocazione delle Risorse**: Gestione di CPU, memoria, file e dispositivi.
- **Contabilità (Accounting)**: Tracciamento dell'uso delle risorse.
- **Protezione e Sicurezza**: Controllo degli accessi e isolamento dei processi.

## Chiamate di Sistema (System Calls)
Le system call rappresentano l'interfaccia fondamentale tra lo *user mode* e il *kernel mode*.
- **Gerarchia di Astrazione**: I programmi interagiscono con le **API** (come POSIX, Win API, Java API), che fungono da wrapper sopra le system call. Le librerie (es. `libc`) gestiscono la mappatura tra funzioni di alto livello e istruzioni di basso livello.
- **Meccanismo di Esecuzione**: Una chiamata tipica (es. `read()`) segue il flusso:
  1. Programma C chiama funzione della libreria (uso dello stack).
  2. La libreria prepara i registri della CPU.
  3. Viene eseguita l'istruzione `syscall`.
  4. Il kernel esegue l'operazione e restituisce il risultato.

## Passaggio dei Parametri
Esistono tre metodi principali per trasmettere dati al kernel:
1. **Registri**: Passaggio diretto (es. architettura x86-64 su Linux usa `rax`, `rdi`, `rsi`, `rdx`, `r10`, `r8`, `r9`).
2. **Blocchi in Memoria**: Passaggio di un indirizzo di una tabella/blocco tramite registro.
3. **Stack**: I parametri vengono inseriti nello stack dal programma e estratti dal SO (metodo meno comune nei sistemi moderni per le system call dirette).
