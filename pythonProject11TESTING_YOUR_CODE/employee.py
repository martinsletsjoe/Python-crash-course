class Employee:
    '''Collect information about an employee.'''

    def __init__(self,first_name, last_name, annual_salary=0):
        '''Store each of these as attributes.'''
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def employee_info(self):
        '''Return employee information.'''
        return f"{self.first_name} {self.last_name} {self.annual_salary}"

    def give_raise(self, raise_amount=5000):
        '''Add annual salary, or a different amount.'''
        self.annual_salary += raise_amount

# employee = Employee("leo", "hoe", 50000)
# print(employee.employee_info())
#
# employee.give_raise()
# print(employee.employee_info())
#
# employee.give_raise(420)
# print(employee.employee_info())



