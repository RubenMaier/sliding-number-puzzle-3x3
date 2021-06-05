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
        """ ESTA HECHO EL SELECCION POR CONTROL, FALTA CONTINUAR LA SELECCION POR RULETA :$
        seleccionados = []
        aptitudes = map(lambda un_cromosoma: un_cromosoma.calcular_aptitud(), self.poblacion)
        promedio_total = sum(aptitudes) / len(aptitudes)
        aptitudes_promediadas = map(lambda una_aptitud: una_aptitud/promedio_total, aptitudes)
        aptitudes_promediadas_decimales = []
        i=0
        for cromosoma in self.poblacion:
            if int(aptitudes_promediadas[i]) > 0:
                j=0
                while j<int(aptitudes_promediadas[i]): 
                    seleccionados.append(cromosoma)
                    j+=1
                aptitudes_promediadas_decimales.append(aptitudes_promediadas[i] - int(aptitudes_promediadas[i]))
            else:
                aptitudes_promediadas_decimales.append(aptitudes_promediadas[i])    
            i+=1

        suma_aptitudes_promediadas_decimales = sum(aptitudes_promediadas_decimales)

        aptitudes_porcentuales = map(lambda una_aptitud: una_aptitud*100/suma_aptitudes_promediadas_decimales, aptitudes_promediadas_decimales)

        i=0
        for cromosoma in self.poblacion:
            if i > 0: aptitudes_porcentuales[i] = aptitudes_porcentuales[i] + aptitudes_porcentuales[i-1]
            
        #RULETA
        for i in range(len(self.poblacion)-len(seleccionados)):
        """
        #salioRanking, no me juzguen, estaba cansado
        cromosomas_con_aptitud = []
        def obtenerAptitud(un_cromosoma):
            return un_cromosoma.calcular_aptitud()
        self.poblacion.sort(reverse=True, key=obtenerAptitud)

    def _cruzar(self):
        for i in range(self.poblacion_inicial/2):
            #cruzar los primeros 500
            #el if sirve para que tome de a pares, espaciado en 2
            if i > 0 and (i % 2 == 0):
                #obtengo el punto de corte, que va de la posicion 1 (arranca en 0) a la anteultima posicion
                punto_corte = random.randrange(1, len(self.poblacion[i].lista_de_movimientos)-2)
                #si tienen ganas de dejarlo más lindo, se puede meter todo esto, dentro del cromosoma, en la funcion de cruzar (para no romper el encapsulamiento)
                #obtengo el hijoA, formado por la primer parte del primer padre y la segunda parte del segundo padre
                hijo_a = self.poblacion[i-1].lista_de_movimientos[0:punto_corte] + self.poblacion[i].lista_de_movimientos[punto_corte+1:len(self.poblacion[i].lista_de_movimientos)]
                hijo_b = self.poblacion[i].lista_de_movimientos[0:punto_corte] + self.poblacion[i-1].lista_de_movimientos[punto_corte+1:len(self.poblacion[i].lista_de_movimientos)]
                #reemplazo los padres por sus hijos
                self.poblacion[i-1].lista_de_movimientos = hijo_a
                self.poblacion[i].lista_de_movimientos = hijo_b

    def _mutar(self):
        for cromosoma in self.poblacion:
            #si tienen ganas, pueden hacer que mute uno solito, no me parece mal que intente hacer mutar algunos segun los que salgan seleccionados por el random
            if random.random() < self.probabilidad_de_mutacion:
                cromosoma.mutar(True)

    def solve(self, max_iter=1000, error_ideal=0):
        random.seed()
        self._iniciar_poblacion()
        iteracion = 0
        #cambiar el error, por cantidad de iteraciones maximas
        #habria que sacar el error, o de ultima, evaluarlo en base a la ponderacion de la longitud de manhattan de todos los movimientos (GENES) del cromosoma
        while iteracion < max_iter and (not self.el_mejor_cromosoma or self.el_mejor_cromosoma.costo_de_error_del_juego > error_ideal):
            self._seleccionar()#self._calcular_error() funcion aptitud -> va adentro de seleccionar
            self._cruzar()
            #HAY QUE INICIALIZAR LA LISTA DE MOVIMIENTOS, YA QUE ARRANCA VACIA
            self._mutar()
            self._imprimir_resultado(iteracion)
            iteracion += 1
        return self.el_mejor_cromosoma

    def _imprimir_resultado(self, iteracion):
        print('~~~~~~~~ iteracion: %d ~~~~~~~~' % iteracion)
        print('tamaño de poblacion (%d) | error total (%0.4f)' % (
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