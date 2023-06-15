targets = list(map(int, input().split()))
command = input()
shot_values = 0

while command != 'End':
    index_of_the_target = int(command)

    if 0 <= index_of_the_target < len(targets) and targets[index_of_the_target] != -1:
        value_of_target = targets[index_of_the_target]
        targets[index_of_the_target] = -1
        shot_values += 1

        for current_target in range(len(targets)):
            if targets[current_target] != -1:
                if targets[current_target] > value_of_target:
                    targets[current_target] -= value_of_target
                else:
                    targets[current_target] += value_of_target
    command = input()

print(f"Shot targets: {shot_values} -> {' '.join(map(str, targets))}")
