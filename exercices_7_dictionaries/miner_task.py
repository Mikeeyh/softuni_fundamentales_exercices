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

# OR --------------------------------------------------------------------------

resources = {}

while True:
    current_resource = input()
    if current_resource == "stop":
        break

    current_quantity = int(input())

    if current_resource not in resources.keys():
        resources[current_resource] = 0
    resources[current_resource] += current_quantity

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
