---
type: concept
title: Protezione vs Sicurezza
tags: [so, sicurezza, protezione, kernel, accesso]
related: ["servizi-sistema-operativo"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2b-AA25-26.txt"]
---
# Protezione vs Sicurezza

Sebbene spesso usati come sinonimi, nel contesto dei sistemi operativi i termini "protezione" e "sicurezza" hanno sfumature distinte:

## Protezione (Protection)
Si riferisce al controllo degli accessi **interni** al sistema.

- **Obiettivo**: Garantire la segregazione tra processi diversi e tra utenti diversi all'interno del sistema. Mira ad assicurare che i processi simultanei non interferiscano tra loro e che gli utenti non accedano a risorse non autorizzate.
- **Meccanismi**: 
    - Isolamento della memoria.
    - Gestione dei permessi sui file.
    - Controllo degli privilegi dei processi.

## Sicurezza (Security)
Si riferisce alla difesa contro accessi **esterni** o non autorizzati.

- **Obiettivo**: Proteggere il sistema da attacchi provenienti dall'esterno e garantire l'identità degli utenti.
- **Meccanismi**: 
    - Autenticazione dell'utente (password, biometria).
    - Crittografia.
    - Firewall.
    - Difesa dei dispositivi I/O esterni da accessi non consentiti.