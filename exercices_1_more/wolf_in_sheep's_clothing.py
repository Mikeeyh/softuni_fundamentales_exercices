animals = input().split(', ')
list_of_animals = []

for animal in animals:
    list_of_animals.append(animal)

for index in range(len(list_of_animals)):
    if list_of_animals[-1] == 'wolf':
        print(f"Please go away and stop eating my sheep")
        break

    if list_of_animals[index] == 'wolf':
        sheep_to_be_eaten = len(list_of_animals) - index - 1
        print(f"Oi! Sheep number {sheep_to_be_eaten}! You are about to be eaten by a wolf!")
        break

