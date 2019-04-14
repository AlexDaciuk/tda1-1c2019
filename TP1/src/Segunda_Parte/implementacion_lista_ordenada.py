# !/usr/bin/env python3
import sys

file_path = sys.argv[1]

operation = sys.argv[2]

lista = []
lista.sort(reverse=True)


def cargar_numeros(file_path):
    file = open(file_path, "r")

    lines = file.readline()

    for line in lines:
        number_tmp = line.rstrip()
        lista.append(number_tmp)
        lista.sort(reverse=True)

# Como es un heap de maximo es tan facil como devolver el primer elemento
# si este existe

#O(1)
def maximo(lista):
    maxi = None
    if (len(lista) != 0):
        maxi = lista[0]

    print('maximo:')
    print(maxi)
    return maxi

# No veo por que esta funcion deberia ser distinta a la de la lista desordenada
# Salvo en el precondicion de que aca la lista ya llega ordenada


def mediana(lista):
    pos = (len(lista) - 1) // 2
    # Si el largo de la lista es par devuelvo el promedio
    # de los 2 valores medios de la lista
    print('mediana' )
    if (len(lista) % 2) == 0:
        return (lista[pos] + lista[pos + 1]) / 2.0
    # Sino devuelvo el valor medio
    return lista[pos]


def main():
    cargar_numeros(file_path)

    switch = {
        "maximo": "maximo",
        "media": "media",
        "moda": "moda",
        "mediana": "mediana",
        "desviacion_estandar": "desviacion_estandar",
        "permutaciones": "permutaciones",
        "variaciones": "variaciones_r_elementos_sin_repeticion",
        "variaciones_con_repeticion": "variaciones_con_repeticion"

    }

    maximo(lista)
    result = mediana(lista)
    print(str(result))
    func = switch.get(operation, lambda: "Operacion invalida")

    func()


main()
