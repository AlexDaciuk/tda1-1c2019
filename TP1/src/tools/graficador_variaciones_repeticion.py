import matplotlib.pyplot as plt

# Setteo titulo del grafico
plt.title("Variaciones con repeticion")
plt.style.use('seaborn-whitegrid')

plt.xlabel("Tamaño de vector.")
plt.ylabel("Segundos")

datapoints_names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

# Armo listas con los tiempos de ejecucion de cada implementacion
tiempos_lista = [9.53E-6, 2.33E-5, 3.21E-5,
                 9.29E-5, 0.0003, 0.0014, 0.005, 0.021, 0.08, 0.34]
tiempos_lista_ordenada = [9.53E-6, 1.37E-5, 3.12E-5,
                          0.000123, 0.000328, 0.001, 0.005, 0.02, 0.08, 0.34]
tiempos_arbol_abb = [1.26E-5, 1.78E-5, 3.60E-5,
                     0.0001, 0.0003, 0.0012, 0.0056, 0.020, 0.08, 0.34]

plt.plot(datapoints_names, tiempos_lista, '--g', label="Lista / Vector")
plt.plot(datapoints_names, tiempos_lista_ordenada,
         ':r', label="Lista / Vector Ordenado")
plt.plot(datapoints_names, tiempos_arbol_abb, '-.k', label="Arbol ABB")
plt.legend()

plt.tight_layout()
plt.savefig("../../assets/images/variaciones_con_repeticion.png")
