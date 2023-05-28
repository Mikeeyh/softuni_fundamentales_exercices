group_size = int(input())
days = int(input())

current_day = 0
coins_earned = 0
coins_wagered = 0

for day in range(1, days + 1):
    current_day += 1

    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5

    coins_earned += 50 - (2 * group_size)

    if current_day % 3 == 0:
        coins_wagered += 3 * group_size
        if current_day % 5 == 0:
            coins_wagered += 2 * group_size
    if current_day % 5 == 0:
        coins_earned += 20 * group_size

total_coins = coins_earned - coins_wagered
total_coins_per_person = total_coins / group_size

print(f"{group_size} companions received {int(total_coins_per_person)} coins each.")
