def ascii_converter(start, end):
    list_of_chars = []
    start = ord(start)
    end = ord(end)
    for char in range(start + 1, end):
        list_of_chars.append(chr(char))
    return ' '.join(list_of_chars)


start_index = input()
end_index = input()
result = ascii_converter(start_index, end_index)
print(result)

# OR -----------------


def ascii_converter(start, end):
    list_of_chars = []
    start = ord(start)
    end = ord(end)
    for char in range(start + 1, end):
        list_of_chars.append(chr(char))
    return list_of_chars


start_index = input()
end_index = input()
result = ascii_converter(start_index, end_index)
print(' '.join(result))
