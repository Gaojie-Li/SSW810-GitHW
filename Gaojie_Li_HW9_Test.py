import unittest
import Gaojie_Li_HW9


class HW9Test(unittest.TestCase):
    def test_summary(self):
        tables = Gaojie_Li_HW9.main()
        student_table = tables[0]
        instructor_table = tables[1]

        # test data in student table
        self.assertEqual(student_table._rows[0], ['10103', 'Baldwin, C', [
                         'CS 501', 'SSW 564', 'SSW 567', 'SSW 687']])
        self.assertEqual(student_table._rows[3], ['10175', 'Erickson, D', [
                         'SSW 564', 'SSW 567', 'SSW 687']])

        # test data in instructor table
        self.assertEqual(instructor_table._rows[3], [
                         '98764', 'Feynman, R', 'SFEN', 'SSW 687', 3])
        self.assertEqual(instructor_table._rows[7], [
                         '98763', 'Newton, I', 'SFEN', 'SSW 689', 1])


if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)
