import re
text = input()

pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"

valid_emails = re.findall(pattern, text)

for valid_email in valid_emails:
    print(valid_email[0])

# adding \s to check if it starts with interval " " empty string.
# * from 0 to more
# + from 1 to more

# Example: info-bg@hotmail-university.co.uk

# \s([a-z0-9]+[a-z0-9\.\-\_]*) --> info-bg
# @ --> info-bg@
# ([a-z\-]+) --> info-bg@hotmail-university
# (\.[a-z]+)+\b --> info-bg@hotmail-university.co.uk
# we added additional () in order to regroup all groups
