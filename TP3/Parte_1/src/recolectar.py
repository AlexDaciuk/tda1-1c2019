import sys
from pathlib import Path 
from collections import defaultdict
from Juego.Mapa import Mapa
   
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

def guardarCosecha(num, imperio, mapa):
    archivo = open(Path("../assets/txt/" + "cosecha" + str(num) +".txt"), "w+")
    # Para cada ciudad en imperio.ciudades
        # Guardar la suma de todos los valores devueltos por FordFulkerson.flow(ciudad,imperio.metropolis)
    
    archivo.close()

if __name__ == "__main__":  

    numJugador = sys.argv[1]
    archivoCiudades = sys.argv[2]
    archivoRutas = sys.argv[2]
    archivoImperio = sys.argv[3]

    mapa = Mapa(archivoCiudades, archivoRutas)
    
    guardarCosecha(numJugador, archivoImperio, mapa)
