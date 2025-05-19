"""
student: Asaf Fitusi
ID:318763430
Assignment no.4
program: student_grades
"""
"""
This program processes student and course data, calculates averages and top scores, 
and outputs the results to a file. It handles mismatched IDs, sorts courses alphabetically, 
and ensures a clean format by removing underscores from keys and values.
"""

def read_students(input_file_stu):#Reads student data and creates a dictionary of student names.
    stu_name_dict = {}
    for row in input_file_stu:
        listed_row = row.split()
        stu_name_dict[listed_row[0]] = listed_row[1] + ' ' + listed_row[2]
    return stu_name_dict

def read_grades(input_file_gra):#Reads student grades and creates a dictionary of grades.
    stu_gra_dict = {}
    for row in input_file_gra:
        listed_row = row.split()
        lst = [(listed_row[i], int(listed_row[i+1])) for i in range(1, len(listed_row), 2)]
        stu_gra_dict[listed_row[0]] = lst
    return stu_gra_dict

def average_grade(stu_gra_dict):#Calculates the average grade for each student.
    stu_avg_gra_dict = {ID: sum(grade for subject, grade in subject) / len(subject) for ID, subject in stu_gra_dict.items()}
    return stu_avg_gra_dict

def find_max_average(stu_avg_gra_dict, stu_name_dict):#Finds the student with the highest average grade.
    max_Grade = max(stu_avg_gra_dict.values())
    for s in stu_name_dict:
        if stu_avg_gra_dict[s] == max_Grade:
            best_stu = ([stu_name_dict[s]])
    return best_stu, max_Grade

def get_courses(stu_name_dict, stu_gra_dict):#Processes courses and maps them to student names and grades.
    course_name_grade_dict = {}
    for student_id, grades in stu_gra_dict.items():
        if student_id in stu_name_dict:
            student_name = stu_name_dict[student_id]
            for subject, grade in grades:
                subject = subject.replace("_", " ")  
                if subject not in course_name_grade_dict:
                    course_name_grade_dict[subject] = []
                course_name_grade_dict[subject].append((student_name.replace("_", " "), grade))
    return course_name_grade_dict

def get_max_students(course_name_grade_dict):#Finds students with maximum grades for each course.
    max_Grade_by_course = []
    for course, students in course_name_grade_dict.items():
        max_grade = max([grade for student, grade in students])
        max_students = [(student, max_grade) for student, grade in students if grade == max_grade]
        max_Grade_by_course.extend(max_students)
    return max_Grade_by_course

def get_max_grade(course_name_grade_dict, max_Grade_by_course):#Maps courses to their maximum grades.
    keys = list(course_name_grade_dict.keys())
    max_Grade_by_course_dict = {keys[i]: (f'{max_Grade_by_course[i][0]}', max_Grade_by_course[i][1]) for i in range(len(keys))}
    return max_Grade_by_course_dict

def get_average_grade(course_name_grade_dict):#Calculates the average grade for each course.
    cou_avg_gra_dict = {course: sum(grade for student, grade in students) / len(students) for course, students in course_name_grade_dict.items()}
    return cou_avg_gra_dict

def verify_ids(stu_name_dict, stu_gra_dict):#Verifies and removes mismatched IDs.
    removed_ids = []
    for student_id in list(stu_gra_dict.keys()):
        try:
            if student_id not in stu_name_dict:
                removed_ids.append(f'{student_id} does not exist. Removed from grades list.')
                stu_gra_dict.pop(student_id)
        except KeyError:
            print(f"Unexpected error: Failed to process student ID {student_id}.")
    return removed_ids

def courses_name(course_name_grade_dict):#Sorts the courses alphabetically by keys.
    courses = ', '.join(sorted(course_name_grade_dict.keys()))
    return courses

def sorted_max_Grade_by_course_dict(max_Grade_by_course_dict):#Sorts the dictionary alphabetically by keys.
    sorted_dict = dict(sorted(max_Grade_by_course_dict.items()))
    return sorted_dict

def sorted_cou_avg_gra_dict(cou_avg_gra_dict):#Sorts the dictionary alphabetically by keys.
    sorted_dict = dict(sorted(cou_avg_gra_dict.items()))
    return sorted_dict

def main():#The main function of the program.
    try:
        input_file_stu = open('students_list.txt', 'r')
    except FileNotFoundError:
        print("Error: 'students_list.txt' file not found.")
        return
    stu_name_dict = read_students(input_file_stu)
    input_file_stu.close()

    try:
        input_file_gra = open('grades_list.txt', 'r')
    except FileNotFoundError:
        print("Error: 'grades_list.txt' file not found.")
        return
    stu_gra_dict = read_grades(input_file_gra)
    input_file_gra.close()

    removed_ids = verify_ids(stu_name_dict, stu_gra_dict)
    stu_avg_gra_dict = average_grade(stu_gra_dict)
    name, grade = find_max_average(stu_avg_gra_dict, stu_name_dict)
    course_name_grade_dict = get_courses(stu_name_dict, stu_gra_dict)
    lst_courses_sorted = courses_name(course_name_grade_dict)
    max_Grade_by_course = get_max_students(course_name_grade_dict)
    max_Grade_by_course_dict = get_max_grade(course_name_grade_dict, max_Grade_by_course)
    sorted_max_Grade_by_course_dict1 = sorted_max_Grade_by_course_dict(max_Grade_by_course_dict)
    cou_avg_gra_dict = get_average_grade(course_name_grade_dict)
    sorted_cou_avg_gra_dict1 = sorted_cou_avg_gra_dict(cou_avg_gra_dict)

    output_file = open('grades_output.txt', 'w')
    output_file.write('My name: Asaf Fitusi\n\n')
    output_file.write(f'Best student: {name[0]}, average: {grade:.2f}\n\n')
    output_file.write(f'courses:\n{lst_courses_sorted}\n\n')
    for course, avg_grade in sorted_cou_avg_gra_dict1.items():#Iterates through each course and its average grade from the sorted dictionary of course averages.
        max_student, max_grade = sorted_max_Grade_by_course_dict1[course]
        output_file.write(f'{course}:\n')
        output_file.write(f'average grade: {avg_grade:.2f}, maximum grade: {max_grade}, Obtained by {max_student}\n')
    output_file.write('\nErrors:\n')
    for error in removed_ids:#Iterates through the list of removed IDs and adds the relevant error messages to the output.
        output_file.write(f'{error}\n')
    output_file.close()

main()