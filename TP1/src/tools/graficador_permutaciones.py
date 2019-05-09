import matplotlib.pyplot as plt
import numpy as np

# Setteo titulo del grafico
plt.title("Permutaciones")

# Indico cantidad de benchmarks y nombres
datapoints_number = 11
datapoints_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

# Armo listas con los tiempos de ejecucion de cada implementacion
tiempos_lista = []
tiempos_lista_ordenada = []
tiempos_arbol_abb = []

# Calculo la cantidad de posiciones en el eje x
index = np.arange(len(datapoints_names))

# Setteo las variables del grafico
bar_width = 0.2
opacity = 0.5

# Armo las barras de cada implementacion
barra_lista = plt.bar(index, tiempos_lista, bar_width,
                      alpha=0.7,
                      color="c",
                      label="Lista / Vector")

barra_lista_ordenada = plt.bar(index + bar_width, tiempos_lista_ordenada,
                               bar_width,
                               alpha=0.7,
                               color="b",
                               label="Lista / Vector\n ordenado")

barra_arbol_abb = plt.bar(index + 2 * bar_width, tiempos_arbol_abb,
                          bar_width,
                          alpha=0.7,
                          color="m",
                          label="Arbol ABB")

plt.grid(True, axis="y", linewidth=0.2)
plt.xlabel("Cantidad de Elementos")
plt.ylabel("Tiempo (segundos)")
plt.xticks(index + 2 * bar_width, datapoints_names)
plt.yticks(np.arange(0, 1, 0.001))
plt.legend()

plt.tight_layout()
plt.savefig("../../assets/images/permutaciones.png")
