from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Hummer", 200, 2)
    my_taxi.drive(18)
    print(f"{my_taxi}, Current Fare = ${my_taxi.get_fare():.2f}")


main()
