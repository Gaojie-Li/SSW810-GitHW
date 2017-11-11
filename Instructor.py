from collections import defaultdict

""" A class designed for storing "instructor" objects """


class Instructor:
    def __init__(self, cwid, name, department):
        self.cwid = cwid
        self.name = name
        self.department = department
        self.courses = defaultdict(int)

    # Functions to add student number into instructors' profile
    def add_course(self, course_name):
        self.courses[course_name] += 1
