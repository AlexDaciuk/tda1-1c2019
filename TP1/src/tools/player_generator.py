#!/usr/bin/env python3

import random


players = ["Juan", "Jose", "Ana", "Helena", "Martin", "Virginia", "Julia",
           "Matias", "Luis", "Veronica", "Daniel", "Lucia", "Lucas", "Marina",
           "Ariel", "Valeria", "Ezequiel", "Florencia", "Damian", "Romina"]

numbers = list(range(1, 21, 1))

players_mod = list(players)

file = open("../../assets/txt/20_jugadores.rank", "w+")

# Ordeno el array alfabeticamente
players.sort()

for number_tmp in numbers:

    # Elijo un nombre random, se va a usar para el ranking principal
    player_tmp = random.choice(players_mod)

    # Mezclo los numeros para crear las preferencias aleatorias
    # Elimino el numero propio del jugador en cuestion, ya que nunca
    # se podria elegir a si mismo
    numbers_shuffled = list(range(1, 20, 1))
    random.shuffle(numbers_shuffled)

    pref_file_tmp = "jugador_" + str(number_tmp) + ".pref"

    # Abro el archivo
    pref_file = open("../../assets/txt/" + pref_file_tmp, "w+")

    for name2 in players:
        if name2 != player_tmp:
            pref_jug_tmp = name2 + "," + str(numbers_shuffled.pop()) + "\n"
            pref_file.write(pref_jug_tmp)

    # Cierro el archivo de preferencias del jugador number_tmp
    pref_file.close()

    player_string = str(number_tmp) + "," + player_tmp + \
        "," + pref_file_tmp + "\n"

    players_mod.remove(player_tmp)

    file.write(player_string)

file.close()
