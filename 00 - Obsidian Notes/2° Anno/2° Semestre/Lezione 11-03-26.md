---
Date: 2026-03-11
Professore: Finzi
tags:
  - OS
---
# Appunti sulla Comunicazione Interprocesso (IPC)

## 1. Comunicazione in Shared Memory (Memoria Condivisa)
La memoria condivisa permette a più processi di accedere a una stessa zona di memoria fisica mappandola nel proprio spazio di indirizzamento virtuale.

*   **Apertura e Allocazione**: Si utilizzano le **API POSIX** come `shm_open` per creare o aprire un oggetto di memoria condivisa, associandogli un **nome** affinché processi diversi possano riferirsi allo stesso segmento.
*   **Permessi**: I permessi vengono definiti in fase di creazione (es. `0666` per lettura e scrittura). Questi seguono una codifica binaria (triplette per utente, gruppo e altri): ad esempio, `6` (110) indica lettura e scrittura, mentre `7` (111) include l'esecuzione.
*   **Mappatura (`mmap`)**: Una volta allocata la dimensione con `ftruncate`, l'area viene mappata in memoria tramite `mmap`, restituendo un **puntatore** (solitamente `void*` per generalità) che permette di operare sui dati come se fossero variabili locali.
*   **Chiusura**: È fondamentale usare `shm_unlink` per rimuovere il nome dell'oggetto dal file system e liberare le risorse una volta terminato l'uso.

## 2. Message Passing: Pipe Ordinarie (Anonime)
Le pipe sono flussi di byte unidirezionali utilizzati per la comunicazione tra **processi imparentati** (padre e figlio).

*   **Creazione**: La funzione `pipe()` crea un canale nel kernel e restituisce due **file descriptor** in un array: `fd` per la lettura e `fd` per la scrittura.
*   **Funzionamento Alf-Duplex**: Sebbene la pipe nasca con due imboccature, è progettata per essere unidirezionale. Per un funzionamento corretto, il programmatore deve chiudere l'estremità inutilizzata in ogni processo (es. il padre chiude la lettura se deve solo scrivere).
*   **Sincronizzazione e Segnali**: 
    *   La lettura è **bloccante**: se la pipe è vuota, il lettore attende finché non arrivano dati o il canale viene chiuso.
    *   Se il lettore chiude il canale e lo scrittore prova a inviare dati, il kernel invia un segnale **`SIGPIPE`** che, se non gestito, uccide il processo scrittore.
    *   Se lo scrittore chiude il canale, il lettore riceve **0 byte**, interpretandolo come fine della comunicazione.

## 3. Named Pipes (FIFO)
A differenza delle pipe ordinarie, le **FIFO** hanno un nome nel file system e permettono la comunicazione tra **processi non imparentati**.

*   **Creazione**: Si creano con il comando o la funzione `mkfifo`.
*   **Caratteristiche**: Sono bidirezionali (duplex) e persistono nel file system finché non vengono cancellate esplicitamente con `unlink`.
*   **Uso**: Vengono aperte con la classica funzione `open` e gestite con `read` e `write` come se fossero file comuni, sebbene i dati passino attraverso il kernel e non risiedano stabilmente sul disco.

## 4. Socket
Le socket rappresentano un **endpoint di comunicazione** e sono lo strumento standard per far comunicare processi su macchine diverse attraverso una rete, o localmente.

*   **Interfaccia Uniforme**: Unix unifica il concetto di comunicazione: che si tratti di un file, di una pipe o di una socket, il programmatore usa sempre i **file descriptor** e le primitive `read`/`write` (o `send`/`recv`).
*   **Modello Client-Server**: Il server esegue `bind`, `listen` e `accept` per attendere connessioni; il client esegue `connect` conoscendo l'indirizzo del server.

## 5. Comandi Utili e Programmazione in C
*   **Argomenti del Main**: `argc` indica il numero di argomenti passati da riga di comando (incluso il nome del programma), mentre `argv` è l'array di stringhe contenente tali argomenti.
*   **Gestione Processi da Shell**:
    *   `ps -ef`: Mostra tutti i processi con il loro **PID** (Process ID) e **PPID** (Parent PID).
    *   `&`: Lanciando un comando con la "e commerciale" (es. `gedit &`), il processo viene eseguito in **background**, restituendo subito il controllo alla shell.
    *   `kill -9 [PID]`: Invia un segnale di terminazione immediata e non intercettabile a un processo.
    *   `>`: Reindirizza lo standard output di un programma su un file (es. `./programma > file.txt`).
*   **Funzioni C**: `fork()` duplica il processo corrente. `atoi()` converte una stringa in intero. `sprintf()` scrive dati formattati in una stringa anziché sullo schermo.