'''
@Author: Tejaswini Shinde
@Date: 2022-04-20 14:04
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title :UC1_Check Employee Present or absent
'''

print('Welcome to Employee Wage Program')

#Importing Random
import random

#CONSTANTS
IS_PRESENT = 1
WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8


def get_work_hours():
    '''
            Description: Function to get Employee Working hours
            Parameter: None
            Return: work_hrs as per Random Calculation
        '''
    emp_check = random.randint(0,1)
    if emp_check == IS_PRESENT:
        work_hrs = FULL_DAY_HOUR
    else:
        work_hrs = 0
    return work_hrs

daily_emp_wage = WAGE_PER_HOUR * get_work_hours()
print(f"Person earns {daily_emp_wage} rupees this day")