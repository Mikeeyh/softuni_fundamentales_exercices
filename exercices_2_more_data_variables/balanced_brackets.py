number_of_lines = int(input())
my_list = []

for character in range(number_of_lines):
    current_character = input()
    my_list.append(current_character)

b = my_list.count(')')
a = my_list.count('(')

if a == b:
    print('BALANCED')
else:
    print('UNBALANCED')

# OR ----------------------------------------------------------------

def check_balanced_parentheses(lines):
    stack = []

    for line in lines:
        if line == "(":
            stack.append(line)
        elif line == ")":
            if len(stack) == 0 or stack[-1] != "(":
                return False
            stack.pop()

    return len(stack) == 0

# Read the number of lines
n = int(input())

# Read the lines
lines = [input() for _ in range(n)]

# Check if parentheses are balanced
is_balanced = check_balanced_parentheses(lines)

# Print the result
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
