"""
Write a program that asks the user how many "quick
picks" they wish to generate. The program then generates
that many lines of output. Each line consists of 6 random
numbers between 1 and 45.
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


lines_of_output = int(input("How many quick picks? "))
for line in range(lines_of_output):
    quick_picks = []
    for i in range(NUMBERS_PER_LINE):
        quick_picks.append(random.randint(MIN_NUMBER, MAX_NUMBER))
        quick_picks.sort()
    print(' '.join(map(str, quick_picks)).format(quick_picks))
