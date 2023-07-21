banned_words = input().split(", ")
text = input()

for word in banned_words:
    while word in text:
        replaced_value = '*' * len(word)
        text = text.replace(word, replaced_value)

print(text)