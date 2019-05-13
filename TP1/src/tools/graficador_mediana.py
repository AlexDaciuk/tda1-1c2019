import matplotlib.pyplot as plt

# Setteo titulo del grafico
plt.title("Mediana")
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
tiempos_lista = [2.83E-6, 3.95E-6, 9.96E-6, 8.18E-5, 0.001, 0.013, 0.219, 3.37]
tiempos_lista_ordenada = [2.43E-6, 3.43E-6, 4.14E-6,
                          3.91E-6, 4.86E-6, 1.06E-5, 1.01E-5,  1.13E-5]
tiempos_arbol_abb = [3.81E-6, 1.18E-5,
                     6.38E-5, 0.0006, 0.008, 0.097, 0.99, 10.86]

plt.plot(datapoints_names, tiempos_lista, '--g', label="Lista / Vector")
plt.plot(datapoints_names, tiempos_lista_ordenada,
         ':r', label="Lista / Vector Ordenado")
plt.plot(datapoints_names, tiempos_arbol_abb, '-.k', label="Arbol ABB")
plt.legend()
plt.tight_layout()
plt.savefig("../../assets/images/mediana.png")
