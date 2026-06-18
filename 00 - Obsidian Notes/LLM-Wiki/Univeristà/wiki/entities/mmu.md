---
type: entity
title: MMU
tags: ["hardware", "memoria", "architettura", "memoria-virtuale", "kernel"]
related: ["tlb", "paginazione", "indirizzi-logici-vs-fisici", "memoria-virtuale", "device-driver"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-principale-AA25-26.txt", "SO/Slide/SO1-Lezioni-mem-virtuale-AA25-26.txt", "SO/Trascrizioni/Lezione 25.txt"]
---
# MMU (Memory Management Unit)

La **MMU** (Memory Management Unit) è un dispositivo hardware fondamentale, gestito dai driver, responsabile della traduzione degli indirizzi logici (virtuali) generati dalla CPU in indirizzi fisici nella memoria principale. È il componente essenziale per l'implementazione della [[memoria-virtuale]], la gestione della memoria e la protezione dei processi.

### Funzionamento e Mappatura
L'MMU gestisce la mappatura degli indirizzi attraverso strutture dati come le tabelle delle pagine. Durante il processo di traduzione, l'unità è responsabile della gestione dei segnali di *page fault* nel caso in cui un indirizzo richiesto non sia presente nella memoria fisica.

### Ottimizzazione e Isolamento
Per accelerare le operazioni di traduzione, l'MMU lavora in stretta collaborazione con la [[tlb]]. Grazie a questo meccanismo, è possibile implementare il **binding a tempo di esecuzione**, lo standard nei sistemi operativi moderni, che consente ai processi di operare in uno spazio di indirizzamento virtuale isolato.