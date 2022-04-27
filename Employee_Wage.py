'''
@Author: Tejaswini Shinde
@Date: 2022-04-27 9:22
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title :Employee Wage UC8_Store the daily wage along with total wage
'''

import random

print('Welcome to Employee Wage Program')


fullDayEmpHour = 8
partTimeEmpHour = 4
empWagePerHour = 20
daysInMonth  = 20
hoursInMonth =100
totalWorkingHours = 0



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
            none
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

def empWageComputation():
    """
        Description:
            Getting employee wage calculation for now it is giving total employee working hours
        Parameter:
            none
        Return:
            returns total working hours
    """
    totalEmpWage = 0
    workingDays =0
    totalWorkingHours =0
    days= 0
    i = 0
    dailyWage =[]

    while i < 20:
      empCheck = random.randint(0, 1)
      employeeWage = empPresentyCheck(empCheck)

      if empCheck == 0:
        # print(employeeWage)
        i = i-1
      else:
        if totalWorkingHours < 92:
            # print(employeeWage[0])
            totalEmpWage += employeeWage[1]
            dailyWage.append(employeeWage[1])
            workingDays += 1
            totalWorkingHours += employeeWage[1]

        else:

             if employeeWage[2] == 4:
                totalWorkingHours += employeeWage[2]
                dailyWage.append(employeeWage[2])


        if totalWorkingHours >= 100:
            break

        i = i + 1
        days += 1

    return totalWorkingHours, dailyWage


print("Total Employee working Hours in a month Is", empWageComputation())