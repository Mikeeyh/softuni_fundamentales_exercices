n = int(input())
results = {}

for _ in range(n):
    student_name = input()
    student_note = float(input())

    if student_name not in results:
        results[student_name] = []
    results[student_name].append(student_note)

for student, average_note in results.items():
    average = sum(average_note) / len(average_note)
    if average < 4.50:
        continue
    print(f"{student} -> {average:.2f}")

