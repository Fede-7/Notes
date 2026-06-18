---
type: concept
title: Ridirezione e Pipe
tags: [bash, shell, flussi]
related: [standard-io]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione6-bash-AA25-26.txt"]
---
# Ridirezione e Pipe

La shell permette di deviare i flussi standard verso file o altri canali, o di concatenare i comandi tra loro.

## Ridirezione (Redirection)
- **Output**: `comando > file` (sovrascrive il file), `comando >> file` (accoda all'output).
- **Input**: `comando < file` (usa il file come fonte di input).
- **Errore**: `comando 2> file` (devia solo gli errori).
- **Canale su Canale**: `comando (codiceA)>&(codiceB)` (es. `comando > file 2>&1` per deviare sia stdout che stderr nello stesso file).

## Pipeline (`|`)
La pipeline permette di collegare due o più comandi in modo che lo standard output di uno diventi lo standard input del successivo.
- Esempio: `cat file | sort | wc -l`
- Comandi comuni concatenabili: `cat`, `sort`, `wc`, `ls`, `less`.

## Altri Simboli di Flusso
- `< <delim`: *Here document* (ridirezione dell'input da una stringa multi-riga).
- `;`: Sequenza di comandi.
- `&&`: Esecuzione condizionale (successo).
- `||`: Esecuzione condizionale (fallimento).
- `(...)`: Raggruppamento di comandi.