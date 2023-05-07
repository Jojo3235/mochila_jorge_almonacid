from cola import *

class nodoArista(object):

    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None

class nodoVertice(object):

    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()

class Grafo(object):

    def __init__(self, dirigido=True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0

class Arista(object):

    def __init__(self):
        self.inicio = None
        self.tamanio = 0

def insertar_vertice(grafo, dato):
    nodo = nodoVertice(dato)
    if grafo.inicio is None or grafo.inicio.info > dato:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info < nodo.info:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1

def insertar_arista(grafo, dato, origen, destino):
    o = buscar_vertice(grafo, origen)
    d = buscar_vertice(grafo, destino)
    if o is not None and d is not None:
        insertar_arista_aux(o, dato, destino)
        if not grafo.dirigido:
            insertar_arista_aux(d, dato, origen)

def insertar_arista_aux(origen, dato, destino):
    insertar_arista_aux(origen.adyacentes, dato, destino)

def agregar_arista(origen, dato, destino):
    nodo = nodoArista(dato, destino)
    if origen.inicio is None or origen.inicio.destino > destino:
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while act is not None and act.destino < nodo.destino:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1

def eliminar_vertice(grafo, clave):
    x = None
    if grafo.inicio.info == clave:
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info != clave:
            ant = act
            act = act.sig
        if act is not None:
            x = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if x is not None:
        aux = grafo.inicio
        while aux is not None:
            if aux.adyacentes.inicio is not None:
                eliminar_arista(aux.adyacentes, clave)
            aux = aux.sig
    return x

def eliminar_arista(vertice, destino):
    x = None
    if vertice.inicio.destino == destino:
        x = vertice.inicio.info
        vertice.inicio = vertice.inicio.sig
        vertice.tamanio -= 1
    else:
        ant = vertice.inicio
        act = vertice.inicio.sig
        while act is not None and act.destino != destino:
            ant = act
            act = act.sig
        if act is not None:
            x = act.info
            ant.sig = act.sig
            vertice.tamanio -= 1
    return x

def tamanio(grafo):
    return grafo.tamanio

def grafo_vacio(grafo):
    return grafo.inicio is None

def buscar_vertice(grafo, buscado):
    aux = grafo.inicio
    while aux is not None and aux.info != buscado:
        aux = aux.sig
    return aux

def buscar_arista(vertice, buscado):
    aux = vertice.adyacentes.inicio
    while aux is not None and aux.destino != buscado:
        aux = aux.sig
    return aux

def existe_paso(grafo, origen, destino):
    resultado = False
    if not origen.visitado:
        origen.visitado = True
        vadyacentes = origen.adyacentes.incio
        while vadyacentes is not None and not resultado:
            adyacente = buscar_vertice(grafo, vadyacentes.destino)
            if adyacente.info == destino.info:
                resultado = True
            elif not adyacente.visitado:
                resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado

def adyacentes(vertice):
    aux = vertice.adyacentes.inicio
    while aux is not None:
        print(aux.destino, aux.info)
        aux = aux.sig

def es_adyacente(vertice, destino):
    resultado = False
    aux = vertice.adyacentes.inicio
    while aux is not None and not resultado:
        if aux.destino == destino:
            resultado = True
        aux = aux.sig
    return resultado

def marcar_no_visitado(grafo):
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig

def barrido_vertices(grafo):
    aux = grafo.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig

def barrido_profundidad(grafo, vertice):
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while adyacentes is not None:
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if not adyacente.visitado:
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig

def barrido_amplitud(grafo, vertice):
    cola = Cola()
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
            while not cola_vacia(cola):
                nodo = atencion(cola)
                print(nodo.info)
                adyacentes = nodo.adyacentes.inicio
                while adyacentes is not None:
                    adyacente = buscar_vertice(grafo, adyacentes.destino)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacentes = adyacentes.sig
        vertice = vertice.sig

from heap import *
from pila import *

def dijkstra(grafo, origen, destino):
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info == origen:
            arribo(no_visitados, [aux, None], 0)
        else:
            arribo(no_visitados, [aux, None], 99999)
        aux = aux.sig
    while not heap_vacio(no_visitados):
        dato = atencion(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = buscar(no_visitados, aux.destino)
            if no_visitados.vector[pos][0] > dato[0] + aux.info:
                no_visitados.vector[pos][0] = dato[0] + aux.info
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino


grafo = Grafo(False)

#cargar grafo: peso, origen, destino {[2, F, R], [2, F, X], [3, F, T], [4, R, Z], [5, R, X], [6, T, X], [8, T, R], [9, X, Z]}
def cargar_grafos(grafo):
    insertar_vertice(grafo, 'F')
    insertar_vertice(grafo, 'R')
    insertar_vertice(grafo, 'T')
    insertar_vertice(grafo, 'X')
    insertar_vertice(grafo, 'Z')
    insertar_arista(grafo, 2, 'F', 'R')
    insertar_arista(grafo, 2, 'F', 'X')
    insertar_arista(grafo, 3, 'F', 'T')
    insertar_arista(grafo, 4, 'R', 'Z')
    insertar_arista(grafo, 5, 'R', 'X')
    insertar_arista(grafo, 6, 'T', 'X')
    insertar_arista(grafo, 8, 'T', 'R')
    insertar_arista(grafo, 9, 'X', 'Z')

cargar_grafos(grafo)

barrido_profundidad(grafo, grafo.inicio)
marcar_no_visitado(grafo)
barrido_amplitud(grafo, grafo.inicio)

origen = buscar_vertice(grafo, 'T')
destino = buscar_vertice(grafo, 'Z')
camino_mas_corto = None
if origen is not None and destino is not None:
    if existe_paso(grafo, origen, destino):
        camino_mas_corto = dijkstra(grafo, origen, destino)
        fin = destino.info
        while not pila_vacia(camino_mas_corto):
            dato = desapilar(camino_mas_corto)
            if fin == dato[1][0].info:
                print(dato[1][0].info)
                fin = dato[1][1]

# marcar_no_visitado(grafo)
# arbol_minimo = Kruskal(grafo)
# print(arbol_minimo)