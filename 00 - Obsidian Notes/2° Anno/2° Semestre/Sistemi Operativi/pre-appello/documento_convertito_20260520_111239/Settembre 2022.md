## Pagina 1

Sistemi Operativi 1 – Appello d’esame del 06/09/2022

Nome e cognome DARLO FRANZESE Matricola N860036+3

La durata della prova è di 2 ore. Scrivere in stampatello maluscolo. E’ obbilgatorio restituire il testo e tutti i fogli forniti, anche se non si consegna il compito.

1. Considerati CPU-burst time (in ms) del set di processi descritto in tabella, e considerato che l’ordine di arrivo dei processi è P1, P2, P3, P4, P5.

| Processo | Burst Time | Priorità | Tempo di arrivo |
| :--- | :--- | :--- | :--- |
| P1 | 5 | 3 | 0 |
| P2 | 3 | 1 | 2 |
| P3 | 4 | 2 | 4 |
| P4 | 2 | 4 | 5 |
| P5 | 2 | 1 | 6 |

a) Disegnare 2 diagrammi di Gantt che illustrino l’esecuzione di questi processi usando gli algoritmi di scheduling Priorità con prelazione e RR (quanto = 3 ms). Indicare l’istante di tempo di ciascuna commutazione fra un processo e l’altro.

b) Calcolare il tempo di attesa per ciascun processo e per ciascun algoritmo di scheduling. Descrivere il procedimento usato (in estrema sintesi definire il tempo d’attesa e come l’avete applicato per calcolare i risultati esposti)

| RR | Priorità (con RR) |
| :--- | :--- |
| P1 | 3-0=3 | 9-0=3 |
| P2 | 3-2=1 | 2-2=0 |
| P3 | 12-4-8 | 7-4=3 |
| P4 | 11-5=6 | 14-6=9 |
| P5 | 13-6=7 | 6-6=0 |

c) Calcolare il tempo di tournaround per ciascun processo e per ciascun algoritmo di scheduling. Descrivere il procedimento usato (in estrema sintesi definire il tempo di risposta e come l’avete applicato per calcolare i risultati esposti)

| RR | Priorità (con RR) |
| :--- | :--- |
| P1 | 3+5=8 | 9+5=14 |
| P2 | 1+3=4 | 0+3=3 |
| P3 | 8+4=12 | 3+4=7 |
| P4 | 6+2=8 | 7+2=11 |
| P5 | 7+2=9 | 0+2=2 |

2. Tenuto conto che:

- il pid del processo padre è 9 e quello del primo figlio è 10 e quello del secondo figlio è 11.

Cosa stamperà il seguente programma? Giustificare in estrema sintesi la risposta

---

## Pagina 2

```c
int var = 5;

int main()
{
    pid_t pid1, pid2;

    printf("Sono il processo padre.\n");

    pid1 = fork();

    if(pid1 == 0)
        var = var + 1;
    else {
        pid2 = fork();
        var = var + pid1 + pid2;
    }

    printf("pid = %d var = %d \n", var, getpid());

    return 0;
}

3. Dato il frammento di programma che segue:

a) Quanti processi e quanti thread genera il frammento di programma seguente?

b) Evidenziare, se ci sono, le corse critiche.

c) Cosa stamperà il programma?

Giustificare in estrema sintesi le risposte

#define NUM_THREADS 3

int var1 = 10, var2 = 0;

void *func1(void* param)
{
    var1 -= 1;
    return 0;
}

void *func2(void* param)
{
    var2 += 1;
    return 0;
}

int main()
{
    pthread_t threads[NUM_THREADS];

    pthread_create(&threads[0], NULL, func1, NULL);  VAR1=3
    pthread_create(&threads[1], NULL, func2, NULL);  VAR2=1
    pthread_join(threads[0], NULL);
    pthread_join(threads[1], NULL);

    fork();

    pthread_create(&threads[1], NULL, func2, NULL);  LAR1=8
    pthread_create(&threads[2], NULL, func1, NULL);  VAR2=2
}
```

---

## Pagina 3

pthread_join(threads[1], NULL);
pthread_join(threads[2], NULL);

printf("%d %d\n", var1, var2);

return 0;
}

4. Nel contesto dei metodi per evitare i deadlock:
a) Dati tre thread T0, T1, T2 e tre tipi di risorsa A (4 istanze), B (4 istanze), C (4 istanze) con le seguenti matrici di Allocazione e Max:
| Allocazione | Max |
| :--- | :--- |
| A B C | A B C |
| T0 0 2 1 | 2 3 3 |
| T1 2 1 2 | 3 2 2 |
| T2 1 0 0 | 2 2 2 |

b) Calcolare il vettore Disponibile e la matrice Bisogno
c) Verificare se il sistema è in uno stato sicuro (spiegare i passaggi)
d) Può T2 richiedere subito (1, 0, 0)? Se viene assegnato cosa succede?

5. Si consideri una memoria paginata:
Si assumano uno spazio di indirizzo logici di 4096 pagine con pagine di 2 KB mappate su memoria fisica da 512 frame.
a) Quante sono i bit dell'indirizzo logico?
b) Quante sono i bit dell'indirizzo fisico?
c) Quanti entry per una tabella delle pagine invertita?

6. Si consideri un processo che genera la seguente stringa dei riferimenti alle pagine virtuali:
5, 1, 3, 4, 1, 2, 1, 4

a) Se il processo ha 3 frame gestiti con LRU quanti page fault vengono generati?
b) Quanti page fault vengono generati con l'algoritmo OPT?

7. Assumendo 3500 cilindri e testina su 1800 (con richiesta precedente a 500)
a) Data la coda di richieste 10, 1500, 1450, 3200, 20, 250 come vengono servite le richieste con SCAN
b) Qual è la distanza in cilindri percorsi della testina con l'algoritmo SCAN?

8. Spiegare brevemente vantaggi e svantaggi dei metodi di allocazione dei file concatenata e indicizzata.

9. Cos’è un read-write lock? Discutere brevemente il problema dei lettori e scrittori (illustrandone una soluzione).

10. Nell’ambito dello scheduling dei processi spiegare brevemente il problema dell’inversione di priorità.

---

