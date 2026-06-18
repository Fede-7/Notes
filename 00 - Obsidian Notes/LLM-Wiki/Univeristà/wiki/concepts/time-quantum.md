---
type: concept
title: Time Quantum
tags: [scheduling, round-robin]
related: [dispatcher]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# Time Quantum

Il **Time Quantum** è l'unità di tempo fissa assegnata a ogni processo durante l'esecuzione in un algoritmo di scheduling **Round Robin (RR)**. Se un processo non termina entro il quantum, viene messo in coda e il dispatcher passa il controllo al processo successivo. Un quantum troppo piccolo aumenta l'overhead dei context switch, mentre uno troppo grande rende il sistema meno interattivo.