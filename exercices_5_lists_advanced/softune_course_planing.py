def add_lesson(list_of_lessons, title):
    if title not in list_of_lessons:
        list_of_lessons.append(title)
    return list_of_lessons


def insert_lesson(list_of_lessons, title, index):
    if title not in list_of_lessons:
        list_of_lessons.insert(index, title)
    return list_of_lessons


def remove_lesson(list_of_lessons, title):
    if title in list_of_lessons:
        list_of_lessons.remove(title)
    return list_of_lessons


def swap_lesson(list_of_lessons, title, index):
    if title and index_or_lesson_title in list_of_lessons:
        pass


def exercise(list_of_lessons, title):
    if title in list_of_lessons:
        list_of_lessons.append(title + '-Exercise')
    else:
        list_of_lessons.append(title)
        list_of_lessons.append(title + '-Exercise')


lessons = input().split(', ')
command = input()

while command != 'course start':
    command = command.split(':')
    action, lesson_title = command[0], command[1]
    if len(command) > 2:
        index_or_lesson_title = command[2]

        if action == 'Add':
            lessons = add_lesson(lessons, lesson_title)
        elif action == 'Insert':
            lessons = insert_lesson(lessons, lesson_title, index_or_lesson_title)
        elif action == 'Remove':
            lessons = remove_lesson(lessons, lesson_title)
        elif action == 'Swap':
            lessons = swap_lesson(lessons, lesson_title, index_or_lesson_title)
        elif action == 'Exercise':
            lessons = exercise(lessons, lesson_title)

    command = input()

