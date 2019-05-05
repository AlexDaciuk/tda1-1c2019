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

class Laberinto:
    def __init__(self,fils,cols):
         self.fils = fils
         self.cols = cols
         # Grafo del laberinto con diccionario de adyacencias y representación matricial de los nodos (celdas)
         self.grilla = [[Celda(x,y) for y in range(self.fils)] for x in range(self.cols)] 
         self.pila = [self.grilla[0][0]]
         self.generar(self.grilla[0][0])

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
    
    #dfs con recursive backtraking
    def generar(self, celda):                
        if self.pila[-1] is not None:
            celda.visitado = True
            self.pila.append(self.conectarVecino(celda))
            self.generar(self.pila[-1])
        else:
            try:
                self.pila.pop()
                self.pila.pop() 
                self.generar(self.pila[-1])              
            except IndexError:
                return

    def generar2(self,celda):                
        if type(celda) is Celda :
            celda.visitado = True
            if self.conectarVecino(celda) is not None:
                self.pila.append(celda)            
            self.generar2(self.conectarVecino(celda))
        elif celda is None and self.pila:
            self.pila.pop()
            self.generar2(self.pila[-1])
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
        
        if celda.conexiones['N'] is None:
            self.canva.create_line(ix+2,iy+2,fx+2,iy+2, fill="black") # Norte
        if celda.conexiones['E'] is None:
            self.canva.create_line(fx+2,iy+2,fx+2,fy+2, fill="black") # Este
        if celda.conexiones['S'] is None:
            self.canva.create_line(ix+2,fy+2,fx+2,fy+2, fill="black") # Sur
        if celda.conexiones['O'] is None:
            self.canva.create_line(ix+2,iy+2,ix+2,fy+2, fill="black") # Oeste     

    def guardar(self):
        archivo = open(Path("../../assets/txt/laberinto_dfs.txt"), "w+")

        lineas = []
        lineas.append('*'*((self.lab.cols*2) + 1)) #Muro N

        for x in range(self.lab.fils):
            linea1='*' # Agrego pared oeste
            linea2='*' # Agrego pared oeste
            for y in range(self.lab.cols):
                celda = self.lab.grilla[y][x]
                
                linea1 +=' ' # Agergo celda
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
    lab = Laberinto(3,4)
    imp = Impresora(lab,30)
    imp.presentar()
    imp.guardar()
    mainloop()
    a=1