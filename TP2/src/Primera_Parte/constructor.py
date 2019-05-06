import sys

import laberinto_dsf as lab_dfs
import laberinto_dyc as lab_dyc
from tkinter import mainloop

if __name__ == "__main__": 
    metodo = sys.argv[1]
    filas = int(sys.argv[2])
    columnas = int(sys.argv[3])

    sys.setrecursionlimit(100000)
    
    if metodo == 'dfs':
        lab = lab_dfs.Laberinto(fils=filas,cols=columnas)
        imp = lab_dfs.Impresora(lab,20)
        imp.presentar()    
        imp.guardar()
        mainloop()
    elif metodo == 'dyc':
        mapa = lab_dyc.crear_mapa_vacio(filas + 2,columnas + 2)
        lab_dyc.generar_mapa(mapa, filas + 2, columnas + 2)
        lab_dyc.guardar_mapa(mapa)