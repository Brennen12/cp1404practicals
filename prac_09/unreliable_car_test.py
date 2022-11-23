from prac_09.unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("Toyota", 150, 50)
    my_car.drive(40)
    print(f"{my_car}")


main()
