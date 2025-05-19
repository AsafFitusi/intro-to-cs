"""
student: Asaf Fitusi
ID:318763430
Assignment no.6
program: student.py
"""
class Student:
    def __init__(self, name: str, student_id: str):
        # Initializes a Student object with a name and ID, performing validation
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(student_id, str) or not student_id.isdigit() or len(student_id) != 9:
            raise ValueError("ID must be a string containing exactly 9 digits.")
        
        self.__name = name
        self.__id = student_id
        self.__grades = {}

    def update_grade(self, course: str, grade: int):
        # Updates or adds a grade for a specific course
        if not isinstance(course, str) or not course:
            raise ValueError("Course name must be a non-empty string.")
        if not isinstance(grade, int) or not (0 <= grade <= 100):
            raise ValueError("Grade must be an integer between 0 and 100.")
        
        self.__grades[course] = grade

    def get_grade(self, course: str) -> int:
        # Returns the grade of a specific course
        if course not in self.__grades:
            raise ValueError(f"No grade found for the course: {course}.")
        return self.__grades[course]

    def better_grades(self, other_student) -> list:
        # Compares grades with another student and returns courses with higher grades
        if not isinstance(other_student, Student):
            raise ValueError("Argument must be an instance of Student.")
        
        better_courses = []
        for course, grade in self.__grades.items():  # Iterates through all courses in the current student
            if course in other_student.__grades and grade > other_student.__grades[course]:
                better_courses.append(course)
        
        return better_courses

    def courses_not_taken(self, courses_lst: list) -> list:
        # Returns a list of courses that the student has not taken
        if not isinstance(courses_lst, list) or not all(isinstance(course, str) for course in courses_lst):
            raise ValueError("courses_lst must be a list of course names (strings).")
        
        return [course for course in courses_lst if course not in self.__grades]

    # Getters
    @property
    def name(self):
        # Returns the name of the student
        return self.__name

    @property
    def id(self):
        # Returns the ID of the student
        return self.__id

    @property
    def grades(self):
        # Returns the grades dictionary of the student
        return self.__grades