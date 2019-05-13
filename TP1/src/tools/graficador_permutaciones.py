import matplotlib.pyplot as plt

# Setteo titulo del grafico
plt.title("Permutaciones")
plt.style.use('seaborn-whitegrid')

plt.xlabel("Tamaño de vector.")
plt.ylabel("Segundos")

datapoints_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

# Armo listas con los tiempos de ejecucion de cada implementacion
tiempos_lista = [2.74E-6, 5.12E-6, 7.58E-6, 1.20E-5,
                 3.95E-5, 0.0001, 0.0009, 0.0064, 0.049, 0.45, 4.66]
tiempos_lista_ordenada = [3.33E-6, 7.10E-6, 9.10E-6, 1.52E-5,
                          4.42E-5, 0.0001, 0.0009, 0.0068, 0.052, 0.47, 4.62]
tiempos_arbol_abb = [4.52E-6, 8.34E-6, 1.62E-5,
                     0.0001, 0.0001, 0.0065, 0.055, 50.52]

plt.plot(datapoints_names, tiempos_lista, '--g', label="Lista / Vector")
plt.plot(datapoints_names, tiempos_lista_ordenada,
         ':r', label="Lista / Vector Ordenado")
plt.plot(datapoints_names[:8], tiempos_arbol_abb, '-.k', label="Arbol ABB")
plt.legend()

plt.tight_layout()
plt.savefig("../../assets/images/permutaciones.png")
