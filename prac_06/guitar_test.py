from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012, 0)
    print(gibson)

    print(gibson.get_age())
    print(another_guitar.get_age())

    print(gibson.is_vintage())
    print(another_guitar.is_vintage())


main()
