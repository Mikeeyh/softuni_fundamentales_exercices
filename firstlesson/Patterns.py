n = int(input())

for i in range(1, n + 1):   # ot 1 do n
    print( i * '*')

for i in range(n - 1, 0, -1):  # ot n - 1, zashtoto ot 1st loop imame nai golqm red veche / do 0 / step -1 za da namalq
    print(i * '*')

# za figura primerno:

n = 5

for i in range(n):
    for j in range(n - i):
        print(end=' ')
    for j in range(i + 1):
        print('* ', end='')
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i + 1):
        print(end=' ')
    for j in range(i):
        print('* ', end='')
    print()
