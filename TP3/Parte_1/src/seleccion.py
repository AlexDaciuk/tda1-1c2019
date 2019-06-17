import sys
from pathlib import Path
from Juego.Mapa import Mapa

# utilizamos BFS y asiganamos primero por proximidad y luego por cantidad de especia producida
# Con este objetivo maximizamos la probilidad de mantener lo mas lejos posible al enemigo
# y a la vez maximizar la recolecciónd de especia, ambas condiciones necesarias para ganar.
def generarPreferencias(jugador,mapa):
    capital = None
    capitalOponente = None
    listaPrefs = []

    # Asignación inicio bfs (capital) y capital oponente
    if jugador == 1:
        capital= mapa.ciudades[0]
        capitalOponente = mapa.ciudades[1]
    elif jugador ==2:
        capital= mapa.ciudades[1]
        capitalOponente = mapa.ciudades[0]

    asignaciónBFS(capital,capitalOponente)

    # Elimino las capitales del mapa para no incluirlas en las preferencias
    mapa.ciudades.remove(capital)
    mapa.ciudades.remove(capitalOponente)

    # Armo lista de preferencias con las ciudades y sus distancias a la capital
    for ciudad in mapa.ciudades:
        listaPrefs.append({ 'ciudad': ciudad, 'distancia': calcularDistancia(ciudad)})

	# Ordeno la lista segun los dos criterios: primero distancia y luego producción  
    listaPrefs = sorted(listaPrefs,key=lambda x : (x['distancia'],-x['ciudad'].produccion))

    return listaPrefs

# Establece el nodo ciudad.anterior mas cercano a la capital en cada ciudad en el mapa
def asignaciónBFS(capital,capitalOponente):
    cola = []
    visitados = []
    # Seteo la capital como nodo de partida
    cola.append(capital)
    # Agrego capital oponente a lista de visitados para ignorarla en el recorrido BFS
    visitados.append(capitalOponente)

    while cola:
        actual = cola.pop(0)

        if actual not in visitados:
            visitados.append(actual)
        for rutaVecina in actual.rutas:
            if rutaVecina.destino not in visitados:
                cola.append(rutaVecina.destino)
                rutaVecina.destino.anterior = actual

# calcula distancia de una ciudad respecto a la capital
def calcularDistancia(ciudad):
    ciudadActual = ciudad
    distancia = 0   

    #La capital no tiene anterior, asi que lo utilizo como condición de corte
    while ciudadActual.anterior:
       distancia +=1       
       ciudadActual = ciudadActual.anterior

    return distancia

def guardarPreferencias(nombreArchivo,listaPrefs):
    archivo = open(Path("../assets/txt/" + nombreArchivo), "w+")

    lineas = [x['ciudad'].nombre for x in listaPrefs ]
    
    for linea in lineas:
        archivo.write(linea + '\n')

    archivo.close()        

if __name__ == "__main__":
    jugador = int(sys.argv[1])
    archivoCiudades = sys.argv[2]
    archivoRutas = sys.argv[3]

    mapa = Mapa(archivoCiudades,archivoRutas)

    listaprefs = generarPreferencias(jugador,mapa)

    guardarPreferencias('seleccion' + str(jugador) + '.txt',listaprefs)