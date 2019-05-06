### (75.29 / 95.06) - Teoría de Algoritmos - FIUBA

# Informe Trabajo Práctico 2

## Grupo : 3 + 1
## Integrantes
  * Matias Onorato (93179)
  * Juan Cruz Opizzi (99807)
  * Francisco Strambini (92135)
  * Alexis Daciuk (97630)

---
# Parte 1 - Laberintos
## 1.1 - Generacion de laberintos

## Division y Conquista

### **Pseudocodigo**

### **Complejidad**

### **Implementacion**

### **Ejecución**

## Depth-First Search y Recursive Backtracking

La técnica dfs tiene utilidad para generar laberintos. Comenzamos con un grafo plano del cual, mediante una búsqueda en profundidad aleatoria vamos generando un subgrafo que vaya avanzando entre los nodos vecinos mascándolos como visitidos hasta que se encuentre sin salida, es decir que el nodo actual no posea vecinos no visitados.  A partir de ese instante, haciendo uso de una pila, aplicamos un técnica conocida como backtraking mediante la cual comenzamos a revisar los nodos anteriores ya recorridos hasta encontrar un nuevo vecino sin visitar y volver a aplicar una búsqueda en profundidad aleatoria. Cuando la pila se quede sin elementos habremos recorrido todo el grafo inicial y el laberinto habrá quedado conformado.

### **Pseudocodigo**

El procedimiento queda determinado de la siguiente manera

```
Convertir el nodo inicial en el nodo actual y marcarlo como visitado.

Mientras queden nodos por visitar

    Si el nodo actual tiene vecinos que no han sido visitadas

        Agregar el nodo actual a la pila

        generar una arista entre el nodo actual y el nodo a visitar

        Marcar el nodo actual como visitado

        Hacer del nodo a visitar el nodo actual

    En caso contrario verificar si la pila no está vacía y

        Eliminar el nodo actual de la pila

        Hacer del último nodo de la pila el nodo actual
```
### **Analisis de Complejidad**

El algoritmo DFS tiene una complejidad *O(n)*, done n es el número de nodos del grafo. Y el backtraking es un proceso recursive donde ante cada recursión se ve reducido el numero de nodos n que quedan sin visitar. La complejidad de dicha recursión se puede modelar como  *T(n) <= T(n/2) + T(n/3) + T(n/4) + ... + T(1)*, generarndo una complejidad O(log(n))

Por lo tanto la complejidad queda determinada por *O(n.log(n))*

### **Implementación algoritmo**

el codigo esta implementado en *laberinto_dfs.py*

El grafo plano queda representado por un vector de 2 dimensiones dentro de la propiedad grilla de la clase Laberinto. Dentro de la grilla hay instancias de la clase celda, donde en la propiedad conexiones estan conectados los vecinos que forman el sub grafo del laberinto al recorrelos.

```
class Celda:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.conexiones = {'N':None, 'S':None, 'E':None, 'O':None} # subgrafo mediante dfs donde estan conectadas las celdas vecinas
        self.visitado= False

        #para uso en  Dijkstra
        self.caminoMin = False
        self.distancia = -1 #infinito
        self.anterior = None 

class Laberinto:
    def __init__(self,fils = 0,cols = 0,archivo = None):
        self.fils = fils
        self.cols = cols
        self.grilla = [] # grafo plano
        self.pila = []
        self.recorridoMin = []

        if type(archivo) is str:
            self.cargar(archivo) 
        else:
            self.crear() # Generación de la grilla y ejecución dfs-backtraking

```
### **Ejecución**
```
cd TP2/src/Primera_Parte
py constructor.py dfs 10 30
```
El algoritmo genera el archivo 

*TP2/assets/tst/mapa-laberinto.txt*

que contiene la representación del laberinto, donde los *  son muros y los espacios son las celdas/nodos y sus conexiones

Además imprime en pantalla un diagrama del laberinto generado:

![Laberinto](laberinto.png)

## 1.2 - Generación camino minimo
### **Algoritmo Dijkstra**
La idea subyacente en este algoritmo consiste en ir explorando todos los caminos más cortos que parten del vértice origen y que llevan a todos los demás vértices; cuando se obtiene el camino más corto desde el vértice origen hasta el resto de los vértices que componen el grafo, el algoritmo se detiene.

Al detenerse, quedan todos los nodos del grafo con una distancia marcada desde el origen y un subgrafo que conecta el verticie final con el de inicio formando un camino mínimo

