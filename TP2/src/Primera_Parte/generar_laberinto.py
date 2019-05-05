#!/usr/bin/env python3
import sys
import random

# El orden de los argumentos esta definido en el enunciado
metodo = sys.argv[1]
# Sumo 2 para que las paredes exteriores no le saquen tamaño al mapa
alto_mapa = int(sys.argv[2]) + 2
ancho_mapa = int(sys.argv[3]) + 2

sys.setrecursionlimit(100000)


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
    elif ancho > alto:
        return "vertical"
    else:
        return (random.choice(["horizontal", "vertical"]))


# Siempre la pared se hace de izq a derecha o de arriba a abajo
def poner_pared(mapa, orientacion, x, y, largo):
    print("Pongo pared " + orientacion + " en " + str(x) + "," + str(y)
          + " de largo " + str(largo))

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


def aleatorio(a, b):
    print("a vale " + str(a) + " b vale " + str(b))
    if a == b:
        return a
    elif b == 1 or b == 0:
        return a
    else:
        return random.randint(a, b)


def metodo_dyc(mapa):

    def dividir(mapa, x, y, ancho, alto):
        # Pongo un limite inferior para las subdivisiones
        if alto < 4 or ancho < 4:
            return

        # Decido la orientacion dependiendo del tamaño de la division
        es_horizontal = (decidir_orientacion(alto, ancho) == "horizontal")

        # Busco punto de inicio de la pared, siempre va a estar sobre la pared
        # derecha o superior del recuadro definido por (x,y), ancho y alto
        # OSEA, SIEMPRE QUE ARMO UNA PARED, ES PARA ABAJO O PARA LA DERECHA
        pared_x = x + (aleatorio(2, alto - 2) if es_horizontal else 0)
        pared_y = y + (0 if es_horizontal else aleatorio(2, ancho - 2))

        # Defino el largo de la pared
        largo_pared = ancho if es_horizontal else alto

        poner_pared(mapa,
                    ("horizontal" if es_horizontal else "vertical"),
                    pared_x, pared_y, largo_pared)

        # Lo que queda a la izquierda o arriba de la pared
        ancho_parte_arriba = ancho if es_horizontal else (pared_y - y)
        alto_parte_arriba = (pared_x - x) if es_horizontal else alto
        dividir(mapa, x, y, ancho_parte_arriba, alto_parte_arriba)

        # Lo que queda a la derecha o abajo de la pared
        ancho_parte_abajo = ancho if es_horizontal else (ancho - pared_y - 1)
        alto_parte_abajo = (alto - pared_x - 1) if es_horizontal else alto
        dividir(mapa, pared_x, pared_y,
                ancho_parte_abajo, alto_parte_abajo)

    dividir(mapa, 0, 0, ancho_mapa - 2, alto_mapa - 2)


def metodo_dfs(mapa):
    None


if __name__ == "__main__":
    mapa = crear_mapa_vacio(alto_mapa, ancho_mapa)
    mostrar_mapa(mapa)

    metodo_dyc(mapa)

    mostrar_mapa(mapa)

    # if metodo == "dyc":
    #     metodo_dyc(mapa)
    # elif metodo == "dfs":
    #     metodo_dfs(mapa)
