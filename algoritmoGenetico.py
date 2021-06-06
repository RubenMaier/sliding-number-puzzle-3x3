import random
import math

from copy import deepcopy
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
        self.error = None

    def _iniciar_poblacion(self):
        self.poblacion = [Cromosoma(juego=self.juego) for _ in range(self.poblacion_inicial)]

    def _calcular_error(self):
        if not self.poblacion:
            return
        if self.el_mejor_cromosoma is None:
            self.el_mejor_cromosoma = self.poblacion[0]
        error = 0
        for cromosoma in self.poblacion:
            cromosoma.actualizar_error()
            if cromosoma.error < self.el_mejor_cromosoma.error:
                self.el_mejor_cromosoma = deepcopy(cromosoma)
            error += cromosoma.error
        self.error = error / len(self.poblacion)

    def _seleccionar(self):
        totales = []
        corridas_totales = 0
        for cromosoma in self.poblacion:
            w = 1 / (0.000001 + cromosoma.error)
            corridas_totales += w
            totales.append(corridas_totales)
        def select_i():
            rnd = random.random() * corridas_totales
            for i, total in enumerate(totales):
                if rnd < total:
                    return i
        resultado = []
        while len(resultado) < self.poblacion_inicial:
            i = select_i()
            resultado.append(self.poblacion[i])
        self.poblacion = resultado

    def _cruzar(self, always=False):
        if len(self.poblacion) < 2:
            return
        cruzar_occur = math.ceil(len(self.poblacion) * self.tasa_de_cruce)
        genes_aptos = [i for i in range(len(self.poblacion))]
        for i in range(int(cruzar_occur)):
            a, b = random.sample(genes_aptos, 2)
            for idx, k in enumerate(genes_aptos):
                if k == b or k == a:
                    del genes_aptos[idx]
            hijo_a, hijo_b = Cromosoma.cruzar(self.poblacion[a], self.poblacion[b])
            if (hijo_a.error < min(self.poblacion[a].error, self.poblacion[b].error) and \
               hijo_b.error < min(self.poblacion[a].error, self.poblacion[b].error)) or always:
                self.poblacion[a] = hijo_a
                self.poblacion[b] = hijo_b

    def _mutar(self):
        for cromosoma in self.poblacion:
            if random.random() < self.probabilidad_de_mutacion:
                cromosoma.mutar()

    def solve(self, max_iter=1000, error_ideal=0):
        random.seed()
        self._iniciar_poblacion()
        iteracion = 0
        while iteracion < max_iter and (not self.el_mejor_cromosoma or self.el_mejor_cromosoma.costo_de_error_del_juego > error_ideal):
            self._cruzar(always=True)
            self._calcular_error()
            self._seleccionar()
            self._mutar()
            self._imprimir_resultado(iteracion)
            iteracion += 1
        return self.el_mejor_cromosoma

    def _imprimir_resultado(self, iteracion):
        print('~~~~~~~~ iteracion: %d ~~~~~~~~' % iteracion)
        print('longitud de poblacion (%d) | error total (%0.4f)' % (
            len(self.poblacion),
            self.error
        ))
        if self.el_mejor_cromosoma:
            print('el_mejor_cromosoma: %0.4f   ->   %0.4f  +  %0.4f' % (
                self.el_mejor_cromosoma.error,
                self.el_mejor_cromosoma.costo_de_error_del_juego,
                self.el_mejor_cromosoma.error_gen_len
            ))
            print('el_mejor_cromosoma es: %s' % self.el_mejor_cromosoma)
        print('--------------------------------')