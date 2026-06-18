---
type: concept
title: sospensione-processi
tags: [semaforo, scheduling]
related: [busy-waiting, deadlock, semaforo]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 11.txt"]
---
# sospensione-processi

La sospensione dei processi è il meccanismo con cui il sistema operativo rimuove i processi dalla coda di esecuzione (*ready queue*) e li inserisce in una coda di attesa specifica (*waiting queue*) quando questi non possono procedere a causa della mancanza di una risorsa.

A differenza del *busy waiting*, la sospensione permette alla CPU di eseguire altri task mentre il processo è in attesa.