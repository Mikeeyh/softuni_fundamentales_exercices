my_list = [1, 8, 4, 43, 2, 132] # can be used with stings only too

# .SORT
my_list.sort(reverse=False) # reverse=False 1-> +inf, reverse=True +inf -> 1
print(my_list)

my_list = [1, 8, 4, 43, 2, 2, 132, "Gosho", "Pesho"]

# .POP - DELETE AN ELEMENT
# my_list.pop() # we can add a number in pop() to delete an exact index
# print(my_list)

# .POP - DELETE AN ELEMENT AND ADD IT TO THE END OF THE LIST
# my_list.append(my_list.pop(2)) #delete the index 2 (number 4 in our case) and add it at the end of the list
# print(my_list)

# .INSERT
# my_list.insert(3, "Atanas") # insert Atanas on index 3
# print(my_list)

# .INDEX
# number = my_list.index(2) # gives the element in index 2
# print(number)

# .COUNT - Repetition
# repetition = my_list.count("Gosho")
# print(repetition)

# .REVERSE
# my_list.reverse()
# print(my_list) # or (my_list[::-1])

# DEL
# del my_list[3] # delete the element at index 3
# print(my_list)

# .REMOVE
# my_list.remove('Gosho')
# print(my_list)

# REMOVE MIN VALUES FROM A LIST
# for index in range(numbers_to_be_removed):
#     my_list.remove(min(my_list))

# PRINT ELEMENTS OF LIST WITHOUT PARENTHESES
# print(*my_list, sep=", ")