import Student
import Instructor
from collections import defaultdict

""" Class to save all student/instructor data """


class Repository:
    def __init__(self):
        self.student_list = defaultdict(Student.Student)
        self.instructor_list = defaultdict(Instructor.Instructor)

    def insert_student(self, student):
        self.student_list[student.cwid] = student

    def insert_instructor(self, instructor):
        self.instructor_list[instructor.cwid] = instructor

    def insert_course_student(self, cwid, course_name, grade):
        self.student_list[cwid].add_course(course_name, grade)

    def insert_course_instructor(self, cwid, course_name):
        self.instructor_list[cwid].add_course(course_name)
