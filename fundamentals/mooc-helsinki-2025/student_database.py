def add_student(students: dict, name: str):
    """Add a student with an empty list of completed courses."""
    students[name] = []


def add_course(students: dict, name: str, completion: tuple):
    """Add a (course, grade) completion, keeping only the best grade per course."""
    course_name, grade = completion

    if grade == 0 or name not in students:
        return

    for index, (existing_name, existing_grade) in enumerate(students[name]):
        if existing_name == course_name:
            if grade > existing_grade:
                students[name][index] = (course_name, grade)
            return

    students[name].append((course_name, grade))


def average_grade(courses: list):
    """Return the average grade of a list of (course, grade) tuples."""
    if len(courses) == 0:
        return 0
    return sum(grade for _, grade in courses) / len(courses)


def print_student(students: dict, name: str):
    """Print a student's completed courses and average grade."""
    if name not in students:
        print(f'{name}: no such person in the database')
        return

    print(f'{name}:')
    courses = students[name]

    if len(courses) == 0:
        print(' no completed courses')
        return

    print(f' {len(courses)} completed courses:')
    for course_name, grade in courses:
        print(f'  {course_name} {grade}')

    print(f' average grade {average_grade(courses)}')


def summary(students: dict):
    """Print the number of students, most courses completed and best average."""
    print(f'students {len(students)}')

    most_name, most_courses = max(students.items(), key=lambda item: len(item[1]))
    print(f'most courses completed {len(most_courses)} {most_name}')

    best_name, best_courses = max(students.items(), key=lambda item: average_grade(item[1]))
    print(f'best average grade {average_grade(best_courses)} {best_name}')
