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

# "\d" returns a match where the string contains digits 0-9
# "\D" returns a match where the string DOES NOT contain digits
# "\b" returns a match where the specified characters are at the BEGINNING or at the END of a word
# "\s" returns a match where the string contains a WHITESPACE character
# "\S" returns a match where the string DOES NOT contain a WHITESPACE character
# "\w" returns a match where the string contains any word characters a-z,  A-Z,  0-9 and underscore_character
# "\W" returns a match where the string DOES NOT contain any word characters

# re.IGNORECASE - ignores if it upper or lower case

# re.M - returns all the matches from different lines
text = """start one
start two"""
print(re.findall('^start', text))
print(re.findall('^start', text, re.M))

# re.sub - returns the replaced characters for the given characters
string = 'There are 3 dogs and 4 cats'
pattern = r'\d'
result = re.sub(pattern, 'number', string)
print(result)

# re.search - returns only the first one match !!!
string = 'The quick brown fox jumped over the lazy dog. Python is fun. Programing is fun!'
match = re.search(r'\bp\w*', string, re.IGNORECASE)
if match:
    print(f"The first word that starts with 'p' is: {match.group()}") # returns Python
else:
    print("No words starting with 'p' were found")

# capturing groups
date = '13/Jul/1928, 10-Nov-1934, 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016'
pattern = r"(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})" # this '\2' means that we copied the cap. group 2 ([-./])

result = re.findall(pattern, date)
for current_date in result:
    day = current_date[0]
    month = current_date[2]
    year = current_date[3]

    print(f"Day: {day}, Month: {month}, Year: {year}")

# OR
result = re.finditer(pattern, date)
for current_date in result:
    day = current_date.group(1)
    month = current_date.group(3)
    year = current_date.group(4)

    print(f"Day: {day}, Month: {month}, Year: {year}")

