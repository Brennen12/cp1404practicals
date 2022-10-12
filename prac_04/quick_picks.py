import random

number_of_quick_picks = int(input("How many quick picks would you like? "))

for n in range(number_of_quick_picks):
    for i in range(6):
        print(random.randint(1, 45), end=" ")
    print("")