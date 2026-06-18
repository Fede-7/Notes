---
type: concept
title: Trap
tags: [so, hardware, kernel]
related: [system-call, user-mode, kernel-mode]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione3-AA25-26.txt"]
---
# Trap
Una **Trap** è un'istruzione hardware utilizzata per passare il controllo dal programma utente al kernel durante l'esecuzione di una chiamata di sistema. 

Quando viene eseguita l'istruzione (es. `syscall` su x86-64), la CPU:
1. Salva lo stato corrente del programma utente.
2. Passa dalla modalità *user mode* alla modalità *kernel mode*.
3. Salta a un indirizzo predefinito nel kernel (la tabella degli handler).
4. Una volta completata l'operazione, il kernel restituisce il controllo al programma utente, che riprende l'esecuzione dal punto di interruzione.
