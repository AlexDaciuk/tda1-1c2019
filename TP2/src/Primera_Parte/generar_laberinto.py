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

    poner_entrada_salida(mapa_tmp, alto, ancho)

    return mapa_tmp


def poner_entrada_salida(mapa, alto, ancho):
    # Entrada
    mapa[0][1] = " "
    # Salida
    mapa[alto - 1][ancho - 2] = " "


def poner_paredes_externas(mapa, alto, ancho):
    for i in range(1, ancho - 1):
        # Pared superior e inferior, uso signo menos
        mapa[0][i] = "*"
        mapa[alto - 1][i] = "*"
    for i in range(alto):
        # Paredes laterales, uso pipe
        mapa[i][0] = "*"
        mapa[i][ancho - 1] = "*"


def mostrar_mapa(mapa):
    for fila in range(len(mapa)):
        print(*mapa[fila], sep=' ')


def decidir_orientacion(alto, ancho):
    if alto > ancho:
        return "horizontal"
    elif ancho < alto:
        return "vertical"
    else:
        return (random.choice(["horizontal", "vertical"]))


# Siempre la pared se hace de izq a derecha o de arriba a abajo
def poner_pared(mapa, orientacion, x, y, largo):

    if orientacion == "horizontal":
        for i in range(y, y + largo):
            mapa[x][i] = "*"
        y_a_sacar = random.randint(y, y + largo)
        x_a_sacar = x

    elif orientacion == "vertical":
        for i in range(x, x + largo):
            mapa[i][y] = "*"
        x_a_sacar = random.randint(x, x + largo)
        y_a_sacar = y

    mapa[x_a_sacar][y_a_sacar] = " "


def metodo_dyc(mapa):

    def dividir(mapa, x, y, ancho, alto):
        if alto < 2 or ancho < 2:
            return

        es_horizontal = (decidir_orientacion(ancho, alto) == "horizontal")

        # Busco punto de inicio de la pared, siempre va a estar sobre la pared
        # derecha o superior del recuadro definido por (x,y), ancho y alto
        # OSEA, SIEMPRE QUE ARMO UNA PARED, ES PARA ABAJO O PARA LA DERECHA
        pared_x = x + (0 if es_horizontal else random.randint(x, alto - x))
        pared_y = y + (random.randint(y, ancho - y) if es_horizontal else 0)

        # Defino el largo de la pared
        largo_pared = ancho if es_horizontal else alto

        poner_pared(mapa,
                    ("horizontal" if es_horizontal else "vertical"),
                    pared_x, pared_y, largo_pared)


def metodo_dfs(mapa):
    None


if __name__ == "__main__":
    mapa = crear_mapa_vacio(alto, ancho)
    mostrar_mapa(mapa)

    if metodo == "dyc":
        metodo_dyc(mapa)
    elif metodo == "dfs":
        metodo_dfs(mapa)
