---
type: concept
title: Programmi di Sistema
tags: [SO, software, shell]
related: [system-call]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-AA25-26.txt"]
---
# Programmi di Sistema

I programmi di sistema forniscono un ambiente conveniente per lo sviluppo e l'esecuzione di applicazioni. Mentre le chiamate di sistema sono l'interfaccia di basso livello, la maggior parte degli utenti interagisce con i programmi di sistema che fungono da wrapper.

## Categorie Principali
- **Manipolazione File**: Editor di testo, comandi per copiare, rinominare, stampare e scaricare file.
- **Informazioni sullo Stato**: Programmi che visualizzano data, ora, memoria disponibile, spazio su disco e numero di utenti.
- **Supporto Linguaggio**: Compilatori, assemblatori, debugger e interpreti.
- **Caricamento ed Esecuzione**: Strumenti come il *dynamic loader* e il *linker*.
- **Comunicazioni**: Meccanismi per creare connessioni virtuali tra processi, utenti e sistemi.
- **Servizi di Background**: Programmi in esecuzione costante (demoni o servizi) come il monitoraggio degli errori o i servizi di stampa. Questi girano solitamente in contesto *user mode*.