products = input().split('!')
command = input()

while command != 'Go Shopping!':
    command = command.split()
    action = command[0]

    if action == 'Urgent':
        product = command[1]
        if product not in products:
            products.insert(0, product)

    elif action == 'Unnecessary':
        product = command[1]
        if product in products:
            products.remove(product)

    elif action == 'Correct':
        product = command[1]
        new_product = command[2]
        if product in products:
            index = products.index(product)
            products.pop(index)
            products.insert(index, new_product)

    elif action == 'Rearrange':
        product = command[1]
        if product in products:
            products.remove(product)
            products.append(product)

    command = input()

print(', '.join(products))
