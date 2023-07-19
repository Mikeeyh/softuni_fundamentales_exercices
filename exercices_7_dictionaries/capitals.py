first_line = input().split(', ')
second_line = input().split(', ')

countries_capitals = {key: value for (key, value) in zip(first_line, second_line)}

for country, capital in countries_capitals.items():
    print(f"{country} -> {capital}")

# OR ------------------------------------------------------------------------------

countries = input().split(", ")
capitals = input().split(", ")

information = {countries[index]: capitals[index] for index in range(len(countries))}
for country, capital in countries_capitals.items():
    print(f"{country} -> {capital}")
