---
type: concept
title: Passaggio dei Parametri
tags: ["so", "architettura", "x86-64", "system-calls"]
related: ["system-call", "trap", "abi", "wrapper-di-libreria"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione3-AA25-26.txt", "SO/Slide/SO1-Lezione2b-AA25-26.txt"]
---
# Passaggio dei Parametri

Il passaggio dei parametri definisce come i dati vengono trasmessi dal programma utente al kernel durante l'esecuzione di una **System Call**. Esistono tre metodi principali per gestire questa comunicazione:

## Metodi Generali
1. **Passaggio diretto nei registri**: I parametri vengono inseriti direttamente nei registri della CPU. È il metodo più veloce, ma è limitato dal numero di registri disponibili nell'architettura.
2. **Passaggio tramite blocchi di memoria**: I parametri sono organizzati in una tabella o blocco in memoria; il programma passa al kernel solo l'indirizzo di tale blocco tramite un registro. Questo metodo è utilizzato in sistemi come Linux e Solaris.
3. **Passaggio tramite stack**: Il programma predispone i parametri nello stack e il kernel li estrae. Questo metodo è meno comune nei sistemi moderni per le system call dirette.

## Implementazione su x86-64 (GNU/Linux)
Nei sistemi moderni a 64 bit, il passaggio avviene preferibilmente tramite registri per massimizzare l'efficienza. Una chiamata di sistema può accettare fino a sei parametri, mappati sui seguenti registri:

| Registro | Ruolo / Argomento | Esempio tipico |
| :--- | :--- | :--- |
| `rax` | Identificatore numerico della syscall / Valore di ritorno | - |
| `rdi` | Argomento 0 | Descrittore di file (`fd`) |
| `rsi` | Argomento 1 | Buffer (`msg`) |
| `rdx` | Argomento 2 | Lunghezza (`count`) |
| `r10` | Argomento 3 | - |
| `r8` | Argomento 4 | - |
| `r9` | Argomento 5 | - |

### Flusso di Esecuzione con `libc`
Sebbene il kernel utilizzi i registri per ricevere i dati, il programmatore interagisce spesso con le funzioni della libreria standard (`libc`). In questo contesto, il flusso di dati segue un percorso a più stadi:

1. **Chiamata alla funzione**: Il programma esegue `call read()`. In questa fase, i parametri vengono messi nello **stack** per la chiamata alla funzione della libreria.
2. **Wrapper di libreria**: La `libc` agisce come un wrapper: estrae i parametri dallo stack e li sposta nei **registri** corretti richiesti dalla convenzione dell'architettura.
3. **Istruzione `syscall`**: L'istruzione hardware passa il controllo al kernel, che trova i dati già pronti nei registri.