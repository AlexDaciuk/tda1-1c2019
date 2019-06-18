import sys
from pathlib import Path
from Juego.Mapa import Mapa
from Juego.Imperio import Imperio

def BuscarCiudadesImperio(archivoSeleccion,mapa):
    archivoSelec = open(Path("../assets/txt/" + archivoSeleccion), "r")
    nombresCiudades = archivoSelec.read().splitlines()
    ciudades = []
    
    for nombreCiudad in nombresCiudades:
        ciudades.append(mapa.buscarCiudad(nombreCiudad))

    return ciudades

def generarImperios(archivoSelección1, archivoSelección2, mapa):
    imperio1 = Imperio(mapa.ciudades[0])
    imperio2 = Imperio(mapa.ciudades[1])

    prefsImperio1=BuscarCiudadesImperio(archivoSelección1,mapa)
    prefsImperio2=BuscarCiudadesImperio(archivoSelección2,mapa)

    # Seteo inicial metropolis
    imperio1.metropolis.metropolis = True
    imperio2.metropolis.metropolis = True
    imperio1.metropolis.ejercito = 1    
    imperio2.metropolis.ejercito = 1

    # Pareo inicial según las reglas de "La especia debe Fluir"
    for c1,c2 in zip(prefsImperio1,prefsImperio2):
        if c1 != c2:
            if not c1.imperio:
                imperio1.anexarCiudad(c1)
                c1.ejercito = 1
            if not c2.imperio:
                imperio2.anexarCiudad(c2)    
                c2.ejercito = 1

    return imperio1, imperio2

def guardarImperio(num,imperio):
    archivo = open(Path("../assets/txt/" + "imperio" + str(num) +".txt"), "w+")

    archivo.write(imperio.metropolis.nombre + ',' + str(imperio.metropolis.ejercito) + '\n')
    for ciudad in imperio.ciudades:
        archivo.write(ciudad.nombre + ',' + str(ciudad.ejercito) + '\n')

    archivo.close()

if __name__ == "__main__":    
    archivoCiudades = sys.argv[1]
    archivoRutas = sys.argv[2]
    archivoSeleccion1 = sys.argv[3]
    archivoSeleccion2 = sys.argv[4]

    mapa = Mapa(archivoCiudades,archivoRutas)

    imperio1, imperio2 = generarImperios(archivoSeleccion1,archivoSeleccion2,mapa)

    guardarImperio(1,imperio1)
    guardarImperio(2,imperio2)