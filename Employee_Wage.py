'''
@Author: Tejaswini Shinde
<<<<<<< HEAD
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
=======
@Date: 2022-04-21 20:43
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title :Employee Wage UC3_Part Time
>>>>>>> UC3_Adding_PartTime
'''

print('Welcome to Employee Wage Program')
import random
<<<<<<< HEAD
<<<<<<< HEAD

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
            

<<<<<<< HEAD
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
=======
>>>>>>> UC3_Adding_PartTime
