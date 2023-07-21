import re

text = """
I am born on 30-Dec-1994. 
My father is born on the 9-Jul-1955.
01-July-2000 is not a valid date.
"""

pattern = "\\b\d{1,2}-[A-Z][a-z]{2}-\d{4}\\b"

result = re.findall(pattern, text)
for date in result:
    print(date)

# \d{1,2} to take only 1 to 2 digits
# [A-Z][a-z]{2} to take 1 upper character, followed by two lower characters
# \d{4} to take exactly 4 digits
# And we add \\b to the start to match only the first one couple of digits
# And we add \\b to the end to match only the year [AAAA] and to skip strings as 1995python
