"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = get_score()
    if score < 0:
        print("Invalid score")
    elif score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def get_score():
    score = float(input("Enter score: "))
    return score


main()
