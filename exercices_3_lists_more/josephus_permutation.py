def josephus_permutation(persons, special_number):
    executions = []
    index = 0

    while people:
        index = (index + k - 1) % len(people) # we add this to turn in cycle in the indexes of people.
        executed = people.pop(index)
        executions.append(executed)

    converted_list = [str(number) for number in executions]
    final_list = ','.join(converted_list)

    return final_list


people = list(map(int, input().split()))
k = int(input())

result = josephus_permutation(people, k)
print(f"[{result}]")





