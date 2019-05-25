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

    # El metodo recibe la ciudad con la que va a atacar y la ciudad que va a atacar
    # Este metodo ahora que lo pienso es probable que deberia pertenecer a la clase Partida o Mapa
    def atacarCiudad(self, ciudadAtq, ciudadDef):
        # Chequear si las ciudades son vecinas
        int ataque  = 
        int defensa = 
        if (ataque > defensa):
            # Tomar ciudad
            # Actualizar ejercitos
        return NotImplementedError

class Ciudad:
    def __init__(self, produccion, ejercitos = 1):
        # Atributo para la cantidad de especias que puede producir la ciudad
        self.produccion = produccion 
        
        # Cantidad de especias en la ciudad
        self.cantEspecias  = 0
        
        # Cantidad de ejercitos en la ciudad, al tomarse una ciudad esta empieza con un ejercito
        self.cantEjercitos  = ejercitos
        
        # Este atributo guarda una cantidad de ejercitos que tiene la ciudad pero que no puede usar en ese turno
        self.ejercitosNoAtq = 0

        # Cantidad de ejercitos con la que ciudad va a atacar a la ciudad vecina
        self.ejercitosParaAtq = 0

        # Lista de vecinos de la ciudad, o sea, todas las ciudades con las que esta conectada
        self.listaVecinos = []

    def agregarEjercitos(self, refuerzos):
        self.cantEjercitos += refuerzos

    def obtenerListaDeVecinos(self):
        return self.listaVecinos
    
    # Recibe la cantidad de especias que quiere convertir a ejercitos
    # Cada especia equivale a 2 ejercitos
    # Los ejércitos transformados en especia no se pueden usar en ese turno
    def transformarEspeciaEnEjercito(self, especias):
        # No puedo transformar mas especias de las que poseo
        if (especias > self.cantEspecias):
            print("Error: no puede convertir mas especias de las que posee")
            return False
        
        # Descuento la cantidad de especias que paso a ejercitos
        self.cantEspecias -= especias
        
        # Agrego la nueva cantidad de ejercitos
        self.cantEjercitos
        # Dichos ejercitos no podran atacar hasta el siguiente turno
        self.ejercitosNoAtq += especias * 2
        return True



    # Recibe la cantidad de ejercitos que quiere trasnformar a especia
    def transformarEjercitoEnEspecia(self, ejercitos):
        # No puedo transformar mas ejercitos de las que poseo
        # Para evitar problemas asumo que solo puedo transformar ejercitos que puedo usar para atacar
        if (ejercitos > self.ejercitosParaAtq):
            print("Error: no puede convertir mas ejercitos de los que posee")
            return False

        # Como máximo se pueden transformar 5 ejercitos en especia.
        if (ejercitos > 5):
            print("Error: no puede convertir mas de 5 ejercitos")
            return False
        
        self.cantEjercitos    -= ejercitos 
        self.ejercitosParaAtq -= ejercitos
        self.cantEspecias     += ejercitos
        return True





#clase que funciona de moderador para el juego    
class Partida:
    def __init__(self, jugador1, jugador2):  
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        # Contador de turnos
        self.cantTurnos = 0

    def finDeParida(self):
        # Primera condicion de fin de partida: un jugador recolecto mas de 100 especias
        int especia1 = self.jugador1.obtenerCantEspecias()
        int especia2 = self.jugador2.obtenerCantEspecias()

        if (especia1 > 100):
            return True

        if (especia2 > 100):
            return True

        # segunda condicion de fin de partida: el rival quedo con su metropolis aislada
        # Deberia chequear solo si el rival tiene su metropoli desconexa
        # pero no estoy seguro por ahora como hacer eso asi que lo hago para
        # ambas ciudades
        lista1 = []
        lista2 = []
        ciudad1 = self.jugador1.obtenerMetropolis()
        ciudad2 = self.jugador2.obtenerMetropolis()
        lista1  = self.ciudad1.obtenerListaDeVecinos()
        lista2  = self.ciudad2.obtenerListaDeVecinos()
        
        if (len(lista1) == 0):
            return True
        
        if (len(lista2) == 0):
            return True

        # Tercera condicion de fin de partida: pasaron 50 turnos
        if (self.cantTurnos >= 50):
            return True

        return False

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
