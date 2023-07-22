import re

text = input()
while text:
    pattern = r"\d+"
    result = re.findall(pattern, text)
    if result:
        print(" ".join(result), end=" ")

    text = input()

