items = int(input("Number of Items: "))
while True:
    total = 0
    if items >= 0:
        for i in range(items):
            cost = float(input("Price of Item: $"))
            total = total + cost
        if total > 100:
            total = total * 0.9
        print("Total price for", items, "items is ${:.2f}".format(total))
        items = int(input("Number of Items: "))
    else:
        print("Invalid number of items! Please try again")
        items = int(input("Number of Items: "))