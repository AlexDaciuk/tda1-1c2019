import sys
from pathlib import Path 
from Juego.Mapa import Mapa
from Juego.Imperio import Imperio
from division import guardarImperio
from recolectar import calcularCosecha


#busca las ciudades adversarias y asigna mas ejercitos que el oponente de ser posible, acumula el resto
def producir(imperio1,imperio2):

    fronteras = buscarFrontera(imperio1,imperio2)

    #si imperio1 cosecha mas que imperio2 -> actitud defensiva
    #if calcularCosecha(imperio1) > calcularCosecha(imperio2):
    for frontera in fronteras:
        if frontera['origen'].ejercitos <= frontera['destino'].ejercitos:
            #muevo diferencia de ejercitos entre orien y destino para defender
            diferencia = frontera['destino'].ejercitos - frontera['origen'].ejercitos
            if diferencia % 2 == 0:
                if diferencia == 0:
                    diferencia = 2
                else:
                    diferencia += 1
            
            imperio1.crearyMoverEjercitos(diferencia,frontera['origen'])
    # si no -> actitud ofensiva (crear todos los ejercitos con el objetivo de avanzar)
    #else:
    #    pass
             

#devuelve un dic con las fronteras entre ambos imperios
def buscarFrontera(imperio1,imperio2):
    fronteras = []
    for ciudad in imperio1.ciudades:
        for ruta in ciudad.rutas:
            if ruta.destino.imperio == imperio2:
                fronteras.append({'origen': ciudad,'destino':ruta.destino})
    return fronteras

def actulizarCosecha(imperio):
    archivo = open(Path("../assets/txt/" + "cosecha" + str(numJugador) +"_temp.txt"), "w+")  
    archivo.write(str(imperio.especias))    
    archivo.close()


if __name__ == "__main__":  

    numJugador = sys.argv[1]
    archivoCiudades = sys.argv[2]
    archivoRutas = sys.argv[3]
    archivoImperio1 = sys.argv[4]
    archivoCosecha1 = sys.argv[5]
    archivoImperio2 = sys.argv[6]
    archivoCosecha2 = sys.argv[7]

    mapa = Mapa(archivoCiudades, archivoRutas)
    imperio1 = Imperio(archivoImperio1,mapa,archivoCosecha1)
    imperio2 = Imperio(archivoImperio2,mapa,archivoCosecha2)

    if numJugador == '1':
        producir(imperio1,imperio2)
        guardarImperio(int(numJugador),imperio1,True)
        actulizarCosecha(imperio1)
    elif numJugador == '2':
        producir(imperio2,imperio1)
        guardarImperio(int(numJugador),imperio2,True)
        actulizarCosecha(imperio2)
    
    

        