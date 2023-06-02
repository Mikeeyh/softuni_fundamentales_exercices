items = input().split("|")
budget = float(input())
sell_prices = []
profit = 0
total_sell_products = 0

train_ticket = 150
CLOTHES_MAX_PRICE = 50.00
SHOES_MAX_PRICE = 35.00
ACCESSORIES_MAX_PRICE = 20.50

for item in items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)
    item_price_is_valid = False

    if item_type == "Clothes":
        if item_price <= CLOTHES_MAX_PRICE:
            item_price_is_valid = True
    elif item_type == "Shoes":
        if item_price <= SHOES_MAX_PRICE:
            item_price_is_valid = True
    elif item_type == "Accessories":
        if item_price <= ACCESSORIES_MAX_PRICE:
            item_price_is_valid = True

    if item_price_is_valid:
        if budget >= item_price:
            budget -= item_price
            sell_price = item_price * 1.40
            profit += sell_price - item_price
            sell_prices.append(f"{sell_price:.2f}")
            total_sell_products += sell_price

print(*sell_prices, sep=' ')
print(f"Profit: {profit:.2f}")
if total_sell_products + budget >= train_ticket:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")



