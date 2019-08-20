# Problem 1
name_file = open('name.txt', 'w')
name = input("Enter name: ")
print(name, file=name_file)
name_file.close()

# Problem 2
name_file = open('name.txt', 'r')
name = name_file.read()
print("Your name is", name)
name_file.close()

# Problem 3
number_file = open('numbers.txt', 'r')
number1 = int(number_file.readline())
number2 = int(number_file.readline())
print(number1 + number2)
number_file.close()

# Problem 4
total = 0
number_file = open('numbers.txt', 'r')
for line in number_file:
    line = int(line)
    total += line
print(total)
number_file.close()


