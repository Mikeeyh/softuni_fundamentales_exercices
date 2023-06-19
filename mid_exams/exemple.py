from math import ceil, floor

biscuits_produced_per_day_per_worker = int(input('Enter the number of biscuits produced per day, per worker: '))
workers = int(input('Enter the number of workers: '))
number_of_biscuits_produced_by_the_competing_factory = int(input('Total production of biscuits of the other factory: '))

production = (biscuits_produced_per_day_per_worker * 20 * workers) + \
             (biscuits_produced_per_day_per_worker * 10 * workers * 0.75)
production = int(production)
difference = (abs(production - number_of_biscuits_produced_by_the_competing_factory))

print(f"You have produced {production} biscuits for the past month.")

percentage = difference / number_of_biscuits_produced_by_the_competing_factory * 100

if production > number_of_biscuits_produced_by_the_competing_factory:
    print(f"You produce {percentage:.2f}% percent more biscuits.")
else:
    print(f"You produce {percentage:.2f}% percent less biscuits.")
