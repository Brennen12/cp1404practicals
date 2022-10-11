def main():
    numbers = get_numbers()
    process_numbers(numbers)


def process_numbers(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average or the numbers is {sum(numbers)/5}")


def get_numbers():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Number: ")))
    print(numbers)
    return numbers


main()

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
