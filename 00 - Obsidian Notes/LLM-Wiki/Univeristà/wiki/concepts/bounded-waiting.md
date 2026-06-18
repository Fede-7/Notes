---
type: concept
title: Bounded Waiting
tags: ["sincronizzazione", "requisiti", "thread", "liveness", "starvation"]
related: ["sezione-critica", "mutua-esclusione", "progresso", "soluzione-di-peterson", "starvation"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
# Bounded Waiting

Il [[bounded-waiting]] (attesa limitata) è una proprietà di un sistema di sincronizzazione che garantisce che nessun processo debba attendere indefinitamente per accedere alla [[sezione-critica]]. 

Questa garanzia assicura che ogni processo che richiede l'accesso alla sezione critica lo ottenga entro un tempo limitato. In particolare, il *bounded waiting* stabilisce un limite massimo al numero di volte in cui altri processi possono entrare nelle loro sezioni critiche dopo che un processo ha fatto richiesta di entrarci. In altre parole, impedisce che altri processi entrino e escano ripetutamente dalla stessa sezione a scapito di un processo che è già in attesa.

### Starvation
Questa proprietà è fondamentale per prevenire la *starvation*, assicurando che nessun processo rimanga in attesa indefinitamente mentre altri accedono ripetutamente alla risorsa.

### Note sui Semafori
È importante sottolineare che i semafori base non garantiscono automaticamente il *bounded waiting*.