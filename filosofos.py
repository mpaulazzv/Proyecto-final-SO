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


while True:

    for i in range (num_filosofos):
        filosofos[i] = threading.Thread(target=comensales, args=(i))