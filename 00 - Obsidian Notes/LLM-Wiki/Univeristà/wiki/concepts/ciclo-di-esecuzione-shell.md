---
type: concept
title: Ciclo di Esecuzione Shell
tags: [bash, shell, processi]
related: [bash]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione6-bash-AA25-26.txt"]
---
# Ciclo di Esecuzione Shell

Il ciclo di esecuzione descrive il processo iterativo attraverso il quale la shell gestisce l'interazione con l'utente. Le fasi principali sono:

1.  **Operazioni di start-up**: Caricamento delle configurazioni e delle variabili d'ambiente.
2.  **Acquisizione di un comando**: Lettura dell'input dall'utente.
3.  **Verifica EOF**: Controllo se la fine del file/input è stata raggiunta.
4.  **Macro espansione**: Sostituzione di variabili, metacaratteri e altre espansioni prima dell'esecuzione.
5.  **Esecuzione del comando**: Chiamata al programma (built-in o file eseguibile).
6.  **Operazioni di terminazione**: Pulizia delle risorse e chiusura del processo della shell.