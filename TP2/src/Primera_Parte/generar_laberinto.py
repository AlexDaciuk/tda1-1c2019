#!/usr/bin/env python3
import sys

# El orden de los argumentos esta definido en el enunciado
metodo = sys.argv[1]

alto = int(sys.argv[2])
ancho = int(sys.argv[3])


def crear_mapa_vacio(alto, ancho):
    # Creo el mapa vacio
    mapa_tmp = [[" " for x in range(ancho + 2)] for y in range(alto + 2)]

    poner_paredes(mapa_tmp, alto, ancho)

    return mapa_tmp


def poner_paredes(mapa, alto, ancho):
    for i in range(1, ancho + 1):
        # Pared superior e inferior, uso signo menos
        mapa[0][i] = "¯"
        mapa[alto + 1][i] = "_"
    for i in range(alto + 2):
        # Paredes laterales, uso pipe
        mapa[i][0] = "|"
        mapa[i][ancho + 1] = "|"


def mostrar_mapa(mapa):
    for fila in range(len(mapa)):
        print(*mapa[fila], sep=' ')


def metodo_dyc(mapa):
    None


if __name__ == "__main__":
    mapa = crear_mapa_vacio(alto, ancho)

    mostrar_mapa(mapa)
