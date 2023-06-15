sequence = input().split()
moves = 0

while True:
    command = input()

    if command == "end":
        break

    indexes = list(map(int, command.split()))

    if indexes[0] == indexes[1] or any(index < 0 or index >= len(sequence) for index in indexes):
        middle_index = len(sequence) // 2
        moves += 1
        sequence.insert(middle_index, f"-{moves}a")
        sequence.insert(middle_index + 1, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue

    if sequence[indexes[0]] == sequence[indexes[1]]:
        element = sequence[indexes[0]]
        sequence.pop(indexes[1])
        sequence.pop(indexes[0])
        moves += 1
        print(f"Congrats! You have found matching elements - {element}!")
    else:
        print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        break

if len(sequence) > 0:
    print("Sorry you lose :(")
    print(" ".join(sequence))