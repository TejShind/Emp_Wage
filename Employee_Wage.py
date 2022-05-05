'''
@Author: Tejaswini Shinde
@Date: 2022-04-27 9:22
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title :Employee Wage UC9_Store the Day the daily wage along with total wage
'''

import random

print('Welcome to Employee Wage Program')


fullDayEmpHour = 8
partTimeEmpHour = 4
empWagePerHour = 20



def empFullDayWage():
    """
        Description:
            Checking employee full day wage
        Parameter:
            None
        Return:
            Sending total emp wage and message of full day
    """
    totalEmpWage = fullDayEmpHour * empWagePerHour

    return("Employee Is Present And Done Full Day", totalEmpWage,fullDayEmpHour)


def empPartTimeDayWage():
    """
        Description:
            Checking employee half day wage
        Parameter:
            None
        Return:
            Sending total emp wage and message of half day
    """
    totalEmpWage = partTimeEmpHour * empWagePerHour

    return("Employee Is Present And Done half Day", totalEmpWage,partTimeEmpHour)


def empPresentyCheck(presentCheck):
    """
        Description:
            Checking employee attendace present or absent
        Parameter:
            Sending parameter of two random number
        Return:
            Return absent message
    """
    switcher = {
        0: 'Employee Is Absent',
        1: empwageCalculate(random.randint(0, 1)),
    }
    return switcher[presentCheck]

def empwageCalculate(num):
    """
        Description:
            Checking employee half day or full day
        Parameter:
            Sending parameter of two random number for checking half day or full day
        Return:
            Return function values from half or full day.
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
    dailyDays = []
    dailyWage = []

    while i < 20:
      empCheck = random.randint(0, 1)
      employeeWage = empPresentyCheck(empCheck)

      if empCheck == 0:
        print(employeeWage)
        i = i-1
      else:
        if totalWorkingHours <= 92:
           # print(employeeWage[0])
            totalEmpWage += employeeWage[1]
            dailyDays.append(i)
            dailyWage.append(employeeWage[1])
            workingDays += 1
            totalWorkingHours += employeeWage[1]
        else:
             if employeeWage[2] == 4:
                totalWorkingHours += employeeWage[2]
                dailyWage.append(employeeWage[1])


        if totalWorkingHours >= 100:
            break

        i = i + 1
        days += 1

    return totalWorkingHours,dailyDays, dailyWage 

totalWorkingHours,dailyDays,dailyWage = empWageComputation()

print("Total Employee working Hours in a month :", totalWorkingHours)
print("Total Employee working Daily Days in a month :", dailyDays)
print("Total Employee working Daily Wages in a month :" ,dailyWage)