numbers = list(map(int, input().split(', ')))
# numbers = [int(number) for number in input().split(',')]

even = [number for number in numbers if number % 2 == 0]
odd = [number for number in numbers if number % 2 != 0]
positives = [number for number in numbers if number >= 0]
negatives = [number for number in numbers if number < 0]

print('Positive:', end=' '), print(*positives, sep=", ")
print('Negative:', end=' '), print(*negatives, sep=", ")
print('Even:', end=' '), print(*even, sep=", ")
print('Odd:', end=' '), print(*odd, sep=", ")
# OR print(f'Odd: {", ".join(map(str, odd))}')

# OR ----------------------------------------------------------------

numbers = input().split(', ')

even = [number for number in numbers if int(number) % 2 == 0]
odd = [number for number in numbers if int(number) % 2 != 0]
positives = [number for number in numbers if int(number) >= 0]
negatives = [number for number in numbers if int(number) < 0]

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")

# OR ----------------------------------------------------------------


def positive_numbers(some_numbers):
    return [number for number in numbers if int(number) >= 0]


def negative_numbers(some_numbers):
    return [number for number in numbers if int(number) < 0]


def even_numbers(some_numbers):
    return [number for number in numbers if int(number) % 2 == 0]


def odd_numbers(some_numbers):
    return [number for number in numbers if int(number) % 2 != 0]


numbers = input().split(', ')
print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")
