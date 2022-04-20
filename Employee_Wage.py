'''
@Author: Tejaswini Shinde
@Date: 2022-04-20 09:31
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title :Employee Wage
'''

print('Welcome to Employee Wage Program')

#Importing Random
import random
IS_PRESENT = 1

emp_check = random.randint(0,1)
if emp_check == IS_PRESENT:
    print("Employee is present")
else:
    print("Employee is absent")