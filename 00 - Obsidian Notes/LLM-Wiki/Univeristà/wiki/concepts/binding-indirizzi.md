---
type: concept
title: Binding degli Indirizzi
tags: [memoria, architettura]
related: [indirizzi-logici-vs-fisici, mmu]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-principale-AA25-26.txt"]
---
# Binding degli Indirizzi

Il **binding degli indirizzi** è il processo di associazione degli indirizzi di istruzioni e dati alla memoria fisica. Questo può avvenire in tre momenti diversi:

1. **Tempo di Compilazione**: Il codice viene generato con indirizzi assoluti (codice assoluto).
2. **Tempo di Caricamento**: Il codice è rilocabile; gli indirizzi vengono assegnati quando il programma viene caricato in memoria.
3. **Tempo di Esecuzione (Runtime)**: Gli indirizzi vengono mappati dinamicamente durante l'esecuzione del programma. Questo metodo è lo standard nei sistemi operativi moderni grazie all'uso della MMU.