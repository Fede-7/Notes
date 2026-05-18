# Trascrizione Lezione: Bootstrap, Swap Space e Architetture RAID

**Data:** 6 Maggio 2026
**Argomento:** Partizionamento, Boot Process (MBR vs UEFI/GPT), Gestione dello Swap Space, Affidabilità dei Dischi e Livelli RAID.

---

### 1. Organizzazione Logica del Disco: Partizioni e Volumi

Il Sistema Operativo astrae la struttura fisica del disco (settori, tracce, cilindri o pagine NAND) in una struttura logica gestibile.

1.  **Partizionamento (Low-Level Logical Structure):**
    *   Il disco fisico viene suddiviso in **partizioni**, che sono gruppi contigui di blocchi logici.
    *   Su HDD, le partizioni corrispondono spesso a gruppi di cilindri. La posizione fisica influenza le prestazioni (le partizioni esterne sono più veloci per ZBR).
    *   Le partizioni possono essere "grezze" (*raw*) o formattate con un file system.

2.  **Volumi (High-Level Abstraction):**
    *   Un **volume** è un'astrazione superiore alla partizione.
    *   Può coincidere 1:1 con una partizione, oppure span across multiple partitions (es. RAID software, LVM).
    *   Il volume è l'unità su cui viene creato il **File System**.

3.  **File System:**
    *   Organizza i blocchi del volume in file e directory gerarchiche.
    *   I/O operations avvengono a livello di blocchi/cluster, non di byte singoli.
    *   **Relazione Pagina/Blocco:** Idealmente, la dimensione del blocco del disco dovrebbe essere uguale o un sottomultiplo della pagina di memoria (es. 4KB) per ottimizzare le operazioni di Paging (Page In/Page Out).

---

### 2. Il Processo di Bootstrap (Avvio del Sistema)

Il bootstrap è la sequenza di caricamento del Sistema Operativo dalla memoria secondaria alla RAM.

#### A. Architettura Legacy: BIOS + MBR
*   **BIOS (Basic Input/Output System):** Firmware che esegue il POST (Power-On Self-Test) e cerca un dispositivo di boot.
*   **MBR (Master Boot Record):** Primi 512 byte del disco.
    *   **Boot Code (446 byte):** Codice eseguibile minimo.
    *   **Partition Table (64 byte):** Descrive max 4 partizioni primarie.
    *   **Signature (2 byte).**
*   **Limiti:** Indirizzamento a 32-bit -> Max disco ~2.2 TB. Max 4 partizioni primarie.
*   **Flusso:**
    1.  BIOS carica MBR in RAM ed esegue il Boot Code.
    2.  Il Boot Code legge la Partition Table e identifica la partizione attiva ("bootable").
    3.  Carica il **Bootloader di secondo livello** (es. GRUB, NTLDR) dal settore di avvio della partizione.
    4.  Il Bootloader carica il Kernel in RAM e passa il controllo.

#### B. Architettura Moderna: UEFI + GPT
*   **UEFI (Unified Extensible Firmware Interface):** Sostituisce il BIOS. Interfaccia più ricca, supporto mouse/grafica, networking pre-boot.
*   **GPT (GUID Partition Table):** Standard moderno per partizionamento.
    *   **Protective MBR:** Primo settore riservato per compatibilità legacy (indica che il disco è GPT).
    *   **GPT Header:** Descrive la struttura della tabella.
    *   **Partition Entries:** Tabella delle partizioni molto più grande (supporta >128 partizioni, indirizzi a 64-bit -> dischi enormi).
    *   **Backup GPT:** Copia della tabella alla fine del disco per ridondanza.
*   **EFI System Partition (ESP):** Una partizione speciale formattata FAT32 contenente i bootloader (.efi) dei vari SO installati.
*   **Flusso:**
    1.  UEFI esegue POST.
    2.  Legge GPT e identifica l'ESP.
    3.  Carica il **Boot Manager** dall'ESP (es. `bootx64.efi`, `grubx64.efi`).
    4.  Il Boot Manager presenta un menu (se multi-boot) e carica il Kernel specifico.
    5.  Il Kernel inizializza i subsistemi e monta il File System Root (`/` o `C:`).

> **Nota sul Dual-Boot:** Ogni SO ha la sua directory nell'ESP. Conflitti possono sorgere se un SO sovrascrive il bootloader predefinito (es. Windows Update che resetta il boot order).

---

### 3. Gestione dello Swap Space

Lo **Swap Space** è l'area su disco utilizzata per estendere la memoria virtuale (Backing Store).

