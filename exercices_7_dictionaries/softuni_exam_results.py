results = {}
submissions = {}

while True:
    current_result = input().split("-")

    if len(current_result) == 1:
        break

    elif len(current_result) == 2:
        name = current_result[0]
        del results[name]

    elif len(current_result) == 3:
        name, current_course, current_points = current_result[0], current_result[1], int(current_result[2])
        if name not in results.keys():
            results[name] = 0

        if results[name] < current_points:
            results[name] = current_points

        if current_course not in submissions.keys():
            submissions[current_course] = 0
        submissions[current_course] += 1

print("Results:")
for username, points in results.items():
    print(f"{username} | {points}")
print("Submissions:")
for course, submissions_count in submissions.items():
    print(f"{course} - {submissions_count}")
