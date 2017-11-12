import Student
import Instructor
import Major
from collections import defaultdict

""" Class to save all student/instructor data """


class Repository:
    def __init__(self):
        self.student_dict = defaultdict(Student.Student)
        self.instructor_dict = defaultdict(Instructor.Instructor)
        self.major_dict = defaultdict(Major.Major)

    def insert_student(self, student):
        self.student_dict[student.cwid] = student

    def insert_instructor(self, instructor):
        self.instructor_dict[instructor.cwid] = instructor

    def insert_major(self, major):
        self.major_dict[major.name] = major

    def insert_course_student(self, cwid, course_name, grade):
        self.student_dict[cwid].add_course(course_name, grade)

    def insert_course_instructor(self, cwid, course_name):
        self.instructor_dict[cwid].add_course(course_name)

    def insert_course_major(self, major_name, is_required, course_name):
        if is_required is True:
            self.major_dict[major_name].add_required(course_name)
        else:
            self.major_dict[major_name].add_elective(course_name)
