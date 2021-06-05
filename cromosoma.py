import random
from copy import deepcopy

class Cromosoma:
    VALID_MOVES = ['norte', 'sur', 'oeste', 'este']

    def __init__(self, juego, gen=None):
        #inicializar la lista de genes con movimientos random (no se van a cambiar la cantidad de movimientos, ya que entiendo que según el mail que nos mandaron, la cantidad puede quedar fija, y solo habría que revisar si con los movimientos que tenemos, se cumple la resolucion final del tablero)
        if gen is None:
            gen = []
        self.error = None
        self.costo_de_error_del_juego = None
        self.error_gen_len = None
        self.juego = juego
        self.lista_de_movimientos = gen
        self.actualizar_error()

    def actualizar_error(self):
        aux = deepcopy(self.juego)
        aux.movimientos(self.lista_de_movimientos)
        self.costo_de_error_del_juego = aux.costo()
        self.error_gen_len = len(self.lista_de_movimientos) * 0.01
        self.error = self.costo_de_error_del_juego + self.error_gen_len

    def calcular_aptitud(self):
        #calcular distancia manhattan para aumetar o disminuir valor
        #penalizar si tiene algun movimiento invalido o si el estado final es incorrecto
        #llama a la funcion movimientos
        #devuelve un valor
        return 1

    @staticmethod
    def cruzar(a, b):
        if len(b.lista_de_movimientos) > len(a.lista_de_movimientos):
            return Cromosoma.cruzar(b, a)
        lista_de_movimientos_A = []
        lista_de_movimientos_B = []
        len_a = len(a.lista_de_movimientos)
        len_b = len(b.lista_de_movimientos)
        for i in range(len_b):
            if random.random() < 0.5:
                lista_de_movimientos_A.append(a.lista_de_movimientos[i])
                lista_de_movimientos_B.append(b.lista_de_movimientos[i])
            else:
                lista_de_movimientos_A.append(b.lista_de_movimientos[i])
                lista_de_movimientos_B.append(a.lista_de_movimientos[i])
        if len_b != len_a:
            for i in range(len_a-len_b):
                lista_de_movimientos_A.append(a.lista_de_movimientos[len_b+i])
        return Cromosoma(a.juego, lista_de_movimientos_A), Cromosoma(b.juego, lista_de_movimientos_B)

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