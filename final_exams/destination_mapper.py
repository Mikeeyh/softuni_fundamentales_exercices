import re
text = input()
travel_points = 0
valid_list = []

pattern = r"(=|/)([A-Z][a-zA-Z]{2,})\1"

valid_locations = re.findall(pattern, text)

for location in valid_locations:
    valid_location = location[1]
    travel_points += len(valid_location)
    valid_list.append(valid_location)

print(f"Destinations: {', '.join(valid_list)}")
print(f"Travel Points: {travel_points}")

# OR ---------------------------------------------------------

text = input()
travel_points = 0
valid_list = []

pattern = r"(=|/)([A-Z][a-zA-Z]{2,})\1"

valid_locations = re.finditer(pattern, text)

for location in valid_locations:
    valid_list.append(location.group(2))
    travel_points += len(location.group(2))

print(f"Destinations: {', '.join(valid_list)}\nTravel Points: {travel_points}")