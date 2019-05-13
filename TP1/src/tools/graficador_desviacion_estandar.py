import matplotlib.pyplot as plt

# Setteo titulo del grafico
plt.title("Desviacion Estandar")
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
tiempos_lista = [6.96E-6, 9.27E-6, 2.76E-5,
                 0.0001, 0.0014, 0.0139, 0.138, 1.407]
tiempos_lista_ordenada = [1.16E-5, 9.67E-6,
                          2.67E-5, 0.0001, 0.0012, 0.020, 0.266, 2.85]
tiempos_arbol_abb = [1.37E-5, 2.37E-5,
                     0.0002, 0.0010, 0.013, 0.183, 1.87, 20.77]

plt.plot(datapoints_names, tiempos_lista, '--g', label="Lista / Vector")
plt.plot(datapoints_names, tiempos_lista_ordenada,
         ':r', label="Lista / Vector Ordenado")
plt.plot(datapoints_names, tiempos_arbol_abb, '-.k', label="Arbol ABB")
plt.legend()

plt.tight_layout()
plt.savefig("../../assets/images/desviacion_estandar.png")
