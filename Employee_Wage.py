'''
@Author: Tejaswini Shinde
@Date: 2022-04-21 20:43
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title :Employee Wage UC3_Part Time
'''

print('Welcome to Employee Wage Program')
import random

class Employee:
    def __init__(self):
        self.attendance = random.randint(0, 1)
    """

    Below functions checks whether the employee is present or absent. And print the status
    Calculate Daily Wage assume Wage per hour=20,Fullday hour=8,Part time day Hour=4
    """

    def check_attendance(self):
        if self.attendance == 0:
            print("Employee is Absent")
        elif self.attendance ==1:
            self.attendance = random.randint(0, 1)  
            print("Employee is Present ")   
            daily_wage=20*8
            print(f"The daily employee wage is Rs.{daily_wage}")
        else:
            print("Employee is part time prsent")
            daily_wage=20*4
            print(f"The daily employee wage is Rs.{daily_wage}")
            employee = Employee()
            employee.check_attendance()
            employee.daily_emp_wage()
            

