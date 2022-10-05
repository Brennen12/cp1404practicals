def main():
    write_name_to_file()
    read_name_from_file()
    read_some_numbers_from_file()
    read_all_numbers_from_file()


def write_name_to_file():
    user_name = input("What is your name? ")
    out_file = open("name.txt", "w")
    print(user_name, file=out_file)
    out_file.close()


def read_name_from_file():
    in_file = open("name.txt", "r")
    user_name = in_file.read()
    in_file.close()
    print(f"Your name is {user_name}")


def read_some_numbers_from_file():
    in_file = open("numbers.txt", "r")
    text = in_file.readlines(3)
    line_one = int(text[0])
    line_two = int(text[1])
    number_sum = line_one + line_two
    print(f"{number_sum}")
    in_file.close()


def read_all_numbers_from_file():
    in_file = open("numbers.txt", "r")
    total = 0
    for line in in_file:
        number = int(line)
        total = total + number
    print(total)
    in_file.close()


main()
