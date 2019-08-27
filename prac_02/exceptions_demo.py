"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError occurs if either the numerator or the denominator is not
    an integer, so if the input contains a letter, special character or
    is a decimal number.
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError occurs if the denominator input
    is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Probably but not sure how to do this...
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
