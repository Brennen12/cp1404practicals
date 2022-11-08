from prac_06.guitar import Guitar


def main():
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013)
    print(f"{my_guitar.name} get_age() - Expected 100 Got {my_guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9 Got {another_guitar.get_age()}")
    print(f"{my_guitar.name} is_vintage() - Expected True Got {my_guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False Got {another_guitar.is_vintage()}")


main()
