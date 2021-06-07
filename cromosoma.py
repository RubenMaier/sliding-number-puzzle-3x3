import random

class Cromosoma:
    VALID_MOVES = ['norte', 'sur', 'oeste', 'este']

    def __init__(self, juego, longitud_cromosoma=10):
        gen = []
        for i in range(longitud_cromosoma):
            gen.append(random.choice(self.VALID_MOVES))   
        self.juego = juego
        self.lista_de_movimientos = gen

    def calcular_aptitud(self):
        result = 999
        if (not(self.juego.movimientos(self.lista_de_movimientos) == True)):
            result = self.juego.manhattan()
        return result

    def mutar(self):
        add_vs_mutate_chance = 0.5
        if not self.lista_de_movimientos:
            add_vs_mutate_chance = 1.0
        if random.random() < add_vs_mutate_chance:
            i = random.randint(0, len(self.lista_de_movimientos)-1)
            self.lista_de_movimientos[i] = random.choice(self.VALID_MOVES)

    def __str__(self):
        return '(%d)  %s' % (len(self.lista_de_movimientos), ' -> '.join(self.lista_de_movimientos))