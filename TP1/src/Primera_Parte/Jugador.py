#!/usr/bin/env python3

class Jugador:

    def __init__(self, ranking, nombre, archivoPrefs):
        self._indexPreferencia = 0
        self.ranking = int(ranking)        
        self.nombre = nombre
        self.archivoPrefs = archivoPrefs
        self.preferencias = []
        self.pareja = None

    def asignarPreferencias(self,prefs):
        prefs.sort(key=lambda x : x['nPref'])
        self.preferencias = prefs

    def proximoCandidato(self):
        if (self._indexPreferencia < len(self.preferencias)):
            candidato = self.preferencias[self._indexPreferencia]['jugador']
            self._indexPreferencia += 1
            return candidato
        else:
            return None

    def prefiere(self,jugador):
        prefJugador = [x['nPref'] for x in self.preferencias if x['jugador']==jugador].pop()
        prefPareja = [x['nPref'] for x in self.preferencias if x['jugador']==self.pareja].pop()
        return prefJugador < prefPareja

    def formarPareja(self,jugador):
        if jugador.pareja != None: jugador.pareja.pareja = None
        jugador.pareja = self

        if self.pareja != None: self.pareja.pareja = None
        self.pareja = jugador
        
    def __str__(self):
        return "Nombre: " + self.nombre # + "\n" + "Preferencias: " + self.preferencias #convertir a string

