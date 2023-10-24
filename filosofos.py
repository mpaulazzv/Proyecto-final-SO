import threading 

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

