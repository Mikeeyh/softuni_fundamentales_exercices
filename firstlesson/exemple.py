a = int(input("Please enter your age: "))

if a > 18:
    print("Please enter")
else:
    print("Underaged!")


# if we add .lower or .upper - we get the word converted in lower or upper cases only:
# example: if we want to stop a loop when we put Stop as command, if we add command.lower or command.upper
# we will be sure that the loop will stop in all cases of "Stop" ( STOP / StOp / stoP etc)