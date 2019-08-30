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
        quick_pick = random.randint(MIN_NUMBER, MAX_NUMBER)
        while quick_pick in quick_picks:
            quick_pick = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_picks.append(quick_pick)
    quick_picks.sort()
    print(" ".join("{:2}".format(quick_pick) for quick_pick in quick_picks))
