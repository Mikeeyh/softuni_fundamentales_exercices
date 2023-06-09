version = input()
version_numbers = version.split('.')

num_1 = int(version_numbers[0])
num_2 = int(version_numbers[1])
num_3 = int(version_numbers[2])

num_3 += 1
if num_3 > 9:
    num_3 = 0
    num_2 += 1
    if num_2 > 9:
        num_2 = 0
        num_1 += 1

new_version = f'{num_1}.{num_2}.{num_3}'
print(new_version)

# OR -------------------------------------------------------


def next_version(version):
    version_parts = version.split('.')

    n_1 = int(version_parts[0])
    n_2 = int(version_parts[1])
    n_3 = int(version_parts[2])

    n_3 += 1
    if n_3 > 9:
        n_3 = 0
        n_2 += 1
        if n_2 > 9:
            n_2 = 0
            n_1 += 1

    new_version = f'{n_1}.{n_2}.{n_3}'
    return new_version


version = input()
print(next_version(version))

# OR -----------------------------------------------------------

version = input().split('.')

first = int(version[0])
second = int(version[1])
third = int(version[2])
new_version = 0

for n_1 in range(1):
    for n_2 in range(1):
        for n_3 in range(1):
            third += 1
            if third > 9:
                third = 0
                second += 1
                if second > 9:
                    second = 0
                    first += 1

new_version = f'{first}.{second}.{third}'

print(new_version)

