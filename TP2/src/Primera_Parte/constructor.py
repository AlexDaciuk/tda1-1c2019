import sys

import laberinto_dsf as lab_dfs
from tkinter import mainloop

if __name__ == "__main__": 
    metodo = sys.argv[1]
    filas = int(sys.argv[2])
    columnas = int(sys.argv[3])

    sys.setrecursionlimit(5000)

    #lab = Laberinto(archivo='laberinto_dfs.txt')
    if metodo == 'dfs':
        lab = lab_dfs.Laberinto(fils=filas,cols=columnas)
        imp = lab_dfs.Impresora(lab,20)
        imp.presentar()    
        imp.guardar()
        mainloop()
    elif metodo == 'dyc':
        pass