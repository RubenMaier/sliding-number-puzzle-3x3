import random
from copy import deepcopy

class Cromosoma:
    VALID_MOVES = ['norte', 'sur', 'oeste', 'este']

    def __init__(self, juego, gen=None):
        #inicializar la lista de genes con movimientos random (no se van a cambiar la cantidad de movimientos, ya que entiendo que según el mail que nos mandaron, la cantidad puede quedar fija, y solo habría que revisar si con los movimientos que tenemos, se cumple la resolucion final del tablero)
        if gen is None:
            gen = []
        self.juego = juego
        self.lista_de_movimientos = gen

    def calcular_aptitud(self):
        #calcular distancia manhattan para aumetar o disminuir valor
        #penalizar si tiene algun movimiento invalido o si el estado final es incorrecto
        #llama a la funcion movimientos
        #devuelve un valor
        self.juego.movimientos()
        return self.juego.manhattan()

    @staticmethod
    def cruzar(a, b):
        return

    def mutar(self):
        #cambiar si se quiere más o menos mutacion
        add_vs_mutate_chance = 0.5
        #se podria sacar, si la lista de movimientos se inicializa al principio de todo
        if not self.lista_de_movimientos:
            add_vs_mutate_chance = 1.0
        if random.random() < add_vs_mutate_chance:
            i = random.randint(0, len(self.lista_de_movimientos)-1)
            self.lista_de_movimientos[i] = random.choice(self.VALID_MOVES)

    # redefino el print
    def __str__(self):
        return '(%d)  %s' % (len(self.lista_de_movimientos), ' -> '.join(self.lista_de_movimientos))