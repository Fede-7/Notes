## Pagina 1

Sistemi Operativi 1 – Appello d’esame del 15/07/2024

Nome e cognome ___ Matricola ___

La durata della prova è di 2 ore. Scrivere in modo legibile. E’ obbligatorio restituire il testo e tutti i fogli forniti, anche se non si consegna il compito.

1. Considerati CPU-burst time (in ms) del set di processi descritto in tabella, e considerato che l’ordine di arrivo dei processi è P1, P2, P3, P4, P5.

| Processo | Burst Time | Tempo di arrivo |
| :--- | :--- | :--- |
| P1 | 2 | 0 |
| P2 | 5 | 1 |
| P3 | 3 | 2 |
| P4 | 4 | 4 |
| P5 | 3 | 5 |

a) Disegnare 2 diagrammi di Gantt che illustrino l’esecuzione di questi processi usando gli algoritmi di SJF e RR (quanto 2 mm). Indicare l’istante di tempo di ciascuna commutazione fra un processo e l’altro.

b) Calcolare il tempo di attesa per ciascun processo e per ciascun algoritmo di scheduling. Descrivere il procedimento usato (in estrema sintesi definire il tempo d’attesa e come l’avete applicato per calcolare i risultati esposti.

| SJF | RR |
| :--- | :--- |
| P1 | |
| P2 | |
| P3 | |
| P4 | |
| P5 | |

c) Calcolare il tempo di risposta per ciascun processo e per ciascun algoritmo di scheduling. Descrivere il procedimento usato (in estrema sintesi definire il tempo di risposta e come l’avete applicato per calcolare i risultati esposti).

| SJF | RR |
| :--- | :--- |
| P1 | |
| P2 | |
| P3 | |
| P4 | |
| P5 | |

2. Tenuto conto che:
- il pid del processo padre è 10 e quello del primo figlio è 11 quello del figlio del figlio è 12.

Cosa stamperà il seguente programma? Giustificare in estrema sintesi la risposta

```c
int var = 10;

int main()
{
    pid_t pid1, pid2;
    int status = 1;

    pid1 = fork();

    status++;
    if (pid1 > 0){
        var = var + status + pid1;
    }
    else {
        pid2 = fork();
        if (pid2 > 0) var = var + pid1 + pid2 + status;
    }

    printf("var = %d \n", var);
    printf("pid = %d \n", getpid());

    return 0;
}

3. Dato il frammento di programma che segue:
a) Quanti processi e quanti thread genera il frammento di programma seguente?
b) Evidenziare, se ci sono, le corse critiche. Come si possono evitare?
c) Cosa stamperà il programma?

Giustificare in estrema sintesi le risposte

```c
#define NUM_THREADS 3

int var1 = 30, var2 = 3;

void *func1(void* param)
{
    var1 = var1 + 10;
    return 0;
}

void *func2(void* param)
{
    var2 = var1 - 20;
    return 0;
}

int main()
{
    pthread_t threads[NUM_THREADS];

    for (int i = 0; i < NUM_THREADS -1; ++i) {
```

---

## Pagina 2

```python
pthread_create(&threads[i], NULL, func1, NULL);
}

for (int i = 0; i < NUM_THREADS - 1; ++i) {
    pthread_join(threads[i], NULL);
}

fork();

for (int i = 0; i < NUM_THREADS - 1; ++i) {
    pthread_create(&threads[i], NULL, func2, NULL);
}

for (int i = 0; i < NUM_THREADS - 1; ++i) {
    pthread_join(threads[i], NULL);
}

printf("var1:%d, var2:%d\n", var1, var2);

return 0;
}

4. Nel contesto dei metodi per evitare i deadlock:
a) Dati tre thread T0, T1, T2 e tre tipi di risorsa A (5 istanze), B (5 istanze), C (5 istanze) con le seguenti matrici di Allocazione e Max:
   Allocazione Max
   A B C A B C
T0 2 1 1 3 4 4
T1 2 1 1 4 3 3
T2 0 1 2 1 3 3

b) calcolare il vettore Disponibile e la matrice Bisogno
c) Verificare se il sistema è in uno stato sicuro (spiegare i passaggi)
d) Può T0 richiedere (0, 1, 0)? Se viene assegnato cosa succede?

5. Si consideri una memoria paginata:
Si assuma uno spazio di indirizzi logici di 2048 pagine con pagine da 8 KB mappate su memoria fisica di 1024 frame
a) Quanti bit occorrono per l'indirizzo logico?
b) Quanti bit occorrono per l'indirizzo fisico?

6. Si consideri un processo che genera la seguente stringa dei riferimenti alle pagine virtuali:
   6, 4, 2, 6, 1, 4, 2, 1, 4, 3, 5, 2, 1

a) Se il processo ha 3 frame gestiti con LRU quanti page fault vengono generati?
b) Quanti page fault vengono generati con l’algoritmo FIFO?

7. Assumendo 5000 cilindri e testina su 1000 (con richiesta precedente a 1100)
a) Data la coda di richieste 2000, 300, 1800, 800, 4800, 1200, 900 come vengono servite le richieste con l’algoritmo SSTF
```

---

## Pagina 3

b) Qual è la distanza in cilindri percorsi della testina con l’algoritmo SSTF?

8. Descrivere brevemente le caratteristiche degli algoritmi second chance discutendone vantaggi e svantaggi

9. Cos’è un vettore delle interruzioni? Descrivere come viene utilizzato per la gestione delle interruzioni.

10. Cos’è un read-write lock? Discutere brevemente il problema dei lettori e scrittori (illustrandone una soluzione).

---

