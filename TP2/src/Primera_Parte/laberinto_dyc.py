#!/usr/bin/env python3
import sys
import random
from pathlib import Path

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
    if orientacion == "horizontal":
        for i in range(y, y + largo):
            mapa[x][i] = "*"
        y_a_sacar = random.randint(y, y + largo - 1)
        x_a_sacar = x

    elif orientacion == "vertical":
        for i in range(x, x + largo):
            mapa[i][y] = "*"
        x_a_sacar = random.randint(x, x + largo - 1)
        y_a_sacar = y

    mapa[x_a_sacar][y_a_sacar] = " "


def validar_pared(mapa, x, y, largo, es_horizontal):
    if es_horizontal \
            and mapa[x][y + largo] != " " \
            and mapa[x][y - 1] == "*" \
            and mapa[x][y] != "*":
        return True
    elif not es_horizontal \
            and mapa[x + largo][y] != " " \
            and mapa[x - 1][y] == "*" \
            and mapa[x][y] != "*":
        return True
    else:
        return False


def generar_mapa(mapa, alto_mapa, ancho_mapa):

    def dividir(mapa, x, y, ancho, alto):
        # Pongo un limite inferior para las subdivisiones
        if alto < 4 or ancho < 4:
            return

        # Busco punto de inicio de la pared, siempre va a estar sobre la pared
        # derecha o superior del recuadro definido por (x,y), ancho y alto
        # OSEA, SIEMPRE QUE ARMO UNA PARED, ES PARA ABAJO O PARA LA DERECHA
        pared_valida = False

        while not pared_valida:
            # Decido la orientacion dependiendo del tamaño de la division
            es_horizontal = (decidir_orientacion(alto, ancho) == "horizontal")

            # Defino el largo de la pared
            largo_pared = ancho if es_horizontal else alto

            # Defino aleatoriamente donde va a estar la pared
            pared_x = x + (random.randint(2, alto - 2) if es_horizontal else 0)
            pared_y = y + \
                (0 if es_horizontal else random.randint(2, ancho - 2))

            # Valido que no este frente a una puerta
            pared_valida = validar_pared(mapa,
                pared_x, pared_y, largo_pared, es_horizontal)

        poner_pared(mapa,
                    ("horizontal" if es_horizontal else "vertical"),
                    pared_x, pared_y, largo_pared)

        x_a = x
        y_a = y
        ancho_a = ancho if es_horizontal else pared_y - y
        alto_a = pared_x - x if es_horizontal else alto

        dividir(mapa, x_a, y_a, ancho_a, alto_a)

        x_b = pared_x + 1 if es_horizontal else pared_x
        y_b = pared_y if es_horizontal else pared_y + 1
        ancho_b = ancho if es_horizontal else ancho - pared_y + y - 1
        alto_b = alto - pared_x + x - 1 if es_horizontal else alto

        dividir(mapa, x_b, y_b, ancho_b, alto_b)

    dividir(mapa, 1, 1, ancho_mapa - 2, alto_mapa - 2)


def guardar_mapa(mapa):
    file_path = "../../assets/txt/mapa-laberinto.txt"

    file = open(Path(file_path), 'w+')

    for fila in range(len(mapa)):
        linea_tmp = "".join(str(x) for x in mapa[fila]) + "\n"
        file.write(linea_tmp)

    file.close()


if __name__ == "__main__":
    alto_mapa = int(sys.argv[1]) + 2
    ancho_mapa = int(sys.argv[2]) + 2
    mapa = crear_mapa_vacio(alto_mapa, ancho_mapa)
    generar_mapa(mapa,alto_mapa,ancho_mapa)
    mostrar_mapa(mapa)
    guardar_mapa(mapa)
