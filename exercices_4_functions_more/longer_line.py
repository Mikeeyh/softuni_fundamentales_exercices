import math


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    distance1 = math.sqrt(x1**2 + y1**2) + math.sqrt(x2**2 + y2**2)
    distance2 = math.sqrt(x3**2 + y3**2) + math.sqrt(x4**2 + y4**2)

    if distance1 >= distance2:
        if math.sqrt(x1**2 + y1**2) <= math.sqrt(x2**2 + y2**2):
            print(f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})")
        else:
            print(f"({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})")
    elif distance1 < distance2:
        if math.sqrt(x3**2 + y3**2) <= math.sqrt(x4**2 + y4**2):
            print(f"({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})")
        else:
            print(f"({int(x4)}, {int(y4)})({int(x3)}, {int(y3)})")


first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())
third_x = float(input())
third_y = float(input())
fourth_x = float(input())
fourth_y = float(input())
longer_line(first_x, first_y, second_x, second_y, third_x, third_y, fourth_x, fourth_y)
