import re


def get_food(text):
    pattern = r'(#|\|)(?P<name>[A-Za-z\s]+)(\1)(?P<date>\d{2}/\d{2}/\d{2})(\1)(?P<calories>\d{1,5})(\1)'
    matches = re.finditer(pattern, text)
    total_calories = 0
    food_items = []

    for match in matches:
        item = match.groupdict()
        item['calories'] = int(item['calories'])
        total_calories += item['calories']
        food_items.append(item)

    available_food = total_calories // 2000
    print(f"You have food to last you for: {available_food} days!")

    for item in food_items:
        print(f"Item: {item['name']}, Best before: {item['date']}, Nutrition: {item['calories']}")


string = input()
get_food(string)
