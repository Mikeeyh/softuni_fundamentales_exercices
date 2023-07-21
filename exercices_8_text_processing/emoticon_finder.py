text = input()
emoticons = []

for index in range(len(text)):
    if text[index] == ':':
        emoticon = ':' + text[index + 1]
        emoticons.append(emoticon)

print('\n'.join(emoticons))

# OR

text = input()

for index in range(len(text)):
    if text[index] == ':':
        print(f":{text[index + 1]}")