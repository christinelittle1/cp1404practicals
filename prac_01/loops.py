for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in reversed(range(1, 21, 1)):
    print(i, end=' ')
print()

"""
Ask the user for a number, 
then print that many stars (*), 
all on one line
"""

n = int(input("Number: "))
for i in range(n):
    print("*", end=' ')
print()

for i in range(n):
    for j in range(i + 1):
        print("*", end=' ')
    print("\r")
