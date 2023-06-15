command = input()
taxes = 0
total_price = 0
total_price_with_taxes = 0
special = False

while True:
    if command == 'special':
        special = True
        break
    if command == 'regular':
        break

    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        taxes += price * 0.20
        total_price += price

    command = input()

total_price_with_taxes = total_price + taxes
if special:
    total_price_with_taxes *= 0.90

if not total_price_with_taxes == 0:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")
else:
    print("Invalid order!")



