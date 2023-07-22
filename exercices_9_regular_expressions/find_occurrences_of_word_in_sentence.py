import re
text = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"

result = re.findall(pattern, text, re.IGNORECASE)

print(len(result))

# OR

text = input()
searched_word = input()

pattern = fr"(?i)\b{searched_word}\b"

result = re.findall(pattern, text)

print(len(result))
