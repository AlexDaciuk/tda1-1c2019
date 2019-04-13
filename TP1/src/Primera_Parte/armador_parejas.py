from pathlib import Path
from Jugador import Jugador

#devuelve lista de objetos jugador con la preferencias cargadas
def cargarJugadores():
    archivoJugadores = open(Path("../../assets/txt/20_jugadores.rank"),"r")    
    lineasJugadores = archivoJugadores.read().splitlines()
    
    jugadores = [{"jugador":Jugador(x.split(',')[1]),"archivoPrefs":x.split(',')[2]} for x in lineasJugadores]  
    
    archivoJugadores.close()

    for j in  jugadores:
        archivoPrefs = open(Path("../../assets/txt/" + j["archivoPrefs"]),"r")
        prefs = archivoPrefs.read().splitlines()
        j["jugador"].asignarPreferencias([{"jugador":next(iter([y["jugador"] for y in jugadores if y["jugador"].nombre==x.split(',')[0]])),"preferencia":int(x.split(',')[1])} for x in prefs])

    archivoPrefs.close()

    return [x['jugador'] for x in jugadores]

#Implementación Algoritmo Gale-Shapley
def armarParajas(jugadores):
    
    grupo = [x["jugador"] for x in jugadores[0].preferencias]
    jugadoresLibres = len(grupo) 

    while jugadoresLibres>0 :
        for jugador in grupo:
            if jugador.pareja is None:
                candidato = jugador.proximoCandidato()
                if candidato.pareja is None:
                    jugador.formarPareja(candidato)
                    jugadoresLibres -= 1
                elif candidato.prefiere(jugador):
                    jugador.formarPareja(candidato)

    return grupo
    
#Ejecución: arma e imprime parejas
if __name__ == "__main__":
    grupo = armarParajas(cargarJugadores())

    for jugador in grupo:
        print(jugador.nombre + ", " + jugador.pareja.nombre)

    
