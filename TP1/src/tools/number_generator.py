#!/usr/bin/env python3
import random
import sys
from pathlib import Path

n = int(sys.argv[1])

number_list = random.sample(range(1, n + 1), n)

file_path = "../../assets/txt/numbers.txt"

file = open(Path(file_path), 'w+')

for number in number_list:
    line_to_file = str(number) + "\n"
    file.write(line_to_file)

file.close()
