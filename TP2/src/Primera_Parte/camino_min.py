import sys
import laberinto_dsf as lab_dfs
from tkinter import mainloop

if __name__ == "__main__": 
    archivo_lab = sys.argv[1]

    sys.setrecursionlimit(5000)

    #lab = Laberinto(archivo='laberinto_dfs.txt')

    sys.setrecursionlimit(5000)
    #lab = Laberinto(archivo='laberinto_dfs.txt')
    lab = lab_dfs.Laberinto(archivo=archivo_lab)
    imp = lab_dfs.Impresora(lab,20)    
    lab.dijkstra() 
    imp.guardar(archivo='mapa-laberinto-camino-min.txt')   
    imp.presentar()
    mainloop()
