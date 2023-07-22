import re
command = input()
total_money = 0
bought_furniture = []

pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_money += float(quantity) * float(price)

    command = input()

print("Bought furniture: ")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")

# Example: >>Sofa<<312.23!3
# ([A-Za-z]+) --> Sofa
# (\d+\.?\d*) --> 312.23 --> \.? to accept if there is '.' or not. And, d* to check if there is a number after the point
# (\d+) --> 3
