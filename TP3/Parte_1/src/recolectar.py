import sys
from pathlib import Path 
from functools import reduce
from collections import defaultdict
from Juego.Mapa import Mapa
from Juego.Imperio import Imperio
   
class FordFulkerson: 
   
    def __init__(self,graph): 

        self.graph = graph # grafo residual
        self.ROW = len(graph)

    # analiza si existe algun camino entre la ciudad y la metropolis
    # en el grafo residual y asigan el camino
    def BFS(self,s, t, parent): 
  
        visited =[False]*(self.ROW)           
        queue=[]           
        queue.append(s) 
        visited[s] = True
           
        while queue: 
            u = queue.pop(0) 

            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
  
        return True if visited[t] else False
              
      
    # Devuelve flujo máximo entre la fuente (una ciudad) y el sumidero (metropolis)
    def flow(self, source, sink):   

        parent = [-1]*(self.ROW)   
        max_flow = 0 
  
        while self.BFS(source, sink, parent) : 
  
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            max_flow +=  path_flow 
  
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
  
        return max_flow 

def armarMatrizGrafo(imperio):

    ciudades = imperio.ciudades
    # matriz incial de flujo 0
    #matriz = [[0]*len(ciudades)]*len(ciudades)
    matriz = [[0 for x in range(len(ciudades))] for y in range(len(ciudades))] 

    #asigno flujos segun conexiones del imperio
    for ciudad in ciudades:
        for conex in ciudad.rutas:
            if conex.destino in ciudades:
                iorigen = ciudades.index(ciudad)
                idestino = ciudades.index(conex.destino)
                matriz[iorigen][idestino]= conex.trafico
    
    return matriz

def calcularCosecha(imperio):

    flujoMax = 0
   
    cflujo = FordFulkerson(armarMatrizGrafo(imperio))        
    
    for ciudad in imperio.ciudades:
        if imperio.ciudades.index(ciudad) != 0:
            flujoMax += cflujo.flow(0,imperio.ciudades.index(ciudad)) 

    #capacidad cosecha
    CosechaMaxima = reduce(lambda a,b : a + b, [c.produccion for c in imperio.ciudades])

    if CosechaMaxima > flujoMax:
        return flujoMax
    else:
        return CosechaMaxima


def guardarCosecha(numJugador, imperio):
    cosecha = calcularCosecha(imperio)
    cosechaAnterior = 0

    # Cargo cosecha anterior si existe archivo
    try:
        archivo = open(Path("../assets/txt/cosecha" + str(numJugador) + '.txt'), "r")
        cosechaAnterior = int(archivo.read())
        archivo.close()
    except FileNotFoundError:
        cosechaAnterior = 0 

    archivo = open(Path("../assets/txt/" + "cosecha" + str(numJugador) +".txt"), "w+")
    
    # Guardo cosecha actual + cosecha anterior
    archivo.write(str(cosecha + cosechaAnterior))    
    archivo.close()


if __name__ == "__main__":  

    numJugador = sys.argv[1]
    archivoCiudades = sys.argv[2]
    archivoRutas = sys.argv[3]
    archivoImperio = sys.argv[4]

    mapa = Mapa(archivoCiudades, archivoRutas)
    imperio = Imperio(archivoImperio,mapa)
    
    guardarCosecha(numJugador, imperio)
