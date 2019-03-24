#!/usr/bin/env python3

import random


players = ["Juan", "Jose", "Ana", "Helena", "Martin", "Virginia", "Julia",
           "Matias", "Luis", "Veronica", "Daniel", "Lucia", "Lucas", "Marina",
           "Ariel", "Valeria", "Ezequiel", "Florencia", "Damian", "Romina"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
           "14", "15", "16", "17", "18", "19", "20"]

numbers_mod = list(numbers)
numbers_shuffled = list(numbers)

file = open("../../assets/txt/20_jugadores.rank", "w+")

# Ordeno el array alfabeticamente
players.sort()

for name in players:

    # Elijo un numero random, se va a usar para el ranking principal
    number_tmp = random.choice(numbers_mod)

    # Mezclo los numeros para crear las preferencias aleatorias
    # Elimino el numero propio del jugador en cuestion, ya que nunca
    # se podria elegir a si mismo
    numbers_shuffled = list(numbers)
    random.shuffle(numbers_shuffled)
    numbers_shuffled.remove(number_tmp)

    pref_file_tmp = "jugador_" + number_tmp + ".pref"

    # Abro el archivo
    pref_file = open("../../assets/txt/" + pref_file_tmp, "w+")

    for name2 in players:
        if name2 != name:
            pref_jug_tmp = name2 + "," + numbers_shuffled.pop() + "\n"
            pref_file.write(pref_jug_tmp)

    # Cierro el archivo de preferencias del jugador number_tmp
    pref_file.close()

    player_string = number_tmp + "," + name + "," + pref_file_tmp + "\n"

    print(numbers)
    print(numbers_mod)

    numbers_mod.remove(number_tmp)

    file.write(player_string)

file.close()
