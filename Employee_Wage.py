'''
@Author: Tejaswini Shinde
@Date: 2022-04-20 09:31
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title :Employee Wage
'''

print('Welcome to Employee Wage Program')
import random
class Employee:

    def __init__(self):
        self.attendance = random.randint(0, 1)
    """
    Below functions checks whether the employee is present or absent. And print the status
    """
    def check_attendance(self):
        if self.attendance == 0:
            print("Employee is absent")
        else:
            print("Employee is present")

print("Welcome to EmployeeWage computation program")
employee = Employee()
employee.check_attendance()