from .Ruta import Ruta

class Ciudad:
    def __init__(self,nombre, produccion, ejercitos = 0, imperio = None, metropolis = False):
        self.nombre = nombre        
        self.metropolis = metropolis
        self.imperio = imperio
        # Atributo para la cantidad de especias que puede producir la ciudad
        self.produccion = produccion 
        # Cantidad de especias en la ciudad
        self.cantEspecias  = 0
        # Los ejercitos de la ciudad se dividen en:
        # ataque, defensa, no se puede usar (AKA: noAtq)
        # ----
        # Este atributo guarda una cantidad de ejercitos 
        self.ejercitos = ejercitos
        # que tiene la ciudad pero que no puede usar en ese turno
        self.ejercitosNoAtq = 0
        # Cantidad de ejercitos con la que ciudad va a atacar a la ciudad vecina
        self.ejercitosParaAtq = 0
        # Ejercitos para defender
        self.ejercitosParaDef = 0
        # Lista de Jugador.Ruta
        self.rutas = []

        #para armar arbol en BFS utilizado en la selección
        self.anterior = None

    def agregarRuta(self, destino,trafico):
        self.rutas.append(Ruta(destino,trafico))

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
        return self.rutas

    # Devuelve la cantidad de ejercitos que posee la ciudad para atacar
    def obtenerCantEjercitosAtq(self):
        return self.ejercitosParaAtq

    # Devuelve la cantidad total de ejercitos que posee la ciudad
    def obtenerEjercitosDef(self):
        return self.ejercitosParaDef

    def enListaDeVecinos(self, ciudadVecina):
        if (ciudadVecina in self.rutas):
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

