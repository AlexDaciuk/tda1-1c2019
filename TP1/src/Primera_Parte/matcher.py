#!/usr/bin/env python3
import sys

file_path = sys.argv[2]
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
        self.pref_list = []
        self.load_pref(pref_file)
        self.current_match = None

    def load_pref(self, pref_file):
        file = open(pref_file, "r")

        pref_lines = file.readlines()

        file.close()

        for pref in pref_lines:
            splitted_pref = pref.split(',')

            name_tmp = splitted_pref[0]
            pref_number = int(splitted_pref[1])

            self.pref_list.append([name_tmp, pref_number])

        self.pref_list.sort(key=lambda x: x[1])

    def eval_match_change(new_proposal):
        for player in self.pref_list:
            if player[0] == new_proposal:
                new_proposal_pref = player[1]
            elif (self.current_match is not None and
                  player[0] == self.current_match):
                current_match_pref = player[1]

        if new_proposal_pref > current_match_pref:
            self.current_match = new_proposal
            return True
        elif (new_proposal_pref == current_match_pref or
              new_proposal_pref < current_match_pref):
            return False


def matcher(best_10, worse_10):


def main():
    leer_archivo(file_path, players_quantity)


main()
