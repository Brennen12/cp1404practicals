def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    names_from_email = str(email.split("@").pop(0)).split(".")

    full_name = []
    for names in names_from_email:
        full_name.append(names.lower().title())
    full_name = " ".join(full_name)
    correct_name = check_correct_name(full_name)
    return correct_name


def check_correct_name(full_name):
    is_correct = input(f"Is your name {full_name}? (Y/N) ")
    if is_correct.lower() == "y" or is_correct == "":
        correct_name = full_name
    else:
        correct_name = input("Name: ")
    return correct_name


main()
