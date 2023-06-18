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

