sequence = input().split(", ")
groups = {}

for number in sequence:
    number = int(number)

    group = (number // 10) * 10
    if group not in groups:
        groups[group] = []
    groups[group].append(number)

for group, sequence in groups.items():
    print(f"Group of {group}'s: {sequence}")



print((5 // 10) * 10)

