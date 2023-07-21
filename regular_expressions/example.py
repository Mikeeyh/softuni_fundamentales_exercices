import re


def regex_test(regex, string):
    match = re.search(regex, string)

    if match:
        print('Match found:', match.group())
    else:
        print('No match found')


regex_test('\\bworld\\b', 'hello world')  # match the word given if exists
regex_test('\\d+', 'Mike12455Mike') # match all digits and print them
regex_test('\\d', 'Mike12455Mike') # match the first digit found and print it

# re.findall(pattern, text) - creating list with all matches

# match digits before and after '.'
text = 'The cost in 12.99 lv.'
pattern = "\d+\.\d+"
result = re.findall(pattern, text)
print(result) # ['12.99']

# match letters
text = 'abc def'
pattern = "a.c"
result = re.findall(pattern, text)
print(result) # ['abc']

# match all elements using '.' and '.+' to match them as a group
pattern = "."
pattern1 = ".+"

# match words and match using '*'
text = 'hi, hiii, hiiii, hiiiiii'
pattern2 = 'hi'
result = re.findall(pattern2, text)
print(result) # ['hi', 'hi', 'hi', 'hi']

pattern2 = 'hi*'
result = re.findall(pattern2, text)
print(result) # ['hi', 'hiii', 'hiiii', 'hiiiiii']

# match using '|' which is equals to 'or'
text = 'The ball is red and big'
pattern = "(red|blue) and (big|small)"
result = re.findall(pattern, text)
result2 = re.search(pattern, text)
print(result)
print(result2.group())

# match the exact specified number of occurrences using {}
text = '1234, 123, 12, 1, 123456'
pattern = "\d{5}"
result = re.findall(pattern, text)
print(result) # ['12345']

# match if starts with, using ^
text = 'Python - Language - Opinion'
pattern = "^Python"
result = re.findall(pattern, text)
print(result) # ['Python']

# match if ends with, using $
text = 'Python - Language - Opinion'
pattern = "Opinion$"
result = re.findall(pattern, text)
print(result) # ['Python']

# [arn] method for searching letters in the string
text = 'Python is an interpreted language'
pattern = "[arn]"
result = re.findall(pattern, text)
print(result) # ['n', 'a', 'n', 'n', 'r', 'r', 'a', 'n', 'a']

# [arn] method for searching count of a letter in the string
text = 'Python is an interpreted language'
pattern = "[arn]"
result = re.findall(pattern, text)
print(result.count('n')) # 4

