from prac_08.taxi import Taxi


def main():
    # 1.
    new_taxi = Taxi("Prius 1", 100, 1.23)
    # 2.
    new_taxi.drive(40)
    # 3.
    print(new_taxi)
    print("current fare = ${}".format(new_taxi.get_fare()))
    # 4.
    new_taxi.start_fare()
    new_taxi.drive(100)
    # 5.
    print(new_taxi)
    print("current fare = ${}".format(new_taxi.get_fare()))


main()
