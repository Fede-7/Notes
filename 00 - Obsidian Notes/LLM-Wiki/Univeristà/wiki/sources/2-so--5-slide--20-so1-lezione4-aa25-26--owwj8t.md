---
type: source
title: "SO1 Lezione 4 - Chiamate di Sistema, Virtualizzazione e Strutture del Kernel"
tags: [SO1, kernel, virtualizzazione, system-calls]
related: [system-call, virtualizzazione, strutture-del-kernel]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-AA25-26.txt"]
authors: []
year: 2025
url: ""
venue: ""
---
# SO1 Lezione 4 - Chiamate di Sistema, Virtualizzazione e Strutture del Kernel

Questa lezione approfondisce l'interfaccia tra programmi utente e kernel, le diverse architetture dei sistemi operativi e le tecnologie di virtualizzazione.

## Chiamate di Sistema (System Calls)
Le chiamate di sistema sono l'interfaccia fondamentale per richiedere servizi dal kernel. Le categorie principali includono:
- **Gestione informazioni**: Ora, data, dati di sistema, attributi di processi/file/dispositivi.
- **Comunicazione**: Creazione connessioni, invio/ricezione messaggi, memoria condivisa.
- **Protezione**: Controllo accessi, gestione permessi.
- **Controllo processi**: Creazione, arresto, caricamento, esecuzione, attendere eventi.
- **Gestione file**: Creazione, cancellazione, apertura, chiusura, lettura, scrittura.
- **Gestione dispositivi**: Richiesta/rilascio, I/O, attributi.

Viene fornita una tabella comparativa tra le chiamate di sistema di **Windows** e **UNIX** (es. `CreateProcess()` vs `fork()`, `ReadFile()` vs `read()`). Viene inoltre illustrato il ruolo della **Standard C Library** come wrapper (es. `printf()` che invoca `write()`).

## Programmi di Sistema
I programmi di sistema forniscono l'ambiente per lo sviluppo e l'esecuzione di applicazioni. Si dividono in:
- Manipolazione file (editor, comandi).
- Informazioni sullo stato (monitoraggio sistema).
- Supporto linguaggi (compilatori, debugger).
- Caricamento ed esecuzione (dynamic loader, linker).
- Comunicazioni.
- Servizi di background (demoni, servizi di stampa).

## Progettazione del Sistema Operativo
- **Politica vs Meccanismo**: Distinzione tra "cosa fare" (politica) e "come farlo" (meccanismo). La separazione garantisce flessibilità.
- **Implementazione**: Evoluzione dai linguaggi di basso livello (Assembly) a linguaggi di sistema (C, C++) e scripting (Python, Perl).

## Virtualizzazione
- **Emulazione**: Riproduce un'architettura hardware diversa (es. QEMU). Lenta ma flessibile.
- **Virtualizzazione**: Esegue sistemi operativi nativi sull'hardware reale.
- **Tipi di Virtualizzazione**:
    - *Full*: Il guest non sa di essere virtualizzato (es. VMware).
    - *Paravirtual*: Il guest collabora con l'VMM tramite API (es. Xen).
    - *Hardware-assisted*: Utilizza istruzioni CPU specifiche (Intel VT-x, AMD-V).
- **Hypervisor**:
    - *Tipo 1*: Gira direttamente sull'hardware (es. KVM, Hyper-V, ESXi).
    - *Tipo 2*: Gira sopra un SO host (es. VirtualBox).

## Strutture del Kernel
- **Monolitico**: Procedure linkate in un unico eseguibile (efficace ma poco modulare).
- **Stratificato**: Livelli gerarchici (es. THE).
- **Microkernel**: Kernel minimale (IPC, memoria, processi); servizi nello spazio utente.
- **Ibrido**: Combinazione di approcci (es. macOS, Windows).
- **Loadable Kernel Modules (LKMs)**: Moduli caricabili dinamicamente.

## Caso Studio: Android
Android è basato sul kernel Linux (monolitico) e utilizza:
- **HAL (Hardware Abstraction Layer)**: Astrae l'hardware.
- **ART (Android Runtime)**: Esegue le applicazioni.