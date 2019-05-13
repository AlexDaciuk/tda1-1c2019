import matplotlib.pyplot as plt

# Setteo titulo del grafico
plt.title("Variaciones sin repeticion")
plt.style.use('seaborn-whitegrid')

plt.xlabel("Tamaño de vector.")
plt.ylabel("Segundos")

datapoints_names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "100"]

# Armo listas con los tiempos de ejecucion de cada implementacion
tiempos_lista = [8.29E-6, 1.15E-5, 1.39E-5, 1.65E-5,
                 2.75E-5, 2.89E-5, 3.41E-5, 4.48E-5, 5.45E-5, 48.38]
tiempos_lista_ordenada = [9.20E-6, 1.31E-5, 1.52E-5, 1.81E-5,
                          3.02E-5, 5.95E-5, 0.00014, 0.00020, 0.00034, 51.09]

tiempos_arbol_abb = [1.15E-5, 1.62E-5, 2.24E-5, 3.30E-5,
                     3.04E-5, 6.70E-5, 0.0001, 0.0002, 0.0006, 51.63]

plt.plot(datapoints_names, tiempos_lista, '--g', label="Lista / Vector")
plt.plot(datapoints_names, tiempos_lista_ordenada,
         ':r', label="Lista / Vector Ordenado")
plt.plot(datapoints_names, tiempos_arbol_abb, '-.k', label="Arbol ABB")
plt.legend()

plt.tight_layout()
plt.savefig("../../assets/images/variaciones.png")
