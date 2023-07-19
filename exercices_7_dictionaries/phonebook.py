phonebook = {}

data = input()

while True:
    if data.isdigit():
        data = int(data)
        break
    data = input()

print(data)