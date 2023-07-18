stock = {}
command = input()

while True:
    if command == "stop":
        break

    element_type = command
    quantity = int(input())

    if element_type not in stock:
        stock[element_type] = 0
    stock[element_type] += quantity

    command = input()

for resource, quantity_of_the_given_resource in stock.items():
    print(f"{resource} -> {quantity_of_the_given_resource}")
