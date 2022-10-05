MENU = """(H)ello
(G)oodbye
(Q)uit"""

name = input("Enter Name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished")