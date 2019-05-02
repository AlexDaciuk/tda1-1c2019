#!/usr/bin/env python3
import sys

file_path = sys.argv[1]

planilla = []


def cargar_planilla(file_path):
    file = open(file_path, "r")

    lines = file.readlines()

    for line in lines:
        persona_tmp = line.split(",")
        persona_tmp[1] = int(persona_tmp[1])
        persona_tmp[2] = int(persona_tmp[2].rstrip())

        planilla.append(persona_tmp)


def buscar_sospechosos(planilla):
    None


if __name__ == "__main__":
    cargar_planilla(file_path)

    buscar_sospechosos(planilla)

    print(planilla)
