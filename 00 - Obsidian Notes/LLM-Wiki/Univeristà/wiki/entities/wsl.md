---
type: entity
title: WSL (Windows Subsystem for Linux)
tags: ["windows", "linux", "virtualizzazione", "strumento"]
related: [ambiente-posix]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione6-bash-AA25-26.txt", "SO/Slide/SO1-Presentazione-AA25-26.txt"]
---
# WSL (Windows Subsystem for Linux)

[[wsl]] è uno strumento software che permette di eseguire un ambiente Linux completo direttamente su Windows. È particolarmente consigliato per gli studenti che utilizzano sistemi operativi Windows, poiché fornisce l'interfaccia **bash** e gli strumenti **POSIX** necessari per le esercitazioni del corso.

## Utilizzi principali
WSL viene utilizzato frequentemente per:
- Lo sviluppo software.
- L'accesso a strumenti di riga di comando tipici di sistemi Unix-like.
- L'esecuzione di ambienti Linux integrati nel sistema Windows.

## Installazione
Il processo di installazione standard prevede i seguenti passaggi:
1. Esecuzione del comando `wsl --install` tramite PowerShell con privilegi di amministratore.
2. Riavvio del sistema.
3. Creazione di un utente Linux.