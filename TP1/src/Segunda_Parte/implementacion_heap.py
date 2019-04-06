#!/usr/bin/env python3
import sys
import math
import heapq

file_path = sys.argv[1]

lista = []
heap = heapq.heapify(lista) #Ahora la lista es un heap de minimo
maxHeap = heapq._heapify_max(heap) #Ahora es un heap de maximo 

def cargar_numeros(file_path):
    file = open(file_path, "r")

    lines = file.readline()

    for line in lines:
        number_tmp = line.rstrip()
         heapq.heappush(maxHeap,MaxHeapInt(number_tmp))  #Creo que asi se tiene que insertar para respetar que es un heap de maximo

#Como es un heap de maximo es tan facil como devolver el primer elemento si este existe
def maximo(maxHeap):
     maxi = None 
     if (len(heap) != 0):
         maxi = maxHeap[0].val
     return maxi


