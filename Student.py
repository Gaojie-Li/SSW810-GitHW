from collections import defaultdict

""" A class designed for storing "student" objects """


class Student:
    def __init__(self, cwid, name, major):
        self.cwid = cwid
        self.name = name
        self.major = major
        self.courses = defaultdict(str)

    # Functions to add course into students' profile
    def add_course(self, course_name, grade):
        self.courses[course_name] = grade
