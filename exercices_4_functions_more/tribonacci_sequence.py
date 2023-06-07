def print_tribonacci_sequence(n):
    sequence = [1, 1, 2]  # Initialize the sequence with the first three numbers as per formula for tribonacci seq.

    for i in range(numbers):
        if i < 3:
            print(sequence[i], end=" ")
        else:
            next_number = sequence[i-1] + sequence[i-2] + sequence[i-3]
            sequence.append(next_number)
            print(next_number, end=" ")


numbers = int(input())
print_tribonacci_sequence(numbers)
