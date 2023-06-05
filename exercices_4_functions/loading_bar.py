def loading_bar(some_number):
    if some_number == 100:
        return f"100% Complete!\n[%%%%%%%%%%]"
    else:
        filled_percentage = number // 10
        empty_percentage = 10 - filled_percentage
        loading_line = "[" + "%" * filled_percentage + "." * empty_percentage + "]"
        return f"{number}% {loading_line}\nStill loading..."ll


number = int(input())
print(loading_bar(number))

# OR -------------------------


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

