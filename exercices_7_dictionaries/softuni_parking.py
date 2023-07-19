parking = {}
n = int(input())

for _ in range(n):
    data = input().split()
    command = data[0]
    name = data[1]

    if command == "register":
        plate_number = data[2]
        if name not in parking.keys():
            parking[name] = 0
            parking[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")

    if command == "unregister":
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            del parking[name]
            print(f"{name} unregistered successfully")

for key, value in parking.items():
    print(f"{key} => {value}")
