---
type: concept
title: Variabili di Shell
tags: [bash, ambiente, variabili]
related: [bash, ciclo-di-esecuzione-shell]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione6-bash-AA25-26.txt"]
---
# Variabili di Shell

Le variabili di shell sono identificatori utilizzati per memorizzare dati che influenzano il comportamento della shell e dei programmi eseguiti.

## Variabili di Ambiente
Sono variabili predefinite che caratterizzano il comportamento del sistema. Per convenzione, sono scritte in maiuscolo:
- **HOME**: Percorso della directory home dell'utente (inizializzato da `/etc/passwd`).
- **PATH**: Elenco di directory in cui il sistema cerca gli eseguibili.
- **PS1**: Stringa che definisce il prompt dell'utente (es. `$` per utenti normali, `#` per super-user).
- **HOSTNAME**: Nome del computer.
- **SHELL**: Percorso della shell corrente.

## Sintassi e Regole
- **Scrittura/Definizione**: `nome_variabile=valore` (senza spazi attorno all'uguale).
- **Lettura**: Si accede al valore tramite il simbolo `$` (es. `$a`) o con la sintassi di espansione `${a}`.
- **Quoting nelle assegnazioni**: Il quoting funziona diversamente durante l'assegnazione rispetto all'uso dei comandi; ad esempio, `a=ciao pippo` fallisce perché la shell interpreta `pippo` come un comando separato.