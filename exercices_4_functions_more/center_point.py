def center_point(first_x, first_y, second_x, second_y):
    first_point_sum = abs(first_x) + abs(first_y)
    second_point_sum = abs(second_x) + abs(second_y)

    if first_point_sum < second_point_sum:
        first_x = round(first_x)
        first_y = round(first_y)
        result = f'{first_x, first_y}'
    if first_point_sum > second_point_sum:
        second_x = round(second_x)
        second_y = round(second_y)
        result = f'{second_x, second_y}'
    else:
        first_x = round(first_x)
        first_y = round(first_y)
        result = f'{first_x, first_y}'

    return result


first_point_x = float(input())
first_point_y = float(input())
second_point_x = float(input())
second_point_y = float(input())

print(center_point(first_point_x, first_point_y, second_point_x, second_point_y))
