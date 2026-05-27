
### **📁 Gestione Memoria e Thrashing** *(Lezioni: 6, 12, 13)*
**Argomenti principali**:
- **Thrashing** (6.6)
- **Page Fault** (13.5.3)
- **Località** (6.4)
- **Layout di memoria di un processo** (5.3)
- **Indirizzi logici vs fisici** (12.6)
- **Algoritmi di sostituzione pagine** (12.7.1)

---

### **📁 File System** *(Lezioni: 14, 15)*
**Argomenti principali**:
- **Journaling** (14.6)
- **Metodi di allocazione** (12.7.1)
- **Strutture dati** (14.4, 14.6)

---

### **📁 Sincronizzazione e Architettura** *(Lezioni: 7, 8, 9, 1.8)*
**Argomenti principali**:
- **Read-Write Lock** (9.12.2)
- **Monitor** (9.9)
- **Compare-and-Swap** (9.6.2)
- **Vettore delle interruzioni** (1.8)
- **Priority Inversion** (9.11)

---
### **📁 Sincronizzazione** *(Lezione: 9)*
**Argomenti principali**:
- **Spin-lock** vs **Blocked-lock**
- **Istruzioni atomiche** (test_and_set, CAS)
- **Semafori** (binari, contatori)
- **Mutex**

---

### **📁 Thread e Processi** *(Lezione: 5, 7)*
**Argomenti principali**:
- **PID e TID**
- **Spazio di indirizzamento**
- **Creazione thread**

---

### **📁 Allocazione dei File** *(Lezione: 12, 14)*
**Argomenti principali**:
- **Frammentazione esterna/interna**
- **Accesso random vs sequenziale**

---

### **📁 Scheduling** *(Lezione: 10, 11)*
**Argomenti principali**:
- **Starvation**
- **Equità degli algoritmi**
- **Scheduling a priorità**

---
### **📁 Struttura del SO** *(Lezione: 1)*
**Argomenti principali**:
- **Monolitico vs Microkernel**
- **Efficienza vs estensibilità**

---
### **📁 Copy-on-Write** *(Lezione: 13)*
**Argomenti principali**:
- **Ottimizzazione fork()**
- **Memoria condivisa padre-figlio**

---
---
---
## **📊 Riassunto per Argomento di Studio**
Ecco come **organizzare lo studio** in base alle domande:

| **Argomento Principale** | **Sottotemi Chiave** | **Domande Aperte** | **Domande Quiz** | **Lezioni Riferite** |
|--------------------------|----------------------|-------------------|------------------|---------------------|
| **Gestione Memoria** | Thrashing, Page Fault, Località, Layout memoria, Indirizzi logici/fisici, Algoritmi sostituzione. | 1, 2, 3, 4, 5, 6 | - | 5, 6, 12, 13 |
| **File System** | Journaling, Allocazione file, Strutture dati (inode, directory, tabelle file aperti). | 7, 8, 9 | 16 | 12, 14, 15 |
| **Sincronizzazione** | RW Lock, Monitor, Variabili di condizione, CAS, Vettore interruzioni, Priority Inversion. | 10, 11, 12, 13 | 14 | 1, 7, 8, 9 |
| **Thread e Processi** | PID/TID, Spazio indirizzamento, Creazione thread. | - | 15 | 5, 7 |
| **Scheduling** | Algoritmi (FCFS, RR, SJF, Priority), Starvation, Equità. | - | 17 | 10, 11 |
| **Struttura SO** | Monolitico, Microkernel, Modulare, Ibrido. | - | 18 | 1 |
| **Copy-on-Write** | Ottimizzazione `fork()`, Pagine condivise. | - | 19 | 13 |
