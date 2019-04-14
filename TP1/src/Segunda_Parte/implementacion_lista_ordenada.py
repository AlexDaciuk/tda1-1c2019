# !/usr/bin/env python3
import sys

file_path = sys.argv[1]
operation = sys.argv[2]

number_lista = []


# O(n*logn)
def cargar_numeros(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    for line in lines:
        number_tmp = line.rstrip()
        number_lista.append(number_tmp)
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


def main():
    cargar_numeros(file_path)


main()
