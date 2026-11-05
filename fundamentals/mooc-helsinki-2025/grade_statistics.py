GRADE_LIMITS = [(28, 5), (24, 4), (21, 3), (18, 2), (15, 1)]


def calculate_grade(exam_points: int, total_points: int):
    """Return the course grade (0-5) based on exam points and total points."""
    if exam_points < 10:
        return 0
    for limit, grade in GRADE_LIMITS:
        if total_points >= limit:
            return grade
    return 0


def print_statistics(results: list):
    """Print the points average, pass percentage and grade distribution."""
    if len(results) == 0:
        print('No data')
        return

    print('Statistics:')

    avg_points = sum(points for points, _ in results) / len(results)
    print(f'Points average: {avg_points:.1f}')

    passed = sum(1 for _, grade in results if grade > 0)
    pass_percent = 100 * passed / len(results)
    print(f'Pass percentage: {pass_percent:.1f}')

    print('Grade distribution:')
    for grade in range(5, -1, -1):
        stars = sum(1 for _, student_grade in results if student_grade == grade)
        print(f'  {grade}: {"*" * stars}')


def main():
    """Read exam points and completed exercises until an empty line."""
    student_results = []

    while True:
        line = input('Exam points and exercises completed: ')
        if line == '':
            break

        exam_points, exercises = map(int, line.split())
        exercise_points = exercises // 10
        total_points = exam_points + exercise_points
        grade = calculate_grade(exam_points, total_points)
        student_results.append((total_points, grade))

    print_statistics(student_results)


if __name__ == '__main__':
    main()
