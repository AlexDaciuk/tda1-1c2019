#!/usr/bin/env python3
import sys

file_path = "../../assets/txt/" + sys.argv[1]

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
    number_list.sort()

    if (len(number_list) % 2) == 0:  # Largo de lista par
        




def mediana(number_list):
    None


def desviacion_estandar(number_list):
    None


def permutaciones(number_list):
    None


def variaciones_r_elementos(number_list):
    None


def variaciones_r_elementos_repeticion(number_list):
    None
