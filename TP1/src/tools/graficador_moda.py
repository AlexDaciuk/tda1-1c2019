import matplotlib.pyplot as plt

# Setteo titulo del grafico
plt.title("Moda")
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
tiempos_lista = [2.90E-6, 3.88E-6, 1.58E-5, 0.0001, 0.0012, 0.011, 0.114, 1.13]
tiempos_lista_ordenada = [2.86E-6, 3.57E-6,
                          1.50E-5, 0.0001, 0.0012, 0.015, 0.19, 2.04]
tiempos_arbol_abb = [3.67E-6, 8.44E-6,
                     5.51E-6, 0.0005, 0.0069, 0.084, 0.85, 9.41]

plt.plot(datapoints_names, tiempos_lista, '--g', label="Vector / Lista")
plt.plot(datapoints_names, tiempos_lista_ordenada,
         ':r', label="Vector / Lista Ordenada")
plt.plot(datapoints_names, tiempos_arbol_abb, '-.k', label="Arbol ABB")
plt.legend()

plt.tight_layout()
plt.savefig("../../assets/images/moda.png")
