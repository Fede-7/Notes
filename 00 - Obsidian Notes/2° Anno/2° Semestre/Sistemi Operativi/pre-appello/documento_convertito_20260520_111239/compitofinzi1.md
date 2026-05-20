## Pagina 1

1. Considerati CPU-burst time (in ms) del set di processi descritto in tabella, e considerato che l’ordine di arrivo dei processi è P1, P2, P3, P4, P5.

| Processo | Burst Time | Priorità | Tempo di arrivo |
| :--- | :--- | :--- | :--- |
| P1 | 7 | 2 | 0 |
| P2 | 5 | 1 | 2 |
| P3 | 3 | 2 | 4 |
| P4 | 3 | 4 | 5 |
| P5 | 5 | 3 | 6 |

a) Disegnare 2 diagrammi di Gantt che illustrino l’esecuzione di questi processi usando gli algoritmi di scheduling Priorità e prelazione e RR (quanto = 4 ms). Indicare l’istante di tempo di ciascuna commutazione fra un processo e l’altro.

b) Calcolare il tempo di attesa per ciascun processo e per ciascun algoritmo di scheduling. Descrivere il procedimento usato (in estrema sintesi definire il tempo d’attesa e come l’avete applicato per calcolare i risultati esposti)

| RR (q=4) | Priority Preemptive |
| :--- | :--- |
| P1 | |
| P2 | |
| P3 | |
| P4 | |
| P5 | |

c) Calcolare il tempo di tournaround per ciascun processo e per ciascun algoritmo di scheduling. Descrivere il procedimento usato (in estrema sintesi definire il tempo di risposta e come l’avete applicato per calcolare i risultati esposti)

| RR (q=4) | Priority Preemptive |
| :--- | :--- |
| P1 | |
| P2 | |
| P3 | |
| P4 | |
| P5 | |

2. Tenuto conto che:

- il pid del processo padre è 100 e quello del suo primo figlio è 101, quello del secondo figlio è 102, quello del figlio del primo figlio è 103.

Cosa stamperà il seguente programma? Giustificare in estrema sintesi la risposta

---

## Pagina 2

int var = 10;

int main()
{
    pid_t pid1, pid2;

    printf("Sono il processo padre.\n");

    pid1 = fork();

    if(pid1 == 0)
        var = var + 5;
        pid2 = fork();
    else {
        pid2 = fork();
    }
    var = var + pid1 + pid2;

    printf("pid = %d var = %d \n", var, getpid());

    return 0;
}

3. Dato il frammento di programma che segue:

a) Quanti processi e quanti thread genera il frammento di programma seguente?

b) Cosa stamperà il programma?

c) Evidenziare, se ci sono, le corse critiche indicando come evitarle

Giustificare in estrema sintesi le risposte

int var1 = 5, var2 = 50;

void *func1(void* param)
{
    var1 += 10;

    var2 -= 15;

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
    int pid;

    pid = fork();

    if (pid == 0) {
        pthread_create(&threads[0], NULL, func1, NULL);

        pthread_create(&threads[1], NULL, func2, NULL);

        pthread_join(threads[0], NULL);

        pthread_join(threads[1], NULL);
    }
}

---

## Pagina 3

else {
    pthread_create(&threads[2], NULL, func1, NULL);
    pthread_join(threads[2], NULL);
}

printf("%d %d\n", var1, var2);

return 0;
}

4. Nel contesto dei metodi per evitare i deadlock:
   a) Dati tre thread T0, T1, T2 e tre tipi di risorsa A (5 istanze), B (5 istanze), C (4 istanze) con le seguenti matrici di Allocazione e Max:
      Allocazione Max
      A B C A B C
      T0 1 2 1 6 5 4
      T1 2 1 2 3 2 3
      T2 1 1 0 5 4 4

   b) Calcolare il vettore Disponibile e la matrice Bisogno
   c) Verificare se il sistema è in uno stato sicuro (spiegare i passaggi)
   d) Può T0 richiedere subito (0, 1, 0)? Se viene assegnato lo stato rimane sicuro?
   e) Spiegare in modo succinto cosa significa stato sicuro.

5. Si consideri una memoria paginata:
   Si assumano uno spazio di indirizzo logici di 4096 pagine con pagine di 4 KB mappate su memoria fisica di 1024 frame.
   a) Quante sono i bit dell’indirizzo logico?
   b) Quante sono i bit dell’indirizzo fisico?
   c) Quanti entry per una tabella delle pagine?
   d) Quante entry ha una tabella delle pagine di secondo livello se quella di primo è di 4 entry?

6. Si consideri un processo che genera la seguente stringa dei riferimenti alle pagine virtuali:
   7, 7,3, 3, 4,7, 1, 4, 1, 4,7,5,3

   a) Se il processo ha 4 frame gestiti con LRU quanti page fault vengono generati?
   b) Quanti page fault vengono generati con l’algoritmo OPT?

7. Assumendo 5000 cilindri e testina su 3800 (con richiesta precedente a 3500)
   a) Data la coda di richieste 1000, 2500, 4450, 4150, 2000, 250 come vengono servite le richieste con C-LOOK
   b) Qual è la distanza in cilindri percorsi della testina con l’algoritmo C-LOOK?

8. Cosa si intende per thrashing? Descrivere schematicamente la problematica.

9. Cos`è un’istruzione compare-and-swap? Spiegarne funzionamento e funzione.

10. Descrivere schematicamente le strutture dati principali utilizzate dal sistema operativo per la gestione del file system.

---

