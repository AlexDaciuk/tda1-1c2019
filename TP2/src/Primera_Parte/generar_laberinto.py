#!/usr/bin/env python3
import sys
import random

# El orden de los argumentos esta definido en el enunciado
metodo = sys.argv[1]
# Sumo 2 para que las paredes exteriores no le saquen tamaño al mapa
alto = int(sys.argv[2]) + 2
ancho = int(sys.argv[3]) + 2


def crear_mapa_vacio(alto, ancho):
    mapa_tmp = [[" " for x in range(ancho)] for y in range(alto)]

    poner_paredes_externas(mapa_tmp, alto, ancho)

    return mapa_tmp


def poner_paredes_externas(mapa, alto, ancho):
    for i in range(1, ancho - 1):
        # Pared superior e inferior, uso signo menos
        mapa[0][i] = "*"
        mapa[alto + 1][i] = "*"
    for i in range(alto - 2):
        # Paredes laterales, uso pipe
        mapa[i][0] = "*"
        mapa[i][ancho + 1] = "*"


def mostrar_mapa(mapa):
    for fila in range(len(mapa)):
        print(*mapa[fila], sep=' ')


def poner_pared(mapa, orientacion, posicion, desde, hasta):
    pos_random = random.randint(desde + 1, hasta - 2)

    if orientacion == "horizontal":
        for celda in range(desde, hasta):
            mapa[posicion][celda] = "*"
        mapa[posicion][pos_random] = " "

    elif orientacion == "vertical":
        for celda in range(desde, hasta):
            mapa[celda][posicion] = "*"
        mapa[pos_random][posicion] = " "


def decidir_orientacion(alto, ancho):
    if alto > ancho:
        return "horizontal"
    elif ancho < alto:
        return "vertical"
    else:
        return (random.choice(["horizontal", "vertical"]))


def metodo_dyc(mapa):
    alto_tmp = random.randint(2, alto - 2)
    ancho_tmp = random.randint(2, ancho - 2)
    # Pongo la primera pared para arrancar
    orientacion_tmp = decidir_orientacion(alto_tmp, ancho_tmp)

    poner_pared(mapa, orientacion_tmp, ancho_tmp, 0, )


def metodo_dfs(mapa):
    None


if __name__ == "__main__":
    mapa = crear_mapa_vacio(alto, ancho)
    mostrar_mapa(mapa)

    if metodo == "dyc":
        metodo_dyc(mapa)
    elif metodo == "dfs":
        metodo_dfs(mapa)
