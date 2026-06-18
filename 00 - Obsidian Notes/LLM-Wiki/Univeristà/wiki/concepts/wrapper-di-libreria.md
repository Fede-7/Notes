---
type: concept
title: Wrapper di Libreria
tags: [so, libc, api, system-calls]
related: [system-call, posix-api, abi]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2b-AA25-26.txt"]
---
# Wrapper di Libreria

Un **wrapper di libreria** è una struttura software (come la `libc`) che incapsula le chiamate di sistema (system calls) per fornire un'interfaccia più semplice, portabile e potente ai programmatori.

## Funzioni principali
- **Astrazione**: Permette ai programmatori di utilizzare API standard (come POSIX) senza dover conoscere i dettagli specifici delle system call del kernel sottostante.
- **Portabilità**: Una libreria può tradurre la stessa chiamata API in diverse system call a seconda del sistema operativo (es. Linux vs Windows).
- **Ottimizzazione**: Alcune operazioni richieste tramite l'API possono essere gestite interamente dalla libreria senza dover attivare un `TRAP` (passaggio al kernel), migliorando le prestazioni.
- **Gestione Errori**: Le librerie spesso gestiscono i codici di errore complessi del kernel, fornendo interfacce più intuitive (es. la variabile globale `errno`).

### Esempio di flusso
Quando un programma esegue `read(fd, buf, count)`:
1. Il programma chiama la funzione della libreria.
2. La libreria verifica i parametri e prepara i registri.
3. La libreria esegue l'istruzione `syscall`.
4. Il kernel esegue l'operazione e restituisce il risultato alla libreria.
5. La libreria restituisce il valore finale al programma.