---
type: entity
title: task_struct
tags: [linux, kernel, processi]
related: [pcb-task-control-block.md]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-5-6-AA25-26.txt"]
---
# task_struct
In ambito Linux, `task_struct` è la struttura dati fondamentale del kernel che rappresenta il [[pcb-task-control-block.md]]. Contiene tutti i metadati necessari per gestire un processo o un thread, inclusi il PID, lo stato della CPU, le priorità, le informazioni sulla memoria e i descrittori di file.