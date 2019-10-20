from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0.00
    current_taxi = None
    print("Let's Drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_number = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_number]
        elif choice == "d":
            if current_taxi is None:
                print("Choose a taxi first :)")
            else:
                current_taxi.start_fare()
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare))
                bill += fare
        else:
            print("Invalid choice")
        print("Bill to date: ${:.2f}".format(bill))
        print(MENU)
        choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
