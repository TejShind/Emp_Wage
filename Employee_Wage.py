'''
@Author: Tejaswini Shinde
@Date: 2022-04-25 15:43
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title :Employee Wage UC4_Solving using Case Statment
'''

import random

print('Welcome to Employee Wage Program')


fullDayEmpHour = 8
partTimeEmpHour = 4
empWagePerHour = 20

def empFullDayWage():
    """
        Description:
            checking employee full day wage
        Parameter:
            none
        Return:
            sending total emp wage and message of full day
    """
    totalEmpWage = fullDayEmpHour * empWagePerHour

    return("Employee Is Present And Done Full Day", totalEmpWage)



def empPartTimeDayWage():
    """
        Description:
            checking employee half day wage
        Parameter:
            none right now
        Return:
            sending total emp wage and message of half day
    """
    totalEmpWage = partTimeEmpHour * empWagePerHour

    return("Employee Is Present And Done half Day", totalEmpWage)


def empPresentyCheck(presentCheck):
    """
        Description:
            checking employee attendace present or absent
        Parameter:
            sending parameter of two random number
        Return:
            return absent message
    """
    switcher = {
        0: 'Employee Is Absent',
        1: empwageCalculate(random.randint(0, 1)),
    }
    return switcher[presentCheck]

def empwageCalculate(num):
    """
        Description:
            checking employee half day or full day
        Parameter:
            sending parameter of two random number for checking half day or full day
        Return:
            return function values from half or full day.
    """
    switcher = {
        0: empPartTimeDayWage(),
        1: empFullDayWage()
    }
    return switcher[num]


empCheck = random.randint(0, 1)

employeeWage = empPresentyCheck(empCheck)

if empCheck == 0:
    print(employeeWage)
else:
    print(employeeWage[0])
    print(employeeWage[1])


