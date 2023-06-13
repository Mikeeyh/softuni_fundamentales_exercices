food_in_kg = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
guinea_weight = float(input()) * 1000

not_enough = False

for day in range(1, 30 + 1):
    food_in_kg -= 300

    if day % 2 == 0:
        quantity_hay -= food_in_kg * 0.05

    if day % 3 == 0:
        quantity_cover -= guinea_weight / 3

    if food_in_kg <= 0 or quantity_cover <= 0 or quantity_hay <= 0:
        not_enough = True
        break

if not_enough:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_in_kg / 1000:.2f}, Hay: {quantity_hay / 1000:.2f}, Cover: {quantity_cover / 1000:.2f}.")