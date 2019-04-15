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

# Temporal : O(n)
# Espacial :  O(4 + n) => O(n)


def cargar_numeros(file_path):  # O(n)
    file = open(file_path, "r")

    lines = file.readlines()

    for line in lines:
        number_tmp = line.rstrip()
        number_list.append(int(number_tmp))

    file.close()


# Temporal : O(1)
# Espacial : O(1)
def archivo_resultados(resultados):
    file_path = "resultados.txt"

    file = open(file_path, 'w+')

    if isinstance(resultados, str):
        file.write(resultados)
    else:
        file.write(str(resultados))

    file.close()

    raise SystemExit


# Temporal : O(n)
# Espacial : O(n)
def maximo(number_list):  # O(n)
    maximo = number_list[0]
    for number in number_list:
        if number > maximo:
            maximo = number

    archivo_resultados(maximo)


# Temporal : O(n)
# Espacial : O(n)
def media(number_list):
    suma = 0
    for number in number_list:
        suma += number

    media = suma / len(number_list)

    archivo_resultados(media)


# Temporal : O(n)
# Espacial : O(n)
# Si no se repite ningun elemento, devuelve todo el vector
def moda(lista):
    mas_frecuentes = [lista[0]]
    frecuencia = 0
    actual = lista[0]
    frecuencia_actual = 0

    for numero in lista:

        if numero != actual:
            actual = numero
            frecuencia_actual = 0

        frecuencia_actual += 1

        if frecuencia_actual > frecuencia:
            frecuencia = frecuencia_actual
            mas_frecuentes = [actual]
        elif frecuencia_actual == frecuencia:
            mas_frecuentes.append(actual)

    archivo_resultados(mas_frecuentes)


# Temporal : O(n log n)
# Espacial :  O(n)
def mediana(number_list):
    number_list.sort()

    pos = (len(number_list) - 1) // 2
    resultado = number_list[pos]

    # Si el largo de la lista es par devuelvo el promedio
    # de los 2 valores medios de la lista
    if (len(number_list) % 2) == 0:
        resultado = (number_list[pos] + number_list[pos + 1]) / 2.0

    # Sino devuelvo el valor medio
    archivo_resultados(resultado)


# Temporal : O(n^2)
# Espacial : O(n)
def desviacion_estandar(number_list):  # O(n^2)
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
# Temporal : O(n!)
# Espacial : O(n!)
def permutaciones(lista):  # O(n!)
    permutaciones = []

    def swap(n1, n2):
        tmp = lista[n1]
        lista[n1] = lista[n2]
        lista[n2] = tmp

    def generar_permutaciones(k, lista):
        if k == 1:
            permutaciones.append(lista)
            return

        for i in range(0, k - 1):
            generar_permutaciones(k - 1, lista)

            if i % 2 == 0:
                swap(i, k - 1)
            else:
                swap(0, k - 1)

    # Llamo a la funcion
    generar_permutaciones(len(lista), lista)

    archivo_resultados(permutaciones)


# No entran todos los elementos, entran r
# Si importa el orden
# No se repiten elementos
# Temporal : O(n!)
# Espacial : O(n!)
def variaciones_r_elementos_sin_repeticion(number_list, r):  # O(nr)
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
# Temporal : O(n!)
# Espacial : O(n!)
def variaciones_r_elementos(number_list, r):
    n = len(number_list)

    if r >= n:
        print("Numero invalido.")
        raise SystemExit

    variaciones = []

    # Inicializo los r indices en 0, ya que es el primer caso trivial
    indices = [0] * r

    variaciones.append(list(number_list[i] for i in indices))

    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            break

        indices[i:] = [indices[i] + 1] * (r - i)

        variaciones.append(list(number_list[i] for i in indices))

    archivo_resultados(variaciones)


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
