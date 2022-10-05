"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



score = float(input("Enter score: "))

if 0 <= score <= 100:
    if score >= 90:
        print("Excellent")
    elif 50 <= score < 90:
        print("Passable")
    else:
        print("Bad")
else:
    print("Invalid")
print("The end")