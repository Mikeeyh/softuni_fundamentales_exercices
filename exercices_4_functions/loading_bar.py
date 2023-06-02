def loading_bar(value):
    filled_percentage = number // 10
    empty_percentage = 10 - filled_percentage
    loading_line = "[" + "%" * filled_percentage + "." * empty_percentage + "]"

    if number < 100:
        result = f"{number}% {loading_line}\nStill loading..."
    else:
        result = f"{number}% Complete!\n{loading_line}"

    return result


number = int(input())
total = loading_bar(number)
print(total)

# OR -------------------------

def loading_bar(some_number)