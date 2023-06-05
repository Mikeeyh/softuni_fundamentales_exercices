string = input()
capital_indices = []

for index in range(len(string)):
    if string[index].isupper():
        capital_indices.append(index)               # capital_indices.append(string[i]) - to print letters
print(capital_indices)
