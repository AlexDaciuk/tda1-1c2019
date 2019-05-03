from random import randint
from tkinter import Tk, Canvas, mainloop

#clase que funciona de nodo y contiene las aristas que lo conectan
class Celda:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.conexiones = {'N':None, 'S':None, 'E':None, 'O':None}
        self.visitado= False        

class Laberinto:
    def __init__(self,fils,cols):
         self.fils = fils
         self.cols = cols
         # Grafo del laberinto con diccionario de adyacencias y representación matricial de los nodos (celdas)
         self.grilla = [[Celda(x,y) for y in range(self.fils)] for x in range(self.cols)] 

    # Busca un vecino al azar, lo conecta con la celda y lo marca como visitado
    def obtenerVecino(self, celda):
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
        if len(vecinos) > 0:        
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
    
class Graficador:
    def __init__(self,laberinto):
        self.laberinto = laberinto
        self.master = Tk()
        self.w = 40 # Ancho de celda
        self.canva = Canvas(self.master, width=(self.laberinto.fils*self.w)+2, height=(self.laberinto.cols*self.w)+2)

    def imprimir(self):
        # Imprimo celdas        
        for fila in self.laberinto.grilla:
            for celda in fila:
                self.iCelda(celda)                     

        self.canva.pack()    

    def iCelda(self,celda):
        ix = celda.x*self.w
        iy = celda.y*self.w
        fx = celda.x*self.w + self.w
        fy = celda.y*self.w + self.w
        
        if celda.conexiones['N'] is None:
            self.canva.create_line(ix+2,iy+2,fx+2,iy+2, fill="black") # Norte
        if celda.conexiones['E'] is None:
            self.canva.create_line(fx+2,iy+2,fx+2,fy+2, fill="black") # Este
        if celda.conexiones['S'] is None:
            self.canva.create_line(ix+2,fy+2,fx+2,fy+2, fill="black") # Sur
        if celda.conexiones['O'] is None:
            self.canva.create_line(ix+2,iy+2,ix+2,fy+2, fill="black") # Oeste         

if __name__ == "__main__": 
    lab = Laberinto(10,10)
    graf = Graficador(lab)

    # algoritmo por dsf
    a = [lab.grilla[0][0]]
    while(a[-1] is not None):
        a[-1].visitado=True          
        a.append(lab.obtenerVecino(a[-1]))

    graf.imprimir()
    mainloop()