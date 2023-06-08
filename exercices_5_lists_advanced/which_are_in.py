first_string = input().split(', ')
second_string = input().split(', ')

substrings = []

for string in first_string:
    for word in second_string:
        if string in word:
            substrings.append(string)
            break

print(substrings)

# OR ------------------------------


def substrings_check(first_str, second_str):
    substrings = []

    for string in first_str:
        for word in second_str:
            if string in word:
                substrings.append(string)
                break
    return substrings


first_string = input().split(', ')
second_string = input().split(', ')
print(substrings_check(first_string, second_string))
