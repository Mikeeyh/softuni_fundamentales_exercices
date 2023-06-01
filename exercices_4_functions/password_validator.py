password = input().split()
flag = False
my_list = []

if not (6 <= len(password) <= 10):
    flag = True

for i in password:
    my_list.append(ord(i))

for y in my_list:
    if not 48 <= my_list[y] <= 57:
        flag = True
    if not 65 <= my_list[y] <= 90:
        flag = True
    if not 97 <= my_list[y] <= 122:
        flag = True
if flag:
    print(f'ok')



