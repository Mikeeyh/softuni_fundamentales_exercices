def exchange(lst, index):
    if index < 0 or index >= len(lst):
        print("Invalid index")
    else:
        first_half = lst[:index + 1]
        second_half = lst[index + 1:]
        exchanged_lst = second_half + first_half
        return exchanged_lst

def find_max_even(lst):
    max_even = float('-inf')
    max_even_index = -1
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and lst[i] >= max_even:
            max_even = lst[i]
            max_even_index = i
    if max_even_index == -1:
        print("No matches")
    else:
        print(max_even_index)

def find_max_odd(lst):
    max_odd = float('-inf')
    max_odd_index = -1
    for i in range(len(lst)):
        if lst[i] % 2 != 0 and lst[i] >= max_odd:
            max_odd = lst[i]
            max_odd_index = i
    if max_odd_index == -1:
        print("No matches")
    else:
        print(max_odd_index)

def find_min_even(lst):
    min_even = float('inf')
    min_even_index = -1
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and lst[i] <= min_even:
            min_even = lst[i]
            min_even_index = i
    if min_even_index == -1:
        print("No matches")
    else:
        print(min_even_index)

def find_min_odd(lst):
    min_odd = float('inf')
    min_odd_index = -1
    for i in range(len(lst)):
        if lst[i] % 2 != 0 and lst[i] <= min_odd:
            min_odd = lst[i]
            min_odd_index = i
    if min_odd_index == -1:
        print("No matches")
    else:
        print(min_odd_index)

def find_first_even(lst, count):
    even_nums = [num for num in lst if num % 2 == 0]
    if count > len(even_nums):
        print("Invalid count")
    else:
        first_even_nums = even_nums[:count]
        print(first_even_nums)

def find_first_odd(lst, count):
    odd_nums = [num for num in lst if num % 2 != 0]
    if count > len(odd_nums):
        print("Invalid count")
    else:
        first_odd_nums = odd_nums[:count]
        print(first_odd_nums)

def find_last_even(lst, count):
    even_nums = [num for num in lst if num % 2 == 0]
    if count > len(even_nums):
        print("Invalid count")
    else:
        last_even_nums = even_nums[-count:]
        print(last_even_nums)

def find_last_odd(lst, count):
    odd_nums = [num for num in lst if num % 2 != 0]
    if count > len(odd_nums):
        print("Invalid count")
    else:
        last_odd_nums = odd_nums[-count:]
        print(last_odd_nums)

initial_list = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break
    elif command.startswith("exchange"):
        index = int(command.split()[1])
        initial_list = exchange(initial_list, index)
    elif command == "max even":
        find_max_even(initial_list)
    elif command == "max odd":
        find_max_odd(initial_list)
    elif command == "min even":
        find_min_even(initial_list)
    elif command == "min odd":
        find_min_odd(initial_list)
    elif command.startswith("first"):
        count = int(command.split()[1])
        if "even" in command:
            find_first_even(initial_list, count)
        elif "odd" in command:
            find_first_odd(initial_list, count)
    elif command.startswith("last"):
        count = int(command.split()[1])
        if "even" in command:
            find_last_even(initial_list, count)
        elif "odd" in command:
            find_last_odd(initial_list, count)

print(f"[{', '.join(map(str, initial_list))}]")



