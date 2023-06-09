text = input().split()
filtered_text = [letter for letter in text if len(letter) % 2 == 0]
print('\n'.join(filtered_text))

# OR ------------------------------------------------------

print('\n'.join([word for word in input().split() if len(word) % 2 == 0]))

# OR ------------------------------------------------------

words = input().split()
filtered_words = []

for word in words:
    if len(word) % 2 == 0:
        filtered_words.append(word)

print('\n'.join(filtered_words))
