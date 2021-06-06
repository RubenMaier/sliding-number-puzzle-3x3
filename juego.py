import numpy as np
from random import randint, choice

class Juego:
    # inicio un tablero de 3x3
    def __init__(self):
        self.tablero = np.zeros((3, 3))
        index = 0
        for i in range (3):
            for j in range (3):
                self.tablero[i, j] = index
                index += 1

    def intercambiar_posicion(self, a, b):
        aux = self.tablero[a]
        self.tablero[a] = self.tablero[b]
        self.tablero[b] = aux

    def mover_este(self):
        index = np.where(self.tablero == 0)
        if index[1] == 2:
            return False
        mover_a = (index[0], index[1]+1)
        self.intercambiar_posicion(index, mover_a)
        return True

    def mover_oeste(self):
        index = np.where(self.tablero == 0)
        if index[1] == 0:
            return False
        mover_a = (index[0], index[1]-1)
        self.intercambiar_posicion(index, mover_a)
        return True

    def mover_sur(self):
        index = np.where(self.tablero == 0)
        if index[0] == 2:
            return False
        mover_a = (index[0]+1, index[1])
        self.intercambiar_posicion(index, mover_a)
        return True

    def mover_norte(self):
        index = np.where(self.tablero == 0)
        if index[0] == 0:
            return False
        mover_a = (index[0]-1, index[1])
        self.intercambiar_posicion(index, mover_a)
        return True

    # redefino el print
    def __str__(self):
        result = ''
        for i in range(3):
            result += '| '
            for j in range(3):
                result += '%s | ' % (str(int(self.tablero[i, j])) if self.tablero[i, j] != 0 else ' ')
            result += '\n'
        return result
    
    # ejecuto un movimiento random entre 10 a 100 veces
    def mezclar(self):
        for i in range(randint(10, 100)):
            f = choice([
                self.mover_sur,
                self.mover_norte,
                self.mover_este,
                self.mover_oeste
            ])
            f()

    def movimientos(self, listaDeMovimientos, mostrarEnPantalla=False):
        movimientoPosibles = {
            'norte': self.mover_norte,
            'sur': self.mover_sur,
            'oeste': self.mover_oeste,
            'este': self.mover_este,
        }
        for movimientoEnConcreto in listaDeMovimientos:
            movimientoPosibles[movimientoEnConcreto]()
            if mostrarEnPantalla:
                print(self)

    def manhattan(self):
        reference = {
            0: (0, 0),
            1: (0, 1),
            2: (0, 2),

            3: (1, 0),
            4: (1, 1),
            5: (1, 2),

            6: (2, 0),
            7: (2, 1),
            8: (2, 2),
        }
        error = 0.0
        for i in range(9):
            index = np.where(self.tablero == i)
            ref_index = reference[i]
            error += ((index[0] - ref_index[0]) ** 2 + (index[1] - ref_index[1]) ** 2) ** (1/2)
        return error 