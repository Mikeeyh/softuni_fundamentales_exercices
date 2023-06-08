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

