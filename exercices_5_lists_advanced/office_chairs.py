rooms = int(input())

total_free_chairs = 0
enough_chairs = True

for room in range(rooms):
    room_information = input()
    chairs, visitors = room_information.split()
    chairs_count = len(chairs)
    visitors_count = int(visitors)

    if visitors_count > chairs_count:
        enough_chairs = False
        needed_chairs = visitors_count - chairs_count
        print(f"{needed_chairs} more chairs needed in room {room + 1}")
    else:
        free_chairs = chairs_count - visitors_count
        total_free_chairs += free_chairs

if enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")

# or -----------------------------------------------------------------------

rooms = int(input())

total_free_chairs = 0
enough_chairs = True

for room in range(rooms):
    room_information = input().split()
    chairs = room_information[0]
    visitors = room_information[1]
    chairs_count = len(chairs)
    visitors_count = int(visitors)

    if visitors_count > chairs_count:
        enough_chairs = False
        needed_chairs = visitors_count - chairs_count
        print(f"{needed_chairs} more chairs needed in room {room + 1}")
    else:
        free_chairs = chairs_count - visitors_count
        total_free_chairs += free_chairs

if enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")

# or -----------------------------------------------------------------------

def check_the_rooms(number_of_rooms):
    free_chairs = 0
    needed_chairs = 0

    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)

        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
            needed_chairs += abs(difference)
        else:
            free_chairs += difference

        return free_chairs, needed_chairs


rooms_counter = int(input())
total_free_chairs, total_needed_chairs = check_the_rooms(rooms_counter)

if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")