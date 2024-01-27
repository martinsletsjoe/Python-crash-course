import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    '''Tests for the class Employee.'''

    def setUp(self):
        '''create an employee and a set of responses for use in all test methods.'''
        self.employee = Employee('leo', 'hoe', 1)

    def test_give_default_raise(self):
        '''Test that the default raise is working properly.'''
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 5001)

    def test_give_custom_raise(self):
        '''Test that a custom raise is working properly.'''
        self.employee.give_raise(6900)
        self.assertEqual(self.employee.annual_salary, 6901)

if __name__ == 'main.py':
    unittest.main