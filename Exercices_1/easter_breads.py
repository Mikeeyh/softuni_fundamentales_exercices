budget = float(input())
price_for_flour_per_kg = float(input())

total_eggs = 0
colored_eggs = 0
lost_eggs = 0
bread_counter = 0

price_for_eggs_per_pack = price_for_flour_per_kg * 0.75
price_for_milk_per_liter = price_for_flour_per_kg * 1.25
price_for_one_bread = price_for_eggs_per_pack + price_for_flour_per_kg + price_for_milk_per_liter / 4

while budget >= price_for_one_bread:
    colored_eggs += 3
    bread_counter += 1

    if bread_counter % 3 == 0:
        lost_eggs += bread_counter - 2

    total_eggs = colored_eggs - lost_eggs
    budget -= price_for_one_bread

print(f"You made {bread_counter} loaves of Easter bread! Now you have {total_eggs} eggs and {budget:.2f}BGN left.")

