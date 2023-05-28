lost_fights_counter = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet_counter = lost_fights_counter // 2
broken_sword_counter = lost_fights_counter // 3
broken_shield_counter = lost_fights_counter // (2 * 3)
broken_armor_counter = broken_shield_counter // 2

total_expenses = broken_helmet_counter * helmet_price + \
                 broken_sword_counter * sword_price + \
                 broken_shield_counter * shield_price + \
                 broken_armor_counter * armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
