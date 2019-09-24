from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_new_guitar = Guitar(name, year, cost)
        guitars.append(add_new_guitar)
        print("{} added.".format(add_new_guitar))
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {} ({}), worth $ {:,.2f}{}".format(i, guitar.name, guitar.year, guitar.cost,
                                                             vintage_string))


main()
