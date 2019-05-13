import matplotlib.pyplot as plt

# Setteo titulo del grafico
plt.title("Maximo")
plt.style.use('seaborn-whitegrid')

plt.xlabel("Tamaño de vector.")
plt.ylabel("Segundos")

datapoints_names = ["1",
                    "10",
                    "100",
                    "1000",
                    "10 000",
                    "100 000",
                    "1 000 000",
                    "10 000 000"]

# Armo listas con los tiempos de ejecucion de cada implementacion
tiempos_lista = [1.40E-6, 1.81E-6, 3.76E-6,
                 2.32E-5, 0.0002, 0.002, 0.020, 0.200]
tiempos_lista_ordenada = [1.54E-6, 1.50E-6, 1.78E-6,
                          1.71E-6, 3.74E-6, 5.53E-6, 5.53E-6, 5.92E-6]
tiempos_arbol_abb = [1.57E-6, 1.62E-6, 1.85E-6,
                     3.17E-6, 4.98E-6, 9.22E-6, 1.05E-5, 1.28E-5]

plt.plot(datapoints_names, tiempos_lista, 'g', label="Lista / Vector")
plt.plot(datapoints_names, tiempos_lista_ordenada,
         ':r', label="Lista / Vector ordenado")
plt.plot(datapoints_names, tiempos_arbol_abb, '-.k', label="Arbol ABB")
plt.legend()

plt.tight_layout()
plt.savefig("../../assets/images/maximo.png")
