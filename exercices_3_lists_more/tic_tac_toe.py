def check_winner(field):
    # Check rows
    for row in field:
        if row[0] == row[1] == row[2] != 0:
            return row[0]

    # Check columns
    for col in range(3):
        if field[0][col] == field[1][col] == field[2][col] != 0:
            return field[0][col]

    # Check diagonals
    if field[0][0] == field[1][1] == field[2][2] != 0:
        return field[0][0]
    if field[0][2] == field[1][1] == field[2][0] != 0:
        return field[0][2]

    return 0  # No winner

# Example usage:
field = []
for _ in range(3):
    line = input().split()
    field.append([int(num) for num in line])

winner = check_winner(field)
if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")