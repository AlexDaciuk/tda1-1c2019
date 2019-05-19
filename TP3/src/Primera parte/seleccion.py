import sys

empire = sys.argv[1]
citys = sys.argv[2]
roads = sys.argv[3]




#cambiar cosas
def cargar_numeros(citys):  # O(n)
    file = open(file_path, "r")

    lines = file.readlines()

    for line in lines:
        number_tmp = line.rstrip()
        number_list.append(int(number_tmp))

    file.close()

# Temporal : O(1)
# Espacial : O(1)
def archivo_resultados(resultados):
    if empire == 1:
        file_path = "seleccion1.txt"
    elif empire == 2:
        file_path = "seleccion2.txt"
    file = open(file_path, 'w+')

    if isinstance(resultados, str):
        file.write(resultados)
    else:
        file.write(str(resultados))

    file.close()
    raise SystemExit


if __name__ == "__main__":
    leer_ciudades(citys)
    leer_rutas(roads)
 
    else:
        print("Argumentos invalidos")


    archivo_resultados(resultado)
