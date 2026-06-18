---
type: concept
title: Virtualizzazione
tags: [virtualizzazione, hypervisor, cloud, hardware, containerizzazione, virtual machine]
related: ["emulazione-vs-virtualizzazione", "kvm", "hyper-v", "wsl2", "containerizzazione", "virtual machine"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-AA25-26.txt", "SO/Trascrizioni/Lezione 29.txt"]
---
# Virtualizzazione

La virtualizzazione è la tecnologia che permette di creare una separazione completa tra l'hardware fisico e il sistema operativo. Attraverso un hypervisor, è possibile eseguire più macchine virtuali (VM) indipendenti su un unico server fisico, facendo sì che ogni sistema operi come se avesse hardware dedicato.

Ogni VM dispone del proprio kernel e di una propria allocazione di risorse hardware virtualizzate. Rispetto ai container, le macchine virtuali risultano più pesanti ma garantiscono un maggiore isolamento.

## Hypervisor (VMM)
Il Virtual Machine Manager (VMM), noto anche come Hypervisor, fornisce i servizi di virtualizzazione gestendo le risorse e l'esecuzione delle VM. Si divide principalmente in due categorie:

- **Tipo 1 (Bare Metal)**: L'hypervisor gira direttamente sull'hardware e funge da sistema operativo host. 
  *Esempi: VMware ESXi, Xen, Hyper-V, KVM.*
- **Tipo 2 (Hosted)**: L'hypervisor gira sopra un sistema operativo host esistente. 
  *Esempi: Oracle VirtualBox, VMware Workstation.*

## Tipi di Virtualizzazione
Esistono diversi approcci per implementare la virtualizzazione, a seconda di come il sistema guest interagisce con l'hardware:

- **Virtualizzazione Completa (Full)**: Il sistema guest non è consapevole di essere virtualizzato e vede l'hardware come reale. Offre massima compatibilità ma comporta un overhead maggiore. *Esempio: VMware.*
- **Paravirtualizzazione**: Il sistema guest è consapevole della virtualizzazione e collabora con l'hypervisor tramite API speciali. Questo riduce l'overhead ma richiede che i sistemi operativi siano modificati. *Esempio storico: Xen.*
- **Virtualizzazione Assistita da Hardware**: Utilizza istruzioni specifiche della CPU (come Intel VT-x o AMD-V) per gestire la virtualizzazione in modo efficiente. È lo standard della virtualizzazione moderna.