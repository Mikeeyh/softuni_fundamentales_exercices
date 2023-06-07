def center_point(first_x, first_y, second_x, second_y):
    first_point_sum = abs(first_x) + abs(first_y)
    second_point_sum = abs(second_x) + abs(second_y)

    if first_point_sum <= second_point_sum:
        first_x = round(first_x)
        first_y = round(first_y)
        result = f'{first_x, first_y}'
    else:
        second_x = round(second_x)
        second_y = round(second_y)
        result = f'{second_x, second_y}'

    return result


first_point_x = float(input())
first_point_y = float(input())
second_point_x = float(input())
second_point_y = float(input())

print(center_point(first_point_x, first_point_y, second_point_x, second_point_y))

# OR -----------------------------------------------

import math


def closest_to_center(x1, y1, x2, y2):
    distance1 = math.sqrt(x1 ** 2 + y1 ** 2)
    distance2 = math.sqrt(x2 ** 2 + y2 ** 2)

    if distance1 <= distance2:
        print(f"({int(x1)}, {int(y1)})")
    else:
        print(f"({int(x2)}, {int(y2)})")


first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())

closest_to_center(first_x, first_y, second_x, second_y)