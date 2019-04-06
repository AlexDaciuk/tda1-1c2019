#!/usr/bin/env python3
import sys
import math

file_path = sys.argv[1]

number_list = []


def cargar_numeros(file_path):
    file = open(file_path, "r")

    lines = file.readline()

    for line in lines:
        number_tmp = line.rstrip()
        number_list.append(number_tmp)


def maximo(number_list):
    maximo = None
    for number in number_list:
        if number > maximo:
            maximo = number

    return maximo


def media(number_list):
    suma = 0
    for number in number_list:
        suma += number

    media = suma / len(number_list)

    return media


def moda(number_list):
     # Aca se obtiene el elemento que mayor frecuencia tiene
     frecuente = max(list(map(number_list.count, number_list )))
     # En caso de que alla mas de 1 valor de maxima frecuencia:
     return list(set(filter(lambda x: number_list.count(x) == frecuente, number_list))) 


def mediana(number_list): 
     number_list.sort()
     pos = (number_list - 1) // 2
     # Si el largo de la lista es par devuelvo el promedio 
     # de los 2 valores medios de la lista
     if (len(number_list) % 2) == 0:
         return (number_list[pos] + number_list[pos + 1]) / 2.0
     # Sino devuelvo el valor medio
     return number_list[pos]



def desviacion_estandar(number_list):
    media_tmp = media(number_list)
    suma_distancias = 0

    for number in number_list:
        distancia_media = number - media_tmp
        suma_distancias = + distancia_media

    media_de_suma = suma_distancias / len(number_list)

    return math.sqrt(media_de_suma)


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


def variaciones_r_elementos_sin_repeticion(number_list, r):
    None


def variaciones_r_elementos(number_list, r):
    None
