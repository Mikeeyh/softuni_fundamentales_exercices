my_list = ["1", "2", "3", "4", "5", "6"]
search_element = 7
index = my_list.index(search_element)
print(index)

#

my_list = ["1", "2", "3", "4", "5", "6"]
search_element = 7

try:
    index = my_list.index(search_element)
    print("Element found at index:", index)
except ValueError:
    print("Element not found!")
