number_of_strings = int(input())
unauthorized_characters = [",", ".", "_"]
flag = False

for string in range(number_of_strings):
    given_string = input()

    for char in given_string:
        if char in unauthorized_characters:
            flag = True
            print(f"{given_string} is not pure!")
            break

    else:
        print(f"{given_string} is pure.")

# OR ----------------------------------------------------------------------------


def check_purity(n):
    for _ in range(n):
        string = input()
        if any(char in string for char in [',', '.', '_']):
            print(f"{string} is not pure!")
        else:
            print(f"{string} is pure.")


n = int(input())
check_purity(n)

