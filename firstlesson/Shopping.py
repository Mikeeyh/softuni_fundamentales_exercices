budget = int(input())
total_price = 0

while True:
    product_price = input()

    if product_price == 'End':
        print(f"You bought everything needed.")
        break

    product_price = int(product_price)      #or price = int(product_price)

    total_price += product_price            #or total_price += price

    if budget < total_price:
        print(f"You went in overdraft!")
        break

