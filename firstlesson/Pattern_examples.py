for i in range(4):
    for j in range(i + 1):
        print('*', end='')
    print()

print()
print("other")
print()

for i in range(4):
    for j in range(4 - i):
        print('*', end='')
    print()

print()
print("other")
print()

for i in range(4):
    for j in range(i):
        print('*', end='')
    print()

print()
print("other")
print()

for i in range(4):
    for j in range(4):
        print('*', end='')
    print()

print()
print("other")
print()

for i in range(4):
    for j in range(i + 1):
        print('* ', end='')
    print()

for i in range(4):
    for j in range(4 - i):
        print('*', end=' ')
    print()

print()
print("other")
print()

for i in range(4):
    for j in range(i + 1):
        print('*', end='')
    print()

for i in range(4):
    for j in range(4 - i):
        print('*', end='')
    print()

print()
print("other")
print()

for i in range(4):
    for j in range(i + 1):
        print('* ', end='')
    print()

for i in range(4):
    for j in range(4 - i - 1):
        print('*', end=' ')
    print()

print()
print("other")
print()

# how to make scware:

n = 5
print("*"*n)

n = 5

for i in range(n):
    for j in range(n):
        print("* ", end='')
    print()

print()
print("other")
print()

# how to make increasing triangle:

for i in range(n):
    for j in range(i + 1):
        print("* ", end='')
    print()

print()
print("other")
print()

# how to make decreasing triangle:

for i in range(n):
    for j in range(i, n):
        print("* ", end='')
    print()

print()
print("other")
print()

n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end='')

    for j in range(i + 1):
        print('*', end='')  # put space in this end part and you get triangle with similar 3 parts
    print()

print()
print("other")
print()

# pyramids:

n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')

    for j in range(i + 1): # change i + 1 to i and you get the pick of the pyramid
        print('*', end=' ')

    for j in range(i + 1):
        print('*', end=' ')

    print()

print()
print("other")
print()

n = 5
for i in range(n):
    for j in range(i + 1):
        print(' ', end=' ')

    for j in range(i, n): # change i, n to i, n - 1 and you get the pick of the pyramid
        print('*', end=' ')

    for j in range(i, n):
        print('*', end=' ')

    print()

print()
print("other")
print()

# pyramids:

n = 5
for i in range(n - 1):
    for j in range(i, n):
        print(' ', end=' ')

    for j in range(i): # change i + 1 to i and you get the pick of the pyramid
        print('*', end=' ')

    for j in range(i + 1):
        print('*', end=' ')

    print()

for i in range(n):
    for j in range(i + 1):
        print(' ', end=' ')

    for j in range(i, n - 1): # change i, n to i, n - 1 and you get the pick of the pyramid
        print('*', end=' ')

    for j in range(i, n):
        print('*', end=' ')

    print()

print()
print("other")
print()

#building

n = 5
for i in range(n):
    for z in range(n):
        for j in range(i, n):
            print(' ', end='')
        for j in range(i + 1):
            print('*', end=' ')
        print()

print()
print("other")
print()

# triangle trees

n = 5
for i in range(n):
    for i in range(n):
        for j in range(i, n):
            print(' ', end='')
        for j in range(i + 1):
            print('*', end=' ')
        print()

print()
print("other")
print()

# other buildings

n = 5
for i in range(n):
    for z in range(n):
        for j in range(i, n):
            print('*', end='')
        for j in range(i + 1):
            print('*', end=' ')
        print()

print()
print("other")
print()