#!/usr/bin/env python3
import sys
import math

file_path = sys.argv[1]

operation = sys.argv[2]

try:
    r = int(sys.argv[3])
    hay_r = True
except IndexError:
    hay_r = False


number_list = []


def cargar_numeros(file_path):  # O(n)
    file = open(file_path, "r")

    lines = file.readlines()

    for line in lines:
        number_tmp = line.rstrip()
        number_list.append(int(number_tmp))

    file.close()


def archivo_resultados(resultados):  # O(1)
    file_path = "resultados.txt"

    file = open(file_path, 'w+')

    if isinstance(resultados, str):
        file.write(resultados)
    else:
        file.write(str(resultados))

    file.close()

    raise SystemExit


def maximo(number_list):  # O(n)
    maximo = number_list[1]
    for number in number_list:
        if number > maximo:
            maximo = number

    archivo_resultados(maximo)


def media(number_list):  # O(n)
    suma = 0
    for number in number_list:
        suma += number

    media = suma / len(number_list)

    archivo_resultados(media)


# Si no se repite ningun elemento, devuelve todo el vector
def moda(number_list):
    # Aca se obtiene el elemento que mayor frecuencia tiene
    frecuente = max(list(map(number_list.count, number_list)))
    # En caso de que haya mas de 1 valor de maxima frecuencia:
    archivo_resultados(
        list(set(filter(lambda x: number_list.count(x) == frecuente,
                        number_list)))
    )


def mediana(number_list):   # O(n log n)
    number_list.sort()  # O(n log n), usa Timsort

    pos = (len(number_list) - 1) // 2
    resultado = number_list[pos]

    # Si el largo de la lista es par devuelvo el promedio
    # de los 2 valores medios de la lista
    if (len(number_list) % 2) == 0:
        resultado = (number_list[pos] + number_list[pos + 1]) / 2.0

    # Sino devuelvo el valor medio
    archivo_resultados(resultado)


def desviacion_estandar(number_list):  # O(n + log n)
    suma = 0
    for number in number_list:
        suma += number

    media = suma / len(number_list)

    suma_distancias = 0

    for number in number_list:  # O(n)
        distancia_media = (number - media) ** 2
        suma_distancias += distancia_media

    media_de_suma = suma_distancias / len(number_list)

    archivo_resultados(math.sqrt(media_de_suma))  # sqrt O(log n)

# Entran todos los elementos del array
# Importa el orden
# No se repiten los elementos


def permutaciones(number_list):
    def swap(n1, n2):
        tmp = number_list[n1]
        number_list[n1] = number_list[n2]
        number_list[n2] = tmp

    def generar_permutaciones(k, lista):
        if k == 1:
            print(lista)
        else:
            generar_permutaciones(k - 1, lista)

        for i in range(1, k):
            if (i % 2) == 0:
                swap(lista[i], lista[k])
            else:
                swap(lista[1], lista[k])

        print(lista)
        generar_permutaciones(k - 1, lista)


# No entran todos los elementos, entran r
# Si importa el orden
# No se repiten elementos

def variaciones_r_elementos_sin_repeticion(number_list, r):
    print("entre a variaciones_r_elementos_sin_repeticion")
    n = len(number_list)

    if r >= n:
        print("Numero invalido.")
        raise SystemExit

    variaciones = []

    # Mi lista de indices va a tener las posiciones de la proxima
    # variacion
    indices = list(range(r))

    # Trivial, los primeros r elementos de la lista
    variaciones.append(list(number_list[i] for i in indices))

    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            break

        indices[i] += 1

        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
            variaciones.append(list(number_list[i] for i in indices))

    archivo_resultados(variaciones)


# No entran todos los elementos, entran r
# Si importa el orden
# Se repiten elementos


def variaciones_r_elementos(number_list, r):
    n = len(number_list)

    if r >= n:
        print("Numero invalido.")
        raise SystemExit


def main():
    cargar_numeros(file_path)

    operations_without_r = {
        "maximo": maximo,
        "media": media,
        "moda": moda,
        "mediana": mediana,
        "desviacion_estandar": desviacion_estandar,
        "permutaciones": permutaciones
    }

    operations_with_r = {
        "variaciones": variaciones_r_elementos_sin_repeticion,
        "variaciones_con_repeticion": variaciones_r_elementos
    }

    if hay_r and operation in operations_with_r:
        operations_with_r[operation](number_list, r)
    elif not hay_r and operation in operations_without_r:
        operations_without_r[operation](number_list)
    else:
        print("Argumentos invalidos")


main()
