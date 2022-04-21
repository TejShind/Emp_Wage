'''
@Author: Tejaswini Shinde
<<<<<<< HEAD
@Date: 2022-04-20 20:18
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title :UC3_Add Part time 
=======
@Date: 2022-04-20 09:31
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title :Employee Wage
>>>>>>> UC2_Calculate_DailyWage
'''

print('Welcome to Employee Wage Program')
import random
<<<<<<< HEAD
<<<<<<< HEAD

#CONSTANTS
IS_ABSENT = 0
IS_PART_TIME = 1
IS_PRESENT = 2
WAGE_PER_HOUR = 20
PART_TIME_HOUR = 4
FULL_DAY_HOUR = 8


def get_work_hours():
    '''
            Description: Function to get Employee Working hours
            Parameter: None
            Return: work_hrs as per Random Calculation
        '''
    emp_check = random.randint(0,2)
    if emp_check == IS_PRESENT:
        work_hrs = FULL_DAY_HOUR
    elif emp_check == IS_PART_TIME:
        work_hrs = PART_TIME_HOUR
    else:
        work_hrs = 0
    return work_hrs

daily_emp_wage = WAGE_PER_HOUR * get_work_hours()
print(f"Person earns {daily_emp_wage} rupees this day")
=======
class Employee:

=======
class Employee:

>>>>>>> UC2_Calculate_DailyWage
    def __init__(self):
        self.attendance = random.randint(0, 1)
    """
    Below functions checks whether the employee is present or absent. And print the status
<<<<<<< HEAD
    """
    def check_attendance(self):
        if self.attendance == 0:
            print("Employee is absent")
        else:
            print("Employee is present")

print("Welcome to EmployeeWage computation program")
employee = Employee()
employee.check_attendance()
>>>>>>> UC1_CheckEmpPresntOrAbsent
=======
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
>>>>>>> UC2_Calculate_DailyWage
