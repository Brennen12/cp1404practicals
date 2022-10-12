import random

number_of_quick_picks = int(input("How many quick picks? "))

for n in range(number_of_quick_picks):
    quick_pick_numbers = []
    for i in range(6):
        print("{:2}".format(random.randint(1, 45)), end=" ")
    print("")
