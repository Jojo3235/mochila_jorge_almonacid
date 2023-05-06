class Heap(object):

    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio

def agregar(heap, dato):
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1

def quitar(heap):
    intercambio(heap, 0, heap.tamanio - 1)
    dato = heap.vector[heap.tamanio - 1]
    heap.tamanio -= 1
    hundir(heap, 0)
    return dato

def cantidad_elementos(heap):
    return heap.tamanio

def heap_vacio(heap):
    return heap.tamanio == 0

def heap_lleno(heap):
    return heap.tamanio == len(heap.vector)

def flotar(heap, indice):
    while indice > 0 and heap.vector[indice] > heap.vector[(indice - 1) // 2]:
        padre = (indice - 1) // 2
        intercambio(heap, indice, padre)
        indice = padre

def hundir(heap, indice):
    hijo_izq = (indice * 2) + 1
    control = True
    while control and hijo_izq < heap.tamanio:
        hijo_der = hijo_izq + 1
        aux = hijo_izq
        if hijo_der < heap.tamanio:
            if heap.vector[hijo_der] > heap.vector[hijo_izq]:
                aux = hijo_der
        if heap.vector[indice] < heap.vector[aux]:
            intercambio(heap, indice, aux)
            indice = aux
            hijo_izq = (indice * 2) + 1
        else:
            control = False

def intercambio(heap, i, j):
    heap.vector[i], heap.vector[j] = heap.vector[j], heap.vector[i]

def monticuluzar(heap):
    for i in range(len(heap.vector)):
        flotar(heap, i)

def arribo(heap, dato, prioridad):
    agregar(heap, [dato, prioridad])

def atencion(heap):
    return quitar(heap)[1]

def buscar(heap, posicion):
    return heap.vector[posicion][1]

def cambiar_prioridad(heap, indice, prioridad):
    prioridad_anterior = heap.vector[indice][1]
    heap.vector[indice][1] = prioridad
    if prioridad > prioridad_anterior:
        flotar(heap, indice)
    else:
        hundir(heap, indice)

def heapsort(heap):
    aux = heap.tamanio
    for i in range(heap.tamanio):
        quitar(heap)
    heap.tamanio = aux

# from random import randint
# import time

# start = time.time()
# heap = Heap(10000)

# while not heap_lleno(heap):
#     num = randint(0, 500)
#     prioridad = randint(1, 3)
#     agregar(heap, [prioridad, num])
# print(heap.vector)
# while not heap_vacio(heap):
#     dato = atencion(heap)
#     print(dato)
# print(heap.vector)
# end = time.time()

# print(buscar(heap, 5))
# cambiar_prioridad(heap, 0, 4)
# # print(heap.vector)

# print(end - start)