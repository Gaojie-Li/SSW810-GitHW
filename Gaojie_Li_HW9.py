import os
import Student
import Instructor
import Repository
from prettytable import PrettyTable


def main():
    school_repo = Repository.Repository()

    try:
        student_file = open('./students.txt')
    except OSError:
        print('File cannot be open.')
    else:
        for line in student_file:
            cur_student = line.strip().split('\t')

            if len(cur_student) != 3:
                continue

            # cur_student[0]: cwid, cur_student[1]: name, cur_student[2]: major
            new_student = Student.Student(
                cur_student[0], cur_student[1], cur_student[2])
            school_repo.insert_student(new_student)

        student_file.close()

    try:
        instructor_file = open('./instructors.txt')
    except OSError:
        print('File cannot be open.')
    else:
        for line in instructor_file:
            cur_prof = line.strip().split('\t')
            if len(cur_prof) != 3:
                continue

            # cur_prof[0]: cwid, cur_prof[1]: name, cur_prof[2]: department
            new_instructor = Instructor.Instructor(
                cur_prof[0], cur_prof[1], cur_prof[2])
            school_repo.insert_instructor(new_instructor)

        instructor_file.close()

    try:
        grade_file = open('./grades.txt')
    except OSError:
        print('File cannot be open.')
    else:

        for line in grade_file:
            cur_grade = line.strip().split('\t')
            if len(cur_grade) != 4:
                continue

            # cur_grade[0]: student_id, cur_grade[1]: course_name, cur_grade[2]: grade, cur_grade[3]: instructor_id
            school_repo.insert_course_student(
                cur_grade[0], cur_grade[1], cur_grade[2])
            school_repo.insert_course_instructor(cur_grade[3], cur_grade[1])

        grade_file.close()

    student_table = PrettyTable(
        field_names=['CWID', 'Name', 'Completed Courses'])

    for key, value in school_repo.student_list.items():
        student_table.add_row(
            [value.cwid, value.name, sorted(key for key, value in value.courses.items())])

    instructor_table = PrettyTable(
        field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])

    for key, value in school_repo.instructor_list.items():
        for k, v in value.courses.items():
            instructor_table.add_row(
                [value.cwid, value.name, value.department, k, v])

    print('\nStudent Summary')
    print(student_table)

    print('Instructor Summary')
    print(instructor_table)

    return [student_table, instructor_table]
