PASSWORD_MIN_LENGTH = 6


def main():
    password = get_password()
    while len(password) < PASSWORD_MIN_LENGTH:
        print(f"Password doesn't meet minimum length of {PASSWORD_MIN_LENGTH}")
        password = input("Enter a password at least 6 characters long: ")

    display_asterisks(password)


def display_asterisks(password):
    for char in password:
        print("*", end="")


def get_password():
    password = input("Enter a password at least 6 characters long: ")
    return password


main()
