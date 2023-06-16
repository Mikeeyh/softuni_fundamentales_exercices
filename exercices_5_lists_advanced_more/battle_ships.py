# Read the number of rows
n = int(input())

# Read the field from input
field = []
for _ in range(n):
    row = list(map(int, input().split()))
    field.append(row)

# Read the attacked squares
attacks = input().split()

# Initialize a variable to count the number of destroyed ships
destroyed_ships = 0

# Iterate through each attacked square
for attack in attacks:
    row, col = map(int, attack.split('-'))

    # Check if there is a ship at the attacked square
    if field[row][col] > 0:
        # Reduce the ship's health by 1
        field[row][col] -= 1

        # Check if the ship has been destroyed
        if field[row][col] == 0:
            destroyed_ships += 1

print(destroyed_ships)