### **Pseudocodigo**
```
function Dijkstra(Grafo, source):
    por cada nodo v en Grafo:
        dist[v] := infinito
 	    anterior[v] := ninguno
 	dist[nodo_inicio] := 0 	
 	pila = todoslos los nodos en grafo 
 	mientras pila tiene algun nodo: 
 	    u := nodo en pila con menor distancia
 	    eliminar u de pila
 	    por cada vecino v de u: 	
            #en nuestro caso la distancia entre nodos vecinos es siempre 1
	        alt := dist[u] + 1             
 	        if alt < dist[v] 	
	        dist[v] := alt
 	        anterior[v] := u
 	return anterior[] 
```

### **Analisis de Complejidad**
El algoritmo consiste en *N-1* iteraciones como máximo, en las cuales se agrega un nodo al conjunto final, siendo *N* el número de nodos. En cada iteración se realiza una búsqueda del nodo con menor distancia, de los que siguen estando en la lista de nodos con distancias sin asignar, se realiza una comparación y una suma para actualizar la distancia de los nodos vecinos lo cual tiene como cota *2(N-1)* operaciones. Por lo tanto:

*O(djkstra) = O(N-1).O(2(N-1)) = O(N^2)*


### **Implementación algoritmo**
```
def dijkstra(self):    
    self.grilla[0][0].distancia = 0 #seteo distancia inicio
    self.grilla[0][0].caminoMin = True
    #lista de nodos
    nodos = []
    for x in self.grilla: #armo una lista con todos los nodos
        for celda in x:
            nodos.append(celda)   

    while nodos: 
        nodoPos = [n for n in nodos if n.distancia != -1] #lista de nodos con distancia no infinita
        u = min(nodoPos, key=lambda x: x.distancia) #nodo con distanci minima
        nodos.remove(u)
        for v in u.obtenerConexiones(): # como maximo 4 nodos
            alt = u.distancia + 1
            if alt < v.distancia or v.distancia == -1:
                v.distancia = alt
                v.anterior = u

    return self.marcarCaminoMin(self.grilla[self.cols-1][self.fils-1]) #recorro el camino minimo desde la salida y lo devuelvo
    
def marcarCaminoMin(self,celda):
    if celda.anterior is not None:
        celda.caminoMin = True
        self.marcarCaminoMin(celda.anterior)
    else:            
        return
```
### **Ejecución**
```
cd TP2/src/Primera_Parte
py constructor.py dfs 10 30
py camino_min.py 'mapa-laberintos.txt'
```
El algoritmo genera el archivo 

*TP2/assets/tst/mapa-laberinto-camino-min.txt*

que contiene la representación del laberinto y un camino mínimo, donde los *  son muros y los espacios son las celdas/nodos y sus conexiones, y los puntos las celdas que forman parte del camino mínimo

Además imprime en pantalla un diagrama del laberinto resuelto:

![Laberinto](camino_minimo.png)

## 1.3 - Comparación de complejidad
### **Depth-First Search y Recursive Backtracking**

```python
def generar(self, celda):                
    if self.pila[-1] is not None: # O(1)
        celda.visitado = True # O(1)
        self.pila.append(self.conectarVecino(celda)) # O(4)
        self.generar(self.pila[-1]) #O(n.log(n))
    else:
        try:
            self.pila.pop() # O(1)
            self.pila.pop() # O(1)
            self.generar(self.pila[-1]) # O(n.log(n)              
        except IndexError: # O(1)
            return
```
La única complejidad que depende de n es la recursión del backtraking descripta en el pseudocodigo, por lo tanto la complejidad de la implementación es igual a la teórica

### **División y Conquista**

### **Dijkstra**
```python
def dijkstra(self):
    self.grilla[0][0].distancia = 0 #0(1)
    self.grilla[0][0].caminoMin = True #0(1)
    nodos = [] #0(1)
    for x in self.grilla: #0(n) 
        for celda in x:
            nodos.append(celda) 

    while nodos: #0(n) 
        nodoPos = [n for n in nodos if n.distancia != -1]  #0(n) 
        u = min(nodoPos, key=lambda x: x.distancia) #0(n)
        nodos.remove(u) #0(1)
        for v in u.obtenerConexiones(): #0(4)
            alt = u.distancia + 1 #0(1)
            if alt < v.distancia or v.distancia == -1: #0(1)
                v.distancia = alt #0(1)
                v.anterior = u #0(1)

    return self.marcarCaminoMin(self.grilla[self.cols-1] [self.fils-1]) #O(n)
    
def marcarCaminoMin(self,celda):
    if celda.anterior is not None: #O(1)
        celda.caminoMin = True #O(1)
        self.marcarCaminoMin(celda.anterior) #O(n)
    else:            
        return
```

*O(dijkstra) = O(3) + O(n) + O(n).(2.O(n) + O(8)) +O(n)*
*O(dijkstra) = O(n^2)*

por lo tanto la complejidad queda igual que la teorica

# Parte 2 - Golpe comando
Proponer y explicar un algoritmo que liste los grupos de sospechosos

## Complejidad
