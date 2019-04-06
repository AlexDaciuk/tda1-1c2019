#!/usr/bin/env python3
import sys
import math
import heapq

file_path = sys.argv[1]

lista = []
lista.sorted(reverse = True)

def cargar_numeros(file_path):
    file = open(file_path, "r")

    lines = file.readline()

    for line in lines:
         number_tmp = line.rstrip()
         lista.append(number_tmp)
         lista.sorted(reverse = True)

#Como es un heap de maximo es tan facil como devolver el primer elemento si este existe
def maximo(lista):
     maxi = None 
     if (len(lista) != 0):
         maxi = lista[0]
     return maxi

def mediana(lista):
     return None