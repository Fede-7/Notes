# Guida alla lettura

Questa dispensa segue gli argomenti e la progressione delle
**lezioni di Tecnologie Web** del PDF fornito (146 pagine). Lo
scopo è imparare a **definire i concetti, spiegare i meccanismi,
confrontare approcci e interpretare semplici frammenti di codice**: non
soltanto memorizzare parole chiave. Sono mantenute anche distinzioni
facilmente oggetto di domanda d'esame. Gli esempi sono illustrativi e
non sostituiscono le esercitazioni pratiche. La lezione 14 del materiale
di partenza è dedicata soprattutto a esercizi di ripasso e alla traccia
del progetto: per questa ragione non compare come capitolo teorico
autonomo.

**Metodo di studio.** Per ciascuna sezione saper rispondere a tre
domande: *che cos'è?*, *come funziona?*, *quando e perché
lo si usa?*. I riquadri **Da ricordare** individuano differenze e
errori ricorrenti. La terminologia tecnica inglese resta presente
accanto a quella italiana.

# Parte I --- DNS

## 1. Domain Name System

### Definizione, nomi e
gerarchia

**DNS (Domain Name System)**: database **distribuito e
gerarchico** di Internet che associa a un nome informazioni descritte
tramite *resource record* (RR). Non associa necessariamente un nome
a un computer: un nome può identificare servizi, alias, server di posta
o nodi amministrativi. DNS non è una semplice rubrica centralizzata.

Un **nome DNS** è una sequenza di **etichette** separate da
punti, lette in senso gerarchico **da destra a sinistra**. In
`informatica.dieti.unina.it.` la gerarchia è: radice `.` →
`it` → `unina` → `dieti` → `informatica`. La
radice corrisponde all'etichetta vuota finale; i nomi sono
**case-insensitive**. Un nome completo terminato dal punto è un
*fully qualified domain name* (FQDN). Uno stesso host può possedere
più nomi.

**Dominio**: nodo dell'albero dei nomi insieme a tutto il suo
sottoalbero. **Zona**: porzione del namespace di cui uno o più name
server pubblicano autoritativamente i record. **Delega**:
trasferimento dell'autorità su un sottoalbero ad altri name server. Se
`unina.it` delega `dieti.unina.it`, quest'ultimo resta nel
**dominio** `unina.it`, ma non nella **zona**
`unina.it`.

Un **name server autoritativo** contiene e distribuisce dati delle
zone per cui è responsabile; può servire molte zone e una zona può avere
più server autoritativi, anche per ridondanza. Un **resolver
ricorsivo** interroga i server necessari fino a ricostruire una risposta,
spesso riutilizzando cache.

### Resource record e attori

Un record DNS contiene: **owner name** (nome a cui si riferisce),
**TTL** (*time to live*, durata in secondi della copia in
cache), **class** (di norma `IN`), **type** (natura del
record) e **value** (dato). Esempio:
`www.example.org. 3600 IN A 192.0.2.5`.
