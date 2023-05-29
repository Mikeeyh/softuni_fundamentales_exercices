number_of_lines = int(input())
keyword = input()
my_list = []
my_list_with_keyword_only = []

for line in range(number_of_lines):
    data = input()
    words = data.split() # moje i bez split

    my_list.append(data)
    if keyword in words:
        my_list_with_keyword_only.append(data)

print(my_list)
print(my_list_with_keyword_only)
