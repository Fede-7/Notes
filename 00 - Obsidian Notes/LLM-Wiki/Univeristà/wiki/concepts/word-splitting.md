---
type: concept
title: Word Splitting
tags: [bash, shell, espansione]
related: [variabili-di-shell, quoting]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione6-bash-AA25-26.txt"]
---
# Word Splitting

Il *word splitting* è l'ultima fase prima dell'esecuzione di un comando, in cui la riga di comando viene suddivisa in parole.

## Variabile IFS
La suddivisione è definita dalla variabile d'ambiente **IFS (Internal Field Separator)**.
- **Valore di default**: `IFS="<space><tab><newline>"`
- **Effetto collaterale**: Il word splitting sostituisce i newline con spazi.

In directory con molti file, questo può causare differenze tra l'output di `ls` e `echo $(ls)`, poiché quest'ultimo potrebbe unire i nomi dei file in un'unica riga separata da spazi.