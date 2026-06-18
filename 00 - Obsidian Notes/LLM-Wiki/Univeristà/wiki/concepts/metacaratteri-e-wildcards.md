---
type: concept
title: Metacaratteri e Wildcards
tags: [bash, shell, espansione]
related: [quoting, word-splitting]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione6-bash-AA25-26.txt"]
---
# Metacaratteri e Wildcards

La shell scansiona i comandi alla ricerca di caratteri speciali chiamati **metacaratteri**, che vengono processati in modo speciale prima dell'esecuzione.

## Wildcards (Abbreviazioni Pathname)
I wildcard sono usati per espandere i nomi dei file:
- `*`: Stringa di 0 o più caratteri (esclude il punto `.`).
- `?`: Singolo carattere.
- `[ ]`: Singolo carattere tra quelli elencati (es. `[a-zA-Z]`).
- `{ }`: Stringhe specifiche elencate (es. `{bin,doc,lib}`).

## Altri Metacaratteri
- `!`: Ripetizione di comandi dalla history.
- `#`: Commento.
- `\`: Escape (inibisce l'effetto speciale del carattere successivo).