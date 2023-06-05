year = int(input())

while True:
    year += 1
    year_str = str(year)
    if len(set(year_str)) == len(year_str):
        break

print(year)
# print(len(set(year_str)))
# print(set(year_str))
# print(len(year_str))
