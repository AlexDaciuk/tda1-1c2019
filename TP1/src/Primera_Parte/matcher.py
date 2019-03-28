#!/usr/bin/env python3
import sys

file_path = "../../assets/txt/" + sys.argv[2]
players_quantity = sys.argv[1]

best_10 = []
worse_10 = []
matches = []


def leer_archivo(file_path, players_quantity):
    file = open(file_path, "r")

    lines = file.readlines()

    for line in lines:
        splitted_line = line.split(',')

        rank = int(splitted_line[0])
        name = splitted_line[1]
        pref_file = "../../assets/txt/" + splitted_line[2].rstrip()

        player_tmp = Players(name, pref_file)

        if rank <= 10:
            best_10.append(player_tmp)
        else:
            worse_10.append(player_tmp)


class Players:
    def __init__(self, name, pref_file):
        self.name = name
        self.pref_list = [None] * 19
        self.load_pref(pref_file)

    def load_pref(self, pref_file):
        file = open(pref_file, "r")

        pref_lines = file.readlines()

        file.close()

        for pref in pref_lines:
            splitted_pref = pref.split(',')

            name_tmp = splitted_pref[0]
            pref_number = int(splitted_pref[1])

            self.pref_list[pref_number - 1] = name_tmp


def main():
    leer_archivo(file_path, players_quantity)


main()
