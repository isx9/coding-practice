class Course:
    """A completed course with a name, grade and credits."""

    def __init__(self, name: str, grade: int, course_credits: int):
        self._name = name
        self._grade = grade
        self._credits = course_credits

    @property
    def name(self):
        """The course name."""
        return self._name

    @property
    def grade(self):
        """The best grade achieved for the course."""
        return self._grade

    @grade.setter
    def grade(self, new_grade: int):
        self._grade = max(self._grade, new_grade)

    @property
    def credits(self):
        """The number of credits for the course."""
        return self._credits


class CourseRecords:
    """Stores completed courses and computes statistics."""

    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, course_credits: int):
        """Add a course, or raise its grade if the new grade is higher."""
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, course_credits)
        else:
            self.__courses[name].grade = grade

    def get_course(self, name: str):
        """Return the course with the given name, or None."""
        return self.__courses.get(name)

    def all_courses(self):
        """Return all stored courses."""
        return list(self.__courses.values())

    def statistics(self):
        """Return the number of courses, total credits and mean grade."""
        courses = self.all_courses()
        total_credits = sum(course.credits for course in courses)
        if len(courses) == 0:
            return 0, total_credits, 0
        mean_grade = sum(course.grade for course in courses) / len(courses)
        return len(courses), total_credits, mean_grade

    def grade_distribution(self):
        """Return how many courses have each grade from 1 to 5."""
        distribution = {grade: 0 for grade in range(5, 0, -1)}
        for course in self.all_courses():
            distribution[course.grade] += 1
        return distribution


class RecordApplication:
    """Text-based user interface for CourseRecords."""

    def __init__(self):
        self.__records = CourseRecords()

    @staticmethod
    def help():
        """Print the available commands."""
        print('1 add course')
        print('2 get course data')
        print('3 statistics')
        print('0 exit')

    def add_course(self):
        """Ask for course details and store them."""
        name = input('course: ')
        grade = int(input('grade: '))
        course_credits = int(input('credits: '))
        self.__records.add_course(name, grade, course_credits)

    def search(self):
        """Ask for a course name and print its data."""
        name = input('course: ')
        course = self.__records.get_course(name)

        if course is None:
            print('no entry for this course')
            return
        print(f'{course.name} ({course.credits} cr) grade {course.grade}')

    def print_statistics(self):
        """Print summary statistics and the grade distribution."""
        count, total_credits, mean_grade = self.__records.statistics()
        print(f'{count} completed courses, a total of {total_credits} credits')
        print(f'mean {mean_grade:.1f}')

        print('grade distribution')
        for grade, amount in self.__records.grade_distribution().items():
            print(f'{grade}: {"x" * amount}')

    def execute(self):
        """Run the command loop until the user enters 0."""
        self.help()
        while True:
            print('')
            command = input('command: ')
            if command == '0':
                break
            if command == '1':
                self.add_course()
            elif command == '2':
                self.search()
            elif command == '3':
                self.print_statistics()
            else:
                self.help()


if __name__ == '__main__':
    application = RecordApplication()
    application.execute()
