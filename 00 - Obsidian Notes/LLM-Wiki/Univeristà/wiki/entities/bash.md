---
type: entity
title: Bash
tags: [shell, linux, terminale, cli]
related: ["ciclo-di-esecuzione-shell", "variabili-di-shell", "standard-io", "ridirezione-e-pipe", "metacaratteri-e-wildcards", "quoting", "word-splitting", "command-substitution"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione6-bash-AA25-26.txt"]
---
# Bash

Bourne Again Shell (`bash`) è la shell di comando standard utilizzata per le esercitazioni e per l'interazione con il sistema operativo tramite riga di comando (CLI). [[bash]] è una shell interpretativa utilizzata come interfaccia principale per l'utente con il sistema operativo. Non è solo un terminale, ma un programma capace di interpretare il linguaggio a riga di comando, gestire variabili, controllare il flusso delle operazioni ed eseguire script.

## Funzioni Principali
- **Gestione del main command loop**: Ciclo iterativo che acquisisce e processa i comandi.
- **Analisi sintattica**: Interpretazione della struttura dei comandi inseriti dall'utente.
- **Esecuzione**: Gestione di comandi "built-in", file eseguibili e script in linguaggio di shell.
- **Gestione I/O**: Gestione dei flussi standard (stdin, stdout, stderr).
- **Gestione Processi**: Gestione dei processi da terminale.

## Modalità di Esecuzione
- **Interattiva, non-login**: Avviata da una sessione esistente, legge tipicamente il file `~/.bashrc`.
- **Interattiva, login**: Avviata all'accesso del sistema, legge file come `/etc/profile`, `~/.bash_profile`, `~/.bash_login` o `~/.profile`.