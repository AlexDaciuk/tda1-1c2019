# !/usr/bin/env python3
import sys
import math
import time

file_path = sys.argv[1]

operation = sys.argv[2]

try:
    r = int(sys.argv[3])
    hay_r = True
except IndexError:
    hay_r = False

number_lista = []


# O(n)
def cargar_numeros(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    for line in lines:
        number_tmp = line.rstrip()
        number_lista.append(int(number_tmp))
    file.close()


# O(1)
def archivo_resultados(resultados):
    file_path = "resultados.txt"
    file = open(file_path, 'w+')
    if isinstance(resultados, str):
        file.write(resultados)
    else:
        file.write(str(resultados))
    file.close()
    raise SystemExit


# O(1)
def maximo(lista):
    archivo_resultados(lista[0])


# O(1)
def mediana(lista):
    pos = (len(lista) - 1) // 2
    if (len(lista) % 2) == 0:
        archivo_resultados((lista[pos] + lista[pos + 1]) / 2.0)
    else:
        archivo_resultados(lista[pos])


# O(n)
def media(lista):
    suma = 0
    for number in lista:
        suma += number
    archivo_resultados(suma / len(lista))


# O(n)
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


if __name__ == "__main__":
    cargar_numeros(file_path)

    number_lista.sort()  # O(n*log n)

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

    start = time.time()
    if hay_r and operation in operations_with_r:
        resultado = operations_with_r[operation](number_lista, r)
    elif not hay_r and operation in operations_without_r:
        resultado = operations_without_r[operation](number_lista)
    else:
        print("Argumentos invalidos")
    end = time.time()

    print("Tiempo de ejecucion de " + operation + " en lista con " +
          str(len(number_lista)) + " elementos : " + str(end - start))

    archivo_resultados(resultado)
