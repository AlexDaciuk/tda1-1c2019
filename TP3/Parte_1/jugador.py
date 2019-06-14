import sys
from pathlib import Path
from random import randint
from tkinter import Tk, Canvas, mainloop

#clase que funciona de jugador
class Jugador:
    def __init__(self, metropolis): 
        self.metropolis    = metropolis
        self.cantEspecias  = 0
        self.cantEjercitos = 0
        self.cantCiudades  = 1
        self.listaCiudades = []
        self.listaCiudades.append(metropolis)

    def obtenerCantEspecias(self):
        return self.cantEspecias
    
    def obtenerCantEjercitos(self):
        return self.cantEjercitos
    
    def obtenerCantCiudades(self):
        return self.cantCiudades

    def obtenerListaDeCiudades(self):
        return self.listaCiudades

    def obtenerMetropolis(self):
        return self.metropolis

    def agregarCiudad(self, ciudad):
        self.listaCiudades.append(ciudad)

    def eliminarCiudad(self, ciudad):
        int index = 0
        for city in self.listaCiudades:
            if (city == ciudad):
                self.listaCiudades.pop(index)
                return
            index += 1
        return
    