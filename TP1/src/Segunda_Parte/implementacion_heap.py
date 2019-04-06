#!/usr/bin/env python3
import sys
import math
import heapq

file_path = sys.argv[1]

lista = []
heap = heapq.heapify(lista) #Ahora la lista es un heap de minimo
maxHeap = heapq._heapify_max(heap) #Ahora es un heap de maximo 

#Como es un heap de maximo es tan facil como devolver el primer elemento si este existe
def maximo(maxHeap):
     maxi = None 
     if (len(heap) != 0):
         maxi = maxHeap[0].val
     return maxi


