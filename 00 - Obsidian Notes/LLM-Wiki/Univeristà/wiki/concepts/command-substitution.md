---
type: concept
title: Command Substitution
tags: [bash, shell, espansione]
related: [ridirezione-e-pipe]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione6-bash-AA25-26.txt"]
---
# Command Substitution

La sostituzione di un comando permette di sostituire un pattern con l'output generato dall'esecuzione di un comando all'interno di una stringa o di una variabile.

## Sintassi
Il pattern viene indicato tramite `$(comando)`.

## Esempi
- `$(ls)` equivale a `*` (elenco file corrente).
- `$(echo ciao)` equivale a `ciao`.
- `a=$(ls)` assegna alla variabile `a` l'elenco dei file nella directory corrente.
- `touch "$(date)"` crea un file chiamato con la data attuale.