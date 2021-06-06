import random

from copy import copy
from cromosoma import Cromosoma

class AlgoritmoGenetico:
    def __init__(self, juego, poblacion_inicial=1000, probabilidad_de_mutacion=0.9, tasa_de_cruce=0.3):
        self.juego = juego
        # parametros
        self.poblacion_inicial = poblacion_inicial
        self.probabilidad_de_mutacion = probabilidad_de_mutacion
        self.tasa_de_cruce = tasa_de_cruce
        # variables
        self.poblacion = []
        self.el_mejor_cromosoma = None
        self.no_es_aptitud_0 = True

    def _iniciar_poblacion(self):
        self.poblacion = [Cromosoma(juego=self.juego) for _ in range(self.poblacion_inicial)]

    def _seleccionar(self):
        def obtenerAptitud(un_cromosoma):
            aptitud = int(un_cromosoma.calcular_aptitud())
            print("aptitud calculada: " + str(aptitud))
            return aptitud
        # manhattan menor implica mejor solucion
        #poblacion_ordenada = self.poblacion.sort(reverse=True, key=obtenerAptitud)
        sorted(self.poblacion, key=obtenerAptitud)
        self.el_mejor_cromosoma = copy(self.poblacion[0])
        print("la mejor aptitud es: " + str(obtenerAptitud(self.el_mejor_cromosoma)))
        if (obtenerAptitud(self.poblacion[0]) == 0):
            self.no_es_aptitud_0 = False

    def _cruzar(self):
        for i in range(int(self.poblacion_inicial/2)):
            #cruzar los primeros 500
            #el if sirve para que tome de a pares, espaciado en 2
            if i > 0 and (i % 2 == 0):
                #obtengo el punto de corte, que va de la posicion 1 (arranca en 0) a la anteultima posicion
                punto_corte = random.randrange(1, len(self.poblacion[i].lista_de_movimientos)-2)
                #si tienen ganas de dejarlo mas lindo, se puede meter todo esto, dentro del cromosoma, 
                #en la funcion de cruzar (para no romper el encapsulamiento)
                #obtengo el hijoA, formado por la primer parte del primer padre y la segunda parte del segundo padre
                hijo_a = self.poblacion[i-1].lista_de_movimientos[0:punto_corte] + self.poblacion[i].lista_de_movimientos[punto_corte+1:len(self.poblacion[i].lista_de_movimientos)]
                hijo_b = self.poblacion[i].lista_de_movimientos[0:punto_corte] + self.poblacion[i-1].lista_de_movimientos[punto_corte+1:len(self.poblacion[i].lista_de_movimientos)]
                #reemplazo los padres por sus hijos

                #################################
                #self.poblacion[i-1].lista_de_movimientos = hijo_a
                #self.poblacion[i].lista_de_movimientos = hijo_b

    def _mutar(self):
        for cromosoma in self.poblacion:
            #si tienen ganas, pueden hacer que mute uno solito, no me parece mal que intente hacer mutar algunos segun los que salgan seleccionados por el random
            if random.random() < self.probabilidad_de_mutacion:
                cromosoma.mutar()

    def resolver(self, max_iter=1000):
        random.seed()
        self._iniciar_poblacion()
        iteracion = 0
        #cambiar el error, por cantidad de iteraciones maximas
        #habria que sacar el error, o de ultima, evaluarlo en base a la ponderacion de la longitud de manhattan de todos los movimientos (GENES) del cromosoma
        while iteracion < max_iter and self.no_es_aptitud_0:
            self._seleccionar()
            self._cruzar()
            #HAY QUE INICIALIZAR LA LISTA DE MOVIMIENTOS, YA QUE ARRANCA VACIA
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