
x = int(input("Pick first number: "))
y = int(input("Pick second number: "))

while x < y:
    for i in range(x, y):
        remainder = i % 2

print("Even numbers: ")
print("Odd numbers: ")
print("Squares: ")
