import sys
from pathlib import Path
from Jugador import Jugador

#devuelve lista de objetos jugador con la preferencias cargadas
def cargarJugadores(nombre_archivo_jugadores):
    
    archivoJugadores = open(Path("../../assets/txt/" + nombre_archivo_jugadores),"r")    
    lineasJugadores = archivoJugadores.read().splitlines()
    
    jugadores = [Jugador(x.split(',')[0],x.split(',')[1],x.split(',')[2]) for x in lineasJugadores] 
    jugadores.sort(key= lambda x : x.ranking)
    
    archivoJugadores.close()

    for j in  jugadores:
        archivoPrefs = open(Path("../../assets/txt/" + j.archivoPrefs),"r")
        prefs = archivoPrefs.read().splitlines()        
        j.asignarPreferencias([{"jugador":next(filter(lambda y: y.nombre == x.split(',')[0],jugadores)),"nPref":int(x.split(',')[1])} for x in prefs])
 
    archivoPrefs.close()

    return jugadores

#Funcíon para cargar pareo del punto 1.5
def armarParejas(jugadores, nombre_archivo_pareo):
    
    grupoA = jugadores[slice(0,len(jugadores)//2)]
    grupoB = jugadores[slice(len(jugadores)//2,len(jugadores))]

    archivo_pareo = open(Path("../../assets/txt/" + nombre_archivo_pareo),"r")
    lineas_pareo = archivo_pareo.read().splitlines()

    for pareo in lineas_pareo:
        jugador1 = next(filter(lambda x: x.nombre == pareo.split(',')[0],jugadores))
        jugador2 = next(filter(lambda x: x.nombre == pareo.split(',')[1],jugadores))
        jugador1.formarPareja(jugador2)

    return grupoA, grupoB

#Funcíon para cargar pareo del punto 1.6
# --- Implementación Algoritmo Gale-Shapley
# --- Recibe la lista de jugadores con sus preferencias 
# --- y devuelve los dos grupos con las parejas asgignas en cada caso
# --- mediante una varación del Algoritmo de Gale-Shapley 
def armarParejasEstables(jugadores):
    
    grupoA = jugadores[slice(0,len(jugadores)//2)]
    grupoB = jugadores[slice(len(jugadores)//2,len(jugadores))]

    proponentesLibres = len(grupoA) 

    while proponentesLibres>0 :
        for proponente in grupoA:
            if proponente.pareja is None:
                propuesto = proponente.proximoCandidato()
                if propuesto.pareja is None:
                    proponente.formarPareja(propuesto)
                    proponentesLibres -= 1
                elif propuesto.prefiere(proponente):
                    proponente.formarPareja(propuesto)                
    return grupoA, grupoB

#Comprobación de estabilidad del algoritmo Gale-Shapley
# --- Una pareja no emparejada A-B es inestable 
# --- si A y B se prefieren mutuamente por sobre sus parejas actuales
def parejasEstables(grupoA, grupoB):
    for jugadorA in grupoA:
        for jugadorB in grupoB:
            if jugadorA.pareja != jugadorB and jugadorA.prefiere(jugadorB) and jugadorB.prefiere(jugadorA):
                return False
    return True         

#Ejecución: arma e imprime parejas
if __name__ == "__main__":    
    
    punto = sys.argv[1]
    nombre_archivo_jugadores = sys.argv[2]
    grupoA, grupoB = (None,None)
     
    jugadores = cargarJugadores(nombre_archivo_jugadores)    
    
    if punto == "1.1":
        print('Parejas por Gale-Shapley:') 
        grupoA, grupoB = armarParejasEstables(jugadores)          
    
    if punto == "1.5":
        print('Parejas por archivo de pareo:') 
        nombre_archivo_pareo = sys.argv[3]        
        grupoA, grupoB = armarParejas(jugadores, nombre_archivo_pareo)

    if grupoA != None:
           
        for jugador in grupoA:
            print(jugador.nombre + ", " + jugador.pareja.nombre)
        print ('Es estable?:', parejasEstables(grupoA,grupoB))

    
