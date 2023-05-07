import csv
import config

lista_pokedex = []
lista_gen = []
lista_stat_total = []
lista_nombre = []
lista_legendario = []

#si no es legendario, peso = 10, si es legendario peso = 50, peso maximo = 100

class Pokemon(object):

    def __init__(self, dex, nombre, total, legendario):
        self.total = total
        self.nombre = nombre
        self.dex = dex
        self.legendario = legendario
        self.peso = 0

    def asignar_peso(self):
        if self.legendario == True:
            self.peso = 50
        else:
            self.peso = 10
        
    def __str__(self):
        return f"#: {self.dex}, Nombre: {self.nombre}, Stats: {self.total}"

    
class Mochila(object):

    with open(config.DATABASE_PATH, "r") as fichero:
        reader = csv.reader(fichero)
        for row in reader:
            lista_pokedex.append(row[0])
            lista_stat_total.append(row[4])
            lista_nombre.append(row[1])
            lista_legendario.append(row[12])            

    def __init__(self):
        self.capacidad = 6
        self.peso_max = 100
        self.pokemons = []
        self.size = 0

    def agregar_pokemon(self, pokemon):
        if self.size < self.capacidad:
            self.pokemons.append(pokemon)
            self.size += 1
        else:
            print("La mochila esta llena")

    def eliminar_pokemon(self, pokemon):
        if self.size > 0:
            self.pokemons.remove(pokemon)
            self.size -= 1
        else:
            print("La mochila esta vacia")

    def mostrar_pokemon(self):
        for pokemon in self.pokemons:
            print(pokemon)

    def seleccionar_mejores_stats(self):
        for i in range(len(lista_stat_total)):
            if lista_legendario[i] == "True":
                pokemon = Pokemon(lista_stat_total[i], True)
                pokemon.asignar_peso()
                self.agregar_pokemon(pokemon)
            else:
                pokemon = Pokemon(lista_stat_total[i], False)
                pokemon.asignar_peso()
                self.agregar_pokemon(pokemon)

    def crear_equipo(self):
        self.seleccionar_mejores_stats()
        while self.peso_max > 0:
            for pokemon in self.pokemons:
                if self.peso_max - pokemon.peso >= 0:
                    self.peso_max -= pokemon.peso
                    self.eliminar_pokemon(pokemon)
                    break
                else:
                    self.eliminar_pokemon(pokemon)
                    break
        self.mostrar_pokemon()

mochila = Mochila()
mochila.crear_equipo()