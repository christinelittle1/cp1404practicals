from prac_08.unreliable_car import UnreliableCar


def main():
    new_unreliable_car = UnreliableCar("Fred", 150, 50)
    new_unreliable_car.drive(40)
    print(new_unreliable_car)
    new_unreliable_car.drive(80)
    print(new_unreliable_car)


main()
