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
tiempos_lista = [1.88E-6, 2.38E-6, 5.88E-6,
                 3.19E-6, 0.0003, 0.0032, 0.033, 0.334]
tiempos_lista_ordenada = [2.31E-6, 3.29E-6,
                          6.03E-6, 3.69E-5, 0.0002, 0.006, 0.100, 1.31]
tiempos_arbol_abb = [4.55E-6, 1.13E-5, 6.48E-5,
                     0.00064, 0.0079, 0.114, 1.20, 13.28]

plt.plot(datapoints_names, tiempos_lista, '--g', label="Lista / Vector")
plt.plot(datapoints_names, tiempos_lista_ordenada,
         ':r', label="Lista / Vector Ordenado")
plt.plot(datapoints_names, tiempos_arbol_abb, '-.k', label="Arbol ABB")
plt.legend()


plt.tight_layout()
plt.savefig("../../assets/images/media.png")
