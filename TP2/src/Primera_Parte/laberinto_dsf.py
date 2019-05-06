import sys
from pathlib import Path
from random import randint
from tkinter import Tk, Canvas, mainloop


#clase que funciona de nodo y contiene las aristas que lo conectan
class Celda:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.conexiones = {'N':None, 'S':None, 'E':None, 'O':None}
        self.visitado= False

        #para uso en  Dijkstra
        self.caminoMin = False
        self.distancia = -1 #infinito
        self.anterior = None  

    def obtenerConexiones(self):
        return [self.conexiones[x] for x in list(self.conexiones.keys()) if self.conexiones[x] != None ]


class Laberinto:
    def __init__(self,fils = 0,cols = 0,archivo = None):
        self.fils = fils
        self.cols = cols
        self.grilla = []
        self.pila = []
        self.recorridoMin = []

        if type(archivo) is str:
            self.cargar(archivo)
        else:
            self.crear()

    def cargar(self,archivo):               
        archivo = open(Path("../../assets/txt/" + archivo), "r")
        lineas = archivo.read().splitlines()

        alto = len(lineas)
        ancho = len(lineas[0])
        self.fils = int((alto-1)/2)
        self.cols = int((ancho-1)/2)
        self.grilla = [[Celda(x,y) for y in range(self.fils)] for x in range(self.cols)] 

        posCols = [x for x in range(ancho) if x%2!=0] 
        posFils = [x for x in range(alto) if x%2!=0] 

        for y in range(self.fils):            
            for x in range(self.cols):
                celda = self.grilla[x][y]
                if lineas[posFils[y]-1][posCols[x]] == ' ':
                    celda.conexiones['N'] = self.grilla[x][y-1]
                if lineas[posFils[y]+1][posCols[x]] == ' ':
                    celda.conexiones['S'] = self.grilla[x][y+1]
                if lineas[posFils[y]][posCols[x]+1] == ' ':
                    celda.conexiones['E'] = self.grilla[x+1][y]
                if lineas[posFils[y]][posCols[x]-1] == ' ':
                    celda.conexiones['O'] = self.grilla[x-1][y]
      
    def crear(self):
        # Grafo del laberinto con diccionario de adyacencias y representación matricial de los nodos (celdas)
        self.grilla = [[Celda(x,y) for y in range(self.fils)] for x in range(self.cols)] 
        self.pila = [self.grilla[0][0]]
        self.generar(self.grilla[0][0])        
    
    #dfs con recursive backtraking
    def generar(self, celda):                
        if self.pila[-1] is not None:
            celda.visitado = True
            self.pila.append(self.conectarVecino(celda))
            self.generar(self.pila[-1])
        else:
            try:
                self.pila.pop() # expulso None
                self.pila.pop() # expulso última celda sin vecinos
                self.generar(self.pila[-1])              
            except IndexError:
                return
    
    # Busca un vecino al azar, lo conecta con la celda y lo retorna. Si no existe retorna None 
    def conectarVecino(self, celda):
        vecinos = []

        # Busco vecinos no visitados
        if celda.y - 1 >= 0 and not self.grilla[celda.x][celda.y-1].visitado:
            vecinos.append({'pos':'N', 'celda': self.grilla[celda.x][celda.y-1]})
        if celda.y + 1 < self.fils and not self.grilla[celda.x][celda.y+1].visitado:
            vecinos.append({'pos':'S', 'celda':  self.grilla[celda.x][celda.y+1]})
        if celda.x + 1 < self.cols and not self.grilla[celda.x+1][celda.y].visitado:
            vecinos.append({'pos':'E', 'celda':  self.grilla[celda.x+1][celda.y]})
        if celda.x - 1 >= 0 and not self.grilla[celda.x-1][celda.y].visitado:
            vecinos.append({'pos':'O', 'celda':  self.grilla[celda.x-1][celda.y]})

        # Eligo uno al azar
        if vecinos:  
            vecino = vecinos[randint(0,len(vecinos)-1)]
        else:
            return None

        # Conecto celda con vecino de forma bidireccional
        celda.conexiones[vecino['pos']]= vecino['celda']
        vecino['celda'].conexiones[self.posOpuesta(vecino['pos'])] = celda  

        return vecino['celda']

    def posOpuesta(self, pos):
        if pos == 'N': return 'S'
        if pos == 'S': return 'N'
        if pos == 'E': return 'O'
        if pos == 'O': return 'E'

    def dijkstra(self):
        #seteo distancia inicio
        self.grilla[0][0].distancia = 0 
        self.grilla[0][0].caminoMin = True
        #lista de nodos
        nodos = []
        for x in self.grilla:
            for celda in x:
                nodos.append(celda)   

        while nodos: 
            nodoPos = [n for n in nodos if n.distancia != -1]           
            u = min(nodoPos, key=lambda x: x.distancia)
            nodos.remove(u)
            for v in u.obtenerConexiones():
                alt = u.distancia + 1
                if alt < v.distancia or v.distancia == -1:
                    v.distancia = alt
                    v.anterior = u

        return self.marcarCaminoMin(self.grilla[self.cols-1][self.fils-1])
        
    def marcarCaminoMin(self,celda):
        if celda.anterior is not None:
            celda.caminoMin = True
            self.marcarCaminoMin(celda.anterior)
        else:            
            return

