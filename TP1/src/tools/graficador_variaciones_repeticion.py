import matplotlib.pyplot as plt

# Setteo titulo del grafico
plt.title("Variaciones con repeticion")
plt.style.use('seaborn-whitegrid')

plt.xlabel("Tamaño de vector.")
plt.ylabel("Segundos")

datapoints_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

# Armo listas con los tiempos de ejecucion de cada implementacion
tiempos_lista = []
tiempos_lista_ordenada = []
tiempos_arbol_abb = []

plt.plot(datapoints_names, tiempos_lista, '--g')
plt.plot(datapoints_names, tiempos_lista_ordenada, ':r')
plt.plot(datapoints_names, tiempos_arbol_abb, '-.k')

plt.tight_layout()
plt.savefig("../../assets/images/variaciones_con_repeticion.png")
