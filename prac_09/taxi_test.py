from prac_09.taxi import Taxi


def main():
    my_taxi = Taxi("Prius", 100)
    my_taxi.drive(40)
    print(f"{my_taxi}, Current Fare = ${my_taxi.get_fare()}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, Current Fare = ${my_taxi.get_fare()}")


main()
