number = int(input())

electron_list = [2 * electron ** 2 for electron in range(1, 10) if 2 * electron ** 2 < number]
if sum(electron_list) > number:
    electron_list[-1] = sum(electron_list) - number
print(electron_list)
