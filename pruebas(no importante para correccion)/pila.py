class nodoPila(object):

    info, sig = None, None

class Pila(object):
        
    def __init__(self):
        self.tamanio = 0
        self.cima = None

def apilar(pila, dato):
    nodo = nodoPila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1

def desapilar(pila):
    x = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return x

def pila_vacia(pila):
    return pila.tamanio == 0

def tamanio(pila):
    return pila.tamanio

def en_cima(pila):
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None
    
def barrido(pila):
    paux = Pila()
    while not pila_vacia(pila):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))

# def main():
#     pila = Pila()
#     apilar(pila, 1)
#     apilar(pila, 2)
#     apilar(pila, 3)
#     apilar(pila, 4)
#     apilar(pila, 5)
#     barrido(pila)
#     print('tamanio: ', tamanio(pila))
#     print('cima: ', en_cima(pila))
#     print('desapilado: ', desapilar(pila))
#     print('tamanio: ', tamanio(pila))
#     print('cima: ', en_cima(pila))
#     print('desapilado: ', desapilar(pila))

# if __name__ == '__main__':
#     main()