*   **Raw Partition vs. Swap File:**
    *   **Raw Partition:** Area dedicata non formattata con file system. Accesso più diretto e veloce (meno overhead metadati). Usato storicamente.
    *   **Swap File:** File regolare all'interno di un file system (es. `/swapfile` in Linux, `pagefile.sys` in Windows). Più flessibile (ridimensionabile), overhead leggermente maggiore ma trascurabile su SSD moderni.
*   **Contenuto dello Swap:**
    *   Principalmente **Memoria Anonima** (stack, heap, dati modificabili).
    *   Il codice eseguibile (Text segment) solitamente non viene swappato, ma ricaricato direttamente dal file eseguibile su disco se necessario (poiché è read-only e già presente su storage).
*   **Strutture Dati Kernel:**
    *   Il Kernel mantiene in RAM una **Swap Map** (array di bit o contatori) per tracciare quali blocchi dello swap sono liberi/occupati.
    *   Le entry nella Page Table delle pagine non residenti contengono un riferimento alla posizione nello swap (offset), permettendo un rapido recupero durante un Page Fault.
    *   Se una pagina swap è condivisa (es. librerie), un contatore di riferimenti tiene traccia di quanti processi la usano. La pagina viene liberata solo quando il contatore arriva a zero.

---

### 4. Affidabilità e Performance: Architetture RAID

**RAID (Redundant Array of Independent/Inexpensive Disks)** combina più dischi fisici in un'unità logica per migliorare performance, affidabilità o entrambi.

#### Concetti Chiave
*   **MTTF (Mean Time To Failure):** Tempo medio tra i guasti di un singolo disco.
*   **Affidabilità dell'Array:** Con $N$ dischi, la probabilità che *almeno uno* si rompa aumenta drasticamente. Es. Se MTTF = 100.000 ore, un array di 100 dischi ha un MTTF sistemico di ~1.000 ore.
*   **Mirroring (Ridondanza):** Duplicazione dei dati. Aumenta affidabilità, costo spazio 2x.
*   **Striping (Performance):** Suddivisione dei dati in blocchi distribuiti su più dischi. Aumenta throughput (parallelismo I/O), ma diminuisce affidabilità (se un disco muore, i dati striped sono persi).

#### Livelli RAID Principali

| Livello | Tecnica | Descrizione | Pro | Contro | Min Dischi |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RAID 0** | Striping | Dati divisi a blocchi su tutti i dischi. No ridondanza. | Massima velocità I/O, 100% capacità. | **Zero tolleranza ai guasti.** Perdita totale dati se 1 disco fallisce. | 2 |
| **RAID 1** | Mirroring | Duplicazione esatta dei dati su due o più dischi. | Alta affidabilità, lettura veloce (parallela). | Costo spazio 50% (o più), scrittura lenta come singolo disco. | 2 |
| **RAID 5** | Striping + Parità Distribuita | Blocchi dati + blocchi di parità distribuiti su tutti i dischi. | Tolleranza a 1 guasto, buona lettura, efficienza spazio ($N-1$). | Scrittura lenta (overhead calcolo parità "write penalty"), ricostruzione complessa. | 3 |
| **RAID 6** | Striping + Doppia Parità | Come RAID 5, ma con due blocchi di parità indipendenti. | Tolleranza a **2 guasti** contemporanei. | Overhead scrittura maggiore, capacità utile $N-2$. | 4 |
| **RAID 10 (1+0)** | Mirror + Stripe | Prima si fa il mirroring di coppie, poi lo striping sulle coppie. | Alta performance (lettura/scrittura) + Alta affidabilità. | Costo spazio 50%. | 4 |
| **RAID 01 (0+1)** | Stripe + Mirror | Prima si fa lo striping, poi si mira l'intero stripe. | Simile a RAID 10, ma meno resiliente durante la ricostruzione. | Meno comune di RAID 10. | 4 |

*   **RAID 2, 3, 4:** Obsoleti o rari. Usavano parità dedicata (collo di bottiglia) o striping a bit/byte (granularità eccessiva per dischi moderni).

#### Considerazioni sulla Ricostruzione
*   Quando un disco fallisce in un RAID ridondante (1, 5, 6, 10), il sistema entra in stato degradato.
*   È cruciale sostituire il disco e ricostruire l'array rapidamente (**Mean Time To Repair - MTTR**).
*   Durante la ricostruzione, l'array è vulnerabile (specialmente RAID 5/6 sotto carico intenso). RAID 6 offre maggiore sicurezza durante questa fase critica.

---

*Fine della lezione.*
