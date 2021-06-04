#!/usr/bin/env python

from juego import Juego
from algoritmoGenetico import AlgoritmoGenetico

PROBABILIDAD_DE_LA_MUTACION = 0.9
TASA_DE_CRUCE = 0.3
TAMAÑO_DE_LA_POBLACION = 1000
MAX_ITERATION = 1000


if __name__ == "__main__":
    try:
        juego = Juego()
        juego.mezclar()
        algoritmoGenetico = AlgoritmoGenetico(juego, TAMAÑO_DE_LA_POBLACION, PROBABILIDAD_DE_LA_MUTACION, TASA_DE_CRUCE)
        algoritmoGenetico.solve(max_iter=MAX_ITERATION)
        print('\n\n====================================================')
        print('Original:')
        print(juego)
        print('Solución encontrada:')
        print(algoritmoGenetico.el_mejor_cromosoma.lista_de_movimientos)
        juego.movimientos(algoritmoGenetico.el_mejor_cromosoma.lista_de_movimientos, mostrarEnPantalla=True)
        print('Resultado:')
        print(juego)
    except KeyboardInterrupt:
        pass