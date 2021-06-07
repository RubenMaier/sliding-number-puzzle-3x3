#!/usr/bin/env python

from juego import Juego
from algoritmoGenetico import AlgoritmoGenetico

PROBABILIDAD_DE_LA_MUTACION = 0.5
LONGITUD_DE_LA_POBLACION = 100
MAX_ITERATION = 200
LONGITUD_CROMOSOMA = 10

if __name__ == "__main__":
    try:
        juego = Juego()
        juego.mezclar()
        algoritmoGenetico = AlgoritmoGenetico(juego, LONGITUD_DE_LA_POBLACION, PROBABILIDAD_DE_LA_MUTACION, LONGITUD_CROMOSOMA)
        algoritmoGenetico.resolver(max_iter=MAX_ITERATION)
        print('\n\n====================================================')
        print('Tablero Original:')
        print(juego)
        print('Mejor Solucion encontrada:')
        print(algoritmoGenetico.el_mejor_cromosoma.lista_de_movimientos)
        juego.movimientos(algoritmoGenetico.el_mejor_cromosoma.lista_de_movimientos, mostrarEnPantalla=True)
        print('Resultado:')
        print(juego)
    except KeyboardInterrupt:
        pass