class Impresora:
    def __init__(self,laberinto, wcelda):
        self.lab = laberinto
        self.master = Tk()
        self.w = wcelda # Ancho de celda
        self.canva = Canvas(self.master, width=(self.lab.cols*self.w)+2, height=(self.lab.fils*self.w)+2)

    def presentar(self):
        # Imprimo celdas        
        for x in self.lab.grilla:
            for celda in x:
                self.iCelda(celda) 
        self.canva.pack()    

    def iCelda(self,celda):
        ix = celda.x*self.w
        iy = celda.y*self.w
        fx = celda.x*self.w + self.w
        fy = celda.y*self.w + self.w
        
        #muros
        if celda.conexiones['N'] is None:
            self.canva.create_line(ix+2,iy+2,fx+2,iy+2, fill="black") # Norte
        if celda.conexiones['E'] is None:
            self.canva.create_line(fx+2,iy+2,fx+2,fy+2, fill="black") # Este
        if celda.conexiones['S'] is None:
            self.canva.create_line(ix+2,fy+2,fx+2,fy+2, fill="black") # Sur
        if celda.conexiones['O'] is None:
            self.canva.create_line(ix+2,iy+2,ix+2,fy+2, fill="black") # Oeste  

        #caminoMin
        if celda.caminoMin:
            self.canva.create_oval(ix+2+self.w/3,iy+2+self.w/3,fx+2-self.w/3,fy+2-self.w/3, fill="red") # Norte

    def guardar(self,distancia = False):
        archivo = open(Path("../../assets/txt/mapa-laberinto.txt"), "w+")

        lineas = []
        lineas.append('*'*((self.lab.cols*2) + 1)) #Muro inicio

        for y in range(self.lab.fils):
            linea1='*' # Agrego pared oeste
            linea2='*' # Agrego pared oeste
            for x in range(self.lab.cols):
                celda = self.lab.grilla[x][y]
                
                if distancia:
                    linea1 +=str(celda.distancia) # Agergo distancia
                else:
                    if celda.caminoMin:
                        linea1 +='.'# Agergo celda camino minimo
                    else:
                        linea1 +=' '# Agergo celda

                if celda.conexiones['E'] is not None:
                    linea1 += ' ' # Agrego conexión al E
                else:
                    linea1 += '*' # Agrego muro al E
                
                if celda.conexiones['S'] is not None:
                    linea2 += ' ' # Agrego conexión al S
                else:
                    linea2 += '*' # agrego muro al S
                linea2 += '*' #agego muro diagonal SE
            lineas.append(linea1)
            lineas.append(linea2)

        for linea in lineas:
            archivo.write(linea +'\n')

        print(archivo.read())
        archivo.close()

if __name__ == "__main__": 
    sys.setrecursionlimit(5000)
    #lab = Laberinto(archivo='laberinto_dfs.txt')
    lab = Laberinto(fils=30,cols=30)
    imp = Impresora(lab,15)    
    lab.dijkstra() 
    imp.guardar()   
    imp.presentar()
    mainloop()
     
        

        
        




    