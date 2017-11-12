import os
import Student
import Instructor
import Major
import Repository
from prettytable import PrettyTable

qualify_grade = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']


def main():
    school_repo = Repository.Repository()

    # read student file
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

    # read instructor file
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

    # read grade file
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
            if cur_grade[2] in qualify_grade:
                school_repo.insert_course_student(
                    cur_grade[0], cur_grade[1], cur_grade[2])
            school_repo.insert_course_instructor(cur_grade[3], cur_grade[1])

        grade_file.close()

    # read major file
    try:
        major_file = open('./majors.txt')
    except OSError:
        print('File cannot be open.')
    else:

        for line in major_file:
            cur_major = line.strip().split('\t')
            if len(cur_major) != 3:
                continue

            # cur_major[0]: major_name, cur_major[1]: requirement, cur_major[2]: course_name
            if cur_major[0] not in school_repo.major_dict:
                new_major = Major.Major(cur_major[0])
                school_repo.insert_major(new_major)

            if cur_major[1] == 'R':
                school_repo.insert_course_major(
                    cur_major[0], True, cur_major[2])
            else:
                school_repo.insert_course_major(
                    cur_major[0], False, cur_major[2])

        major_file.close()

    major_table = PrettyTable(field_names=['Dept', 'Required', 'Electives'])
    for key, value in school_repo.major_dict.items():
        major_table.add_row(
            [key, sorted(value.required), sorted(value.elective)])

    student_table = PrettyTable(
        field_names=['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives'])

    for key, value in school_repo.student_dict.items():
        # check whether they have fulfilled their elective requirement
        fulfilled = False
        for k, v in value.courses.items():
            if k in school_repo.major_dict[value.major].elective:
                fulfilled = True

        if fulfilled is True:
            student_table.add_row([value.cwid, value.name, value.major, sorted(key for key, value in value.courses.items()), sorted(
                item for item in school_repo.major_dict[value.major].required if item not in value.courses), []])
        else:
            student_table.add_row([value.cwid, value.name, value.major, sorted(key for key, value in value.courses.items()), sorted(
                item for item in school_repo.major_dict[value.major].required if item not in value.courses), sorted(school_repo.major_dict[value.major].elective)])

    instructor_table = PrettyTable(
        field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])

    for key, value in school_repo.instructor_dict.items():
        for k, v in value.courses.items():
            instructor_table.add_row(
                [value.cwid, value.name, value.department, k, v])

    print('\nMajor Summary')
    print(major_table)

    print('\nStudent Summary')
    print(student_table)

    print('\nInstructor Summary')
    print(instructor_table)

    return [major_table, student_table, instructor_table]
