for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input("Number of Stars: "))
for i in range(stars):
    print("*", end='')
print()

n = 0
for i in range(stars):
    n = n + 1
    for j in range(n):
        print("*", end='')
    print()