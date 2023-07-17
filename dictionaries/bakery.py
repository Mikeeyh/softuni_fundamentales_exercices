data = input().split()

stock = {}

for i in range(0, len(data), 2): # we take step 2 because we need always a pair (key:value)
    product = data[i]
    quantity = int(data[i + 1])
    stock[product] = quantity

print(stock)
