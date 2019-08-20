total = 0

number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))

for i in range(0, number):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    discount = total - (total * 0.1)
    print("Total price for", number, "items is ${:.2f}".format(discount))
else:
    print("Total price for", number, "items is ${:.2f}".format(total))
