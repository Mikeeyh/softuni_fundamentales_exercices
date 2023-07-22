import re
text = input()

pattern = r"\b_([A-Za-z0-9]+)\b"
variables = re.findall(pattern, text)
print(','.join(variables))

# \b_ means that the string starts with '_' then it is followed with a digit/letter
# we add \b at the end in order to find all matches which stops after the digit/letter
# we add '()' in order to print only the matches in the group ()
