n = int(input())
synonyms = {}

for i in range(n):
    word = input()
    synonym = input()

    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

print(synonyms)
for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")

# OR -----------------------------------------------------------------

n = int(input())
synonyms = {}

for i in range(n):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

print(synonyms)
for word, synonym_list in synonyms.items():
    synonym_str = ', '.join(synonym_list)
    print(f"{word} - {synonym_str}")
