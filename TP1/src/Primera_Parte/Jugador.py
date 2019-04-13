class Jugador:

    def __init__(self, nombre):
        self._indexPreferencia = 0
        self.nombre = nombre
        self.preferencias = []
        self.pareja = None

    def asignarPreferencias(self,prefs):
        prefs.sort(key=lambda x : x['preferencia'])
        self.preferencias = prefs

    def proximoCandidato(self):
        if (self._indexPreferencia < len(self.preferencias)):
            candidato = self.preferencias[self._indexPreferencia]['jugador']
            self._indexPreferencia += 1
            return candidato
        else:
            return None

    def prefiere(self,jugador):
        prefJugador = next(iter([x['preferencia'] for x in self.preferencias if x['jugador']==jugador])) 
        prefPareja = next(iter([x['preferencia'] for x in self.preferencias if x['jugador']==self.pareja])) 
        return prefJugador < prefPareja

    def formarPareja(self,jugador):
        if jugador.pareja != None: jugador.pareja.pareja = None
        jugador.pareja = self

        if self.pareja != None: self.pareja.pareja = None
        self.pareja = jugador
        
    def __str__(self):
        return "Nombre: " + self.nombre # + "\n" + "Preferencias: " + self.preferencias #convertir a string

