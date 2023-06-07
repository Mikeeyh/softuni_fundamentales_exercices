def determine_product_sign():
    negative_count = 0
    is_zero = False

    for num in range(3):
        number = int(input())
        if number == 0:
            is_zero = True
            break
        elif number < 0:
            negative_count += 1

    if is_zero:
        print('zero')
    else:
        if negative_count % 2 != 0:
            print('negative')
        else:
            print('positive')


determine_product_sign()


