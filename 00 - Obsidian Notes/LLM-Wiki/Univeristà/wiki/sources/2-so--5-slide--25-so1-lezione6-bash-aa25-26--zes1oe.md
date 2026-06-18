---
type: source
title: "SO1 Lezione 6: Bash e Utility di Sistema"
tags: [bash, shell, linux, sistemi-operativi]
related: [bash, ciclo-di-esecuzione-shell, variabili-di-shell, standard-io, ridirezione-e-pipe, monitoraggio-processi, metacaratteri-e-wildcards, quoting, word-splitting, command-substitution]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione6-bash-AA25-26.txt"]
authors: []
year: 2026
url: ""
venue: ""
---
# SO1 Lezione 6: Bash e Utility di Sistema

Questa lezione fornisce una panoramica dettagliata dell'utilizzo della shell [[bash]] come interfaccia principale per l'utente con il sistema operativo. Il materiale copre i seguenti argomenti principali:

## Shell e Ciclo di Esecuzione
- Definizione della shell come interprete di linguaggio a riga di comando.
- Analisi del ciclo di esecuzione: startup, acquisizione comando, macro espansione, esecuzione e terminazione.
- Distinzione tra shell interattiva (non-login e login) e i relativi file di configurazione (`.bashrc`, `.bash_profile`, ecc.).

## Variabili e Ambiente
- Gestione delle variabili di shell (ambiente e locali).
- Variabili predefinite come `PATH`, `HOME`, `PS1`, `HOSTNAME` e `SHELL`.
- Regole di assegnazione e lettura delle variabili.

## Gestione dei Flussi e Comandi
- Concetto di file standard (stdin, stdout, stderr).
- Tecniche di ridirezione (`>`, `>>`, `<`, `2>`, `> &`).
- Utilizzo delle pipeline (`|`) per concatenare comandi.
- Sostituzione di comandi (`$(comando)`).
- Gestione dei metacaratteri, wildcard (`*`, `?`, `[]`, `{}`) e meccanismi di quoting (escape, apici singoli e doppi).
- Analisi del *word splitting* e della variabile `IFS`.

## Monitoraggio del Sistema
- Utilizzo di strumenti come `ps`, `top`, `htop` e `vmstat`.
- Interpretazione delle metriche di risorse: PR, NI, VIRT, RES, SHR, %CPU, %MEM e stati del processo (R, S, T, Z).
- Introduzione alla gestione degli interrupt (timer di sistema, IO-APIC).

## Utility Standard Unix
- Panoramica di comandi fondamentali per la manipolazione di file e testo: `ls`, `cp`, `mv`, `rm`, `wc`, `cat`, `cut`, `sort`, `head`, `tail`, `find`.