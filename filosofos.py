import threading 
import multiprocessing

num_filosofos = 5
disponible = 1
no_disponible = 0

tenedores = []
estado = []
filosofos = []

def comensales (args):
    
    print("filósofo["+str(args)+"] pensando ...")
    print("filósofo["+str(args)+"] hambriento ...")

    if (args == 0):
        a = num_filosofos - 1
    else:
        a = args - 1
    
    if (estado[args] == disponible and estado[a]==disponible):
        tenedores[args].acquire(blocking=True)
        tenedores[a].acquire(blocking=True)
        estado[args] = no_disponible
        estado[a] = no_disponible
        print("El filósofo["+str(args+1)+"] toma los tenedores (" + str(args+1)+", "+str(a+1)+")")
        print("Filósofo ["+str(args+1)+"] comiendo...")
    
    if(estado[args] == no_disponible and estado[a]==no_disponible):
        tenedores[args].release()
        tenedores[a].release()
        estado[args] = disponible
        estado[a] = disponible
        print("El filósofo ["+str(args+1)+"] entrega los tenedores ("+ str(args+1)+", "+str(a+1)+")")

i = 0

for i in range(i < num_filosofos):
    estado[i] = disponible

while True:

    for i in range (num_filosofos):
        tenedores[i] = multiprocessing.Semaphore()

    for i in range (num_filosofos):
        filosofos[i] = threading.Thread(target=comensales, args=(i))
    
    for i in range (num_filosofos):
        filosofos[i].join()
    
    for i in range (num_filosofos):
        

    


#     void main(int argc, char *argv[])
# {
#     int i;
#     for (i = 0; i < NUM_FILOSOFO; i++)
#     {
#         estado[i] = DISPONIBLE;
#     }

#     while (1)
#     {

#         pthread_t filosofos[NUM_FILOSOFO];

#         for (i = 0; i < NUM_FILOSOFO; i++)
#         {
#             sem_init(&tenedores[i], 0, 1);
#         }

#         for (i = 0; i < NUM_FILOSOFO; i++)
#         {
#             pthread_create(&filosofos[i], NULL, &comensales, &i);
#         }

#         for (i = 0; i < NUM_FILOSOFO; i++)
#         {
#             pthread_join(filosofos[i], NULL);
#         }

#         for (i = 0; i < NUM_FILOSOFO; i++)
#         {
#             sem_destroy(&tenedores[i]);
#         }
#     }
# }
