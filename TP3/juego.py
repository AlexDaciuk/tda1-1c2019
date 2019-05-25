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

    def obtenerCantEspecias(self):
         return self.cantEspecias
    
    def obtenerCantEjercitos(self):
         return self.cantEjercitos
    
      def obtenerCantCiudades(self):
         return self.cantCiudades

#clase que funciona de moderador para el juego    
class Partida:
    def __init__(self, jugador1, jugador2):  
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def determinar_ganador(self):
        int especia1 = self.jugador1.obtenerCantEspecias()
        int especia2 = self.jugador2.obtenerCantEspecias()

        if (especia1 < especia2):
            return self.jugador2

        if (especia1 > especia2):
            return self.jugador1

        # Resuelvo primer empate
        int ciudades1 = self.jugador1.obtenerCantCiudades()
        int ciudades2 = self.jugador2.obtenerCantCiudades()
        
        if (ciudades1 < ciudades2):
            return self.jugador2
        
        if (ciudades1 > ciudades2):
            return self.jugador1

        # Resuelvo segundo empate
        int ejercitos1 = self.jugador1.obtenerCantEjercitos()
        int ejercitos2 = self.jugador2.obtenerCantEjercitos()

        if (ejercitos1 < ejercitos2):
            return self.jugador2 

        if (ejercitos1 > ejercitos2):
            return self.jugador1

        # Si llego aca, es empate, por ahora devuelvo None
        else:
            return None
