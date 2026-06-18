---
type: entity
title: SSD (Solid State Drive)
tags: ["hardware", "storage", "memoria-di-massa", "nand-flash", "flash"]
related: ["hdd", "gerarchia-di-memorie", "ftl", "gestione-nand-flash", "lba", "usura-delle-memorie-flash", "flash-vs-hdd-mapping"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2a-AA25-26.txt", "SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt", "SO/Trascrizioni/Lezione 20.txt"]
---
# SSD (Solid State Drive)

Gli **SSD** (Solid-State Drives o Solid-State Disks) sono dispositivi di memoria secondaria elettrica basati su tecnologia flash. Utilizzano memorie non volatili basate su semiconduttori, tipicamente [[nand]], anziché parti meccaniche in movimento.

### Caratteristiche principali
- **Velocità**: Offrono tempi di accesso e di trasferimento significativamente più rapidi rispetto ai dischi magnetici.
- **Accesso**: Garantiscono un accesso casuale uniforme e tempi di accesso brevi.
- **Robustezza**: Essendo privi di componenti mobili, sono meno soggetti a guasti meccanici causati da urti o vibrazioni.

### Vantaggi rispetto agli HDD
A differenza degli HDD, gli SSD non possiedono parti meccaniche, il che comporta:
- **Assenza di latenze meccaniche**: Eliminano il *seek time* e la *rotational latency*.
- **Affidabilità fisica**: Maggiore resistenza agli stress fisici grazie alla natura elettronica del dispositivo.

### Gestione e Limitazioni Tecnologiche
Nonostante i vantaggi, gli SSD presentano limitazioni fisiche intrinseche alla tecnologia NAND:

- **Gestione della scrittura**: È necessaria la cancellazione a blocchi prima di poter effettuare nuove operazioni di scrittura.
- **Mappatura dei dati**: La gestione dei dati avviene tramite il [[ftl]] (Flash Translation Layer), che mappa gli indirizzi logici forniti dal sistema operativo agli indirizzi fisici.
- **Usura**: Le celle di memoria subiscono un deterioramento dovuto ai cicli ripetuti di cancellazione e scrittura. Questo fenomeno, noto come [[usura-delle-memorie-flash]], è spesso misurato in [[dwpd]] (*Drive Writes Per Day*).