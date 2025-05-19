from student import *

def main():
    # Create Student objects
    try:
        student1 = Student("John Doe", "123456789")
        student2 = Student("Jane Smith", "987654321")
        print("Students created successfully.")
    except ValueError as e:
        print(f"Error creating students: {e}")

    # Update grades for both students
    try:
        student1.update_grade("Math", 85)
        student1.update_grade("History", 90)
        print("Grades updated successfully for student1.")

        student2.update_grade("Math", 95)
        student2.update_grade("History", 80)
        student2.update_grade("Science", 88)
        print("Grades updated successfully for student2.")
    except ValueError as e:
        print(f"Error updating grades: {e}")

    # Attempt to update a grade for a course that already exists
    try:
        student1.update_grade("Math", 75)
    except ValueError as e:
        print(f"Expected error when updating an existing grade: {e}")

    # Test retrieving grades
    try:
        math_grade = student1.get_grade("Math")
        print(f"Student1's grade for Math: {math_grade}")
    except ValueError as e:
        print(f"Error retrieving grade: {e}")

    # Attempt to retrieve a grade for a course not taken
    try:
        science_grade = student1.get_grade("Science")
    except ValueError as e:
        print(f"Expected error when retrieving a non-existent grade: {e}")

    # Test courses_not_taken function
    try:
        all_courses = ["Math", "History", "Science", "Art"]
        not_taken_by_student1 = courses_not_taken(student1, all_courses)
        print(f"Courses not taken by student1: {not_taken_by_student1}")
    except ValueError as e:
        print(f"Error testing courses_not_taken: {e}")

    # Test better_grades method
    try:
        better_courses = student1.better_grades(student2)
        if better_courses:
            print(f"Courses where student2 has better grades: {better_courses}")
        else:
            print("No courses where student2 has better grades.")
    except ValueError as e:
        print(f"Error comparing grades: {e}")

if __name__ == "__main__":
    main()
