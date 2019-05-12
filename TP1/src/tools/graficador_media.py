import matplotlib.pyplot as plt

# Setteo titulo del grafico
plt.title("Media")
plt.style.use('seaborn-whitegrid')

plt.xlabel("Tamaño de vector.")
plt.ylabel("Segundos")

# Indico cantidad de benchmarks y nombres
datapoints_number = 10
datapoints_names = ["1",
                    "10",
                    "100",
                    "1000",
                    "10 000",
                    "100 000",
                    "1 000 000",
                    "10 000 000"]

# Armo listas con los tiempos de ejecucion de cada implementacion
tiempos_lista = []
tiempos_lista_ordenada = []
tiempos_arbol_abb = []

plt.plot(datapoints_names, tiempos_lista, '--g')
plt.plot(datapoints_names, tiempos_lista_ordenada, ':r')
plt.plot(datapoints_names, tiempos_arbol_abb, '-.k')

plt.tight_layout()
plt.savefig("../../assets/images/media.png")
