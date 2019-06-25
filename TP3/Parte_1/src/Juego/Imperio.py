import sys
from pathlib import Path
from random import randint
from tkinter import Tk, Canvas, mainloop

#clase que funciona de jugador
class Imperio:
    def __init__(self, archivoImperio = None, mapa =None, archivoCosecha = None): 
        self.metropolis = None
        #especia acumulada
        self.especias = 0
        self.ciudades = []

        if archivoImperio and mapa:
            self.cargarCiudades(archivoImperio,mapa)

        if archivoCosecha:
            self.cargarCosecha(archivoCosecha)

    def anexarCiudad(self, ciudad):
        ciudad.imperio = self
        self.ciudades.append(ciudad)

    def desanexarCiudad(self, ciudad):
        ciudad.imperio=None
        self.ciudades.remove(ciudad)
    
    def conteoCiudades(self):
        return len(self.ciudades)

    def cargarCiudades(self, archivoimperio,mapa):
        archivo = open(Path("../assets/txt/" + archivoimperio), "r")
        lineas = archivo.read().splitlines()
        
        lineaMetropolis = lineas.pop(0)

        self.metropolis = mapa.buscarCiudad(lineaMetropolis.split(',')[0])
        self.metropolis.ejercitos = int(lineaMetropolis.split(',')[1])
        self.metropolis.imperio = self
        self.metropolis.metropolis = True

        for linea in lineas:
            ciudad = mapa.buscarCiudad(linea.split(',')[0])
            ciudad.ejercitos = int(linea.split(',')[1])           
            self.anexarCiudad(ciudad)

    def cargarCosecha(self, archivoCosecha):
        archivo = open(Path("../assets/txt/" + archivoCosecha), "r")
        self.especias = int(archivo.read())
        archivo.close()
    
    def convertirEspeciaEnEjercito(self,cantidadEjercito):
        # convierto a par mas proximo superior por condicion 1 especia = 2 ejercitos
        if cantidadEjercito % 2 != 0:
            cantidadEjercito += 1

        if cantidadEjercito <= self.ejercitosMax():            
            self.especias -= int(cantidadEjercito / 2) 
            self.metropolis.ejercitos += cantidadEjercito       

    def ejercitosMax(self):
        return int(self.especias*2)

    def moverEjercitos(self, cantidad, ciudad):
        # convierto a par mas proximo superior por condicion 1 especia = 2 ejercitos
        if cantidad % 2 != 0:
            cantidad += 1

        if cantidad <= self.ejercitosMax(): 
            self.metropolis.ejercitos -= cantidad
            ciudad.ejercitos += cantidad

    def crearyMoverEjercitos(self, cantidad, ciudad):
        if cantidad <= self.ejercitosMax():
            self.convertirEspeciaEnEjercito(cantidad)
            self.moverEjercitos(cantidad,ciudad)

