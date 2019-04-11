#!/usr/bin/env python3
import sys

file_path = sys.argv[2]
players_quantity = sys.argv[1]

best_10 = []
worse_10 = []
matches = []


# Me pasan el con los jugadores por parametro

def leer_archivo(file_path, players_quantity):
    file = open(file_path, "r")

    lines = file.readlines()

    # Cada linea tiene la posicion en el ranking general del jugador
    # su nombre y el nombre del archivo de preferencias sobre los otros
    # jugadores

    for line in lines:
        # line =  rank,name,pref_file
        splitted_line = line.split(',')

        rank = int(splitted_line[0])
        name = splitted_line[1]
        pref_file = "../../assets/txt/" + splitted_line[2].rstrip()

        # Creo la instancia del jugador particular y le paso su propio archivo
        # de preferencias
        player_tmp = Players(name, pref_file)

        # Armo la lista de los mejores y peores 10
        if rank <= 10:
            best_10.append(player_tmp)
        else:
            worse_10.append(player_tmp)


class Players:
    # Cada jugador tiene un nombre, una lista de preferencias y
    # su pareja actual

    def __init__(self, name, pref_file):
        self.name = name
        self.pref_list = []
        self.load_pref(pref_file)
        self.current_match = None

    def load_pref(self, pref_file):
        file = open(pref_file, "r")

        pref_lines = file.readlines()

        file.close()

        for pref in pref_lines:
            splitted_pref = pref.split(',')

            # Cada linea es del estilo => nombre,preferencia
            name_tmp = splitted_pref[0]
            pref_number = int(splitted_pref[1])

            # Cargo cada preferencia como una lista del estilo
            # [nombre, preferencia], por ende pref_list es una lista
            # con sublistas de preferencias
            self.pref_list.append([name_tmp, pref_number])

    def eval_match_change(self, new_proposal):
        # Inicializo current_match_pref en 0, por si no tiene una pareja
        current_match_pref = 0

        # Busco la preferencia del match actual y del nuevo propuesto
        # en la lista de preferencias
        for player in self.pref_list:
            if player[0] == new_proposal:
                new_proposal_pref = player[1]
            elif (self.current_match is not None
                  and player[0] == self.current_match):
                current_match_pref = player[1]

        # Solo actualizo la pareaja si la nueva propuesta tiene preferencia
        # estrictamente mayor que la actual
        if new_proposal_pref > current_match_pref:
            self.current_match = new_proposal
            return True
        elif (new_proposal_pref == current_match_pref
              or new_proposal_pref < current_match_pref):
            return False


def matcher(best_10, worse_10):
    None


def main():
    leer_archivo(file_path, players_quantity)


main()
