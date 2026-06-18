---
type: concept
title: Servizi del Sistema Operativo
tags: [so, servizi, kernel, I/O]
related: ["system-call", "gerarchia-astrazione", "protezione-vs-sicurezza", "passaggio-parametri"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione3-AA25-26.txt", "SO/Slide/SO1-Lezione2b-AA25-26.txt"]
---
# Servizi del Sistema Operativo

I sistemi operativi forniscono un ambiente di servizi fondamentali per garantire il funzionamento efficiente del sistema, permettendo l'interazione con gli utenti e astrando la complessità dell'hardware.

## Elenco dei Servizi
I principali servizi forniti dal sistema operativo includono:

- **Interfaccia Utente (UI)**: Fornisce i mezzi di interazione con il sistema, inclusi CLI (Command-Line Interface), GUI (Graphic User Interface), interfacce touch-screen e comandi vocali.
- **Esecuzione di Programmi**: Gestisce il ciclo di vita completo dei processi, inclusi il caricamento, l'esecuzione e la terminazione.
- **Gestione I/O e Periferiche**: Fornisce interfacce e astrazioni uniformi per l'accesso a file e dispositivi diversi (come dischi, tastiere e display), nascondendo i dettagli fisici dell'hardware e gestendo le periferiche tramite driver.
- **Gestione File-system**: Gestisce la persistenza dei dati, le directory, i permessi di accesso, la ricerca e la manipolazione dei file.
- **Comunicazione (IPC)**: Fornisce meccanismi per lo scambio di dati tra processi locali (IPC) e attraverso diverse reti.
- **Rilevamento di Errori**: Monitora costantemente l'integrità dell'hardware e del software, gestendo guasti hardware, errori di CPU ed eccezioni software per garantire la coerenza del sistema.
- **Allocazione delle Risorse**: Distribuisce cicli CPU, memoria, file e dispositivi tra i vari lavori concorrenti.
- **Contabilità (Accounting)**: Monitora e traccia l'utilizzo delle risorse da parte degli utenti per scopi di gestione e fatturazione.
- **Protezione e Sicurezza**: Garantisce l'integrità dei dati attraverso il controllo degli accessi interni (protezione) e l'autenticazione/difesa da accessi esterni (sicurezza).

## Gerarchia di Accesso
I programmi utente non accedono direttamente ai servizi del kernel, ma seguono un percorso strutturato attraverso diversi livelli di astrazione:

`Programma Utente` $\rightarrow$ `API (es. POSIX)` $\rightarrow$ `Libreria (es. libc)` $\rightarrow$ `System Call` $\rightarrow$ `Kernel`