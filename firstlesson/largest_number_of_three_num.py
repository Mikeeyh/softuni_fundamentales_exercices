from first_Basic_sytax_Conditional_statements_Loops.Number_Definer import num

num1, num2, num3 = int(input()), int(input()), int(input())

print(max(num1, num2, num3))

# OR

num1, num2, num3 = int(input()), int(input()), int(input())

if num1 > num2 and num1 > num3:
    largest = num1

elif num2 > num1 and  num2 > num3:
    largest = num2

else:
    largest = num3

print(largest)