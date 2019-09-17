from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    print(guitar)


main()
