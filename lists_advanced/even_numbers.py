# To check even numbers indices:
numbers = list(map(int, input().split(', ')))

even_numbers = map(lambda x: x if numbers[x] % 2 == 0 else 'no', range(len(numbers)))
even_indices = filter(lambda a: a != 'no', even_numbers)
print(list(even_indices))


# To check even numbers:
numbers = [1, 2, 3, 4, 5, 6, 7]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(list(even_numbers))
