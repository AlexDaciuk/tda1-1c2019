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
    


class Ciudad:
    def __init__(self, produccion, ejercitos = 1):
        # Atributo para la cantidad de especias que puede producir la ciudad
        self.produccion = produccion 
        # Cantidad de especias en la ciudad
        self.cantEspecias  = 0
        # Cantidad de ejercitos en la ciudad
        # al tomarse una ciudad esta empieza con un ejercito.
        # Aclaro que tiene que cumplirse siempre que: 
        # cantEjercitos = ejercitosParaAtq + ejercitosNoAtq
        self.cantEjercitos  = ejercitos
        # Este atributo guarda una cantidad de ejercitos 
        # que tiene la ciudad pero que no puede usar en ese turno
        self.ejercitosNoAtq = 0
        # Cantidad de ejercitos con la que ciudad va a atacar a la ciudad vecina
        self.ejercitosParaAtq = ejercitos
        # Ejercitos para defender
        self.ejercitosParaDef = 0
        # Lista de vecinos de la ciudad, o sea, 
        # todas las ciudades con las que esta conectada
        self.listaVecinos = []

    def agregarEjercitosAtq(self, refuerzos):
        self.ejercitosParaAtq += refuerzos

    # La ciudad pierde ejercitos por hacer un ataque
    def perderEjercitosPorAtq(self, perdidas):
        self.ejercitosParaAtq -= perdidas
        # Para evitar tener numeros negativos
        if (self.ejercitosParaAtq < 0):
            self.ejercitosParaAtq = 0
        return

    def perderEjercitosPorDef(self, perdidas):
        self.ejercitosParaDef -= perdidas
        # Para evitar tener numeros negativos
        if (self.ejercitosParaDef < 0):
            self.ejercitosParaDef = 0
        return          

    def obtenerListaDeVecinos(self):
        return self.listaVecinos

    # Devuelve la cantidad de ejercitos que posee la ciudad para atacar
    def obtenerCantEjercitosAtq(self):
        return self.ejercitosParaAtq

    # Devuelve la cantidad total de ejercitos que posee la ciudad
    def obtenerEjercitosDef(self):
        return self.ejercitosParaDef

    def enListaDeVecinos(self, ciudadVecina):
        if (ciudadVecina in self.enListaDeVecinos):
            return True 
        
        return False
    
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
        int especia1 = self.jugador1.obtenerCantEspecias()
        int especia2 = self.jugador2.obtenerCantEspecias()

        if (especia1 > 100):
            return True

        if (especia2 > 100):
            return True

        # segunda condicion de fin de partida: el rival quedo con su metropolis aislada
        lista = []
        ciudad = self.jugador1.obtenerMetropolis()
        
        if (self.verDeQuienEsElTurno() == 1):
            ciudad = self.jugador2.obtenerMetropolis()

        lista  = self.ciudad.obtenerListaDeVecinos()
        
        if (len(lista) == 0):
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

    def ciudadCambiarBando(ciudad, exDueño, nuevoDueño):
        exDueño.eliminarCiudad(ciudad)
        nuevoDueño.agregarCiudad(ciudad)
        return

    # El mapa debe marcar en el nodo de esa ciudad que no pertenece a nadie
    def ciudadLibre(ciudad):
        return NotImplementedError

    def pasarEjercitos(ciudadAtq, ciudadDef):
        int paso = ciudadAtq.obtenerCantEjercitosAtq()
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
                int defensa = ciudadDef.obtenerEjercitosDef()
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
