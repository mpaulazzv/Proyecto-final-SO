#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define NUM_FILOSOFO 5
#define DISPONIBLE 1
#define NO_DISPONIBLE 0

sem_t tenedores[NUM_FILOSOFO];
int estado[NUM_FILOSOFO];

void *comensales(void *args)
{
    char c = *(int *)args;
    printf("filosofo[%d] pensando...\n", c + 1);
    printf("filosofo[%d] hambriento...\n", c + 1);

    int a;

    if (c == 0)
        a = NUM_FILOSOFO - 1;
    else
        a = c - 1;

    if (estado[c] == DISPONIBLE && estado[a] == DISPONIBLE)
    {
        sem_wait(&tenedores[c]);
        sem_wait(&tenedores[a]);
        estado[c] = NO_DISPONIBLE;
        estado[a] = NO_DISPONIBLE;
        printf("El filosofo[%d] toma los tenedores(%d, %d)\n", c + 1, c + 1, a + 1);
        printf("filosofo[%d] comiendo...\n", c + 1);
    }

    if (estado[c] == NO_DISPONIBLE && estado[a] == NO_DISPONIBLE)
    {
        sem_post(&tenedores[c]);
        sem_post(&tenedores[a]);
        estado[c] = DISPONIBLE;
        estado[a] = DISPONIBLE;
        printf("filosofo[%d] entrega los tenedores(%d, %d)\n", c + 1, c + 1, a + 1);
    }

    sleep(1);
}

void main(int argc, char *argv[])
{
    int i;
    for (i = 0; i < NUM_FILOSOFO; i++)
    {
        estado[i] = DISPONIBLE;
    }

    while (1)
    {

        pthread_t filosofos[NUM_FILOSOFO];

        for (i = 0; i < NUM_FILOSOFO; i++)
        {
            sem_init(&tenedores[i], 0, 1);
        }

        for (i = 0; i < NUM_FILOSOFO; i++)
        {
            pthread_create(&filosofos[i], NULL, &comensales, &i);
        }

        for (i = 0; i < NUM_FILOSOFO; i++)
        {
            pthread_join(filosofos[i], NULL);
        }

        for (i = 0; i < NUM_FILOSOFO; i++)
        {
            sem_destroy(&tenedores[i]);
        }
    }
}
