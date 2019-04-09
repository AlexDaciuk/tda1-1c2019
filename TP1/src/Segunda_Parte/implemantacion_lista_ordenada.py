# !/usr/bin/env python3
import sys

file_path = sys.argv[1]

lista = []
lista.sorted(reverse=True)


def cargar_numeros(file_path):
    file = open(file_path, "r")

    lines = file.readline()

    for line in lines:
        number_tmp = line.rstrip()
        lista.append(number_tmp)
        lista.sorted(reverse=True)

# Como es un heap de maximo es tan facil como devolver el primer elemento
# si este existe


def maximo(lista):
    maxi = None
    if (len(lista) != 0):
        maxi = lista[0]
    return maxi

# No veo por que esta funcion deberia ser distinta a la de la lista desordenada
# Salvo en el precondicion de que aca la lista ya llega ordenada


def mediana(lista):
    pos = (len(lista) - 1) // 2
    # Si el largo de la lista es par devuelvo el promedio
    # de los 2 valores medios de la lista
    if (len(lista) % 2) == 0:
        return (lista[pos] + lista[pos + 1]) / 2.0
    # Sino devuelvo el valor medio
    return lista[pos]
