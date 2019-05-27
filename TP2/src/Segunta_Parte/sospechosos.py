#!/usr/bin/env python3
import sys
from pathlib import Path

file_path = sys.argv[1]

planilla = []


class Entrada:
    def __init__(self, line):
        entrada_tmp = line.split(",")

        self.nombre = entrada_tmp[0]
        self.horario_entrada = int(entrada_tmp[1])
        self.tiempo_estadia = int(entrada_tmp[2].rstrip())
        self.horario_salida = self.horario_entrada + self.tiempo_estadia

    def mostrar(self):
        print(
            self.nombre + ","
            + str(self.horario_entrada)
            + "," + str(self.tiempo_estadia)
            + "," + str(self.horario_salida)
        )


def cargar_planilla(file):
    datos = []

    file = open(Path(file_path), "r")

    lines = file.readlines()

    for line in lines:
        datos.append(Entrada(line))

    return datos


class ListaSospechosos:
    def __init__(self, primer_sospechoso):
        self.lista_sospechosos = []
        self.primer_entrada = primer_sospechoso.horario_entrada
        self.lista_sospechosos.append(primer_sospechoso)
        self.primer_salida = primer_sospechoso.horario_salida
        self.ultima_salida = primer_sospechoso.horario_salida

    def agregar_sospechoso(self, sospechoso):
        if sospechoso not in self.lista_sospechosos:
            self.lista_sospechosos.append(sospechoso)

        if sospechoso.horario_salida < self.primer_salida:
            self.primero_salir = sospechoso.horario_salida
        elif sospechoso.horario_salida > self.ultima_salida:
            self.ultima_salida = sospechoso.horario_salida

    def califica(self, sospechoso):
        # Chequeo que haya entrado en los 120 minutos de la ventana de la lista
        if sospechoso.horario_entrada - self.primer_entrada > 120 \
                and sospechoso.tiempo_estadia <= 120:
            return False

        # Chequeo que el que voy a agregar, estuvo en algun momento con todo el
        # grupo de sospechosos
        # Caso 1 : entrada posterior a X persona de la lista, la entrada del
        # nuevo sospechoso tiene que ser anterior a la hora de salida de X
        # Caso 2 : la entrada es a la misma hora que la del sospechoso X,
        # cumple, ya que no existen estadias de 0 minutos
        for actual_sospechoso in self.lista_sospechosos:
            if actual_sospechoso.horario_salida < sospechoso.horario_entrada:
                return False

        return True

    def largo(self):
        return len(self.lista_sospechosos)

    def mostrar(self):
        print("Lista de sospechosos : ")
        for sospechoso in self.lista_sospechosos:
            print(sospechoso.nombre)

    def tiempo_total(self):
        return self.ultima_salida - self.primer_entrada


class ArmadorListas:
    def __init__(self, planilla):
        self.planilla = planilla
        self.listas = []
        # Creo la primera listas trivial con la primera persona que ingresa
        self.listas.append(ListaSospechosos(planilla[0]))
        # Saco a esa persona asi no lo tomo 2 veces
        self.planilla = self.planilla[1:]

    def largo_valido(self, lista):
        if lista.largo() >= 5 and lista.largo() <= 10:
            return True
        else:
            return False

    def tiempo_valido(self, lista):
        if lista.tiempo_total() >= 40 and lista.tiempo_total() <= 120:
            return True
        else:
            return False

    def armar_listas(self):
        for entrada in self.planilla:
            for lista in self.listas:
                if lista.califica(entrada):
                    lista.agregar_sospechoso(entrada)
                else:
                    self.listas.append(ListaSospechosos(entrada))

        self.definitiva = []

        for lista in self.listas:
            lista.mostrar()
            print("Mi tiempo total es de :" + str(lista.tiempo_total()))
            print(lista.primer_entrada)
            print(lista.ultima_salida)
            if self.largo_valido(lista) and self.tiempo_valido(lista):
                # print("Entre")
                self.definitiva.append(lista)

        return self.definitiva


if __name__ == "__main__":
    planilla = cargar_planilla(file_path)

    for entrada in planilla:
        entrada.mostrar()

    if len(planilla) > 0:
        armador = ArmadorListas(planilla)
        listas = armador.armar_listas()
        print("-------------------------------")
        for lista in listas:
            lista.mostrar()
