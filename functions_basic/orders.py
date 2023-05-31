product = input()
quantity = int(input())


def total_price(product_type):
    if product == "coffee":
        return "{:.2f}".format(quantity * 1.50)
    elif product == "water":
        return "{:.2f}".format(quantity * 1.00)
    elif product == "coke":
        return "{:.2f}".format(quantity * 1.40)
    elif product == "snacks":
        return "{:.2f}".format(quantity * 2.00)


print(total_price(quantity))


