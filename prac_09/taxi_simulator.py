from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                bill_to_date += trip_cost
                print(f"Bill to date: ${bill_to_date:.2f}")
        elif choice == "C":
            current_taxi = choose_taxi(taxis)
            bill_to_date
            print(f"Bill to date: ${bill_to_date:.2f}")
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    taxi_choice = int(input("Choose taxi: "))
    if taxi_choice >= len(taxis):
        print("Invalid taxi choice")

    else:
        return taxis[taxi_choice]


main()
