rooms = int(input())

for room in range(rooms):
    room_information = input().split()
    chairs = room_information[0]
    people = room_information[1]

    chairs_in_room = [chair for chair in chairs]

    if people > len(chairs_in_room):
        print(f"More chairs needed in room.")
