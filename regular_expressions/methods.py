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

# match any character, digit, '_' which is equals to [a-zA-Z0-9_]
text = '_(underscores) are also word characters!'
pattern2 = '\w+'
result = re.findall(pattern2, text)
print(result) # ['_', 'underscores', 'are', 'also', 'word', 'characters']

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

# [arn] returns a match when one of the specified characters are present
text = 'Python is an interpreted language'
pattern = "[arn]"
result = re.findall(pattern, text)
print(result) # ['n', 'a', 'n', 'n', 'r', 'r', 'a', 'n', 'a']

# [arn] returns the count of a match when one of the specified characters are present
text = 'Python is an interpreted language'
pattern = "[arn]"
result = re.findall(pattern, text)
print(result.count('n')) # 4

# [^arn] returns a match for any character EXCEPT a, r, n
text = 'Python is an interpreted language'
pattern = "[^arn]"
result = re.findall(pattern, text)
print(result)

# [a-n] returns a match for ANY lower-case character, alphabetically between a and n
text = 'Python is an interpreted language'
pattern = "[a-n]"
result = re.findall(pattern, text)
print(result)

# [a-n] returns a match for ANY lower-case character, alphabetically between a and n
text = 'Python is an interpreted language'
pattern = "[a-n]"
result = re.findall(pattern, text)
print(result)

# [0123] returns a match where ANY of the specified digits are present (positive only)
text = 'We have 10 e-mails from 8 people and the score is negative of -4'
pattern = "[0-9]"
result = re.findall(pattern, text)
print(result) # ['1', '0', '8', '4']

# [0123] returns a match where ANY of the specified digits are present (positive or negative)
text = 'We have 10 e-mails from 8 people and the score is negative of -4'
pattern = "[0-9]|-[0-9]" # checking positive numbers 0-9 and negative numbers 0-9
result = re.findall(pattern, text)
print(result) # ['1', '0', '8', '-4']

# [0-9] returns a match for any digit between 0 and 9
text = 'We have 10 e-mails from 8 people and the score is negative of -4'
pattern = "[0-9]"
result = re.findall(pattern, text)
print(result) # ['1', '0', '8', '4']

# [0-5][0-9] returns a match for any two-digit between 00 and 59
text = 'We have 10 e-mails from 8 people and the score is negative of -4'
pattern = "[0-5][0-9]"
result = re.findall(pattern, text)
print(result) # ['10']

# [a-zA-Z] returns a match for any character alphabetically between a-z or A-Z
text = '1234a8231b99532A9129312B'
pattern = "[a-zA-Z]"
result = re.findall(pattern, text)
print(result) # ['a', 'b', 'A', 'B']

# [a-zA-Z] returns a match for any character alphabetically between a-z or A-Z or digit 0-9
text = 'Python is fun 66'
pattern = "[a-zA-Z0-9]+"
result = re.findall(pattern, text)
print(result) # ['Python', 'is', 'fun', '66']

# "\d"
# "\D"
# "\b"
# "\s"
# "\S"
# "\w"
# "\W"