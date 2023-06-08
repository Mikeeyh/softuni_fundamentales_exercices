text = input().split()
filtered_text = [letter for letter in text if len(letter) % 2 == 0]
print(filtered_text)
print('\n'.join(filtered_text))
