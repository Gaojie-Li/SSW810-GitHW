from collections import defaultdict

""" A class designed for storing "student" objects """


class Major:
    # name: string, required: list, elective: list
    def __init__(self, name):
        self.name = name
        self.required = []
        self.elective = []

    # Functions to add course into required course list
    def add_required(self, course_name):
        self.required.append(course_name)

    def add_elective(self, course_name):
        self.elective.append(course_name)
