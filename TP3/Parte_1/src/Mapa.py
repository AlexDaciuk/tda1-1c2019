from pathlib import Path
from Ciudad import Ciudad

class Mapa:    
    def __init__(self,archivoCiudades,archivoRutas):
        self.ciudades = []
        self.crearCiudades(archivoCiudades)
        self.crearRutas(archivoRutas)

    # Carga todas las ciudades en la lista ciudades
    def crearCiudades(self,archivoCiudades):
        archivo = open(Path("../assets/txt/" + archivoCiudades), "r")
        lineas = archivo.read().splitlines()

        for linea in lineas:
            nombre = linea.split(',')[0]            
            produccion = int(linea.split(',')[1])
            self.ciudades.append(Ciudad(nombre,produccion))

        archivo.close()
  
    # Carga todas las rutas de forma bidireccional dentro de cada Ciudad
    def crearRutas(self,archivoRutas):
        archivo = open(Path("../assets/txt/" + archivoRutas), "r")
        lineas = archivo.read().splitlines()   

        for linea in lineas:
             origen = self.buscarCiudad(linea.split(',')[0])
             destino = self.buscarCiudad(linea.split(',')[1])
             trafico = int(linea.split(',')[2])

             origen.agregarRuta(destino,trafico)    

        archivo.close()

    def buscarCiudad(self,nombre):
        return next(filter(lambda x : x.nombre == nombre,self.ciudades))

if __name__ == "__main__":
    mapa = Mapa('ciudades.txt','rutas.txt')
    print(mapa)    
    
