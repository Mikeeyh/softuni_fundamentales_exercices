days = int(input())
daily_plunder = int(input())
expected_plunder = int(input())

plunder_gained = 0

for day in range(1, days + 1):
    plunder_gained += daily_plunder

    if day % 3 == 0:
        plunder_gained += daily_plunder / 2

    if day % 5 == 0:
        plunder_gained *= 0.70


if plunder_gained >= expected_plunder:
    print(f"Ahoy! {plunder_gained:.2f} plunder gained.")
else:
    percentage = 100 * (plunder_gained / expected_plunder)
    print(f"Collected only {percentage:.2f}% of the plunder.")
