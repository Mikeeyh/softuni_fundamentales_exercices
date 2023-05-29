word = input()

for i in range(len(word) -1, -1, -1):
    print(word[i], end='')

#OR

print(word[::-1])
