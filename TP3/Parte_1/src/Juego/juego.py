import sys
from pathlib import Path
from random import randint
from tkinter import Tk, Canvas, mainloop

#clase que funciona de moderador para el juego    
class Partida:
    def __init__(self, jugador1, jugador2):  
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        # Contador de turnos
        self.cantTurnos = 0
        # aca guardo quien tiene permiso de jugar en el turno/ronda
        # 0 si el jugador1 le toca jugar
        # 1 si le toca al jugador2 
        self.turnoJugador = 0
        # con este string puedo saber en que fase esta el turno
        self.fase = ""

    def pasarAFaseDeRecoleccion(self):
        self.fase = "recoleccion"
    
    def pasarAFaseDeProduccion(self):
        self.fase = "produccion"
            
    def pasarAFaseDeAtaques(self):
        self.fase = "ataques"
    
    def verFaseDeTurno(self):
        return self.fase 

    def verDeQuienEsElTurno(self):
        return self.turnoJugador

    def cambiarDeQuienEsElTurno(self):
        if (self.turnoJugador == 0):
            self.turnoJugador = 1
            return
        else:
            self.turnoJugador = 0
            return

    def finDeParida(self):
        # Primera condicion de fin de partida: un jugador recolecto mas de 100 especias
        especia1 = self.jugador1.obtenerCantEspecias()
        especia2 = self.jugador2.obtenerCantEspecias()

        if (especia1 > 100):
            return True

        if (especia2 > 100):
            return True

        # segunda condicion de fin de partida: el rival quedo con su metropolis aislada
        lista = []
        ciudad = self.jugador1.obtenerMetropolis()
        
        if (self.verDeQuienEsElTurno() == 1):
            ciudad = self.jugador2.obtenerMetropolis()

        lista  = ciudad.obtenerListaDeVecinos()
        
        if (len(lista) == 0):
            return True

        # Tercera condicion de fin de partida: pasaron 50 turnos
        if (self.cantTurnos >= 50):
            return True

        return False

    def determinar_ganador(self):
        especia1 = self.jugador1.obtenerCantEspecias()
        especia2 = self.jugador2.obtenerCantEspecias()

        if (especia1 < especia2):
            return self.jugador2

        if (especia1 > especia2):
            return self.jugador1

        # Resuelvo primer empate
        ciudades1 = self.jugador1.obtenerCantCiudades()
        ciudades2 = self.jugador2.obtenerCantCiudades()
        
        if (ciudades1 < ciudades2):
            return self.jugador2
        
        if (ciudades1 > ciudades2):
            return self.jugador1

        # Resuelvo segundo empate
        ejercitos1 = self.jugador1.obtenerCantEjercitos()
        ejercitos2 = self.jugador2.obtenerCantEjercitos()

        if (ejercitos1 < ejercitos2):
            return self.jugador2 

        if (ejercitos1 > ejercitos2):
            return self.jugador1

        # Si llego aca, es empate, por ahora devuelvo None
        else:
            return None

    def ciudadCambiarBando(self,ciudad, exDueño, nuevoDueño):
        exDueño.eliminarCiudad(ciudad)
        nuevoDueño.agregarCiudad(ciudad)
        return

    # El mapa debe marcar en el nodo de esa ciudad que no pertenece a nadie
    def ciudadLibre(self,ciudad):
        return NotImplementedError

    def pasarEjercitos(self,ciudadAtq, ciudadDef):
        paso = ciudadAtq.obtenerCantEjercitosAtq()
        # ¿Casos borde? VER
        if (paso <= 1):
            print("Error: como minimo debe pasar 2 ejercitos")
        # En realidad paso los ejercitos pero el metodo sirve igual
        ciudadAtq.perderEjercitosPorAtq(paso)
        # los ejercitos que paso decido pasarlos a Atq
        ciudadDef.agregarEjercitosAtq(paso)


    # El metodo recibe la ciudad con la que va a atacar y la ciudad que va a atacar
    # ataque son los ejercitos que usa ciudadAtq para atacar
    def atacarCiudad(self, ciudadAtq, ciudadDef, ataque, jugAtq, jugDef):
        # La ciudad metrópoli no se puede atacar 
        # (CHEQUEAR CON EL METODO QUE LLAME A ESTO)

        # si las ciudades son vecinas y estoy en fase de ataques, realizo el ataque
        if (self.verFaseDeTurno() == "ataques"):
            if (ciudadAtq.enListaDeVecinos(ciudadDef)):
                # Se supone que alguien debe decidir con cuantos ejercitos atacar en
                # vez de usar todos los disponibles
                # VER
                defensa = ciudadDef.obtenerEjercitosDef()
                if (ataque > defensa):
                    # actualizar ejercitos
                    ciudadDef.perderEjercitosPorDef(defensa)
                    ciudadAtq.perderEjercitosPorAtq(defensa)
                    # Tomar ciudad
                    self.ciudadCambiarBando(ciudadDef, jugDef, jugAtq)
                    self.pasarEjercitos(ciudadAtq, ciudadDef)
                if (ataque == defensa):
                    ciudadDef.perderEjercitosPorDef(defensa)
                    ciudadAtq.perderEjercitosPorAtq(defensa)
                    self.ciudadLibre(ciudadDef)

                # El ataque fracaso
                # El atacante pierde los ejercitos con los que ataco
                else:
                    # ejercitos de ataque < ejercitos de def 
                    ciudadDef.perderEjercitosPorDef(ataque)
                    ciudadAtq.perderEjercitosPorAtq(ataque) 
        # sino, no puedo atacar 
        # o el ataque ya termino
        return
