names_of_the_gifts = input().split()
no_money = False
my_gifts = []

while True:
    command = input()

    if command == "No Money":
        break

    my_gifts.append(names_of_the_gifts)

    if command == "OutOfStock":
        pass
