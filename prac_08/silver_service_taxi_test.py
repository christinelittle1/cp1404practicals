from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    new_silver_service_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    new_silver_service_taxi.drive(18)
    print(new_silver_service_taxi)
    # Without round()
    # print("get_fare() - Expected: $48.78. Got: ${:.2f}".format(new_silver_service_taxi.get_fare()))

    # With round()
    print("get_fare() - Expected: $48.80. Got: ${:.2f}".format(new_silver_service_taxi.get_fare()))


main()
