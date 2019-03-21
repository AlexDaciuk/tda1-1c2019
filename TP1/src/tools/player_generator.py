import random


players = ["Juan", "Jose", "Ana", "Helena", "Martin", "Virginia", "Julia",
           "Matias", "Luis", "Veronica", "Daniel", "Lucia", "Lucas", "Marina",
           "Ariel", "Valeria", "Ezequiel", "Florencia", "Damian", "Romina"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
           "14", "15", "16", "17", "18", "19", "20"]

file = open("../../assets/txt/20_jugadores.rank", "w+")

# Ordeno el array alfabeticamente
players.sort()

for name in players:

    number_tmp = random.choice(numbers)

    pref_file_tmp = "jugador_" + number_tmp + ".pref"

    player_string = number_tmp + "," + name + "," + pref_file_tmp + "\n"

    numbers.remove(number_tmp)

    file.write(player_string)

file.close()
