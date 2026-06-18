---
type: concept
title: Progresso
tags: [sincronizzazione, requisiti, thread]
related: [sezione-critica, mutua-esclusione, bounded-waiting]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
# Progresso

Il [[progresso]] è la terza proprietà fondamentale per la gestione della [[sezione-critica]]. Esso garantisce che la selezione dei processi per l'accesso alla sezione critica non sia posticipata indefinitamente.

Il requisito di progresso stabilisce che:
- Se nessun processo è in sezione critica e almeno uno lo richiede, allora uno di essi deve poter entrare.
- Il meccanismo di selezione deve permettere a uno dei processi in attesa di entrare, e tale decisione deve dipendere esclusivamente dalle caratteristiche dei processi in attesa (non da fattori esterni).