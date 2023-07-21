text = input().split('\\')

file = text[-1]
file_name, extension = file.split(".")

print(f"File name: {file_name}")
print(f"File extension: {extension}")

# OR ------------------------------------------------------------

text = input().split('\\')

file = text[-1]
file = file.split(".")
file_name = file[0]
extension = file[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")