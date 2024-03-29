data = input()
dictionary = {}

for letter in data:
    if letter != " ":
        if letter not in dictionary:
            dictionary[letter] = 0
        dictionary[letter] += 1

for char, occurrences in dictionary.items():
    print(f"{char} -> {occurrences}")

# OR ------------------------------------------------------

data = input()
dictionary = {}

for letter in data:
    if letter != " ":
        dictionary[letter] = dictionary.get(letter, 0) + 1

for char, occurrences in dictionary.items():
    print(f"{char} -> {occurrences}")

# OR ------------------------------------------------------

symbols = [char for char in input() if char != " "]
dictionary = {}

for symbol in symbols:
    if symbol not in dictionary.keys():
        dictionary[symbol] = 0
    dictionary[symbol] += 1

for char, occurrences in dictionary.items():
    print(f"{char} -> {occurrences}")
