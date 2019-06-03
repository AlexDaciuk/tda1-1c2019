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
        self.lista_sospechosos.append(primer_sospechoso)
        self.primer_entrada = primer_sospechoso.horario_entrada
        self.primer_salida = primer_sospechoso.horario_salida
        self.ultima_salida = primer_sospechoso.horario_salida

    def agregar_sospechoso(self, sospechoso):
        if sospechoso not in self.lista_sospechosos:
            self.lista_sospechosos.append(sospechoso)

        if sospechoso.horario_salida < self.primer_salida:
            self.primer_salida = sospechoso.horario_salida
        elif sospechoso.horario_salida > self.ultima_salida:
            self.ultima_salida = sospechoso.horario_salida

    def califica(self, nuevo_sospechoso):
        # Chequeo que haya entrado en los 120 minutos de la ventana de la lista
        if nuevo_sospechoso.horario_entrada - self.primer_entrada > 120 \
                and nuevo_sospechoso.tiempo_estadia <= 120:
            return False

        # Chequeo que el que voy a agregar, estuvo en algun momento con todo el
        # grupo de sospechosos
        # Caso 1 : entrada posterior a X persona de la lista, la entrada del
        # nuevo sospechoso tiene que ser anterior a la hora de salida de X
        # Caso 2 : la entrada es a la misma hora que la del sospechoso X,
        # cumple, ya que no existen estadias de 0 minutos
        for actual_sospechoso in self.lista_sospechosos:
            if actual_sospechoso.horario_salida <=\
                    nuevo_sospechoso.horario_entrada:
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

    def primer_sospechoso(self):
        return self.lista_sospechosos[0]

    def obtener_sospechosos(self):
        return self.lista_sospechosos


class ArmadorListas:
    def __init__(self, planilla):
        self.planilla = planilla
        self.listas = []

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

    def validar_escape(self, lista, planilla):
        planilla_tmp = [sospechoso
                        for sospechoso in planilla if sospechoso
                        not in lista.obtener_sospechosos()]

        # Tengo 2 casos
        # Caso 1 : Persona que entro y salio antes de que salga el sospechoso
        # con el botin
        # Caso 2 : Persona que entro y salio despues de que salga el sospechoso
        # con el botin
        # Entonces si el horario de entrada es menor al horario de
        # primera salida y el horario de salida es mayor al horario de primera
        # salida, el escape es invalido
        # Tomo como valido el caso que la salida del primer sospechoso de una
        # lista sea en el mismo momento que la entrada de una persona que no
        # pertenece al grupo
        for sospechoso in planilla_tmp:
            if sospechoso.horario_entrada < lista.primer_salida and \
                    sospechoso.horario_salida > lista.primer_salida:
                return False

        return True

    def armar_listas(self):
        # Armo una lista por cada sospechoso en la planilla de 1 a n - 4
        for sospechoso in planilla[:len(planilla) - 4]:
            self.listas.append(ListaSospechosos(sospechoso))

        # Recorro cada lista de sospechosos y busco mas sospechosos en la
        # planilla, pero solo desde el primer sospechoso de la lista en
        # adelante
        for lista in self.listas:
            posicion = planilla.index(lista.primer_sospechoso())
            for sospechoso in planilla[posicion:]:
                if lista.califica(sospechoso):
                    lista.agregar_sospechoso(sospechoso)

        self.definitiva = []

        # Chequeo condiciones, largo de lista, tiempo total de duracion
        # y que no haya personas ajenas a la banda cuando se retira la persona
        # con el botin
        for lista in self.listas:
            largo_valido = self.largo_valido(lista)
            tiempo_valido = self.tiempo_valido(lista)
            escape_valido = self.validar_escape(lista, self.planilla)
            if largo_valido and tiempo_valido and escape_valido:
                self.definitiva.append(lista)

        return self.definitiva


if __name__ == "__main__":
    # Cargo la planilla
    planilla = cargar_planilla(file_path)

    # Armo las listas de sospechosos
    armador = ArmadorListas(planilla)
    listas = armador.armar_listas()

    # Guardo el archivo
    file_path = "sospechosos.txt"
    file = open(Path(file_path), 'w+')

    if len(listas) > 0:
        file.write("La/s lista/s de sospechosos es/son: ")
        for lista in listas:
            file.write("\n")
            for sospechoso in lista.obtener_sospechosos():
                file.write(sospechoso.nombre + "_"
                           + str(sospechoso.tiempo_estadia) + ",")
    else:
        file.write("No hay sospechosos")

    file.close()
