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

best_10 = [None] * 10
worse_10 = [None] * 10

for number_tmp in numbers:
    # Elijo un nombre random, se va a usar para el ranking principal
    player_tmp = random.choice(players_mod)

    if number_tmp < 11:
        best_10[number_tmp - 1] = player_tmp
    else:
        worse_10[number_tmp - 11] = player_tmp

    # Mezclo los numeros para crear las preferencias aleatorias
    # Elimino el numero propio del jugador en cuestion, ya que nunca
    # se podria elegir a si mismo
    numbers_shuffled = list(range(1, 20, 1))
    random.shuffle(numbers_shuffled)

    pref_file_tmp = "jugador_" + str(number_tmp) + ".pref"

    player_string = str(number_tmp) + "," + player_tmp + \
        "," + pref_file_tmp + "\n"

    players_mod.remove(player_tmp)

    file.write(player_string)

file.close()

worse_10_copia = list(worse_10)
worse_10_copia.sort()

for player in best_10:
    pref_file_tmp = "jugador_" + str(best_10.index(player) + 1) + ".pref"

    # Abro el archivo
    pref_file = open("../../assets/txt/" + pref_file_tmp, "w+")

    numbers = list(range(1, 21, 1)) * 4
    random.shuffle(numbers)

    for player_w in worse_10_copia:
        pref_jug_tmp = player_w + "," + str(numbers.pop()) + "\n"
        pref_file.write(pref_jug_tmp)

    pref_file.close()


best_10_copia = list(best_10)
best_10_copia.sort()

for player in worse_10:
    pref_file_tmp = "jugador_" + str(worse_10.index(player) + 11) + ".pref"

    print("Entre a worse 10")

    # Abro el archivo
    pref_file = open("../../assets/txt/" + pref_file_tmp, "w+")

    numbers = list(range(1, 21, 1)) * 4
    random.shuffle(numbers)

    for player_w in best_10_copia:
        pref_jug_tmp = player_w + "," + str(numbers.pop()) + "\n"
        pref_file.write(pref_jug_tmp)

    pref_file.close()
