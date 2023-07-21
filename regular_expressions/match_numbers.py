import re
numbers = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, numbers)

for match in matches:
    print(match.group(), end=" ")

# ($|(?=\s)) - checks if the number has the end of the string or has whitespace.
# (^|(?<=\s)) - checks if we are at the start of the string(^) or if there is any whitespace behind the string.
# -? checks if the number is a negative one. '?' because having a negative number is not required. Between 0-1 -> ?
# ([0]|[1-9][0-9]*) checks if there is any digits, one or more. However, it will match '00', so that's why we put 1-9
# (\.\d+)? checks if the decimal point exists
