import re
n = int(input())

for _ in range(n):
    text = input()

    pattern = r'^(\$|\%)([A-Z][a-zA-Z]{2,})(\1): (\[\d+\]\|\[\d+\]\|\[\d+\]\|)$'
    matches = re.finditer(pattern, text)

    if re.match(pattern, text):
        numbers_converted_to_letter_list = []
        tag = re.search(r'([A-Z][a-zA-Z]{2,})', text).group(1)
        numbers_found = re.findall(r'\d+', text)

        for current_number in numbers_found:
            numbers_converted_to_letter_list.append(chr(int(current_number)))
        decrypted_message_found = ''.join(numbers_converted_to_letter_list)
        print(f"{tag}: {decrypted_message_found}")

    else:
        print("Valid message not found!")

# 4
# $Request$: [73]|[115]|[105]|
# %Taggy$: [73]|[73]|[73]|
# %Taggy%: [118]|[97]|[108]|
# $Request$: [73]|[115]|[105]|[32]|[75]|

