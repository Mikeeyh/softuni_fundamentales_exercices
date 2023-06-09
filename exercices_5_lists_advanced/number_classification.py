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
