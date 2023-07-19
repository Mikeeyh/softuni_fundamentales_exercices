companies = {}
command = input().split(" -> ")

while command[0] != 0:
    company, id = command

    if company not in companies.keys():
        companies[company] = []

    if id not in companies[company]:
        companies[company].append(id)

    command = input().split(" -> ")

for company, employees in companies.items():
    print(company)

    for employee in employees:
        print(f"-- {employee}")
