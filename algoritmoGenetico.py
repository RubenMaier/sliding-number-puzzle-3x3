import random
import copy
from cromosoma import Cromosoma

class AlgoritmoGenetico:
    def __init__(self, juego, poblacion_inicial=1000, probabilidad_de_mutacion=0.5, longitud_cromosoma=10):
        self.juego = juego
        self.poblacion_inicial = poblacion_inicial
        self.probabilidad_de_mutacion = probabilidad_de_mutacion
        self.poblacion = []
        self.el_mejor_cromosoma = None
        self.no_es_aptitud_0 = True
        self.longitud_cromosoma = longitud_cromosoma

    def _iniciar_poblacion(self):
        self.poblacion = [Cromosoma(juego=self.juego, longitud_cromosoma=self.longitud_cromosoma) for _ in range(self.poblacion_inicial)]

    def _seleccionar(self):
        def obtenerAptitud(un_cromosoma):
            return un_cromosoma.calcular_aptitud()
        sorted(self.poblacion, key=obtenerAptitud, reverse=True)
        self.el_mejor_cromosoma = copy.deepcopy(self.poblacion[0])
        if (obtenerAptitud(self.el_mejor_cromosoma) == 0):
            self.no_es_aptitud_0 = False

    def _cruzar(self):
        for i in range(int(self.poblacion_inicial/2)):
            if i > 0 and (i % 2 == 0):
                punto_corte = random.randrange(1, len(self.poblacion[i].lista_de_movimientos)-2)
                
                hijo_a = self.poblacion[i-1].lista_de_movimientos[0:punto_corte] + self.poblacion[i].lista_de_movimientos[punto_corte:len(self.poblacion[i].lista_de_movimientos)]
                hijo_b = self.poblacion[i].lista_de_movimientos[0:punto_corte] + self.poblacion[i-1].lista_de_movimientos[punto_corte:len(self.poblacion[i].lista_de_movimientos)]
                
                self.poblacion[i-1].lista_de_movimientos = hijo_a
                self.poblacion[i].lista_de_movimientos = hijo_b

    def _mutar(self):
        for cromosoma in self.poblacion:
            if random.random() < self.probabilidad_de_mutacion:
                cromosoma.mutar()

    def resolver(self, max_iter=1000):
        random.seed()
        self._iniciar_poblacion()
        iteracion = 0
        while iteracion < max_iter and self.no_es_aptitud_0:
            self._seleccionar()
            self._cruzar()
            self._mutar()
            self._imprimir_resultado(iteracion)
            iteracion += 1
        return self.el_mejor_cromosoma

    def _imprimir_resultado(self, iteracion):
        print('~~~~~~~~ iteracion: %d ~~~~~~~~' % iteracion)
        print('longitud de poblacion (%d)' % (
            len(self.poblacion),
        ))
        if self.el_mejor_cromosoma:
            print('el_mejor_cromosoma es: %s' % self.el_mejor_cromosoma)
        print('--------------------------------')