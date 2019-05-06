#!/usr/bin/env python3
import sys

file_path = sys.argv[1]

planilla = []


def cargar_planilla(file_path):
    file = open(file_path, "r")

    lines = file.readlines()

    for line in lines:
        persona_tmp = line.split(",")
        persona_tmp[1] = [persona_tmp[1][:2], persona_tmp[1][2:]]
        persona_tmp[2] = int(persona_tmp[2].rstrip())

        planilla.append(persona_tmp)


def pasar_a_minutos(hora_sospechoso, hora_lista):
    hora_tmp = [int(hora_sospechoso[0]) - int(hora_lista[0]),
                int(hora_sospechoso[1]) - int(hora_lista[1])]

    minutos = hora_tmp[0] * 60 + hora_tmp[1]

    return minutos


def validar_hora(hora_sospechoso, hora_lista):
    diff_sospechoso_min = pasar_a_minutos(hora_sospechoso, hora_lista)

    if int(diff_sospechoso_min) < 120:
        return True


def buscar_sospechosos(planilla):
    lista_tmp = []
    sospechosos = []

    planilla_copia = list(planilla)

    # Agrego la primera persona que entro como sospechosa
    # asi como la hora de ingreso, para que sea mas facil chequear que esta
    # en el timeframe
    # Formato [hora_primer_soospechoso, sospechoso_1 , ... , sospechoso_n]

    lista_tmp.append([planilla[0][1], planilla[0][0]])

    planilla_copia.remove(planilla[0])

    for persona in planilla_copia:
        for lista in lista_tmp:
            if validar_hora(persona[1], lista[0]):
                lista.append(persona[0])
            else:
                lista_tmp.append([persona[0], persona[1]])

    for lista in lista_tmp:
        lista[0] = str(lista[0][0]) + ":" + str(lista[0][1])
        lista = list(dict.fromkeys(lista))
        sospechosos.append(lista)

    return sospechosos


if __name__ == "__main__":
    cargar_planilla(file_path)

    print(planilla)

    print("Las listas de sospechosos son : ")
    print(buscar_sospechosos(planilla))
