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
    Calculate Daily Wage assume Wage per hour=20,Fullday hour=8 
    """
    def check_attendance(self):
        if self.attendance == 1:
            print("Employee is Present")
            daily_wage =20*8
            print(f"The daily employee wage is Rs.{daily_wage}")
        else:
            print("Employee is Absent")
            daily_wage=0
            print(f"The daily employee wage is Rs.{daily_wage}")
employee = Employee()
employee.check_attendance()