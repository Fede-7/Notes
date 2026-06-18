---
type: source
title: "Lezione 1: Introduzione ai Sistemi Operativi"
tags: [SO1, introduzione, storia, architettura]
related: [macchina-estesa, multiprogrammazione, timesharing, interrupt-driven, dual-mode, system-call, kernel]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione1-AA25-26.txt"]
authors: []
year: 2025
url: ""
venue: ""
---
# Lezione 1: Introduzione ai Sistemi Operativi

Questa lezione fornisce le basi teoriche e storiche dei Sistemi Operativi (SO). Il contenuto è strutturato in diverse sezioni chiave:

## Definizioni Fondamentali
Il Sistema Operativo viene presentato attraverso tre prospettive principali:
1. **Allocatore di Risorse**: Gestisce l'accesso alle risorse hardware (CPU, memoria, I/O) e risolve i conflitti tra i processi.
2. **Programma di Controllo**: Coordina l'esecuzione dei programmi per prevenire errori e usi impropri del calcolatore.
3. **Macchina Estesa**: Fornisce un'astrazione che trasforma l'hardware complesso ("brutto") in un ambiente uniforme e coerente ("bello") per l'utente.

## Storia dei Sistemi Operativi
Vengono descritte le cinque generazioni principali:
- **1945–55 (Valvole)**: Gestione manuale, uso esclusivo della macchina.
- **1955–65 (Transistor)**: Introduzione del *batch processing* e dei primi *monitor residenti* (es. IBM 7094).
- **1965–1980 (Circuiti Integrati)**: Introduzione della multiprogrammazione e del *timesharing* (es. MULTICS, Unix).
- **1980–Presente (Personal Computer)**: Diffusione di DOS, MS-DOS e interfacce grafiche (Xerox PARC).
- **1990–Presente (Mobile Computer)**: Sistemi operativi per smartphone e tablet (Android, iOS).

## Architettura e Gestione Hardware
Il corso analizza il legame tra SO e architettura hardware:
- **Bus e Memoria**: Connessione tra CPU e controllori di dispositivo tramite bus (es. PCIe).
- **Gestione I/O**: Confronto tra *polling* (interrogazione periodica) e *interrupt* (segnali asincroni).
- **Interrupt Driven**: Il modello moderno dove il SO risponde a segnali hardware e software.
- **Vettorizzazione**: Uso di *interrupt vector* per mappare i codici di interruzione alle routine di servizio (ISR).

## Protezione e Modalità
- **Dual Mode**: Distinzione tra *User Mode* (privilegi limitati) e *Kernel Mode* (accesso totale).
- **Protezione Hardware**: Uso di bit di modalità, timer per il controllo temporale della CPU e registri Base/Limite per la protezione della memoria.
- **System Calls**: L'interfaccia standard per le richieste di servizio dal programma utente al kernel.