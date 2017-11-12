import unittest
import Gaojie_Li_HW10


class HW10Test(unittest.TestCase):
    def test_summary(self):
        tables = Gaojie_Li_HW10.main()
        major_table = tables[0]
        student_table = tables[1]
        instructor_table = tables[2]

        # test data in major table
        self.assertEqual(major_table._rows[0], ['SFEN', ['SSW 533', 'SSW 540', 'SSW 555', 'SSW 564',
                                                         'SSW 565', 'SSW 567', 'SSW 690', 'SSW 695'], ['CS 501', 'CS 513', 'CS 545']])

        # test data in student table
        self.assertEqual(student_table._rows[0], ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], [
                         'SSW 533', 'SSW 540', 'SSW 555', 'SSW 565', 'SSW 690', 'SSW 695'], []])
        self.assertEqual(student_table._rows[3], ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], [
                         'SSW 533', 'SSW 540', 'SSW 555', 'SSW 565', 'SSW 690', 'SSW 695'], ['CS 501', 'CS 513', 'CS 545']])

        # test data in instructor table
        self.assertEqual(instructor_table._rows[3], [
                         '98764', 'Feynman, R', 'SFEN', 'SSW 687', 3])
        self.assertEqual(instructor_table._rows[7], [
                         '98763', 'Newton, I', 'SFEN', 'SSW 689', 1])


if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)
