import sys
from pathlib import Path
from random import randint
from tkinter import Tk, Canvas, mainloop

#clase que funciona de jugador
class Imperio:
    def __init__(self, metropolis): 
        self.metropolis = metropolis
        self.cantEspecias = 0
        self.cantEjercitos = 0
        self.ciudades = []

    def anexarCiudad(self, ciudad):
        ciudad.imperio = self
        self.ciudades.append(ciudad)

    def desanexarCiudad(self, ciudad):
        ciudad.imperio=None
        self.ciudades.remove(ciudad)
    
    def conteoCiudades(self):
        return len(self.ciudades)
    