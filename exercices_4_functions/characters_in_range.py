start_index = input()
end_index = input()
list_of_chars = []


def ascii_converter(start, end):
    start = ord(start_index)
    end = ord(end_index)
    for char in range(start + 1, end):
        list_of_chars.append(chr(char))
    return ' '.join(list_of_chars)


result = ascii_converter(start_index, end_index)
print(result)



