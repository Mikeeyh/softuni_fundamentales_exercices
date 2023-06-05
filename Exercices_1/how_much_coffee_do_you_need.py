total_coffee = 0
events = ['coding', 'dog', 'cat', 'movie']

while True:
    command = input()

    if command == "END":
        break

    if command.lower() not in events:
        continue

    if command.islower():
        total_coffee += 1
    else:
        total_coffee += 2

if total_coffee > 5:
    print('You need extra sleep')
else:
    print(total_coffee)


