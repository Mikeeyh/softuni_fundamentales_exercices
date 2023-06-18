from tkinter.tix import MAX

people = int(input())
wagons = list(map(int, input().split()))

for wagon in range(len(wagons)):
    while wagons[wagon] < 4 and people > 0:
        wagons[wagon] += 1
        people -= 1

if people == 0 and any(seats < 4 for seats in wagons):
    print("The lift has empty spots!")
    print(" ".join(map(str, wagons)))

elif people > 0 and all(seats == 4 for seats in wagons):
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(map(str, wagons)))

elif people == 0 and all(seats == 4 for seats in wagons):
    print(" ".join(map(str, wagons)))

# OR -----------------------------------------------------

people = int(input())
lift_cabins = [int(number) for number in input().split()]
MAX_SPACES = 4

for current_cabin in range(len(lift_cabins)):
    free_spaces = MAX_SPACES - lift_cabins[current_cabin]

    if people >= free_spaces:
        lift_cabins[current_cabin] += free_spaces
    else:
        lift_cabins[current_cabin] += people

    people -= free_spaces

    if people <= 0 and (current_cabin != len(lift_cabins) - 1 or lift_cabins[current_cabin] < MAX_SPACES):
        print("The lift has empty spots!")
        break
else:
    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!")

print(*lift_cabins)