import threading 
from multiprocessing import Process
import multiprocessing
import time

num_filosofos = 5
disponible = 1
no_disponible = 0

tenedores = []
estado = []
for i in range(num_filosofos):
        estado.append(disponible)
filosofos = []

def comensales (args):
    
    print("filósofo["+str(args+1)+"] pensando ...")
    print("filósofo["+str(args+1)+"] hambriento ...")

    if (args == 0):
        a = num_filosofos - 1
    else:
        a = args - 1
    
    if (estado[args] == disponible and estado[a]==disponible):
        tenedores[args].acquire()
        tenedores[a].acquire()
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
    
    time.sleep(2)


if __name__ == "__main__":
    c = 0
    i =0
    for i in range(num_filosofos):
        estado[i] = disponible

    for i in range (num_filosofos):
        tenedores.append(multiprocessing.Semaphore(1))

    for i in range (num_filosofos):
        filosofos.append(Process(target=comensales, args=[i]))
        filosofos[i].start()

while True:

    for i in range (num_filosofos):
        tenedores[i] = multiprocessing.Semaphore(1)

    for i in range (num_filosofos):
        filosofos[i] = (Process(target=comensales, args=[i]))
        filosofos[i].start()

    for i in range (num_filosofos):
        filosofos[i].join()
    